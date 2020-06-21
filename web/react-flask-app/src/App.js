import React from 'react';
import { HashRouter as Router, Route } from "react-router-dom";


import Header from "./components/layout/Header";
import Search from "./components/Search";
import Summary from "./components/results/Summary";
import Articles from "./components/results/Articles";

import About from "./components/About";

import { Provider } from "./context";

import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

function App() {

  return (
    <Provider>
      <Router>
        <div className="App">
          <Header branding="SplitNews" />
          <div className="container">
            <h1 className='text-left'>
              <span className="text-danger">Split</span><span className="text-primary">News</span>
              <img src="logo.png" alt="" width="80px"/>
            </h1>
            <Route exact path="/about" component={About} />
            <Route exact path="/" component={Search} />
            <Route exact path="/" component={Summary} />
            <Route exact path="/" component={Articles} />
          </div>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
