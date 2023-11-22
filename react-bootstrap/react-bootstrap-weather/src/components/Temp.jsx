import axios from "axios";
import { useState, useEffect } from 'react';
import Button from './Button.jsx';


const Temp = () => {

    //let chicago = [41.881832,-87.623177]

    const locations = {
        'Chicago': '41.881832&longitude=-87.623177',
        'Houston': '29.7633&longitude=-95.3633'
    };
  
    const [currentTemp, setCurrentTemp] = useState("");
    const [location, setLocation] = useState('Chicago');



    useEffect(() => {
    const getTemperature = async () => {
      const coords = locations[location];
      const response = await axios.get(`https://api.open-meteo.com/v1/forecast?latitude=${coords}&current=temperature_2m&hourly=temperature_2m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&forecast_days=1`)

        console.log(response.data.current.temperature_2m)
        setCurrentTemp(response.data.current.temperature_2m)
    };
        getTemperature();
    }, [location]);

    const handleLocationChange = (newLocation) => {
        setLocation(newLocation);
    };

        

    return (
        <div id="temp_div">
            <Button onLocationChange={handleLocationChange} selectedLocation={location}/>
            <p>{currentTemp}</p>
            
        </div>
    );
}
export default Temp;