import React, { Component } from 'react';

export default class Static extends Component {
  render() {
    return (
      <div>
        <div className='container px-5'>
          <h1 className='display-6'>Static Load Analysis</h1>
          <hr />
        </div>
        <div className='row mt-1 justify-content-center'>
          <div className='col-md-3 mt-2'>
            <div className='h-40 p-3 bg-light border rounded-3'>
              <h3 htmlFor='exampleFormControlInput1' className='form-label'>
                Static Load{' '}
                <i>
                  F<sub>static</sub>
                </i>
              </h3>
              <div className='input-group'>
                <input
                  type='text'
                  className='form-control'
                  id='exampleFormControlInput1'
                  placeholder='Ex: 110.2'
									onChange={this.props.eventUpdate('Fs_lbf')}
                />
                <span className='input-group-text'>lbf</span>
              </div>
            </div>
          </div>

          <div className='row justify-content-center'>
            <div className='col-md-3 text-center mt-4'>
              <a
                className='btn btn-primary btn-lg form-control'
                onClick={this.props.calculateStatic}
              >
                Calculate
              </a>

              {this.props.wasValidated.static ? (
                this.props.inputError.static ? (
                  <div className='text-danger'>Error: Check inputs</div>
                ) : (
                  <></>
                )
              ) : (
                <></>
              )}

              {this.props.backendError.static ? (
                <div className='text-danger'>
                  Error: Cannot Calculate (backend error)
                </div>
              ) : (
                <></>
              )}

              {this.props.loading.static ? (
                <div className='my-2'>
                  <img src='assets/spinner.svg' />
                </div>
              ) : (
                <div className='my-2 invisible'>
                  <img src='assets/spinner.svg' />
                </div>
              )}
            </div>
          </div>

          <div className='row mt-2 justify-content-center'>
            <div className='col-md-6'>
              <table className='table table-bordered table-hover'>
                <thead>
                  <tr>
                    <th scope='col'>Property</th>
                    <th scope='col'>Value</th>
                    <th scope='col'>Unit</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td scope='row'>
                      Factor of Safety{' '}
                      <i>
                        n<sub>s</sub>
                      </i>
                    </td>
                    <td>{this.props.staticResults.n_s_}</td>
                    <td></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
