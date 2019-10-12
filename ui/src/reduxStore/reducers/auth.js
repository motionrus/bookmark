import {AUTHENTICATED, AUTHENTICATION_ERROR, UNAUTHENTICATED} from "reduxStore/constants/constants"
import {Record} from "immutable"

const initState = Record({
  authenticated: localStorage.getItem("user") ? true : false,
  error: "",
})

export default function (state = initState(), action) {
  switch (action.type) {
  case AUTHENTICATED:
    return state.set("authenticated", true)
  case UNAUTHENTICATED:
    return state.set("authenticated", false)
  case AUTHENTICATION_ERROR:
    return state.set("error", action.payload)
  default:
    return state
  }
}
