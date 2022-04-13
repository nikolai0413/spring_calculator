import {
  mainResultsTemplate,
  mainSchema,
  staticResultsTemplate,
  staticSchema,
  fatigueResultsTemplate,
  fatigueSchema,
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
      wireDiameter_mm: undefined,
      OD_mm: undefined,
      L0_mm: undefined,
      Ls_mm: undefined,

      Fs_N: undefined,

      F_max_N: undefined,
      F_min_N: undefined,

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
      'wireDiameter_mm',
      'OD_mm',
      'L0_mm',
      'Ls_mm',
    ]);
    numericValues = _.mapValues(numericValues, (value) => _.trim(value));
    numericValues = _.mapValues(numericValues, (value) =>
      value === '' ? null : +value
    );

    // unpack data
    const mainReqData = {
      material: this.state.material?.label || null,
      endType: this.state.endType?.label || null,
      ...numericValues,
    };

    mainSchema
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
                'https://vhdufpz2ne.execute-api.us-east-1.amazonaws.com/attempt1_python',
                this.state.mainReqData,
                { timeout: 3500, params: { CALCULATION: 'MAIN' } }
              )
              .then((rep) => {
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
    let numericValue = this.state.Fs_N;
    numericValue = _.trim(numericValue);
    numericValue = numericValue === '' ? null : +numericValue;

    const staticReqData = {
      Fs_N: numericValue,
    };

    staticSchema
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
                'https://vhdufpz2ne.execute-api.us-east-1.amazonaws.com/attempt1_python',
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
		let numericValues = _.pick(this.state, ['F_max_N', 'F_min_N']);
		numericValues = _.mapValues(numericValues, value => _.trim(value));
		numericValues = _.mapValues(numericValues, value => value === "" ? null : +value);

		const fatigueReqData = {...numericValues};

		fatigueSchema.validate(fatigueReqData)
		.then(() => {
			this.setState({ inputError: { fatigue: false }, fatigueReqData}, cb);
		})
		.catch(() => {
			this.setState({ inputError: { fatigue: true }, fatigueReqData}, cb);
		});
	}

  calculateFatigue() {
		this.setState({
			wasValidated: { fatigue: true },
			fatigueResults: { ... fatigueResultsTemplate },
			loading: { fatigue: true },
			backendError: { fatigue: false }
		}, () => {
			this.validateFatigue(() => {
				if (!this.state.inputError.fatigue) {
					axios.post(
						'https://vhdufpz2ne.execute-api.us-east-1.amazonaws.com/attempt1_python',
						this.state.fatigueReqData,
						{ timeout: 3500, params: { CALCULATION: 'FATIGUE' }}
					)
					.then(rep => {
						this.setState({
							fatigueResults: rep.data,
							loading: { fatigue: false }
						})
					})
					.catch(err => {
						console.log(err);
						this.setState({
							backendError: { fatigue: true },
							loading: { fatigue: false },
						});
					})
				} else {
					this.setState({ loading: { fatigue: false }});
				}
			})
		})
	}

  render() {
    return (
      <div id='app'>
        <div className='container py-4'>
          <div className='p-5 mb-4 bg-light rounded-3'>
            <div className='container-fluid py-5'>
              <h1 className='display-5 fw-bold'>ME35401 Spring Calculator</h1>
              <p className='col-md-8 fs-4'>
                By Peter Salisbury and Nicolas Fransen
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
