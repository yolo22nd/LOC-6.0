import './App.css'
import React from 'react';
import { BrowserRouter ,Routes, Route, } from 'react-router-dom'
// import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import Productlist from './components/Productlist';
import Home  from './components/Home';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
          {/* <AuthProvider>   */}
            <Routes>      
              {/* <Route element={<Loginpage/>} path='/login'/>   */}
              <Route element={<Home/>} path='/'/>  
              <Route element={<Productlist/>} path='/productlist'/>  
              {/* <Route element={<Registerpage/>} path='/register'/>   */}
            </Routes>
          {/* </AuthProvider> */}
      </BrowserRouter>
    </div>
  );
}

export default App;
