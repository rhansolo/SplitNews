import React, { Component } from "react";
import ReactHtmlParser, { processNodes, convertNodeToElement, htmlparser2 } from 'react-html-parser';

import { Consumer } from "../../context";

class Summary extends Component {
  render() {
    return (
      <Consumer>
        {(value) => {
          const { leftSummary, rightSummary, searched } = value;
          if (searched === 2) {
            return (
              <React.Fragment>
                <div className="row">
                  <div className="col-sm-6">
                    <h4 className="display-5 mb-2">
                      Summary of Left wing articles
                    </h4>
                    <div className="text-left">{ReactHtmlParser(leftSummary)}</div>
                  </div>
                  <div className="col-sm-6">
                    <h4 className="display-5 mb-2">
                        Summary of Right wing articles
                    </h4>
                    <div className="text-left">{ReactHtmlParser(rightSummary)}</div>
                  </div>
                </div>
              </React.Fragment>);
          } else if (searched === 1) {
            return (
              <div className="load">
                    <img src="loading.gif" alt=""/>
              </div>);
          } else {
            return null;
          }
        }

        }
      </Consumer>
    )
  }
}

export default Summary;