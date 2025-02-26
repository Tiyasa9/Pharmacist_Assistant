// import React, { useEffect, useState } from "react";
// import axios from "axios";
// import Spinner from "../components/Spinner";
// import { Link, useNavigate } from "react-router-dom";
// import { AiOutlineEdit } from "react-icons/ai";
// import { BsInfoCircle } from "react-icons/bs";
// import { MdOutlineAddBox, MdOutlineDelete } from "react-icons/md";
// import BooksTable from "../components/home/BooksTable";
// // only use table
// // import BooksCard from "../components/home/BooksCard";

// const Home = () => {
//   const [books, setBooks] = useState([]);
//   const [loading, setLoading] = useState(false);
//   const [showType, setShowType] = useState("table");
//   const navigate = useNavigate();

//   if (!localStorage.getItem("token")) {
//     localStorage.setItem(
//       "token",
//       JSON.stringify({ token: "0", isAdmin: false })
//     );
//   }

//   const isAdmin = JSON.parse(localStorage.getItem("token")).isAdmin;

//   useEffect(() => {
//     setLoading(true);
//     axios
//       .get("http://localhost:5555/books")
//       .then((response) => {
//         setBooks(response.data.data);
//         setLoading(false);
//       })
//       .catch((error) => {
//         console.log(error);
//         setLoading(false);
//       });
//   }, []);

//   const handleLogout = () => {
//     localStorage.removeItem("token");
//     navigate("/");
//   };

//   return (
//     <div className="p-4">
//       <div className="flex justify-between items-center">
//         <div className="flex justify-center items-center gap-x-4">
//           {/*............................................. remove card type of showcase of book */}

//           {/* <button
//             className='bg-sky-300 hover:bg-sky-600 px-4 py-1 rounded-lg'
//             onClick={() => setShowType('table')}
//           >
//             Table
//           </button> */}
//           {/* <button
//             className='bg-sky-300 hover:bg-sky-600 px-4 py-1 rounded-lg'
//             onClick={() => setShowType('card')}
//           >
//             Card
//           </button> */}
//         </div>
//         <button
//           className="bg-red-500 hover:bg-red-700 text-white px-4 py-1 rounded-lg"
//           onClick={handleLogout}
//         >
//           Logout
//         </button>
//       </div>

//       <div className="flex justify-between items-center">
//         <h1 className="text-3xl my-8">Books List</h1>

//         {isAdmin ? (
//           <Link to="/books/create">
//             <MdOutlineAddBox className="text-sky-800 text-4xl" />
//           </Link>
//         ) : (
//           <></>
//         )}
//       </div>

//       {loading ? <Spinner /> : <BooksTable books={books} setBooks={setBooks} />}
//     </div>
//   );
// };

// export default Home;

import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  const [preview, setPreview] = useState(null); // URL for the original image preview
  const [generatedImage, setGeneratedImage] = useState(null); // Data URL for the processed image
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  // Logout handler clears token and navigates to landing page
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  // Handle file input change
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      const previewUrl = URL.createObjectURL(selectedFile);
      setPreview(previewUrl);
      setGeneratedImage(null);
      console.log("The image is successfully uploaded and its URL is created");
    }
  };

  // Convert the image to black and white using canvas
  const handleGenerate = () => {
    if (!preview) return;
    const img = new Image();
    // Prevent cross-origin issues if necessary
    img.crossOrigin = "Anonymous";
    img.src = preview;
    img.onload = () => {
      const canvas = document.createElement("canvas");
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext("2d");
      // Apply grayscale filter
      ctx.filter = "grayscale(100%)";
      ctx.drawImage(img, 0, 0);
      // Get the new image as a data URL
      const bwImage = canvas.toDataURL("image/png");
      console.log(bwImage);
      setGeneratedImage(bwImage);
    };
  };

  // Save the processed image to the database via the backend API
  const handleSave = () => {
    if (!generatedImage) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("image", preview); // Ensure `preview` is a File object
    formData.append("result", generatedImage);
    //formData.append("userId", userId);

    axios
      .post("http://localhost:5555/imageroute", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      })
      .then((res) => {
        setLoading(false);
        alert("Image saved successfully.");
      })
      .catch((err) => {
        setLoading(false);
        console.error(err);
        alert("Failed to save image.");
      });
};


  return (
    <div className="min-h-screen p-4">
      {/* Header with Logout Button */}
      <header className="flex justify-end">
        <button
          onClick={handleLogout}
          className="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded"
        >
          Logout
        </button>
      </header>

      {/* Image Upload and Processing Section */}
      <main className="mt-8 max-w-3xl mx-auto">
        <h1 className="text-2xl font-bold mb-4">
          Upload Prescription & Process Image
        </h1>
        <div className="mb-4">
          <input
            type="file"
            accept="image/*"
            onChange={handleFileChange}
            className="border p-2"
          />
        </div>
        {/* Display Original Image Preview */}
        {preview && (
          <div className="mb-4">
            <h2 className="text-lg font-medium">Original Image Preview:</h2>
            <img
              src={preview}
              alt="Original"
              className="mt-2 max-w-full border rounded"
            />
          </div>
        )}
        {/* Generate Button */}
        {preview && (
          <button
            onClick={handleGenerate}
            className="bg-blue-600 hover:bg-blue-800 text-white px-4 py-2 rounded mb-4"
          >
            Generate Black & White
          </button>
        )}
        {/* Display Processed Black & White Image */}
        {generatedImage && (
          <div className="mb-4">
            <h2 className="text-lg font-medium">Black & White Image:</h2>
            <img
              src={generatedImage}
              alt="Black and White"
              className="mt-2 max-w-full border rounded"
            />
          </div>
        )}
        {/* Save Button */}
        {generatedImage && (
          <button
            onClick={handleSave}
            className="bg-green-600 hover:bg-green-800 text-white px-4 py-2 rounded"
            disabled={loading}
          >
            {loading ? "Saving..." : "Save Image"}
          </button>
        )}
      </main>
    </div>
  );
};

export default Home;
