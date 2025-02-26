# 🏥 Medimate - AI-Powered Prescription Processing  

### 🚀 An AI-powered system for digitizing handwritten prescriptions, detecting fraud, and streamlining medicine ordering.
---

## 📌 **Project Overview**  
The **Pharmacist Assistant** is an AI-powered application that:  
✅ **Extracts medicine details** from handwritten prescriptions using **OCR**.  
✅ **Detects fraudulent prescriptions** (forgery, alterations, and duplicate usage).  
✅ **Checks medicine availability** and suggests alternatives if unavailable.  
✅ **Enables one-tap online ordering** of prescribed medicines.  

---

## 🔥 **Key Features**  
- **Handwritten Prescription Recognition** (OCR with FastAPI & Google Vision API).  
- **Fraud Detection** (Image comparison, doctor verification, and signature forgery detection).  
- **Medicine Matching** (Database lookup & alternative suggestions).  
- **Order Processing & Tracking** (Node.js backend + MongoDB).  

---

## 🛠 **Tech Stack**
### **Backend**  
- **FastAPI (Python)** → OCR & AI processing  
- **Node.js + Express.js** → Order management  
- **MongoDB (GridFS)** → Prescription storage   

### **Frontend**  
- **React.js** → User Interface  
- **Tailwind CSS** → UI styling  

### **AI & OCR**  
- **Google Vision API** → Text extraction  
- **OpenCV** → Image preprocessing  
- **Deep Learning (CNN/RNN)** → Signature forgery detection  

---

## 🏗 **Project Setup & Installation**  

### **📌 1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/Pharmacist-assistant.git
cd Pharmacist-assistant
```

### **📌 2️⃣ Set Up the Backend**  
a. Creating environment
```bash
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Linux/macOS)
venv\Scripts\activate  # Activate (Windows)
```
b. Installing the required dependencies
```bash
pip install -r requirements.txt
```
c. Run FastAPI backend
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### **📌 3️⃣ Set Up the Frontend** 
a. Installing all the React dependenies
```bash
cd frontend
npm install
```
b. Run React
```bash
npm start
```

### **📌 4️⃣ Database & Storage Setup**  
a. Installing MongoDB
```bash
mongod --dbpath ./data/db
```
b. Configuring environment variables
```bash
MONGO_URI=mongodb://localhost:27017/pharmacy
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
SECRET_KEY=your_secret_key
```


