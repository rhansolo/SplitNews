import React, { Component } from "react";
import ReactHtmlParser, { processNodes, convertNodeToElement, htmlparser2 } from 'react-html-parser';

class Article extends Component {
  render() {
    const { title, short, long, rating, img } = this.props;

    if (rating < -0.3) {
      return (
        <div className="card card-body border-primary mb-3">
          {/* <img src={img.thumbnail.contentUrl} alt="" width="200"/> */}
          <h4 className="title">{ReactHtmlParser(title)}</h4>
          <h6 className="text-left">{ReactHtmlParser(short)}</h6>
        </div>
      )
    } else if (rating < 0.3) {
      return (
        <div className="card card-body border-dark mb-3">
          {/* <img src={img.thumbnail.contentUrl} alt="" width="200"/> */}
          <h4 className="title">{ReactHtmlParser(title)}</h4>
          <h6 className="text-left">{ReactHtmlParser(short)}</h6>
        </div>
      )
    } else {
      return (
        <div className="card card-body border-danger mb-3">
          {/* <img src={img.thumbnail.contentUrl} alt="" width="200"/> */}
          <h4 className="title">{ReactHtmlParser(title)}</h4>
          <h6 className="text-left">{ReactHtmlParser(short)}</h6>
        </div>
      )
    }
  }
}

export default Article;