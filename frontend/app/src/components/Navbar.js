import React, { useContext ,useState} from 'react';
import { Link as RouterLink } from 'react-router-dom';
// import AuthContext from '../context/AuthContext';
import { AppBar, Toolbar, Typography, Button, Box ,TextField} from '@mui/material';
import SearchOutlinedIcon from '@mui/icons-material/SearchOutlined';
import MenuOutlinedIcon from '@mui/icons-material/MenuOutlined';
import CloseOutlinedIcon from '@mui/icons-material/CloseOutlined';
import { styled } from '@mui/system';


function SidebarContent() {
  return (
    <div className="bg-slate-900 text-white w-64 h-screen fixed top-0 left-0 z-8">
      <ul className='mt-12'>
        <li className='p-4'>Profile</li>
        <li className='p-4'>Events</li>
        <li className='p-4'>Settings</li>
      </ul>
    </div>
  );
}

function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      <MenuOutlinedIcon className="mr-4 cursor-pointer z-100" onClick={toggleSidebar} />
      {isOpen && <SidebarContent />}
      {isOpen && (
        <CloseOutlinedIcon
        className="mr-4 cursor-pointer z-10 absolute top-6 left-52" 
          onClick={toggleSidebar}
        />
      )}
    </div>
  );
}



const Navbar = () => {
//   const { user, logOutUser } = useContext(AuthContext);
  const [searchInput, setSearchInput] = useState("");

  const handleChange = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
  };

  return (
    <AppBar position="fixed" style={{backgroundColor:'black'}}>
      <Toolbar>
      <Sidebar className="z-100"/>
       < nav className='bg-black h-16 text-white font-bold flex w-full'>
     <div className='w-16 h-8 ml-2'>
         <img src='https://img.freepik.com/premium-vector/simple-white-letter-p-logo-with-ring-black-background_620194-1320.jpg'/>
       </div>
       <div className='w-[80%]'>
       <ul className='flex'>
         <li className='mt-4 mb-4 mx-8 cursor-pointer border-b-2 hover:text-lime-300 hover:text-lg hover:border-lime-300'><a href='#'></a>Home</li>
         <li className='mt-4 mb-4 mx-8 cursor-pointer border-b-2 hover:text-lime-300 hover:text-lg hover:border-lime-300'><a href='#'></a>About</li>
         <li className='mt-4 mb-4 mx-8 cursor-pointer border-b-2 hover:text-lime-300 hover:text-lg hover:border-lime-300'><a href='#'></a>Contact</li>
       </ul>
       </div>
       <div className='mt-2 w-[20%] text-right mr-4'>
         <button className='bg-white text-slate-900 px-4 py-2 rounded-full'>
          <a href='/register'>Sign In</a>
      </button>
    </div>
  </nav>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
