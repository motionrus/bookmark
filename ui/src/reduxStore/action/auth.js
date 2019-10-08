import {AUTHENTICATED, AUTHENTICATION_ERROR, UNAUTHENTICATED} from "reduxStore/constants/constants"
import axios from "axios"
import {SIGN_IN} from "reduxStore/constants/urlConstants"


export function signIn({username, password}) {
  return (dispatch) => {
    axios.post(SIGN_IN, {username, password})
      .then(response => {
        dispatch({type: AUTHENTICATED})
        localStorage.setItem("user", response.data.token)
      })
      .catch(() => dispatch({
        type: AUTHENTICATION_ERROR,
        payload: "Invalid email or password",
      }))
  }
}

export function signOut() {
  localStorage.removeItem("user")
  return {
    type: UNAUTHENTICATED,
  }
}
