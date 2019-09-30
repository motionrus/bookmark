import React, {useEffect} from "react"
import CssBaseline from "@material-ui/core/CssBaseline"
import Typography from "@material-ui/core/Typography"
import {SearchAppBar} from "components/SearchAppBar/SearchAppBar"
import {history} from "_helpers"
import {connect} from "react-redux"
import {getBookmarks} from "selectors/bookmark"
import {getAllBookmarks} from "action/bookmark"
import Main from "components/Main/Main"
import {authenticationService} from "_services/authentication.service"


const HomePage = (props) => {
  useEffect(() => {
    props.getAllBookmarks()

  }, [])
  const handleLogout = () => {
    authenticationService.logout()
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
}

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(HomePage)
