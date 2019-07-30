import React from "react";
import {Router, Route, Link} from "react-router-dom";
import {history} from "@/_helpers";
import {PrivateRoute} from "@/_components";
import {HomePage} from "@/HomePage";
import {LoginPage} from "@/LoginPage";

class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router history={history}>
                <PrivateRoute exact path="/" component={HomePage}/>
                <Route path="/login" component={LoginPage}/>
            </Router>
        );
    }
}

export {App};
