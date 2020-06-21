import React, { Component } from "react";


import { Consumer } from "../context"

import SearchBar from "./layout/SearchBar";
import axios from 'axios';

class Search extends Component {
  state = {
    search: "",
    errors: "",
  }

  onSubmit = (dispatch, e) => {
    e.preventDefault();
    const search = this.state.search;

    let param = {search: search};

    if (search === "") {
      this.setState({errors: "Search is empty"});
      return;
    }

    axios.post("search/query", param).then(response => dispatch(response.data));
    
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value })
  };


  render() {
    const { search, errors } = this.state;

    return (
      <Consumer>
        {(value) => {
          const { dispatch } = value;
          return (
            <div className="card mb-3">
            <div className="card-header">Search</div>
            <div className="card-body">
              <form onSubmit={this.onSubmit.bind(this, dispatch)}>
                <SearchBar
                  label="Search"
                  name="search"
                  placeholder="Enter keywords or an article title"
                  value={search}
                  onChange={this.onChange}
                  error={errors}
                />
                <input
                  type="submit"
                  value="Search"
                  className="btn btn-light btn-block"
                />
              </form>
            </div>
          </div>
          )
        }}

      </Consumer>
    );
  }
}

export default Search;