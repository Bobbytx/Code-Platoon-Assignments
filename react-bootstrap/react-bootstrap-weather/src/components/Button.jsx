import { useState } from 'react';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';

function Button({onLocationChange, selectedLocation}) {
    const [checked, setChecked] = useState(false);
    const [radioValue, setRadioValue] = useState('1');
  
    const radios = [
      { name: 'Chicago', value: 'Chicago' },
      { name: 'Houston', value: 'Houston' },
    ];
  
    return (
      <>
        <ButtonGroup>
          {radios.map((radio, idx) => (
            <ToggleButton
              key={idx}
              id={`radio-${idx}`}
              type="radio"
              variant={selectedLocation === radio.value ? 'primary' : 'outline-primary'}
              name="radio"
              value={radio.value}
              checked={selectedLocation === radio.value}
              onChange={(e) => onLocationChange(e.currentTarget.value)}
            >
              {radio.name}
            </ToggleButton>
          ))}
        </ButtonGroup>
      </>
    );
  }
  
  export default Button;