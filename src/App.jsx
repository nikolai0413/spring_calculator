import React from "react";
import Select from "react-select";

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      material: {
        id: 0,
        name: "Select a material...",
      },
    };

    this.materials = [
      {
        id: 1,
        name: "Music wire (ASTM No. A228)",
      },
      {
        id: 2,
        name: "Hard-drawn wire (ASTM No. A227)",
      },
      {
        id: 3,
        name: "Chrome-vanadium wire (ASTM No. A232)",
      },
      {
        id: 4,
        name: "Chrome-silicon wire (ASTM No. A401)",
      },
      {
        id: 5,
        name: "302 stainless wire (ASTM No. A313)",
      },
      {
        id: 6,
        name: "Phosphor-bronze wire (ASTM No. B159)",
      },
    ];
  }

  render() {
    return (
      <div id="app">
        <div className="container py-4">
          <header className="pb-3 mb-4 border-bottom">
            <span className="display-2">Spring Calculator</span>
          </header>

          <div className="p-5 mb-4 bg-light rounded-3">
            <div className="container-fluid py-5">
              <h1 className="display-5 fw-bold">ME35401 Spring Calculator</h1>
              <p className="col-md-8 fs-4">
                By Peter Salisbury and Nicolas Fransen
              </p>
              <a href="#start" className="btn btn-primary btn-lg" type="button">
                Get Started
              </a>
            </div>
          </div>

          <div className="row align-items-md-stretch">
            <div className="col-md-6">
              <div className="h-100 p-5 text-white bg-dark rounded-3">
                <h3>Select a material</h3>
                <Select options={this.materials} />
              </div>
            </div>
            <div className="col-md-6">
              <div className="h-100 p-5 bg-light border rounded-3">
                <h2>Add borders</h2>
                <p>
                  Or, keep it light and add a border for some added definition
                  to the boundaries of your content. Be sure to look under the
                  hood at the source HTML here as we've adjusted the alignment
                  and sizing of both column's content for equal-height.
                </p>
                <button className="btn btn-outline-secondary" type="button">
                  Example button
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
