import React from "react";
import Select from "react-select";
import axios from "axios";

import { materials, endTypes, theSchema, mainResultsTemplate } from "./data.js";

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      material: undefined,
      endType: undefined,
      wireDiameter_mm: undefined,
      OD_mm: undefined,
      L0_mm: undefined,
      Ls_mm: undefined,
      wasValidated: false,
      inputsValid: true,
      springReqData: undefined,
      mainResults: {...mainResultsTemplate}
    };

    this.calculateButton = this.calculateButton.bind(this);
    this.validateData = this.validateData.bind(this);
  }

  validateData(cb) {
    // unpack data
    const springReqData = {
      material: this.state.material?.label || null,
      endType: this.state.endType?.label || null,
      // to float conversions
      wireDiameter_mm: +this.state.wireDiameter_mm,
      OD_mm: +this.state.OD_mm,
      L0_mm: +this.state.L0_mm,
      Ls_mm: +this.state.Ls_mm,
    };

    theSchema
      .validate(springReqData)
      .then(() => {
        this.setState({ inputsValid: true, springReqData }, cb);
      })
      .catch(() => {
        this.setState({ inputsValid: false, springReqData }, cb);
      });
  }

  calculateButton() {
    this.setState({ wasValidated: true, mainResults: {...mainResultsTemplate} }, () => {
      this.validateData(() => {
        if (this.state.inputsValid) {
          axios
            .post(
              "https://vhdufpz2ne.execute-api.us-east-1.amazonaws.com/attempt1_python",
              this.state.springReqData
            )
            .then((rep) => {
              this.setState({ mainResults: rep.data })
            })
            .catch((err) => console.log(err));
        }
      });
    });
  }

  render() {
    return (
      <div id="app">
        <div className="container py-4">
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

          <div className="row align-items-md-stretch" id="start">
            <div className="col-md-6 mt-2">
              <div className="h-40 p-3 text-white bg-dark rounded-3">
                <h3>Select End Type</h3>
                <Select
                  onChange={(endType) => this.setState({ endType: endType })}
                  className="text-black"
                  options={endTypes}
                />
              </div>
            </div>
            <div className="col-md-6 mt-2">
              <div className="h-40 p-3 bg-light border rounded-3">
                <h3>Select Material</h3>
                <Select
                  onChange={(mat) => this.setState({ material: mat })}
                  className="text-black"
                  options={materials}
                />
              </div>
            </div>

            <div className="col-md-3 mt-2">
              <div className="h-40 p-3 text-white bg-dark rounded-3">
                <h3 htmlFor="exampleFormControlInput1" className="form-label">
                  Wire Diameter
                </h3>
                <div className="input-group">
                  <input
                    type="text"
                    className="form-control"
                    id="exampleFormControlInput1"
                    placeholder="Ex: 2.5"
                    onChange={(ev) =>
                      this.setState({ wireDiameter_mm: ev.target.value })
                    }
                  />
                  <span className="input-group-text">mm</span>
                </div>
              </div>
            </div>

            <div className="col-md-3 mt-2">
              <div className="h-40 p-3 bg-light border rounded-3">
                <h3 htmlFor="exampleFormControlInput1" className="form-label">
                  Outer Diameter
                </h3>
                <div className="input-group">
                  <input
                    type="text"
                    className="form-control"
                    id="exampleFormControlInput1"
                    placeholder="Ex: 5.0"
                    onChange={(ev) => this.setState({ OD_mm: ev.target.value })}
                  />
                  <span className="input-group-text">mm</span>
                </div>
              </div>
            </div>

            <div className="col-md-3 mt-2">
              <div className="h-40 p-3 text-white bg-dark rounded-3">
                <h3 htmlFor="exampleFormControlInput1" className="form-label">
                  Free Length{" "}
                  <i>
                    L<sub>0</sub>
                  </i>
                </h3>
                <div className="input-group">
                  <input
                    type="text"
                    className="form-control"
                    id="exampleFormControlInput1"
                    placeholder="Ex: 20.0"
                    onChange={(ev) => this.setState({ L0_mm: ev.target.value })}
                  />
                  <span className="input-group-text">mm</span>
                </div>
              </div>
            </div>

            <div className="col-md-3 mt-2">
              <div className="h-40 p-3 bg-light border rounded-3">
                <h3 htmlFor="exampleFormControlInput1" className="form-label">
                  Solid Length{" "}
                  <i>
                    L<sub>s</sub>
                  </i>
                </h3>
                <div className="input-group">
                  <input
                    type="text"
                    className="form-control"
                    id="exampleFormControlInput1"
                    placeholder="Ex: 25.0"
                    onChange={(ev) => this.setState({ Ls_mm: ev.target.value })}
                  />
                  <span className="input-group-text">mm</span>
                </div>
              </div>
            </div>

            <div className={"row justify-content-center"} noValidate>
              <div className="col-3 text-center mt-4">
                <a
                  className="btn btn-secondary btn-lg form-control"
                  onClick={this.calculateButton}
                >
                  Calculate
                </a>

                {this.state.wasValidated ? (
                  !this.state.inputsValid ? (
                    <div className="text-danger">Error: Check inputs</div>
                  ) : (
                    <></>
                  )
                ) : (
                  <></>
                )}
              </div>
            </div>

            <h1 className="display-2">Results</h1>
            <hr />

            <div className="row mt-1 justify-content-center">
              <div className="col-8">
                <table className="table table-bordered table-hover">
                  <thead>
                    <tr>
                      <th scope="col">Property</th>
                      <th scope="col">Value</th>
                      <th scope="col">Unit</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td scope="row">
                        Pitch <i>p</i>
                      </td>
                      <td>{this.state.mainResults.p}</td>
                      <td>mm</td>
                    </tr>
                    <tr>
                      <td scope="row">
                        Total # of coils{" "}
                        <i>
                          N<sub>t</sub>
                        </i>
                      </td>
                      <td>{this.state.mainResults.nt}</td>
                      <td>#</td>
                    </tr>
                    <tr>
                      <td scope="row">
                        Number of active coils{" "}
                        <i>
                          N<sub>a</sub>
                        </i>
                      </td>
                      <td>{this.state.mainResults.na}</td>
                      <td>#</td>
                    </tr>
                    <tr>
                      <td scope="row">
                        Spring rate <i>k</i>
                      </td>
                      <td>{this.state.mainResults.k}</td>
                      <td>N/m</td>
                    </tr>
                    <tr>
                      <td scope="row">
                        Force needed to compress to{" "}
                        <i>
                          L<sub>s</sub>
                        </i>
                      </td>
                      <td>{this.state.mainResults.F_ls}</td>
                      <td>N</td>
                    </tr>
                    <tr>
                      <td scope="row">
                        Factor of safety <i>n</i> when compressed to{" "}
                        <i>
                          L<sub>s</sub>
                        </i>
                      </td>
                      <td>{this.state.mainResults.F_ls}</td>
                      <td></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div className="container px-5">
              <h1 className="display-6">Static Load Analysis</h1>
              <hr />
              <div className="row mt-1 justify-content-center">
                <div className="col-md-3 mt-2">
                  <div className="h-40 p-3 bg-light border rounded-3">
                    <h3
                      htmlFor="exampleFormControlInput1"
                      className="form-label"
                    >
                      Static Load{" "}
                      <i>
                        F<sub>s</sub>
                      </i>
                    </h3>
                    <div className="input-group">
                      <input
                        type="text"
                        className="form-control"
                        id="exampleFormControlInput1"
                        placeholder="Ex: 110.2"
                        onChange={(ev) =>
                          this.setState({ Ls_mm: ev.target.value })
                        }
                      />
                      <span className="input-group-text">N</span>
                    </div>
                  </div>
                </div>

                <div className={"row justify-content-center"} noValidate>
                  <div className="col-3 text-center mt-4">
                    <a className="btn btn-secondary btn-lg form-control">
                      Calculate
                    </a>

                    {/* {this.state.wasValidated ? (
                      !this.state.inputsValid ? (
                        <div className="text-danger">Error: Check inputs</div>
                      ) : (
                        <></>
                      )
                    ) : (
                      <></>
                    )} */}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
