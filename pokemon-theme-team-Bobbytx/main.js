const getPokemon = async() => {
    let response = await fetch("https://pokeapi.co/api/v2/pokemon/charizard");
    let data = await response.json();
    let pokemonPhoto = data.sprites.front_default;
    let div = document.createElement('div');
    div.id = 'image-holder';
    let img = document.createElement("img");
    img.id = 'pokemonImg';
    img.src = pokemonPhoto;
    div.appendChild(img);
    document.body.appendChild(div);
}

const getRandomPokemon = async() => {
        const responseCount = await fetch('https://pokeapi.co/api/v2/pokemon/');
        const dataCount = await responseCount.json();
        const totalPokemon = dataCount.count;
        console.log(totalPokemon)
}



getRandomPokemon()
getPokemon()