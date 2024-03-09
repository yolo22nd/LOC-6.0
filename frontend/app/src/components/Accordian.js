import React, { useState } from 'react';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';

const AccordionItem = ({ title, content }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleAccordion = () => {
    setIsOpen(!isOpen);
  };

  return (

    <div className="accordion-item flex justify-between flex-col items-center">
      <div className='w-[80vw] bg-orange-500  text-white  font-semibold px-2 py-4 mb-2 rounded-lg text-left'>
        <div className='flex justify-between items-center'>
          <div className="accordion-title">
            {title}
          </div>
          <div>
            <KeyboardArrowDownIcon onClick={toggleAccordion} className='cursor-pointer'/>
          </div>
        </div>
      </div>
      {isOpen && <div className="accordion-content px-2 py-4 border-orange-500 border-2 w-[80vw] mb-2 rounded-lg bg-orange-300">{content}</div>}
    </div>
    
  );
};

const Accordian = ({ items }) => {
  return (
    <div className="accordion">
      {items.map((item, index) => (
        <AccordionItem key={index} title={item.title} content={item.content} />
      ))}
    </div>
  );
};

export default Accordian;
