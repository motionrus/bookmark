import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Link from "@material-ui/core/Link";
import PropTypes from "prop-types";
import React from "react";
import { InputLabel } from '@material-ui/core';

export const LoginForm = ({
    classes,
    handleSubmit,
    handleChange,
    touched,
    errors,
    status,
    isSubmitting
}) => {
    const errorUsername = Boolean(touched.username && errors.username);
    const errorPassword = Boolean(touched.password && !!errors.password);
    return (
        <form className={classes.form} onSubmit={handleSubmit}>
        <TextField
            InputLabelProps={{ required: true }}
            error={errorUsername}
            variant="outlined"
            margin="normal"
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoComplete="username"
            autoFocus
            onChange={handleChange}
            helperText={errorUsername && errors.username}
        />
        <TextField
            InputLabelProps={{ required: true }}
            error={errorPassword}
            variant="outlined"
            margin="normal"
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            onChange={handleChange}
            helperText={errorPassword && errors.password}
        />
        <InputLabel error>{status}</InputLabel>
        <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
            disabled={isSubmitting}
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
    )
};

LoginForm.propTypes = {
    errors: PropTypes.object,
    touched: PropTypes.object,
    handleChange: PropTypes.func.isRequired,
    handleSubmit: PropTypes.func.isRequired,
    isSubmitting: PropTypes.bool,
};

LoginForm.defaultProps = {
    errors: {
        username: "",
        password: "",
    },
    touched: {
        username: false,
        password: false,
    },
    isSubmitting: true,
};

