import HomeCarousel from '../components/HomeCarousel.jsx'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

const HomePage = () => {
    return (
        <Container>
        <Row className="my-4">
            <Col>
                <h1 className="homepage-heading">NEW RICK AND MORTY COMING SOON</h1>
            </Col>
        </Row>
        <Row className="my-4">
            <Col>
                <HomeCarousel />
            </Col>
        </Row>
        </Container>

    );
};

export default HomePage;