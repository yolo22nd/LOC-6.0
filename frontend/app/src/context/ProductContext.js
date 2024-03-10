import { createContext, useState, useEffect } from "react";

const ProductContext = createContext()

export default ProductContext;

export const ProductProvider = ({children}) => {

    let [minPrice, setMinPrice] = useState("");
    let [maxPrice, setMaxPrice] = useState("");
    let [sortBy, setSortBy] = useState("");
    let [searchInput, setSearchInput] = useState("");
    // let [minPrice, setMinPrice] = useState("0");

    let contextData = {
        minPrice:minPrice,
        setMinPrice:setMinPrice,
        maxPrice:maxPrice,
        setMaxPrice:setMaxPrice,
        sortBy:sortBy,
        setSortBy:setSortBy,
        searchInput:searchInput,
        setSearchInput:setSearchInput
    }

    return(
        <ProductContext.Provider value={contextData}>
            {children}
        </ProductContext.Provider>
    )
}