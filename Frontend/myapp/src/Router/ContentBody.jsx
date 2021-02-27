import React, { Component, Fragment } from 'react'
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'

import PostPages from '../Pages/PostPages/PostPages';
import PostDetailPages from '../Pages/PostDetailPages/PostDetailPages';

import './ContentBody.scss';
import Login from '../Pages/Login/Login';


export default class ContentBody extends Component {
    
    render() {
        
        return (
            <Router>
              <Fragment>
                    <div className="navigation">
                        <Link to="/" >Home</Link>
                        <br/>
                        <Link to="/login">Login</Link>
                    </div>
                <Route path="/" exact component={PostPages}/>
                <Route path="/login" component={Login}/>
                <Route path="/detail/:slug" component={PostDetailPages}/>
            </Fragment>   
            </Router>
        )
    }
}
