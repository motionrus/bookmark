import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import React from "react";

export const LoginForm = (props) => (
    <form className={props.classes.form} onSubmit={props.handleSubmit}>
        <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
            autoFocus
            onChange={props.handleChange}

        />
        <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={props.handleChange}
        />
        <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={props.classes.submit}
        >
            Sign In
        </Button>
        <Grid container>
            <Grid item xs>
                <Link href="#" variant="body2">
                    Forgot password?
                </Link>
            </Grid>
            <Grid item>
                <Link href="#" variant="body2">
                    {"Don't have an account? Sign Up"}
                </Link>
            </Grid>
        </Grid>
    </form>
);
