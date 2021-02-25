import React, { Component, Fragment } from 'react'
import './ContentBody.scss';
import CounterContent from './Counter/CounterContent'
import Post from './Posting/PostingContent'
import axios from 'axios'


export default class ContentBody extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             loop : 1,
             post : []
        }

    }

    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/post/admin-1/')
        .then((res) => {
            console.log(res.data);
            this.setState({
                post: res.data
            })
        })
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
                {/* {this.state.post.map(post =>{
                    return <Post key={post.slug} title={post.username} caption={post.caption} image={post.image}/>
                })
                } */}
                <Post key={this.state.post.slug} title={this.state.post.username} caption={this.state.post.caption} image={this.state.post.image}/>
                </div>
                <div className="Counter">
                    <CounterContent getNumber={(value) => this.changeLoop(value)}/>
                </div>
            </div>
                
        )
    }
}
