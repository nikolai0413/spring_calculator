import React, { Component } from "react";
import { endTypes, materials } from "./data";

import Select from "react-select";

export default class extends Component {
  constructor(props) {
    super(props);
    this.myPrecision = this.myPrecision.bind(this)
  }
  myPrecision(value, x) {
    if (value && typeof value === "number") {
      return value.toFixed(x);
    }
  }

  render() {
    return (
      <div className="row align-items-md-stretch" id="start">
        <div className="col-md-6 mt-2">
          <div className="h-40 p-3 text-white bg-dark rounded-3">
            <h3>Select End Type</h3>
            <Select
              // onChange={(endType) => this.setState({ endType: endType })}
              onChange={this.props.selectUpdate("endType")}
              className="text-black"
              options={endTypes}
            />
          </div>
        </div>
        <div className="col-md-6 mt-2">
          <div className="h-40 p-3 bg-light border rounded-3">
            <h3>Select Material</h3>
            <Select
              // onChange={(mat) => this.setState({ material: mat })}
              onChange={this.props.selectUpdate("material")}
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
                placeholder="Ex: 0.125"
                onChange={this.props.eventUpdate("wireDiameter_in")}
              />
              <span className="input-group-text">in</span>
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
                onChange={this.props.eventUpdate("OD_in")}
              />
              <span className="input-group-text">in</span>
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
                onChange={this.props.eventUpdate("L0_in")}
              />
              <span className="input-group-text">in</span>
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
                onChange={this.props.eventUpdate("Ls_in")}
              />
              <span className="input-group-text">in</span>
            </div>
          </div>
        </div>

        <div className={"row justify-content-center"} noValidate>
          <div className="col-md-3 text-center mt-4">
            <a
              className="btn btn-primary btn-lg form-control"
              onClick={this.props.calculateMain}
            >
              Calculate
            </a>

            {this.props.wasValidated.main ? (
              this.props.inputError.main ? (
                <div className="text-danger">Error: Check inputs</div>
              ) : (
                <></>
              )
            ) : (
              <></>
            )}

            {this.props.backendError.main ? (
              <div className="text-danger">
                Error: Cannot Calculate (backend error)
              </div>
            ) : (
              <></>
            )}

            {this.props.loading.main ? (
              <div className="my-2">
                <img src="assets/spinner.svg" />
              </div>
            ) : (
              <div className="my-2 invisible">
                <img src="assets/spinner.svg" />
              </div>
            )}
          </div>
        </div>

        <h1 className="display-2">Results</h1>
        <hr />

        <div className="row mt-1 justify-content-center">
          <div className="col-md-8">
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
                  <td>{this.myPrecision(this.props.mainResults.pitch_in_rev, 4)}</td>
                  <td>in</td>
                </tr>
                <tr>
                  <td scope="row">
                    Total # of coils{" "}
                    <i>
                      N<sub>t</sub>
                    </i>
                  </td>
                  <td>{this.myPrecision(this.props.mainResults.nt_, 1)}</td>
                  <td>#</td>
                </tr>
                <tr>
                  <td scope="row">
                    # of active coils{" "}
                    <i>
                      N<sub>a</sub>
                    </i>
                  </td>
                  <td>{this.myPrecision(this.props.mainResults.na_, 1)}</td>
                  <td>#</td>
                </tr>
                <tr>
                  <td scope="row">
                    Spring rate <i>k</i>
                  </td>
                  <td>{this.myPrecision(this.props.mainResults.k_lbf_in, 4)}</td>
                  <td>lbf/in</td>
                </tr>
                <tr>
                  <td scope="row">
                    Force needed to compress to{" "}
                    <i>
                      L<sub>s</sub>
                    </i>
                  </td>
                  <td>{this.myPrecision(this.props.mainResults.fShut_lbf, 4)}</td>
                  <td>lbf</td>
                </tr>
                <tr>
                  <td scope="row">
                    Factor of safety <i>n</i> when compressed to{" "}
                    <i>
                      L<sub>s</sub>
                    </i>
                  </td>
                  <td>{this.myPrecision(this.props.mainResults.nShut_, 1)}</td>
                  <td></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }
}
