import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import InputBase from "@material-ui/core/InputBase";
import SearchIcon from "@material-ui/icons/Search";
import IconButton from "@material-ui/core/IconButton";
import {useStyles} from "./style";
import {ExitToApp} from "@material-ui/icons";

export const SearchAppBar = ({onClick}) => {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <Typography className={classes.title} variant="h6" noWrap>
                        Bookmarks
                    </Typography>
                    <div className={classes.search}>
                        <div className={classes.searchIcon}>
                            <SearchIcon/>
                        </div>
                        <InputBase
                            placeholder="Search…"
                            classes={{
                                root: classes.inputRoot,
                                input: classes.inputInput,
                            }}
                            inputProps={{"aria-label": "search"}}
                        />
                    </div>
                    <div className={classes.grow}/>
                    <IconButton color="inherit" onClick={onClick}>
                        <ExitToApp/>
                    </IconButton>
                </Toolbar>
            </AppBar>
        </div>
    );
};
