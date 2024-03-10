import './App.css'
import React from 'react';
import { BrowserRouter ,Routes, Route, } from 'react-router-dom'
import { ProductProvider } from './context/ProductContext';
import ProductPage from './components/ProductPage';
import Productlist from './components/Productlist';
import Home  from './components/Home';
import Comparison from './components/Comparison';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
          {/* <AuthProvider>   */}
          <ProductProvider>
            <Routes>      
              <Route path='/pp' element={<ProductPage/>}/>
              {/* <Route element={<Loginpage/>} path='/login'/>   */}
              <Route element={<Home/>} path='/'/>  
              <Route element={<Productlist/>} path='/productlist'/>  
              <Route element={<Comparison/>} path='/comparison'/>  
              {/* <Route element={<Registerpage/>} path='/register'/>   */}
            </Routes>
            </ProductProvider>
          {/* </AuthProvider> */}
      </BrowserRouter>
    </div>
  );
}

export default App;
