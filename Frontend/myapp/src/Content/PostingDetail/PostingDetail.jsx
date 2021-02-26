import React, { Component, Fragment } from 'react'

export default class PostingDetail extends Component {
    render() {
        return (
            <Fragment>
                <div className='parent'>
                    <div className='Content'>
                        <div className='image-post'>
                            <img src={'http://127.0.0.1:8000' + this.props.image} 
                            alt={'http://127.0.0.1:8000' + this.props.image}
                            />
                        </div>
                        <div className="text">
                            <h1>{this.props.title}</h1>
                            <p>{this.props.caption}</p>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}
