import React, { Component } from "react";

class Article extends Component {
  render() {
    const { title, short, long, rating } = this.props;
    return (
      <div className="card card-body mb-3">
        <h4 className="title">{title}</h4>
        <h6>{short}</h6>
      </div>
    )
  }
}

export default Article;