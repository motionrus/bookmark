import {authHeader, handleResponse} from "_helpers"
import {config} from "config"


export const bookmarkService = {
  getAll,
  deleteBookmark,
}

function getAll() {
  const requestOptions = {method: "GET", headers: authHeader()}
  return fetch(`${config.apiUrl}/api/bookmark`, requestOptions).then(handleResponse)
}

function deleteBookmark(id) {
  const requestOptions = {method: "DELETE", headers: authHeader()}
  return fetch(`${config.apiUrl}/api/bookmark/${id}/`, requestOptions).then(handleResponse)
}
