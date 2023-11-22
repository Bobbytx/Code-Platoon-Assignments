import './App.css'
import axios from "axios"
import { useState, useEffect } from "react";

function App() {
//declares and inits state vars
  const [pokeImg, setpokeImg] = useState("");
  const [pokeType, setpokeType] = useState("");
  const [pokeList, setpokeList] = useState([]);
  const [loaded, setLoaded] = useState(false);

  const getPokemon = async () => {
    setLoaded(false);
      const randomNumber = Math.floor(Math.random() * 151) + 1;
      const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${randomNumber}`);
      
      //updated API call
      setpokeImg(response.data.sprites.front_default);
      setpokeType(`Pokemon Type: ${response.data.types[0].type.name}`);
      //new API call for getting types
      const typeResponse = await axios.get(response.data.types[0].type.url);
      const pokeOfType = typeResponse.data.pokemon;

      //pick 5 randomly of same type
      const randomPokemon = pokeOfType.sort(() => 0.5 - Math.random()).slice(0, 5);

      const details = await Promise.all(
        randomPokemon.map(async (poke) => {
          const detailResponse = await axios.get(poke.pokemon.url);
          return detailResponse.data.sprites.front_default;
        })
      );
      setpokeList(details);

  } ;

  return (
    <>
      <h1>Pokemon Theme Team</h1>
      <button onClick={getPokemon}>Get Pokemon Images</button>
      <div>
        <img 
        className={`fade-in ${loaded ? 'loaded' : ''}`}
        onLoad={() => setLoaded(true)}
        src={pokeImg} 
        />
        <p>{pokeType}</p>
      </div>
      <div>
        {pokeList.map((img, index) => (
          <img key={index} src={img} />
        ))}
      </div>
    </>
  );
}

export default App;