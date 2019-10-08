import React, {useEffect} from "react"
import CssBaseline from "@material-ui/core/CssBaseline"
import Typography from "@material-ui/core/Typography"
import {SearchAppBar} from "components/SearchAppBar/SearchAppBar"
import {history} from "_helpers"
import {connect} from "react-redux"
import {getBookmarks} from "reduxStore/selectors/bookmark"
import {getAllBookmarks} from "reduxStore/action/bookmark"
import Main from "components/Main/Main"
import {signOut} from "reduxStore/action/auth"


const HomePage = (props) => {
  useEffect(() => {
    props.getAllBookmarks()

  }, [])
  const handleLogout = () => {
    props.signOut()
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
