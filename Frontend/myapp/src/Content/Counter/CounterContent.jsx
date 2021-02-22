import React, { Component, Fragment } from 'react'
import './CounterContent.scss'

export default class CounterContent extends Component {
    render() {
        return (
            <Fragment>
                <div className='parent'>
                    <p className="like">Like Me</p>
                    <button className="minus">-</button>
                    <input className='field' type="text" value={2}/>
                    <button className="plus">+</button>
                </div>
            </Fragment>
        )
    }
}
