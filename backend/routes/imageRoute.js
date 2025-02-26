import express from "express";
import multer from "multer";
import { Image } from "../models/Image.js";
import mongoose from "mongoose";
import fs from "fs";

const router = express.Router();

// Multer storage setup (stores files locally in 'uploads/' directory)
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/");
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  },
});

const upload = multer({ storage });

// Route to handle image upload and processing
// router.post("/", upload.single("image"), async (req, res) => {
//   try {
//     const { userId, result } = req.body;
    
//     if (!req.file) {
//       return res.status(400).json({ message: "No file uploaded" });
//     }

//     // Save image path and processed result in the database
//     const newImage = new Image({
//       user: new mongoose.Types.ObjectId(userId),
//       imageUrl: req.file.path, // Store the local path or cloud URL
//       result,
//     });

//     await newImage.save();
//     res.status(201).json({ message: "Image saved successfully", image: newImage });
//   } catch (error) {
//     console.error(error);
//     res.status(500).json({ message: "Internal server error" });
//   }
// });

router.post("/", upload.single("image"), async (req, res) => {
    try {
      const { userId } = req.body; // Ensure userId is received correctly
  
      if (!req.file) {
        return res.status(400).json({ message: "No file uploaded" });
      }
  
      // Save image path in DB
      const newImage = new Image({
        user: userId ? new mongoose.Types.ObjectId(userId) : null, // Handle missing userId
        imageUrl: req.file.path, // Store the local path
      });
  
      await newImage.save();
      res.status(201).json({ message: "Image saved successfully", image: newImage });
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: "Internal server error" });
    }
  });
  
// Route to get all images for a user
router.get("/:userId", async (req, res) => {
  try {
    const images = await Image.find({ user: req.params.userId }).sort({ uploadedAt: -1 });
    res.status(200).json(images);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: "Internal server error" });
  }
});

export default router;
