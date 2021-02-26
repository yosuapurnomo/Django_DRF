import axios from 'axios'
import React, { Component, Fragment } from 'react'
import Post from '../../Content/Posting/PostingContent'

export default class PostPages extends Component {
    constructor(props) {
        super(props)
        
        this.state = {
             post : []
        }
    }
    
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/post/list/').then((res) =>{
            console.log(res.data)
            this.setState({
                post:res.data
            })
        })
    }

    handleDetail = (slug) => {
        console.log(slug)
        this.props.history.push(`/detail/${slug}`)
    }

    render() {
        return (
            <Fragment>
                <div className='Parent'>
                    <div className='Posting'>
                        {this.state.post.map(posting => {
                            return <Post 
                                    key={posting.slug} 
                                    title={posting.username} 
                                    caption={posting.caption} 
                                    image={posting.image}
                                    slug={posting.slug}
                                    goDetail={this.handleDetail}/>
                        })}
                    </div>
                </div>
            </Fragment>
        )
    }
}
