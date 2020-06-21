import React, { Component } from "react";

import { Consumer } from "../../context";

class Summary extends Component {
  render() {
    return (
      <Consumer>
        {(value) => {
          const { leftSummary, rightSummary } = value;
          return (
            <React.Fragment>
              <div className="row">
                <div className="col-sm-6">
                  <h4 className="display-5 mb-2">
                    Summary of Left wing articles
                  </h4>
                  <p>
                    {leftSummary}
                  </p>
                </div>
                <div className="col-sm-6">
                  <h4 className="display-5 mb-2">
                      Summary of Right wing articles
                  </h4>
                  <p>
                    {rightSummary}
                  </p>
                </div>
              </div>
            </React.Fragment>
          );
        }

        }
      </Consumer>
    )
  }
}

export default Summary;