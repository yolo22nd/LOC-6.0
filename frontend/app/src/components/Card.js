import React, { useEffect, useState, useContext } from "react";
// import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import LocationOnIcon from "@mui/icons-material/LocationOn";
import AccessTimeIcon from "@mui/icons-material/AccessTime";
import FiberManualRecordIcon from "@mui/icons-material/FiberManualRecord";
import KeyboardArrowRightIcon from "@mui/icons-material/KeyboardArrowRight";
import AddIcon from "@mui/icons-material/Add";
import RemoveRedEyeIcon from "@mui/icons-material/RemoveRedEye";


const Card = ({ title, img,currency,price,discount }) => {
  return (
    // <div className="mt-32 ml-8 shadow-2xl w-80 h-[60vh]">
      <div key={"1"} class="rounded-lg overflow-hidden shadow-2xl ml-8 w-80 bg-white mb-8">
        <div className="flex justify-center">
        <img class=" h-96" src={img} alt="" />
        </div>
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2 text-black">
            {title}
          </div>
          <p><span className="font-bold">Price: </span><span>{currency}</span><span>{price}</span></p>
          <p className="font-semibold text-red-500">{discount}</p>
        </div>
      </div>
    // </div>
  );
};

export default Card;

