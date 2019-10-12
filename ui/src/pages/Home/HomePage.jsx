import React, {useEffect} from "react"
import CssBaseline from "@material-ui/core/CssBaseline"
import {SearchAppBar} from "components/SearchAppBar/SearchAppBar"
import {history} from "_helpers"
import {connect} from "react-redux"
import {getBookmarks} from "reduxStore/selectors/bookmark"
import {getAllBookmarks} from "reduxStore/action/bookmark"
import Main from "components/Main/Main"
import {signOut} from "reduxStore/action/auth"
import * as PropTypes from "prop-types"

const HomePage = (props) => {
  const {getAllBookmarks, signOut} = props

  useEffect(() => {
    getAllBookmarks()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])
  const handleLogout = () => {
    signOut()
    history.push("/login")
  }

  return (
    <React.Fragment>
      <CssBaseline/>
      <SearchAppBar onClick={handleLogout}/>
      <Main props={props}/>
    </React.Fragment>
  )
}

const mapStateToProps = (state) => {
  return ({
    bookmarks: getBookmarks(state),
  })
}

const mapDispatchToProps = {
  getAllBookmarks,
  signOut,
}

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(HomePage)

HomePage.propTypes = {
  getAllBookmarks: PropTypes.func,
  signOut: PropTypes.func,
}
