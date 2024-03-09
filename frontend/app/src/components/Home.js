import React from 'react'
import Navbar from './Navbar'
import Animation from'../assets/Business Analysis.gif'
import Star from'../assets/5 Star Rating.gif'
import Ai from'../assets/aii.png'
import Comparison from '../assets/comparison.png'
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

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

  return (
    <div>
      <Navbar/>

      <div className='h-screen flex'>
        <div className='w-[50%] pt-64 h-screen flex  flex-col pl-6'>
            <p className='font-bold text-6xl text-indigo-500'>Find the <span className='text-orange-500'>perfect</span> products</p>
            <br/>
            <p className='font-bold text-6xl text-indigo-500'> at the <span className='text-orange-500'>best </span>price!</p>
            <br/>
            <p className="text-xl font-bold pl-4 bg-gradient-to-r from-orange-500  to-violet-600 text-transparent bg-clip-text">
          Looking for the ideal gadget, appliance, or accessory? Search no further. This is your one-stop destination for comparing products across a wide range of categories. From smartphones to home appliances, we've got you covered.
        </p>
        <br/>
        <div className='flex justify-center'>
        <button className='bg-orange-500 text-white rounded-full px-2 py-4 text-xl w-64'>Compare products</button>
        </div>
        </div>
        <div className='w-[50%] pt-32'>
            <img src={Animation} className='w-[45vw]'></img>
        </div>
        <div>

        </div>
      </div>

      <div>

    <div className='flex justify-center'>
      <Slider {...settings} position='fixed' className='w-[30vw]'>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 1 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 2 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 3 Content
  </div>
</Slider>
<Slider {...settings} position='fixed' className='w-[30vw] ml-32'>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 1 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 2 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 3 Content
  </div>
</Slider>
</div>

<div className='flex justify-center mt-16 mb-16'>
      <Slider {...settings} position='fixed' className='w-[30vw]'>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 1 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 2 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 3 Content
  </div>
</Slider>
<Slider {...settings} position='fixed' className='w-[30vw] ml-32'>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 1 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 2 Content
  </div>
  <div className='h-72 bg-orange-400 w-16'>
    Slide 3 Content
  </div>
</Slider>
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

    </div>
  )
}

export default Home
