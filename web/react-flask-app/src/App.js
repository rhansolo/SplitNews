import React from 'react';
import { HashRouter as Router, Route } from "react-router-dom";


import Header from "./components/layout/Header";
import Search from "./components/Search";

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
            <Route exact path="/" component={Search} />
          </div>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
