import React, { Component } from "react";

const Context = React.createContext();

const updateState = (state, data) => {
  console.log(data);
  return {
    ...state,
    articles: data.articles,
    leftSummary: data.leftSummary,
    rightSummary: data.rightSummary,
  }
}

export class Provider extends Component {
  state = {
    articles: [],
    leftSummary: "",
    rightSummary: "",
    dispatch: (data) => this.setState(state => updateState(state, data)),
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