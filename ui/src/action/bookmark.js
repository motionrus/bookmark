import axios from "axios"
import {API_BOOKMARK, DELETE_BOOKMARK, ERROR, GET_ALL_BOOKMARK} from "action/constants"
import {authHeader} from "_helpers"
import {config} from "config"

axios.defaults.headers.common["Authorization"] = authHeader().Authorization


export function getAllBookmarks() {
  return (dispatch) => axios.get(config.apiUrl + API_BOOKMARK)
    .then(response => dispatch({data: response.data, type: GET_ALL_BOOKMARK}))
    .catch(() => dispatch({error: true, type: ERROR}))
}

export function deleteBookmark(pk) {
  return (dispatch) => axios.delete(`${config.apiUrl}${API_BOOKMARK}${pk}/`)
    .then(() => dispatch({pk: Number(pk), type: DELETE_BOOKMARK}))
    .catch(() => dispatch({error: true, type: ERROR}))
}
