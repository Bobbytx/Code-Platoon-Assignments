const FavoritesPage = () => {
    return (
    <>
        <h2>
            Favorites
        </h2>
        {FavoritesPage.map((char)=>(
            <CharCard 
            id={char.id}
            name={char.name}
            image={char.image}
            setFavorites={setFavorites}
            favorites={favorites}
            />
        ))}
    </>
    );
};