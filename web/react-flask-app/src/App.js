import React from 'react';
import { HashRouter as Router, Route, Switch } from "react-router-dom";


import { Provider } from "./context";

import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <Provider>
      <Router>
        <div className="App">
          <div className="container">
            <p>
              Hello
            </p>
          </div>
        </div>
      </Router>
    </Provider>
  );
}

export default App;
