import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'
import { Carousel } from 'react-bootstrap';
import './ImageCarousel.scss'
import Peter from './Picture/Peter.jpg'
import Mobil from './Picture/Mobil.jpg'
import Picture from  './Picture/Picture.jpg'

const ImageCarousel = () => {
    return (
        <div className="imageCarousel">
            <Carousel className=' w-50'>
                <Carousel.Item>
                    <img
                    className="d-block w-100"
                    src={Peter}
                    alt="First slide"
                    />
                </Carousel.Item>
                <Carousel.Item>
                    <img
                    className="d-block w-100"
                    src={Mobil}
                    alt="Second slide"
                    />
                </Carousel.Item>
                <Carousel.Item>
                    <img
                    className="d-block w-100" 
                    src={Picture}
                    alt="Third slide"
                    />
                </Carousel.Item>
                </Carousel>
        </div>
    );
}

export default ImageCarousel;
