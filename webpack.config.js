const path = require('path');

module.exports = {
  entry: path.resolve(__dirname, './main.js'),
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  // resolve: {
  //   extensions: ['*', '.jsx']
  // },
  output: {
    path: path.resolve(__dirname, './dist'),
    filename: 'bundle.js',
  },
  devServer: {
    static: '.'
  },
};