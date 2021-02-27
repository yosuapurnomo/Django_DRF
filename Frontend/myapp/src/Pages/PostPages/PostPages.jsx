import axios from 'axios'
import React, { Component, Fragment } from 'react'
import Post from '../../Content/Posting/PostingContent'
import {connect} from 'react-redux';

const mapStateToProps = (state) =>{
    console.log(state)
    return {
        token: state.token
    }
}

export default connect(mapStateToProps) (class PostPages extends Component {
    constructor(props) {
        super(props)
        
        this.state = {
             post : []
        }
    }
    
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/post/list/',{
            headers:{
                'Authorization': `Token d2b0071f61350e5de8209c0f6abcb1ccbe333fe2`
            }
        }).then((res) =>{
            this.setState({
                post:res.data
            })
        })
    }

    handleDetail = (slug) => {
        this.props.history.push(`/detail/${slug}`)
    }

    render() {
        console.log("PostPages : ", this.props)
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
})
