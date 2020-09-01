const path=require("path");
const VueLoaderPlugin = require('vue-loader/lib/plugin')
module.exports = {
  entry:{
    "userScript":"./js/userApp.js",
    // "userPanelApp":"./js/userPanelApp.js"
  },
  output:{
      path:path.resolve(__dirname,"public"),
      filename:"[name].js",
      publicPath:"/public"
  },
  mode: 'development',
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        loader:"file-loader"
      },
      {
        test: /\.(png|svg|jpe?g|gif)$/,
        include: /images/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'images/',
              publicPath: 'images/'
            }
          }
        ]
      },
    ]
  },
  resolve: { alias: { vue: 'vue/dist/vue.esm.js' } },
  plugins: [
    new VueLoaderPlugin()
  ]
}