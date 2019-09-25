import config from "config";
import {authHeader, handleResponse} from "@/_helpers";

export const bookmarkService = {
    getAll,
    deleteBookmark,
};

function getAll() {
    const requestOptions = {method: "GET", headers: authHeader()};
    return fetch(`${config.apiUrl}/api/bookmark`, requestOptions).then(handleResponse);
}

function deleteBookmark(id) {
    const requestOptions = {method: "DELETE", headers: authHeader()};
    return fetch(`${config.apiUrl}/api/bookmark/${id}/`, requestOptions).then(handleResponse);
}
