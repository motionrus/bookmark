import React from "react";
import CssBaseline from "@material-ui/core/CssBaseline";
import Typography from "@material-ui/core/Typography";
import {bookmarkService, authenticationService} from "@/_services";
import {Main} from "@/HomePage/components/Main/Main";
import {SearchAppBar} from "@/HomePage/components/SearchAppBar/SearchAppBar"
import {history} from "@/_helpers";
import { TablePagination } from '@material-ui/core';


class HomePage extends React.Component {
    constructor(props) {
        super(props);
        this.handleDeletePost = this.handleDeletePost.bind(this);
        this.state = {
            bookmarks: []
        }
    }

    componentDidMount() {
        bookmarkService.getAll().then(bookmarks => this.setState({bookmarks}));
    }

    handleDeletePost (event) {
        const {currentTarget: {dataset: {pk}}} = event;
        bookmarkService.deleteBookmark(pk).then(() => this.setState((state) => {
            const filteredBookmarks = state.bookmarks.filter(
                bookmark => bookmark.pk !== Number(pk)
            );
            return {...state, bookmarks: filteredBookmarks}
        }))
    }

    handleLogout() {
        authenticationService.logout();
        history.push("/login");
    }

    render() {
        const currentUser = authenticationService.currentUserValue;
        const {bookmarks} = this.state;
        return (
            <React.Fragment>
                <CssBaseline/>
                <SearchAppBar onClick={this.handleLogout}/>
                <Main bookmarks={bookmarks} onClick={this.handleDeletePost}/>
                <footer>
                    <Typography variant="h6" align="center" gutterBottom>
                        Footer
                    </Typography>
                    <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
                        Something here to give the footer a purpose!
                    </Typography>
                </footer>
            </React.Fragment>
        );
    }
}

export {HomePage}
