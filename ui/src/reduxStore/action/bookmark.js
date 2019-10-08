import axios from "axios"
import {DELETE_BOOKMARK, ERROR, GET_ALL_BOOKMARK} from "reduxStore/constants/constants"
import {BOOKMARK} from "reduxStore/constants/urlConstants"

axios.interceptors.request.use(config => {
  const token = localStorage.getItem("user")

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  return config
})

export function getAllBookmarks() {
  return (dispatch) => axios.get(BOOKMARK)
    .then(response => dispatch({data: response.data, type: GET_ALL_BOOKMARK}))

}

export function deleteBookmark(pk) {
  return (dispatch) => axios.delete(BOOKMARK + pk)
    .then(() => dispatch({pk: Number(pk), type: DELETE_BOOKMARK}))

}
