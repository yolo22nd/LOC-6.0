import React, { useState, useEffect } from "react";
import Navbar from "./Navbar";
import Card from "./Card";
import { useLocation } from "react-router-dom";

const Productlist = () => {
  const [data, setData] = useState([]);
  const [render, setRender] = useState(true);
  const { state } = useLocation();
  const getData = async () => {
    const res = await state;
    setData(res);
    if (data) {
      setRender(true);
      console.log(data)
    }
  };
  useEffect(() => {
    getData();
  }, [state]);

  console.log("state: ", state);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 30; // Number of items to display per page

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data.slice(indexOfFirstItem, indexOfLastItem);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <>
      <Navbar />
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
            />
          ))}
      </div>
      <div className="flex justify-center mt-4">
        <nav>
          <ul className="pagination flex">
            {Array.from(
              { length: Math.ceil(data.length / itemsPerPage) },
              (_, index) => (
                <li key={index} className="page-item mr-4">
                  <button
                    onClick={() => paginate(index + 1)}
                    className="page-link w-8 h-8 border-orange-400 border-2 hover:bg-orange-400 rounded-sm"
                  >
                    {index + 1}
                  </button>
                </li>
              )
            )}
          </ul>
        </nav>
      </div>
    </>
  );
};

export default Productlist;
