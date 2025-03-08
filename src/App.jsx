import {
	apiUrl,
  mainResultsTemplate,
  mainRequestSchema,
  staticResultsTemplate,
  staticRequestSchema,
  fatigueResultsTemplate,
  fatigueRequestSchema,
} from './data.js';

import _ from 'lodash';

import Main from './Main.jsx';
import Static from './Static.jsx';
import React from 'react';

import axios from 'axios';
import Fatigue from './Fatigue.jsx';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      material: undefined,
      endType: undefined,
      wireDiameter_in: undefined,
      OD_in: undefined,
      L0_in: undefined,
      Ls_in: undefined,

      Fstatic_lbf: undefined,

      F_max_lbf: undefined,
      F_min_lbf: undefined,

      wasValidated: {
        main: false,
        static: false,
        fatigue: false,
      },
      inputError: {
        main: false,
        static: false,
        fatigue: false,
      },
      backendError: {
        main: false,
        static: false,
        fatigue: false,
      },
      loading: {
        main: false,
        static: false,
        fatigue: false,
      },

      mainReqData: undefined,
      staticReqData: undefined,
      fatigueReqData: undefined,

      mainResults: { ...mainResultsTemplate },
      staticResults: { ...staticResultsTemplate },
      fatigueResults: { ...fatigueResultsTemplate },
    };

    this.selectUpdate = this.selectUpdate.bind(this);
    this.eventUpdate = this.eventUpdate.bind(this);
    this.validateMain = this.validateMain.bind(this);
    this.calculateMain = this.calculateMain.bind(this);
    this.validateStatic = this.validateStatic.bind(this);
    this.calculateStatic = this.calculateStatic.bind(this);
    this.validateFatigue = this.validateFatigue.bind(this);
    this.calculateFatigue = this.calculateFatigue.bind(this);
  }

  selectUpdate(key) {
    return (value) => {
      this.setState({ [key]: value });
    };
  }

  eventUpdate(key) {
    return (ev) => {
      this.setState({ [key]: ev?.target?.value });
    };
  }

  validateMain(cb) {
    // clean numeric data
    let numericValues = _.pick(this.state, [
      'wireDiameter_in',
      'OD_in',
      'L0_in',
      'Ls_in',
    ]);
    numericValues = _.mapValues(numericValues, (value) => _.trim(value));
    numericValues = _.mapValues(numericValues, (value) =>
      value === '' ? null : +value
    );

    // unpack data
    const mainReqData = {
      material: this.state.material?.value || null,
      endType: this.state.endType?.value || null,
      ...numericValues,
    };

    mainRequestSchema
      .validate(mainReqData)
      .then(() => {
        this.setState({ inputError: { main: false }, mainReqData }, cb);
      })
      .catch(() => {
        this.setState({ inputError: { main: true }, mainReqData }, cb);
      });
  }

  calculateMain() {
    this.setState(
      {
        wasValidated: { main: true },
        mainResults: { ...mainResultsTemplate }, // clear results table
        loading: { main: true }, // show spinner
        backendError: { main: false },
      },
      () => {
        this.validateMain(() => {
          if (!this.state.inputError.main) {
            axios
              .post(
                apiUrl,
                this.state.mainReqData,
                { timeout: 3500, params: { CALCULATION: 'MAIN' } }
              )
              .then((rep) => {
                console.log(rep.data)
                this.setState({
                  mainResults: rep.data,
                  loading: { main: false },
                });
              })
              .catch((err) => {
                console.log(err);
                this.setState({
                  backendError: { main: true },
                  loading: { main: false },
                });
              });
          } else {
            this.setState({ loading: { main: false } });
          }
        });
      }
    );
  }

  validateStatic(cb) {
    let numericValues = _.pick(this.state, [
      'wireDiameter_in',
      'OD_in',
      'L0_in',
      'Ls_in',
      'Fstatic_lbf',
    ]);
    numericValues = _.mapValues(numericValues, (value) => _.trim(value));
    numericValues = _.mapValues(numericValues, (value) =>
      value === '' ? null : +value
    );

    const staticReqData = {
      material: this.state.material?.value || null,
      endType: this.state.endType?.value || null,
      ...numericValues,
    };

    staticRequestSchema
      .validate(staticReqData)
      .then(() => {
        this.setState({ inputError: { static: false }, staticReqData }, cb);
      })
      .catch(() => {
        this.setState({ inputError: { static: true }, staticReqData }, cb);
      });
  }

  calculateStatic() {
    this.setState(
      {
        wasValidated: { static: true },
        staticResults: { ...staticResultsTemplate }, // clear table
        loading: { static: true }, // show spinner
        backendError: { static: false }, // reset backend error
      },
      () => {
        this.validateStatic(() => {
          if (!this.state.inputError.static) {
            axios
              .post(
                apiUrl,
                this.state.staticReqData,
                { timeout: 3500, params: { CALCULATION: 'STATIC' } }
              )
              .then((rep) => {
                this.setState({
                  staticResults: rep.data,
                  loading: { static: false },
                });
              })
              .catch((err) => {
                console.log(err);
                this.setState({
                  backendError: { static: true },
                  loading: { static: false },
                });
              });
          } else {
            this.setState({ loading: { static: false } });
          }
        });
      }
    );
  }

  validateFatigue(cb) {
    let numericValues = _.pick(this.state,[
      'wireDiameter_in',
      'OD_in',
      'L0_in',
      'Ls_in',
			'F_max_lbf',
			'F_min_lbf'
		]);
    numericValues = _.mapValues(numericValues, (value) => _.trim(value));
    numericValues = _.mapValues(numericValues, (value) =>
      value === '' ? null : +value
    );

    const fatigueReqData = {
			material: this.state.material?.value || null,
      endType: this.state.endType?.value || null,
			...numericValues
		};

    fatigueRequestSchema
      .validate(fatigueReqData)
      .then(() => {
        this.setState({ inputError: { fatigue: false }, fatigueReqData }, cb);
      })
      .catch(() => {
        this.setState({ inputError: { fatigue: true }, fatigueReqData }, cb);
      });
  }

  calculateFatigue() {
    this.setState(
      {
        wasValidated: { fatigue: true },
        fatigueResults: { ...fatigueResultsTemplate },
        loading: { fatigue: true },
        backendError: { fatigue: false },
      },
      () => {
        this.validateFatigue(() => {
          if (!this.state.inputError.fatigue) {
            axios
              .post(
                apiUrl,
                this.state.fatigueReqData,
                { timeout: 3500, params: { CALCULATION: 'FATIGUE' } }
              )
              .then((rep) => {
                this.setState({
                  fatigueResults: rep.data,
                  loading: { fatigue: false },
                });
              })
              .catch((err) => {
                console.log(err);
                this.setState({
                  backendError: { fatigue: true },
                  loading: { fatigue: false },
                });
              });
          } else {
            this.setState({ loading: { fatigue: false } });
          }
        });
      }
    );
  }

  render() {
    return (
      <div id='app'>
        <div className='container py-4'>
          <div className='p-5 mb-4 bg-light rounded-3'>
            <div className='container-fluid py-5'>
              <h1 className='display-5 fw-bold'>ME35401 Spring Calculator</h1>
              <p className='col-md-8 fs-4'>
                By Nicolas Fransen and Peter Salisbury
              </p>
              <a href='#start' className='btn btn-primary btn-lg' type='button'>
                Get Started
              </a>
            </div>
          </div>

          <Main
            selectUpdate={this.selectUpdate}
            eventUpdate={this.eventUpdate}
            calculateMain={this.calculateMain}
            wasValidated={this.state.wasValidated}
            inputError={this.state.inputError}
            backendError={this.state.backendError}
            loading={this.state.loading}
            mainResults={this.state.mainResults}
          />

          <Static
            eventUpdate={this.eventUpdate}
            calculateStatic={this.calculateStatic}
            wasValidated={this.state.wasValidated}
            inputError={this.state.inputError}
            backendError={this.state.backendError}
            loading={this.state.loading}
            staticResults={this.state.staticResults}
          />

          <Fatigue
            eventUpdate={this.eventUpdate}
            calculateFatigue={this.calculateFatigue}
            wasValidated={this.state.wasValidated}
            inputError={this.state.inputError}
            backendError={this.state.backendError}
            loading={this.state.loading}
            fatigueResults={this.state.fatigueResults}
          />
        </div>
      </div>
    );
  }
}

export default App;
