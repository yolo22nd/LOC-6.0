import React,{useState,useEffect} from 'react'
import Naavbar2 from './Naavbar2'
// import axios from './Axios';
import axios from "axios";


const Comparison = () => {
    const [data, setData] = useState([]);
console.log(data)
const [render, setRender] = useState(false);
    const getData = async () => {
        let res = await axios.post('http://127.0.0.1:8000/compare/', {
            "product1":4,
            "product2":2
          }, { headers: { 'Content-Type': 'application/json' } });
        console.log(res.data.comparison_data); // Check the retrieved data
        setData(res.data)
        if(data){
            setRender(true)
        }
    }
    useEffect(() => {
        getData();
    },[])

  return (
    <div>
        <Naavbar2/>
    <div className='mt-16'>
        <div className='text-6xl pt-8 mb-8 font-bold text-black flex flex-col justify-center '>Product comparison</div>
            <div className='flex justify-center items-center rounded-full'>
            <table className='w-[90vw]'>
                <thead>
                    <tr>
                        <th className='border-2 bg-orange-500 px-2 py-4 text-white text-2xl'>Attribute</th>
                        <th className='border-2 bg-orange-500 px-2 py-4 text-white text-2xl'>Product1</th>
                        <th className='border-2 bg-orange-500 px-2 py-4 text-white text-2xl'>Product2</th>
                    </tr>
                </thead>
                <tbody>
                    {render && data.comparison_data.map((comparison, index) => (
                          index !== 11 ? (
                            <tr key={index} className={index % 2 === 0 ? 'bg-orange-200' : 'bg-orange-300'}>
                                <td className='border-2 font-bold text-violet-900 text-xl p-2'>{comparison[0]}</td>
                                <td className='border-2 p-2'>{comparison[1]}</td>
                                <td className='border-2 p-2'>{comparison[2]}</td>
                            </tr>
                        ):(
                            <tr key={index} className={index % 2 === 0 ? 'bg-orange-200' : 'bg-orange-300'}>
                                <td className='border-2 font-bold text-violet-900 text-xl p-2'>{comparison[0]}</td>
                                <td className='border-2 p-2'>{comparison[1][0] && <img src={comparison[1][0]} alt="Product1" className='h-48'/>}</td>
                                <td className='border-2 p-2'>{comparison[2][1] && <img src={comparison[2][1]} alt="Product1" className='h-48'/>}</td>
                            </tr>
                        )
                    ))}
                </tbody>
            </table>
            </div>
      </div>
    </div>
  )
}

export default Comparison
