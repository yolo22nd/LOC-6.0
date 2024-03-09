import React from 'react'
import Navbar from './Navbar'
import Animation from'../assets/Business Analysis.gif'
import Star from'../assets/5 Star Rating.gif'
import Ai from'../assets/aii.png'
import Comparison from '../assets/comparison.png'
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Accordian from './Accordian.js';
import { useNavigate } from 'react-router-dom'
import axios from './Axios.js'


const Home = () => {
    var settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true, // Enable automatic sliding
        autoplaySpeed: 3000,
      };
      const navigate=useNavigate();
      const accordionItems = [
        {
          title: 'What is a product comparison website?',
          content: 'A product comparison website is a platform where users can compare various products and services across different brands and categories to make informed purchasing decisions.',
        },
        {
          title: 'How does a product comparison website work?',
          content: 'Product comparison websites gather information about products from various sources and present them to users in a structured format, allowing them to compare features, prices, reviews, and other relevant information side by side.',
        },
        {
          title: 'What types of products can I compare on a product comparison website?',
          content: 'Product comparison websites typically cover a wide range of categories, including electronics, appliances, clothing, home goods, automotive, financial products, and more.',
        },
        {
          title: 'Why should I use a product comparison website?',
          content: 'Product comparison websites save you time and effort by providing a comprehensive overview of products available in the market, helping you find the best deals, features, and options tailored to your needs.',
        },
        {
          title: 'Are the prices on product comparison websites accurate?',
          content: 'While product comparison websites strive to provide accurate pricing information, prices may vary depending on factors such as location, availability, and ongoing promotions. Always verify prices directly on the retailer\'s website before making a purchase.',
        },
        {
          title: 'How can I trust the reviews and ratings on a product comparison website?',
          content: 'Product comparison websites aggregate reviews and ratings from multiple sources, including verified purchasers, expert reviewers, and editorial teams. Look for websites that disclose their review methodologies and prioritize platforms with transparent review processes.',
        },
        {
          title: 'Can I filter and customize my product search on a product comparison website?',
          content: 'Yes, most product comparison websites offer advanced search and filtering options, allowing users to refine their product searches based on criteria such as price range, brand, features, customer ratings, and more.',
        },
        {
          title: 'Is my personal information safe when using a product comparison website?',
          content: 'Reputable product comparison websites prioritize user privacy and security, employing encryption protocols and data protection measures to safeguard personal information. However, it\'s essential to review the website\'s privacy policy and terms of service to understand how your data is handled.',
        },
        {
          title: 'Can I purchase products directly from a product comparison website?',
          content: 'While some product comparison websites may offer direct purchasing options, many serve as informational platforms that redirect users to third-party retailers or affiliate partners to complete their purchases. Always ensure you\'re transacting with trusted sellers and secure payment gateways.',
        },
        {
          title: 'Are there any fees or charges associated with using a product comparison website?',
          content: 'In most cases, using a product comparison website is free for consumers. However, some websites may generate revenue through advertising, referral commissions, or sponsored placements. Be mindful of sponsored content disclosures and potential biases in product recommendations.',
        },
      ];
      const handleClick = async () => {
        try {
          let res = await axios.post(
            "fetchfiltered/",
            { search: "", filter: {} },
            { headers: { "Content-Type": "application/json" } }
          );  
          if(res){
            navigate('/productlist', { state: res.data.data});
          }
        } catch (error) {
          console.log(error);
        }
      };

  return (
    <div>
      <Navbar/>

      <div className='h-screen flex'>
        <div className='w-[50%] pt-52 h-screen flex  flex-col pl-6'>
            <p className='font-bold text-6xl text-indigo-500'>Find the <span className='text-orange-500'>perfect</span> products</p>
            <br/>
            <p className='font-bold text-6xl text-indigo-500'> at the <span className='text-orange-500'>best </span>price!</p>
            <br/>
            <p className="text-xl font-bold pl-4 bg-gradient-to-r from-orange-500  to-violet-600 text-transparent bg-clip-text">
          Looking for the ideal gadget, appliance, or accessory? Search no further. This is your one-stop destination for comparing products across a wide range of categories. From smartphones to home appliances, we've got you covered.
        </p>
        <br/>
        <div className='flex justify-center'>
        <button className='bg-orange-500 text-white rounded-full px-2 py-4 text-xl w-64' onClick={handleClick}>Compare products</button>
        </div>
        </div>
        <div className='w-[50%] pt-8'>
            <img src={Animation} className='w-[45vw]'></img>
        </div>
        <div>

        </div>
      </div>

      <div>

          <div className='text-6xl mb-16 text-violet-600 font-bold'>Our categories</div>
    <div className='flex justify-center'>
        <div>
        <div className='text-4xl font-medium text-violet-600'>Electronics</div>
      <Slider {...settings} position='fixed' className='w-[30vw]'>
  <div className='h-72 bg-orange-400'>
    <div className='flex justify-center'>
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzMG7NsZnjV-1lF6Qg4jEcQQhxzJ2GeLovzQ&usqp=CAU" className='h-72'/>  
  </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    <div className='flex justify-center'>
      <img src="https://cdn.thewirecutter.com/wp-content/media/2023/10/smartphone-2048px-4858.jpg?auto=webp&quality=75&width=1024" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzMG7NsZnjV-1lF6Qg4jEcQQhxzJ2GeLovzQ&usqp=CAU" className="h-72"/>
      </div>
  </div>
</Slider>
</div>
<div>
    <div>
    <div className="text-4xl font-medium text-violet-600 ml-32">Shoes</div>
<Slider {...settings} position='fixed' className='w-[30vw] ml-32'>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://m.media-amazon.com/images/I/51mAog9RZWS._AC_UY300_.jpg" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://www.skechers.in/dw/image/v2/BGNZ_PRD/on/demandware.static/-/Sites-skechersin-Library/default/dw5ab426e1/Category-Landing/Category-Mobile/Mens-New/Mobile_Men_Lace-Ups.jpg?sw=780" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://m.media-amazon.com/images/I/51mAog9RZWS._AC_UY300_.jpg" className="h-72"/>
      </div>
  </div>
</Slider>
</div>
</div>
</div>

<div className='flex justify-center mt-16 mb-16'>
    <div>
    <div className="text-4xl font-medium text-violet-600">Clothes</div>
      <Slider {...settings} position='fixed' className='w-[30vw]'>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://img.freepik.com/free-photo/blue-t-shirt_125540-727.jpg" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyM5ahXqYgRbCcFH1fr10JBuLH2yFReTV7zw&usqp=CAU" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://img.freepik.com/free-photo/blue-t-shirt_125540-727.jpg" className="h-72"/>
      </div>
  </div>
</Slider>
</div>
<div>
<div className="text-4xl font-medium text-violet-600 ml-32">Accessoires</div>
<Slider {...settings} position='fixed' className='w-[30vw] ml-32'>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://assets.myntassets.com/dpr_1.5,q_60,w_400,c_limit,fl_progressive/assets/images/17550846/2023/6/15/7c3ade16-6ec5-4975-bc73-f4e01ffba2db1686819761298-Saraf-RS-Jewellery-Rose-Gold-Plated-White-AD-Studded-Jewelle-13.jpg" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://5.imimg.com/data5/SELLER/Default/2023/1/KN/CG/BZ/134365886/wholesale-brass-men-s-fashion-accessories-jewelry-manufacture.jpg" className="h-72"/>
      </div>
  </div>
  <div className='h-72 bg-orange-400 w-16'>
  <div className='flex justify-center'>
      <img src="https://assets.myntassets.com/dpr_1.5,q_60,w_400,c_limit,fl_progressive/assets/images/17550846/2023/6/15/7c3ade16-6ec5-4975-bc73-f4e01ffba2db1686819761298-Saraf-RS-Jewellery-Rose-Gold-Plated-White-AD-Studded-Jewelle-13.jpg" className="h-72"/>
      </div>
  </div>
</Slider>
</div>
</div>


      </div>

      <div className='p-4 pl-16 flex flex-col justify-center items-center'>
        <div className='flex'>
        <div className='h-96 w-72 ml-8 mb-8 mr-16 bg-orange-300 rounded-full'>
        <img src={Comparison} className='h-[40vh] w-[40vw] mt-32 mr-32'/>
        </div>
        <span className='text-6xl mt-32 font-bold ml-8 text-orange-500'>Product comparison & Detailed Analysis</span>
        </div>
        <div className='flex ml-32'>
        <span className='text-6xl mt-32 font-bold mr-16 text-violet-600'>Customer Review</span>
        <div className='h-96 w-72 ml-16 mb-8 bg-violet-300 rounded-full'>
        <img src={Star} className='h-32 mt-32 ml-8'/> </div>
        </div>
        <div className='flex mr-32'>
        <div className='h-96 w-72 ml-8 mb-8 bg-orange-300 rounded-full'>
        <img src={Ai} className='h-80 mt-28 ml-8'/> 
        </div>
        <span className='text-6xl mt-32 font-bold ml-16 text-orange-500'>AI Customer Support</span>
        </div>
      </div>

        <div>
            <p className='text-4xl font-semibold text-violet-600 mb-2'>FAQS</p>
      <Accordian items={accordionItems} />
      </div>

    </div>
  )
}

export default Home
