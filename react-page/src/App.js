import React, { Component } from 'react';
import logo from './animu.jpg';
import './App.css';


class App extends Component {

    render() {
    return (
      <div className="App">
        <header >
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <header>
          <h1 className="App-title">Welcome to React</h1>
        </header>
         <a href="home" > <button type="button">
          Back to Joukkue
        </button></a>
      </div>
    );
  }
}

export default App;
