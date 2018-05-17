import React, { Component } from 'react';
import logo from './animu.jpg';
import './App.css';


class App extends Component {

    render() {
    return (
      <div className="App">

          <header className="App-header">
            <a href="home" > <button type="button">
            Back to Joukkue
            </button></a>
          </header>

          <div className="App-intro">
          <img src={logo} className="App-logo" alt="logo" />
              <h1 className="App-title">Welcome to React</h1>
          </div>
      </div>
    );
  }
}

export default App;
