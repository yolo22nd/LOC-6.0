import './App.css'
import React from 'react';
import { BrowserRouter ,Routes, Route, } from 'react-router-dom'
// import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import ProductPage from './components/ProductPage';
import Productlist from './components/Productlist';
import Home  from './components/Home';
import Comparison from './components/Comparison';

import Register from './components/register';
import Login from './components/login';

import { AuthProvider } from './context/AuthContext';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
          {/* <AuthProvider>   */}
            <Routes>      
              <Route path='/pp' element={<ProductPage/>}/>
              <Route element={<Login/>} path='/login'/>  
              <Route element={<Home/>} path='/'/>  
              <Route element={<Productlist/>} path='/productlist'/>  
              <Route element={<Comparison/>} path='/comparison'/>  
              <Route element={<Register/>} path='/register'/>  
            </Routes>
          {/* </AuthProvider> */}
      </BrowserRouter>
    </div>
  );
}

export default App;
