import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import axios from 'axios';


function CharacterDetailsPage(){
    const params = useParams();
    const [character, setCharacter] = useState(null)
    useEffect(()=>{ 
        console.log("Useeffect")
        loadCharacter()
        
      },[])
 
    const loadCharacter = async () => {

        try {
            console.log("Loading")
            const response = await axios.get(`https://rickandmortyapi.com/api/character/${params.id}`,);
            console.log(response)
            if (response.status == 200){
                setCharacter(response.data)
            }else{
                setCharacter(null)
            }
        } catch (error) {
            setCharacter(null)

        }
    };


    return (
        <>
        {
            character == null ?
            ("Character does not exist")
            :
            (
                <Card style={{ width: '18rem' }}>
                    <Card.Img variant="top" src={character.image} />
                    <Card.Body>
                        <Card.Title>{character.name}</Card.Title>
                        <Card.Subtitle className="mb-2 text-muted">{character.species} - {character.status}</Card.Subtitle>
                        <Card.Subtitle className="mb-2 text-muted">Location: {character.location.name} </Card.Subtitle>
                        <Button onClick=setFavorites([...favorites, {"id":id, "name":character.name, "image":character.image variant="primary">Go somewhere</Button>
                    </Card.Body>
                </Card>
            )
        }
        </>
    );
}

export default CharacterDetailsPage;