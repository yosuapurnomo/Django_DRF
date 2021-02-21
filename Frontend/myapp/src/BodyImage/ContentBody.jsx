import React, { Component } from 'react'
import Bandung_2 from '../Image/Bandung_2.jpg'
import './ContentBody.scss'

const Title = (props) => {
    return (
        <div className='parent'>
        <div className='Content'>
            <div className='image-post'>
                <img src={Bandung_2} alt=""/>
            </div>
            <h1>{props.title}</h1>
            <p>{props.caption}</p>
        </div>
        </div>
    )
}

export default class ContentBody extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             
        }
    }

    render() {
        return (
            <div>
                <Title title='Hello World' caption="First Post"/>
                <Title title='Halo Dunia' caption="second Post"/>
                <Title title='Hello World' caption="Third Post"/>
                <Title title='Hello World' caption="Third Post"/>
            </div>
        )
    }
}
