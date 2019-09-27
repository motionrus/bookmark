import React from "react"
import {Route, Router} from "react-router-dom"
import {history} from "_helpers"

import {LoginPage} from "pages/Login"
import {PrivateRoute} from "components"
import HomePage from "pages/Home/HomePage"

class App extends React.Component {

  render() {
    return (
      <Router history={history}>
        <PrivateRoute exact path="/" component={HomePage}/>
        <Route path="/login" component={LoginPage}/>
      </Router>
    )
  }
}

export {App}
