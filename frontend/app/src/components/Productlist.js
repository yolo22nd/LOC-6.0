import React, { useState, useEffect } from "react";
import Navbar from "./Navbar";
import Card from "./Card";
import { useLocation } from "react-router-dom";
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';

const Productlist = () => {
  const [data, setData] = useState([]);
  const [render, setRender] = useState(true);
  const { state } = useLocation();
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 30; // Number of items to display per page
  const maxPageNumbers = 3; // Maximum number of page numbers to display

  const getData = async () => {
    const res = await state;
    if (res.data) {
      setData(res.data);
    } else {
      setData(res);
    }
    if (data) {
      setRender(true);
    }
  };

  useEffect(() => {
    getData();
  }, [state]);

  // Calculate total number of pages
  const totalPages = Math.ceil(data.length / itemsPerPage);

  // Calculate the index of the last and first item on the current page
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data?.slice(indexOfFirstItem, indexOfLastItem);

  // Generate an array of page numbers to display
  const generatePageNumbers = () => {
    const pageNumbers = [];
    const startPage = Math.max(currentPage - Math.floor(maxPageNumbers / 2), 1);
    const endPage = Math.min(startPage + maxPageNumbers - 1, totalPages);

    for (let i = startPage; i <= endPage; i++) {
      pageNumbers.push(i);
    }
    return pageNumbers;
  };

  // Function to handle pagination
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  const handleSelect = (title, isSelected) => {
    // Handle selection logic here
    console.log(`${title} is selected: ${isSelected}`);
  };

  return (
    <>
      <Navbar />
      {state.parameter && (
        <div className="flex justify-end p-4 pt-24 flex justify-center">
          <button className="bg-orange-500 text-white px-4 py-2 rounded-md">Compare</button>
        </div>
      )}
      <div className="flex flex-wrap justify-center pt-32 ml-64">
        {render &&
          currentItems.map((product) => (
            <Card 
              key={product.pid}
              title={product.title}
              img={product.images?.[0]}
              currency={product.currency}
              price={product.price}
              discount={product.discount}
              onSelect={handleSelect}
            />
          ))}
      </div>
      <div className="flex justify-center mt-4">
        <nav>
          <ul className="pagination flex">
            {currentPage > 1 && (
              <li className="page-item mr-4">
                <button
                  onClick={() => paginate(currentPage - 1)}
                  className="page-link w-8 h-8 "
                >
                  <ArrowBackIosIcon/>
                </button>
              </li>
            )}
            {generatePageNumbers().map((pageNumber) => (
              <li key={pageNumber} className="page-item mr-4">
                <button
                  onClick={() => paginate(pageNumber)}
                  className={`page-link w-8 h-8 border-orange-400 border-2 hover:bg-orange-400 rounded-sm ${
                    pageNumber === currentPage ? "bg-orange-400" : ""
                  }`}
                >
                  {pageNumber}
                </button>
              </li>
            ))}
            {currentPage < totalPages && (
              <li className="page-item mr-4">
                <button
                  onClick={() => paginate(currentPage + 1)}
                  className="page-link w-8 h-8"
                >
                  <ArrowForwardIosIcon/>
                </button>
              </li>
            )}
          </ul>
        </nav>
      </div>
    </>
  );
};

export default Productlist;
