import express from "express";
import { PORT, mongoDBURL } from "./config.js";
import mongoose from "mongoose";
import cors from "cors";
import dotenv from "dotenv";

import signupRoutes from "./routes/signupRoute.js";
import loginRoutes from "./routes/loginRoute.js";
import imageRoutes from "./routes/imageRoute.js"; // Adjust path if needed

dotenv.config();

const app = express();

app.use(express.json({ limit: "50mb" }));  
app.use(express.urlencoded({ extended: true, limit: "50mb" })); 
app.use(cors({
  origin: "http://localhost:5173",
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"],
  credentials: true,
}));


// Serve static files from the 'uploads' directory (for accessing uploaded images)
app.use("/uploads", express.static("uploads"));

app.get("/", (request, response) => {
  console.log(request);
  return response.status(234).send("Welcome To MERN Stack Tutorial");
});

// Routes
app.use("/signup", signupRoutes);
app.use("/login", loginRoutes);
app.use('/imageroute', imageRoutes);

// Connect to MongoDB and start the server
mongoose
  .connect(mongoDBURL)
  .then(() => {
    console.log("App connected to database");
    app.listen(PORT, () => {
      console.log(`App is listening to port: ${PORT}`);
    });
  })
  .catch((error) => {
    console.log(error);
  });

const db = mongoose.connection;
db.on("error", console.error.bind(console, "MongoDB connection error:"));
db.once("open", () => console.log("Connected to MongoDB"));
