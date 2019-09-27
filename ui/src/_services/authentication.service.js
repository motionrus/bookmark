import {BehaviorSubject} from "rxjs"
import {config} from "config"
import {handleResponse} from "_helpers"

const currentUserSubject = new BehaviorSubject(JSON.parse(localStorage.getItem("currentUser")))

export const authenticationService = {
  login,
  logout,
  currentUser: currentUserSubject.asObservable(),
  get currentUserValue() {
    return currentUserSubject.value
  },
}

function login(username, password) {
  const requestOptions = {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({username, password}),
  }

  return fetch(`${config.apiUrl}/api/token-auth/`, requestOptions)
    .then(handleResponse)
    .then(token => {
      // store user details and jwt token in local storage to keep user logged in between page refreshes
      localStorage.setItem("currentUser", JSON.stringify(token))
      currentUserSubject.next(token)

      return token
    })
}

function logout() {
  // remove user from local storage to log user out
  localStorage.removeItem("currentUser")
  currentUserSubject.next(null)
}
