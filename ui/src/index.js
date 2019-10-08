import React from "react"
import ReactDOM from "react-dom"
import {Provider} from "react-redux"
import {store} from "reduxStore"
import {history} from "_helpers"
import PrivateRoute from "components/PrivateRoute"
import HomePage from "pages/Home/HomePage"
import LoginPage from "pages/Login/LoginPage"
import {SignUp} from "pages/Register"
import {Route, Router} from "react-router-dom"


ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      <PrivateRoute exact path="/" component={HomePage}/>
      <Route path="/login" component={LoginPage}/>
      <Route path="/register" component={SignUp}/>
    </Router>
  </Provider>
  , document.querySelector("#root"))
