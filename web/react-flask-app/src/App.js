import React, { useState, useEffect } from 'react';
import { HashRouter as Router, Route, Switch } from "react-router-dom";

import Header from "./components/layout/Header";
import Search from "./components/Search";

import { Provider } from "./context";

import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <Provider>
      <Router>
        <div className="App">
          <Header branding="SplitNews" />
          <div className="container">
            <Route exact path="/" component={Search} />
          </div>
          <p>The current time is {currentTime}.</p>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
