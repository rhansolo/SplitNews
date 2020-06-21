import React, { Component } from "react";

import SearchBar from "./layout/SearchBar";
import axios from 'axios';

class Search extends Component {
  state = {
    search: "",
    errors: "",
  }

  onSubmit = (e) => {
    e.preventDefault();
    const search = this.state.search;

    let param = {search: search};

    if (search === "") {
      this.setState({errors: "Search is empty"});
      return;
    }

    axios.post("search/query", param).then(response => console.log(response));
    
  }

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value })
  };


  render() {
    const { search, errors } = this.state;

    return (
      <div className="card mb-3">
        <div className="card-header">Search</div>
        <div className="card-body">
          <form onSubmit={this.onSubmit}>
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
    );
  }
}

export default Search;