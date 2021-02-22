import React, { Component, Fragment } from 'react'
import Bandung_2 from '../Image/Bandung_2.jpg'
import './PostingContent.scss'

const Post = (props) => {
    return (
        <Fragment>
            <div className='parent'>
                <div className='Content'>
                    <div className='image-post'>
                        <img src={Bandung_2} alt=""/>
                    </div>
                    <div className="text">
                        <h1>{props.title}</h1>
                        <p>{props.caption}</p>
                    </div>
                </div>
            </div>
        </Fragment>
    )
}

export default Post