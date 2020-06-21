import React, { Component } from "react";

const Context = React.createContext();

const updateState = (state, data) => {
  return {
    ...state,
    articles: data.articles,
    leftSummary: data.leftSummary,
    rightSummary: data.rightSummary,
    searched: 2,
  }
}

const loading = (state) => {
  return {
    ...state,
    searched: 1
  }
} 

export class Provider extends Component {
  state = {
    articles: [],
    leftSummary: "",
    rightSummary: "",
    searched: 0,
    dispatch: (data) => {
      this.setState(state => updateState(state, data))
      console.log(data)},
    load: () => this.setState(state => loading(state)),
  };

  render() {
    return (
      <Context.Provider value={this.state}>
        {this.props.children}
      </Context.Provider>
    );
  }
}

export const Consumer = Context.Consumer;