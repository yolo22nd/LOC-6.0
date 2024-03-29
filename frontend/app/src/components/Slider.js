import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';

function valuetext(value) {
  return `${value}°C`;
}

const minDistance = 10;

export default function CustomSlider() {
  const [value1, setValue1] = useState([1, 50000]);

  const handleChange1 = (
    event,
    newValue,
    activeThumb,
  ) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (activeThumb === 0) {
      setValue1([Math.min(newValue[0], value1[1] - minDistance), value1[1]]);
    } else {
      setValue1([value1[0], Math.max(newValue[1], value1[0] + minDistance)]);
    }
  };

  const handleApply = () => {
    const [minValue, maxValue] = value1;
    // You can now use minValue and maxValue as the selected range
    console.log('Min Value:', minValue);
    console.log('Max Value:', maxValue);
  };

  return (
    <div className='pt-8'>
        <div className='text-white font-semibold text-xl text-left'>Price range: </div>
    <Box sx={{ width: 200 }}>
      <Slider
        getAriaLabel={() => 'Minimum distance'}
        value={value1}
        onChange={handleChange1}
        valueLabelDisplay="auto"
        getAriaValueText={valuetext}
        disableSwap
        color={'secondary'}
        className='w-4'
        min={1}
        max={50000}
      />
    </Box>
    <button className='bg-white text-violet-500 rounded-xl font-semibold p-2' onClick={handleApply}>Apply</button>
  </div>
  );
}
