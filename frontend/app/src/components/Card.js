import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";

const Card = ({ title, img, currency, price, discount, onSelect }) => {
  const { state } = useLocation();
  const { parameter } = state || {}; // Extract parameter from the state object

  const [isSelected, setIsSelected] = useState(false);
  const [selectedItems, setSelectedItems] = useState([]);

  useEffect(() => {
    console.log("selectedItems length:", selectedItems.length);
  }, [selectedItems]); // Log selectedItems length whenever it changes

  const handleCardClick = () => {
    // If selectedItems length is less than 2 or the clicked item is already selected, proceed
    if (isSelected || selectedItems.length < 2) {
      setIsSelected(!isSelected);
      // If the item is already selected, remove it from selectedItems
      if (isSelected) {
        const updatedItems = selectedItems.filter((item) => item !== title);
        setSelectedItems(updatedItems);
      } else {
        // If the item is not selected, add it to selectedItems
        setSelectedItems([...selectedItems, title]);
      }
      onSelect(title, !isSelected);
    } else {
      // If more than 2 items are already selected, do nothing
      // You might want to add some feedback to the user, e.g., a toast message
    }
  };

  return parameter ? (
    <div
      key={title}
      className={`rounded-lg overflow-hidden shadow-2xl ml-8 w-80 bg-white mb-8 hover:bg-slate-200 cursor-pointer ${
        isSelected ? "border-2 border-slate-500" : ""
      }`}
      onClick={handleCardClick}
    >
      <div className="flex justify-center">
        <img className="h-96" src={img} alt="" />
      </div>
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2 text-black">{title}</div>
        <p>
          <span className="font-bold">Price: </span>
          <span>{currency}</span>
          <span>{price}</span>
        </p>
        <p className="font-semibold text-red-500">{discount}</p>
      </div>
    </div>
  ) : (
    <div
      key={title}
      className="rounded-lg overflow-hidden shadow-2xl ml-8 w-80 bg-white mb-8"
    >
      <div className="flex justify-center">
        <img className="h-96" src={img} alt="" />
      </div>
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2 text-black">{title}</div>
        <p>
          <span className="font-bold">Price: </span>
          <span>{currency}</span>
          <span>{price}</span>
        </p>
        <p className="font-semibold text-red-500">{discount}</p>
      </div>
    </div>
  );
};

export default Card;
