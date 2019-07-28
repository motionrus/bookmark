import React from "react";

import {bookmarkService, authenticationService} from "@/_services";

class HomePage extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            currentUser: authenticationService.currentUserValue,
            bookmarks: null
        };
    }

    componentDidMount() {
        bookmarkService.getAll().then(bookmarks => this.setState({bookmarks}));
    }

    render() {
        const {currentUser, bookmarks} = this.state;
        return (
            <div>
                <h1>Hi {currentUser.firstName}!</h1>
                <p>You're logged in with React & JWT!!</p>
                <h3>Users from secure api end point:</h3>
                {bookmarks &&
                <ul>
                    {bookmarks.map(bookmark =>
                        <li key={bookmark.pk}>{bookmark.url}</li>
                    )}
                </ul>
                }
            </div>
        );
    }
}

export {HomePage}
