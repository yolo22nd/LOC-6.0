import React, { useEffect ,useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import ProductContext from '../context/ProductContext';
import { AppBar, Toolbar, Typography, Button, Box ,TextField} from '@mui/material';
import MenuOutlinedIcon from '@mui/icons-material/MenuOutlined';
import CloseOutlinedIcon from '@mui/icons-material/CloseOutlined';
import SearchIcon from '@mui/icons-material/Search';
// import Slider from './Slider';
import axios from './Axios'


const Naavbar2 = () => {
  const naviagte = useNavigate();

  const searchContent = () => {
    let s = document.getElementById("search-content")?.value;
    if (s) {
    //   setSearchInput(s);
      console.log(s);
    }
  };


  useEffect(() => {}, []);

  return (
    <AppBar position="fixed" style={{ backgroundColor: "#fff" }}>
      <Toolbar>
        {/* <Sidebar className="z-100" /> */}
        <nav className="bg-white h-16 text-black font-bold flex w-full">
          {/* <div className='w-16 h-8 ml-2'>
         <img src='https://img.freepik.com/premium-vector/simple-white-letter-p-logo-with-ring-black-background_620194-1320.jpg'/>
       </div> */}
          <div className="w-[60%]">
            <ul className="flex">
              <li className="mt-4 mb-4 mx-8 cursor-pointer text-orange-500 hover:text-orange-700 hover:text-lg">
                <a href="#"></a>Home
              </li>
              <li className="mt-4 mb-4 mx-8 cursor-pointer text-orange-500 hover:text-orange-700 hover:text-lg">
                <a href="#"></a>About
              </li>
              <li className="mt-4 mb-4 mx-8 cursor-pointer text-orange-500 hover:text-orange-700 hover:text-lg">
                <a href="#"></a>Contact
              </li>
            </ul>
          </div>
          <div className="mt-2 w-[40%] text-right mr-4">
            <div className="relative mb-4 flex w-full flex-wrap items-stretch">
              <div className="flex w-[60vh] bg-orange-100 shadow-lg border-orange-400 border-2 rounded-full mr-4">
                <SearchIcon className="ml-2 mt-2 mr-2" />
                <input
                  type="search"
                  className="relative m-0 mr-2 block w-[1px] min-w-0 flex-auto bg-transparent px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-black outline-none transition duration-200 ease-in-out focus:z-[3]   focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:placeholder:text-neutral-200 dark:focus:border-primary"
                  placeholder="Search"
                  aria-label="Search"
                  aria-describedby="button-addon1"
                  id='search-content'
                  onChange={() => searchContent()}
                />
                <button
                  className="text-gray-500 text-sm mr-2"
                //   onClick={() => handleClick()}
                >
                  Search
                </button>
              </div>
              <button className="bg-orange-500 text-white px-4 py-2 rounded-full">
                <a href="/register">Sign In</a>
              </button>
            </div>
          </div>
        </nav>
      </Toolbar>
    </AppBar>
  );
};

export default Naavbar2;
