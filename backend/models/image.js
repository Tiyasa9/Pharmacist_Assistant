import mongoose from "mongoose";

const imageSchema = new mongoose.Schema(
  {
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User", // Reference to the User model
      required: true,
    },
    imageUrl: {
      type: String, // Stores image path or cloud URL
      required: true,
    },
    result: {
      type: String, // Stores ML model output (e.g., classification result)
    },
    uploadedAt: {
      type: Date,
      default: Date.now,
    },
  },
  { timestamps: true }
);

export const Image = mongoose.model("Image", imageSchema);
