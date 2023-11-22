import Carousel from 'react-bootstrap/Carousel';
import ExampleCarouselImage from '/assets/One.jpg';
import ExampleCarouselImage2 from '/assets/Two.png';
import ExampleCarouselImage3 from '/assets/Three.jpg';


function HomeCarousel() {
  return (
    <Carousel className="carousel">
      <Carousel.Item>
        <img src={ExampleCarouselImage} alt="First Slide" />
        <Carousel.Caption>
          <h3>IN THE NEW SEASON</h3>
          <p>Morty messed around and found out</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img src={ExampleCarouselImage2} alt="Second Slide" />
        <Carousel.Caption>
          <h3>WILL THEY SURVIVE???</h3>
          <p>Only time will tell...</p>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img src={ExampleCarouselImage3} alt="Third Slide" />
        <Carousel.Caption>
          <h3>WILL THINGS WILL EVER BE THE SAME AGAIN?</h3>
          <p>
            Find out in the NEW SEASON of RICK and MORTY
          </p>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
}

export default HomeCarousel;