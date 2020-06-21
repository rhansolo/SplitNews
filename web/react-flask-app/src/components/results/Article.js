import React, { Component } from "react";
import ReactHtmlParser, { processNodes, convertNodeToElement, htmlparser2 } from 'react-html-parser';

class Article extends Component {
  render() {
    const { title, short, long, rating } = this.props;
    return (
      <div className="card card-body mb-3">
        <h4 className="title">{ReactHtmlParser(title)}</h4>
        <h6 className="text-left">{ReactHtmlParser(short)}</h6>
      </div>
    )
  }
}

export default Article;