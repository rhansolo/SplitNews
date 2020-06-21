import React, { Component } from "react";

import { Consumer } from "../../context";
import Article from "./Article";

class Articles extends Component {
  render() {
    return (
      <Consumer>
        {(value) => {
          const { articles } = value;
          return (
            <React.Fragment>
              <h1 className="display-5 mb-2">
                Articles
              </h1>
              {articles.map(article => (
                <Article title={article.title} short={article.short} long={article.long} rating={article.rating} />
              ))}
            </React.Fragment>
          );
        }

        }
      </Consumer>
    )
  }
}

export default Articles;