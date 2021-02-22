import React, { Component, Fragment } from 'react'
import './ContentBody.scss';
import CounterContent from './Counter/CounterContent'
import Post from './Posting/PostingContent'


export default class ContentBody extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             loop : 1,
        }

    }

    changeLoop = (value) =>{
        this.setState({
            loop: value
        })
    }
    
    render() {
        
        return (
            <div className='Parent'>
                <div className='Posting'>
                <p>{this.state.loop}</p>
                <Post title='Hello World' caption="First Post"/>
                </div>
                <div className="Counter">
                    <CounterContent getNumber={(value) => this.changeLoop(value)}/>
                </div>
            </div>
                
        )
    }
}
