import axios from 'axios'
import React, { Component, Fragment } from 'react'
import PostingDetail from '../../Content/PostingDetail/PostingDetail'

export default class PostDetailPages extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             post:[]
        }
    }
    
    componentDidMount(){
        let slug = this.props.match.params.slug
        axios.get(`http://127.0.0.1:8000/api/post/${slug}/`, {
            headers:{
                'Authorization': `Token d2b0071f61350e5de8209c0f6abcb1ccbe333fe2`
            }
        }).then(res =>{
            this.setState({
                post:res.data
            })
        })
    }
    render() {
        return (
            <Fragment>
                <div className='Parent'>
                    <div className='Posting'>
                       <PostingDetail 
                            key={this.state.post.slug} 
                            title={this.state.post.username} 
                            caption={this.state.post.caption} 
                            image={this.state.post.image}
                        />
                    </div>
                </div>
            </Fragment>
        )
    }
}
