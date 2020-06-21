import React, { Component } from "react";

import { Consumer } from "../../context";
import Article from "./Article";

class Articles extends Component {
  render() {
    return (
      <Consumer>
        {(value) => {
          const { articles, searched } = value;
          if (searched === 2) {
            return (
              <React.Fragment>
                <h1 className="display-5 mb-2">
                  Articles
                </h1>
                {articles.map(article => (
                  <Article title={article.title} short={article.short} long={article.long} rating={article.rating} img={article.pic_json} />
                ))}
              </React.Fragment>
            );
          } else {
            return null;
          }
        }
        }
      </Consumer>
    )
  }
}

export default Articles;