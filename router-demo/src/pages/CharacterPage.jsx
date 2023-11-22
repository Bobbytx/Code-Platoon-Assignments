import axios from "axios";
import { useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useNavigate, useOutlet } from "react-router-dom";
import { useOutletContext } from "react-router-dome";

const CharactersPage = () => {
    const [characters, setCharacters] = useState([]);
    const navigate = useNavigate()
    const { setFavorites } = useOutletContext();
    const { id } = useParams;

        const fetchData = async () => {
            const response = await axios.get("https://rickandmortyapi.com/api/character")
            console.log(response.data.results)
            setCharacters(response.data.results)

            if (response.data.info.next) {
                await fetchData(response.data.info.next);
            }
        };



    useEffect(() => {
        fetchData();
    }, []);
return (
    <>
        <h1 className="charHeader"> Character Page </h1>
    <Row>
        {characters.map(character => (
            <Col sm={12} md={6} lg={4} xl={3} key={character.id}>
                <Card style={{ width: '100%', height: '90%', marginBottom: '4rem'}} >
                <Card.Img variant="top" src={character.image} />
                <Card.Body>
                    <Card.Title>{character.name}</Card.Title>
                    <Card.Text>
                        <strong>Species:</strong> {character.species}<br />
                        <strong>Location:</strong> {character.location.name}<br />
                        <strong>Status:</strong> {character.status}
                        Favorites: {favorites}
                    </Card.Text>
                    <Button variant="warning"
                    onClick={()=> setFavorites([...favorites, {"name": name, "image":image}])
                    </Button>
                </Card.Body>
            </Card>
        </Col>
    ))}
    </Row>
        </>
    );
}

export default CharactersPage;