import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import ContentBody from './Router/ContentBody';
import { createStore as reduxStore } from 'redux';
import {Provider} from 'react-redux';

const createStore = reduxStore;

const globalState = {
    token: ''
}

//Reducer
const rootReducer = (state = globalState, action) =>{
    switch (action.type) {
        case "ADD_TOKEN":
            return {
                ...state,
                token: state.token
            }
        
        case "REMOVE_TOKEN":
            return {
                ...state,
                token: ''
            }

        default:
            return state
    }
 
}

// Store
const storeRedux = createStore(rootReducer);

ReactDOM.render( 
        <Provider store={storeRedux}>
            <ContentBody />
        </Provider>,
    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();