import React from "react"
import {Redirect, Route} from "react-router-dom"
import {getAuthentication} from "reduxStore/selectors/auth"
import {connect} from "react-redux"
import * as PropTypes from "prop-types"


export const PrivateRoute = ({ component, ...rest }) => {
  return (
    <Route
      {...rest}
      component={({ location }) =>
        rest.authenticated ? (
          component()
        ) : (
          <Redirect
            to={{
              pathname: "/login",
              state: { from: location }
            }}
          />
        )
      }
    />
  )
}

const mapStateToProps = (state) => ({
  authenticated: getAuthentication(state),
})

export default connect(
  mapStateToProps,
  null,
)(PrivateRoute)

PrivateRoute.propTypes = {
  location: PropTypes.object,
  component: PropTypes.func,
  authenticated: PropTypes.bool,
}
