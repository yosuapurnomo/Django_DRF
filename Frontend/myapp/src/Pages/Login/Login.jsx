import React, { Component, Fragment } from 'react'
import './Login.scss'
import { Jumbotron, Button, Container, InputGroup, FormControl } from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import {connect} from 'react-redux';
import ImageCarousel from './ImageCarousel/ImageCarousel';

const mapStateToProps = (state) =>{
    console.log("mapStateToProps : ", state)
    return {
        token: state.token
    }
}

const mapDispatchToProps = (dispatch) =>{
    console.log(dispatch)
    return {
        token: () => dispatch({type: 'ADD_TOKEN'})
    }
}

export default connect(mapStateToProps, mapDispatchToProps) (class Login extends Component{
    constructor(props) {
        super(props)
    
        this.state = {
            form:{
                username:'',
                password:''  
            },
            token:''
        }
    }
    
    handleFormChange = (event) =>{
        let formNew = {...this.state.form}
        formNew[event.target.name] = event.target.value
        this.setState({
            form: formNew
        }, () =>{
            console.log(this.state.form)
        })
    }

    handleSubmit = () =>{
        axios.post('http://127.0.0.1:8000/api/account/login/', this.state.form).then((res) => 
        {
            console.log('Send :', res.data.token)
            this.setState({
                token: res.data.token
                }, ()=>{console.log("Token : ", this.state.token)})
        })
            
            this.props.history.push('/')
    }

    render() {
        console.log("Login : ", this.props);
        return (
            <Fragment>
                    <Container>
                <div className="parent">
                        <div className="imageCarousel">
                            <ImageCarousel/>
                        </div>
                        <div className="formLogin">
                            <Jumbotron>
                            <h1 className="mb-4">Instagram</h1>
                            <InputGroup className="mb-4">
                            <InputGroup.Prepend>
                                <InputGroup.Text id="basic-addon1">@</InputGroup.Text>
                            </InputGroup.Prepend>
                                <FormControl type='text' placeholder='Email' name='username' onChange={this.handleFormChange}/>
                            </InputGroup>
                            <InputGroup className="mb-4">
                                <FormControl type='password' placeholder='Password' name='password' onChange={this.handleFormChange}/>
                            </InputGroup>
                            <p>
                                <Button variant="primary" onClick={this.handleSubmit}>Login</Button>
                            </p>
                        </Jumbotron> 
                        </div>
                </div>
                    </Container>
            </Fragment>
        )
    }
}
)