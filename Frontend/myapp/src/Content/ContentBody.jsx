import React, { Component, Fragment } from 'react'
import './ContentBody.scss';
import CounterContent from './Counter/CounterContent'
import Post from './Posting/PostingContent'


export default class ContentBody extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             
        }
    }

    render() {
        return (
            <Fragment>
                <div className='Posting'>
                    <Post title='Hello World' caption="First Post"/>
                    <Post title='Halo Dunia' caption="Second Post"/>
                    <Post title='Hello World' caption="Third Post"/>
                    <Post title='Hello World' caption="Third Post"/>
                </div>
                <hr/>
                <div className="Counter">
                    <CounterContent />
                </div>
            </Fragment>
        )
    }
}
