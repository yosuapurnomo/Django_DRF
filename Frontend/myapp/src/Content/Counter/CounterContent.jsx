import React, { Component, Fragment } from 'react'
import './CounterContent.scss'

export default class CounterContent extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             number: 1
        }
    }

    setNumber = () =>{
        this.props.getNumber(this.state.number)
    }
    
    handleMinus = () => {
        if (this.state.number != 0) {
            this.setState({
                number: this.state.number - 1
            }, () => {
                this.setNumber();
            })
        }
    }

    handlePlus = () => { 
        this.setState({
            number: this.state.number + 1
        }, () => {
            this.setNumber();
        })
    }

    render() {
        return (
            <Fragment>
                <div className='parent'>
                    <p className="like">Like Me</p>
                    <button className="minus" onClick={this.handleMinus}>-</button>
                    <input className='field' type="text" value={this.state.number}/>
                    <button className="plus" onClick={this.handlePlus}>+</button>
                </div>
            </Fragment>
        )
    }
}
