import React from "react"
import {Redirect, Route} from "react-router-dom"
import {getAuthentication} from "reduxStore/selectors/auth"
import {connect} from "react-redux"

export const PrivateRoute = ({authenticated, component: Component, ...rest}) => (
  <Route {...rest} render={props => {
    if (authenticated) {
      return <Component {...props} />
    }
    return <Redirect to={{pathname: "/login", state: {from: props.location}}}/>
  }}/>
)

const mapStateToProps = (state) => ({
  authenticated: getAuthentication(state)
})

export default connect(
  mapStateToProps,
  null
)(PrivateRoute)
