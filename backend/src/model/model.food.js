import mongoose from "mongoose";
import { Schema, model } from "mongoose";

const foodSchema = new Schema(
  {
    user_id: {
      type: Number,
      required: true
    },
    category: {
      type: String,
    },
    name: {
      type: String,
      required: true,
      trim: true,
    },
    quantity: {
      type: Number,
      min: 0,
    },
    ice: {
      type: Boolean,
      default: false
    },
    registeredAt: {
      type: Date,
      default: Date.now,
    },
  },
  {
    timestamps: true,
    versionKey: false, // __v 제거
  }
);

const Food = model("Food", foodSchema);

export default Food;
