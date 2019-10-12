import React from "react"
import Avatar from "@material-ui/core/Avatar"
import CssBaseline from "@material-ui/core/CssBaseline"
import LockOutlinedIcon from "@material-ui/icons/LockOutlined"
import Typography from "@material-ui/core/Typography"
import Container from "@material-ui/core/Container"
import {Formik} from "formik"
import * as Yup from "yup"
import {useStyles} from "components/Forms/style"
import {LoginForm} from "components/Forms/LoginForm"
import {getAuthentication, getErrorMessage} from "reduxStore/selectors/auth"
import {signIn} from "reduxStore/action/auth"
import {connect} from "react-redux"
import * as PropTypes from "prop-types"

export const LoginPage = (props) => {
  const classes = useStyles()
  const {
    signIn,
    authenticated,
    history,
  } = props
  const handleSubmit = ({username, password}, {setStatus, setSubmitting}) => {
    setStatus("")
    signIn({username, password})
    setSubmitting(false)
  }
  if (authenticated) {
    history.push("/")
  }
  // if (props.errorMessage) {
  //   props.setStatus(props.errorMessage)
  // }
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline/>
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon/>
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <Formik
          initialValues={{
            username: "",
            password: "",
          }}
          validationSchema={Yup.object().shape({
            username: Yup.string().required("Username is required"),
            password: Yup.string().required("Password is required"),
          })}
          onSubmit={handleSubmit}
          render={(props) =>
            <LoginForm
              {...props}
              classes={classes}
            />
          }
        />
      </div>
    </Container>
  )
}

const mapStateToProps = (state) => ({
  errorMessage: getErrorMessage(state),
  authenticated: getAuthentication(state),
  state: state
})

const mapDispatchToProps = {
  signIn,
}

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(LoginPage)


LoginPage.propTypes = {
  signIn : PropTypes.func,
  authenticated: PropTypes.bool,
  history: PropTypes.object,
}
