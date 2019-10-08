import {combineReducers} from "redux"
import bookmarks from "reduxStore/reducers/bookmark"
import auth from "reduxStore/reducers/auth"

export default combineReducers({
  bookmarks,
  auth,
})
