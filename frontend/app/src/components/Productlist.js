import React, { useState } from "react";
import Navbar from "./Navbar";
import Card from "./Card";

const products =[
    {
      "title": "Bastex Back Cover for Moto G9 (Multicolor)",
      "url": "https://www.flipkart.com/bastex-back-cover-moto-g9/p/itmb772e270a8476",
      "pid": "itmb772e270a8476",
      "formatted_url": "https://www.flipkart.com/product/p/itmb772e270a8476",
      "brand": "",
      "stock": "",
      "f_assured": false,
      "price": 219,
      "currency": "INR",
      "original_price": 999,
      "discount": "78% off",
      "images": "",
      "seller": "",
      "seller_rating": "",
      "return_policy": "",
      "description": "Bastex back covers are the best attractive accessory to make your mobile unique from other models. The Premium case is made out of a light, durable plastic called Polycarbonate. It is strong enough to protect it from bumps, drops, and scratches. Wide array of designs and models. A raised bezel protects your display when mobile is laid flat, and the volume and power buttons are explicitly carved, so all buttons and ports are easily accessible. This case is 100% compatible with your regular charger and headphones. Kindly Note: There may be a slight change in the color of the design printed on the case as seen on the website, as there can be different monitors/tablets/smartphones settings.",
      "highlights": "Suitable For: Mobile | Material: Plastic | Theme: For Her | Type: Back Cover",
      "specifications": [
        {"Sales Package": "1 Mobile Cover"},
        {"Model Number": "ABC1399T37958-Teddy bear Gift Girlie"},
        {"Designed For": "Moto G9"},
        {"Brand Color": "Multicolor"},
        {"Pack of": "1"}
      ],
      "formatted_specifications": "Sales Package: 1 Mobile Cover | Model Number: ABC1399T37958-Teddy bear Gift Girlie | Designed For: Moto G9 | Brand Color: Multicolor | Pack of: 1",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "3fff7830-b71e-5968-9f2a-af7f89378ad0",
      "scraped_at": "06/15/22"
    },
    {
      "title": "Devilart Back Cover for Lava X11 (Multicolor, Waterproof, Silicon)",
      "url": "https://www.flipkart.com/devilart-back-cover-lava-x11/p/itmfbqyhwqvedcdn",
      "pid": "itmfbqyhwqvedcdn",
      "formatted_url": "https://www.flipkart.com/product/p/itmfbqyhwqvedcdn",
      "brand": "",
      "stock": "",
      "f_assured": false,
      "price": 188,
      "currency": "INR",
      "original_price": 659,
      "discount": "71% off",
      "images": [
        "https://rukminim1.flixcart.com/image/jpk2z680/cases-covers/back-cover/c/q/w/devilart-x41-318-original-imafbzzabv9apksq.jpeg",
        "https://rukminim1.flixcart.com/image/jur9nrk0/cases-covers/back-cover/z/q/f/devilart-sam-a40-142-original-imafyf4refjpdvpp.jpeg",
        "https://rukminim1.flixcart.com/image/jur9nrk0/cases-covers/back-cover/z/q/f/devilart-sam-a40-142-original-imafyf4sstnyraz9.jpeg"
      ],
      "seller": "",
      "seller_rating": "",
      "return_policy": "",
      "description": "Now you can stylishly & easily protect your smartphone with this modern case protection. This case covers the back and corners of your smartphone with an impact-resistant, flexible Soft shell while still providing access to all ports and buttons. Designed for your phone, this sleek and lightweight case is the perfect way to show off your style. This case acts as the perfect weapon you require to guard your phone from everything unwanted. It covers the entire front of the case with the artwork. It has permanent embedded designs with high print quality, which are long-lasting. Hence your design won't peel off. This case fully covers the backside of your mobile, and hence you do not have to replace the original back cover.",
      "highlights": "Suitable For: Mobile | Material: Silicon | Theme: Patterns | Type: Back Cover",
      "specifications": [
        {"Sales Package": "1 Designer Case"},
        {"Model Number": "X11_318"},
        {"Designed For": "Lava X11"},
        {"Brand Color": "Multicolor"},
        {"Pack of": "1"},
        {"Other Features": "Shock Proof"}
      ],
      "formatted_specifications": "Sales Package: 1 Designer Case | Model Number: X11_318 | Designed For: Lava X11 | Brand Color: Multicolor | Pack of: 1 | Other Features: Shock Proof",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "0e6e67fb-df1d-51a6-a23d-8a1ddfe79dc0",
      "scraped_at": "06/15/22"
    },
    {
      "title": "SY Gifts Back Cover for Apple iPhone 7 (Multicolor)",
      "url": "https://www.flipkart.com/sy-gifts-back-cover-apple-iphone-7/p/itm99e6ac4c0b9cd",
      "pid": "itm99e6ac4c0b9cd",
      "formatted_url": "https://www.flipkart.com/product/p/itm99e6ac4c0b9cd",
      "brand": "",
      "stock": "",
      "f_assured": false,
      "price": 199,
      "currency": "INR",
      "original_price": 599,
      "discount": "66% off",
      "images": "",
      "seller": "",
      "seller_rating": "",
      "return_policy": "",
      "description": "Samurai Mobile Back Cover For iPhone 7",
      "highlights": "Suitable For: Mobile | Material: Plastic | Theme: No Theme | Type: Back Cover",
      "specifications": [
        {"Sales Package": "1 Mobile Back Cover"},
        {"Model Number": "SYG2505 4548"},
        {"Designed For": "Apple iPhone 7"},
        {"Brand Color": "Samurai"},
        {"Pack of": "1"}
      ],
      "formatted_specifications": "Sales Package: 1 Mobile Back Cover | Model Number: SYG2505 4548 | Designed For: Apple iPhone 7 | Brand Color: Samurai | Pack of: 1",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "3f8a411a-2c26-5fea-a0ae-ee44dd75aec0",
      "scraped_at": "06/15/22"
    },
    {
      "title": "Exclusivebay Back Cover for Micromax Canvas 5 E481 (Black, White)",
      "url": "https://www.flipkart.com/exclusivebay-back-cover-micromax-canvas-5-e481/p/itmafcf69ec9cf97",
      "pid": "itmafcf69ec9cf97",
      "formatted_url": "https://www.flipkart.com/product/p/itmafcf69ec9cf97",
      "brand": "",
      "stock": "Hurry, Only 5 left!",
      "f_assured": true,
      "price": 219,
      "currency": "INR",
      "original_price": 999,
      "discount": "78% off",
      "images": "",
      "seller": "DaadujiOfficial",
      "seller_rating": 3.3,
      "return_policy": "7 Days Replacement Policy",
      "description": "Exclusivebay back covers are the best attractive accessory to make your mobile unique from other models. The Premium case is made out of a light, durable plastic called Polycarbonate. It is strong enough to protect it from bumps, drops, and scratches. Wide array of designs and models. A raised bezel protects your display when mobile is laid flat, and the volume and power buttons are explicitly carved, so all buttons and ports are easily accessible. This case is 100% compatible with your regular charger and headphones. Kindly Note: There may be a slight change in the color of the design printed on the case as seen on the website, as there can be different monitors/tablets/smartphones settings.",
      "highlights": "Suitable For: Mobile | Material: Plastic | Theme: Quotes/Signs/Symbols | Type: Back Cover",
      "specifications": [],
      "formatted_specifications": "",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "dc31f707-dea0-5a4d-bd7f-f7280fa253c9",
      "scraped_at": "06/15/22"
    },
    {
      "title": "Coolboys Back Cover for Tecno KE-6 / KE6 (Purple, Waterproof, Silicon)",
      "url": "https://www.flipkart.com/coolboys-back-cover-tecno-ke-6-ke6/p/itm414c308bcbb71",
      "pid": "itm414c308bcbb71",
      "formatted_url": "https://www.flipkart.com/product/p/itm414c308bcbb71",
      "brand": "",
      "stock": "",
      "f_assured": false,
      "price": 197,
      "currency": "INR",
      "original_price": 659,
      "discount": "70% off",
      "images": [
        "https://rukminim1.flixcart.com/image/kka1si80/cases-covers/back-cover/u/k/u/1261057-flanker-original-imafzns6tu78yxvg.jpeg",
        "https://rukminim1.flixcart.com/image/kk2wl8w0/cases-covers/back-cover/d/r/m/242043-sam-gadgets-world-original-imafzgkepgxfnazh.jpeg",
        "https://rukminim1.flixcart.com/image/kklhbbk0/cases-covers/back-cover/h/p/t/246133-sam-gadgets-world-original-imafzwzmcuqqae6j.jpeg",
        "https://rukminim1.flixcart.com/image/kklhbbk0/cases-covers/back-cover/h/a/v/246133-sam-gadgets-world-original-imafzwzmghdhmemq.jpeg",
        "https://rukminim1.flixcart.com/image/kk2wl8w0/cases-covers/back-cover/x/s/l/242043-sam-gadgets-world-original-imafzgkeyu5aaxmy.jpeg"
      ],
      "seller": "",
      "seller_rating": "",
      "return_policy": "",
      "description": "Now you can stylishly & easily protect your smartphone with this modern case protection. This case covers the back and corners of your smartphone with an impact-resistant, flexible Soft shell while still providing access to all ports and buttons. Designed for your phone, this sleek and lightweight case is the perfect way to show off your style. This case acts as the perfect weapon you require to guard your phone from everything unwanted. It covers the entire front of the case with the artwork. It has permanent embedded designs with high print quality, which are long-lasting. Hence your design won't peel off. This case fully covers the backside of your mobile, and hence you do not have to replace the original back cover.",
      "highlights": "Suitable For: Mobile | Material: Silicon | Theme: Patterns | Type: Back Cover",
      "specifications": [
        {"Sales Package": "1 Designer soft Silicon Cover"},
        {"Model Number": "1264057"},
        {"Designed For": "Tecno KE-6 / KE6"},
        {"Brand Color": "Purple"},
        {"Pack of": "1"},
        {"Other Features": "Shock Proof"}
      ],
      "formatted_specifications": "Sales Package: 1 Designer soft Silicon Cover | Model Number: 1264057 | Designed For: Tecno KE-6 / KE6 | Brand Color: Purple | Pack of: 1 | Other Features: Shock Proof",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "265428fc-4ed3-5de8-b7f7-4e1e27231609",
      "scraped_at": "06/15/22"
    },
    {
      "title": "quadronic Back Cover for Redmi Note 9 Pro Max, Smoke Translucent Shock Proof Smooth Rubberized Matte Hard Back Case Cover (Green)",
      "url": "https://www.flipkart.com/quadronic-back-cover-redmi-note-9-pro-max-smoke-translucent-shock-proof-smooth-rubberized-matte-hard-case/p/itm89ba80122e631",
      "pid": "itm89ba80122e631",
      "formatted_url": "https://www.flipkart.com/product/p/itm89ba80122e631",
      "brand": "",
      "stock": "Hurry, Only a few left!",
      "f_assured": true,
      "price": 179,
      "currency": "INR",
      "original_price": 398,
      "discount": "55% off",
      "images": [],
      "seller": "m s store",
      "seller_rating": 3.8,
      "return_policy": "7 Days Replacement Policy",
      "description": "",
      "highlights": "Suitable For: Mobile | Material: Plastic, Rubber | Theme: No Theme | Type: Back Cover",
      "specifications": [],
      "formatted_specifications": "",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "54d44499-7321-5a4d-87c8-8ff13cf69d5e",
      "scraped_at": "06/15/22"
    },
    {
      "title": "MotohunK 1 Car Body Cover, 2 Light 1 Remote Combo",
      "url": "https://www.flipkart.com/motohunk-1-car-body-cover-2-light-remote-combo/p/itmde11bb2749a5c",
      "pid": "itmde11bb2749a5c",
      "formatted_url": "https://www.flipkart.com/product/p/itmde11bb2749a5c",
      "brand": "",
      "stock": "",
      "f_assured": false,
      "price": 1499,
      "currency": "INR",
      "original_price": 1999,
      "discount": "25% off",
      "images": [],
      "seller": "Matguwanwala",
      "seller_rating": 3.2,
      "return_policy": "7 Days Replacement Policy",
      "description": "Material Protects Your Vehicle Against Wet, Humid And Dusty Climatic Conditions. Hi-Performance Fabric Naturally Resists Moisture, Fungus And Expels Stale Odour. Ultrasonic Welding Seals Seams Tight And Securely (Other Covers Use Common Thread) Keeps Your Vehicle Cooler, Dry And Dust Free, It Remains Unaffected By Climatic Conditions Uses Reinforced Side Grommets For Cover Tie-Down Uv Stable Materials Ensure A Long Life. 2x T10 5050 RGB Led Light Bulbs With 16 Super RGB Colorful SMD Easy installation, just plug & play. 1. Flash mode: Colorful dazzling changes, 2. Strobe mode: Colorful gradual changes, 3. Fade mode: Colorful with dazzling changes and fade in and out, 4. Smooth mode: Flashing between red and blue.",
      "highlights": "Car Body Cover | Mercedes-Benz | E-Class All Terrain | Contains: 1 Car Body Cover, 2 Light 1 Remote",
      "specifications": [],
      "formatted_specifications": "",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "19135e98-f882-53d8-b45b-13378b8fa5df",
      "scraped_at": "06/15/22"
    },
    {
      "title": "Zaapy Back Cover for Vivo S1, Vivo Z1x (Blue)",
      "url": "https://www.flipkart.com/zaapy-back-cover-vivo-s1-z1x/p/itm491e9862c078c",
      "pid": "itm491e9862c078c",
      "formatted_url": "https://www.flipkart.com/product/p/itm491e9862c078c",
      "brand": "",
      "stock": "Hurry, Only 5 left!",
      "f_assured": true,
      "price": 206,
      "currency": "INR",
      "original_price": 899,
      "discount": "77% off",
      "images": [],
      "seller": "ZAPPY1",
      "seller_rating": 3.8,
      "return_policy": "7 Days Replacement Policy",
      "description": "premium quality polycarbonate material which is durable and lightweight that ensures sleek and compact look for your Mobile phone. Every Printed Designer Pouch is printed with precision and designed in a way that it perfectly fits onto the back of the mobile phone.",
      "highlights": "Suitable For: Mobile | Material: Plastic | Theme: Animals/Birds/Nature | Type: Back Cover",
      "specifications": [
        {"Sales Package": "1 back cover"},
        {"Model Number": "3DSM-VVO S1-9875"},
        {"Designed For": "Vivo S1, Vivo Z1x"},
        {"Brand Color": "Blue"},
        {"Pack of": "1"}
      ],
      "formatted_specifications": "Sales Package: 1 back cover | Model Number: 3DSM-VVO S1-9875 | Designed For: Vivo S1, Vivo Z1x | Brand Color: Blue | Pack of: 1",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "fead33d3-732b-5e6c-83b6-1c6c077016ce",
      "scraped_at": "06/15/22"
    },
    {
      "title": "Nassion Back Cover for Infinix Smart 5A (Multicolor, Grip Case, Silicon)",
      "url": "https://www.flipkart.com/nassion-back-cover-infinix-smart-5a/p/itmc97f4193611cb",
      "pid": "itmc97f4193611cb",
      "formatted_url": "https://www.flipkart.com/product/p/itmc97f4193611cb",
      "brand": "",
      "stock": "Hurry, Only 5 left!",
      "f_assured": true,
      "price": 199,
      "currency": "INR",
      "original_price": 799,
      "discount": "75% off",
      "images": [
        "https://rukminim1.flixcart.com/image/ksnjp8w0/cases-covers/back-cover/h/x/6/inf-smr-5a-689-king-maker-original-imag66cfzvhfyxve.jpeg",
        "https://rukminim1.flixcart.com/image/ksnjp8w0/cases-covers/back-cover/6/x/v/inf-smr-5a-689-king-maker-original-imag66cfdn8hbjxf.jpeg",
        "https://rukminim1.flixcart.com/image/ksnjp8w0/cases-covers/back-cover/f/f/c/inf-smr-5a-689-king-maker-original-imag66cfsjkw2p8g.jpeg",
        "https://rukminim1.flixcart.com/image/ksnjp8w0/cases-covers/back-cover/a/l/u/inf-smr-5a-689-king-maker-original-imag66cfscbpctnu.jpeg",
        "https://rukminim1.flixcart.com/image/ksnjp8w0/cases-covers/back-cover/2/v/y/inf-smr-5a-689-king-maker-original-imag66cfz5rftg3y.jpeg"
      ],
      "seller": "",
      "seller_rating": "",
      "return_policy": "7 Days Easy Return",
      "description": "Nassion brings to you this Silicone Grip Case, which is compatible with Infinix Smart 5A. This cover is made of silicon and comes in multicolor. It has a slim design that adds minimal bulk to the phone. The case is easy to install and remove. It provides easy access to all buttons, controls, and ports without having to remove the case. The precise cutouts and openings enable you to use all features of your device.",
      "highlight s": "Suitable For: Mobile | Material: Silicon | Theme: No Theme | Type: Back Cover",
      "specifications": [
        {"Sales Package": "1 Silicone Grip Case"},
        {"Model Number": "INFIN 5A 689"},
        {"Designed For": "Infinix Smart 5A"},
        {"Brand Color": "Multicolor"},
        {"Pack of": "1"}
      ],
      "formatted_specifications": "Sales Package: 1 Silicone Grip Case | Model Number: INFIN 5A 689 | Designed For: Infinix Smart 5A | Brand Color: Multicolor | Pack of: 1",
      "avg_rating": "",
      "reviews_count": "",
      "category": "",
      "sub_category_1": "",
      "sub_category_2": "",
      "breadcrumbs": "",
      "payment_options": "",
      "uniq_id": "76a8a33b-fd6e-5f60-bdba-9e6fcafc45d8",
      "scraped_at": "06/15/22"
    }
  ]; 

const Productlist = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 6; // Number of items to display per page

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = products.slice(indexOfFirstItem, indexOfLastItem);

  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  return (
    <>
      <Navbar />
      <div className="flex flex-wrap justify-center pt-32 ml-64">
        {currentItems.map((product) => (
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
            {Array.from({ length: Math.ceil(products.length / itemsPerPage) }, (_, index) => (
              <li key={index} className="page-item mr-4">
                <button onClick={() => paginate(index + 1)} className="page-link w-8 h-8 border-orange-400 border-2 hover:bg-orange-400 rounded-sm">
                  {index + 1}
                </button>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </>
  );
};

export default Productlist;
