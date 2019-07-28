import config from "config";
import {authHeader, handleResponse} from "@/_helpers";

export const bookmarkService = {
    getAll
};

function getAll() {
    const requestOptions = {method: "GET", headers: authHeader()};
    return fetch(`${config.apiUrl}/api/bookmark`, requestOptions).then(handleResponse);
}
