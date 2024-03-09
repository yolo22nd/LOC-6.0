import { useEffect } from "react";
import axios from "./Axios";

const ProductPage = () => {
    const getData = async () => {
        const res = await axios.get('fetchall/', { headers: { 'Content-Type': 'application/json' } });
        console.log(res)
    }
    useEffect(() => {
        getData();
    },[])
  return (
    <div>
      <div className="max-w-2xl mx-auto bg-white p-8 shadow-md rounded-md">
        {/* Product Title */}
        <h1 className="text-2xl font-semibold mb-4">Product Title</h1>

        {/* Product Images */}
        <div className="grid grid-cols-3 gap-4 mb-6">
          <img
            src="image_url_1.jpg"
            alt="Product Image 1"
            className="w-full h-32 object-cover rounded-md"
          />
          <img
            src="image_url_2.jpg"
            alt="Product Image 2"
            className="w-full h-32 object-cover rounded-md"
          />
          <img
            src="image_url_3.jpg"
            alt="Product Image 3"
            className="w-full h-32 object-cover rounded-md"
          />
        </div>

        {/* Product Information */}
        <div className="grid grid-cols-2 gap-4 mb-6">
          {/* Product Details */}
          <div>
            <p className="text-lg font-semibold mb-2">Product Details</p>
            <ul className="list-disc pl-4">
              <li>
                <strong>Brand:</strong> Brand Name
              </li>
              <li>
                <strong>Stock:</strong> In Stock
              </li>
              <li>
                <strong>Flipkart Assured:</strong> Yes
              </li>
              <li>
                <strong>Price:</strong> $99.99
              </li>
              <li>
                <strong>Original Price:</strong> $129.99
              </li>
              <li>
                <strong>Discount:</strong> 23%
              </li>
              <li>
                <strong>Seller:</strong> Seller Name
              </li>
              <li>
                <strong>Seller Rating:</strong> 4.5
              </li>
              <li>
                <strong>Return Policy:</strong> Easy Returns
              </li>
              <li>
                <strong>Category:</strong> Main Category | Subcategory 1 |
                Subcategory 2
              </li>
            </ul>
          </div>

          {/* Product Description */}
          <div>
            <p className="text-lg font-semibold mb-2">Product Description</p>
            <p className="text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
              gravida diam eget metus bibendum, at dapibus urna efficitur. ...
            </p>
          </div>
        </div>

        {/* Product Highlights */}
        <div className="mb-6">
          <p className="text-lg font-semibold mb-2">Product Highlights</p>
          <ul className="list-disc pl-4">
            <li>Highlight 1</li>
            <li>Highlight 2</li>
            <li>Highlight 3</li>
          </ul>
        </div>

        {/* Product Specifications */}
        <div className="mb-6">
          <p className="text-lg font-semibold mb-2">Product Specifications</p>
          <ul className="list-disc pl-4">
            <li>
              <strong>Specification 1:</strong> Value 1
            </li>
            <li>
              <strong>Specification 2:</strong> Value 2
            </li>
            <li>
              <strong>Specification 3:</strong> Value 3
            </li>
          </ul>
        </div>

        {/* Product Reviews */}
        <div>
          <p className="text-lg font-semibold mb-2">Product Reviews</p>
          <div className="flex items-center">
            <p className="mr-2">Average Rating: 4.5</p>
            <p>(123 Reviews)</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductPage;
