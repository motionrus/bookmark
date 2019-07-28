import React from "react";
import Avatar from "@material-ui/core/Avatar";
import CssBaseline from "@material-ui/core/CssBaseline";
import LockOutlinedIcon from "@material-ui/icons/LockOutlined";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import {authenticationService} from "@/_services";
import {LoginForm} from "@/components/LoginPage/LoginForm";
import {useStyles} from "@/components/LoginPage/style";
import {Formik} from "formik";
import * as Yup from "yup";


export const LoginPage = (props) => {
    const classes = useStyles();
    if (authenticationService.currentUserValue) {
        props.history.push("/");
    }
    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline/>
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                    <LockOutlinedIcon/>
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <Formik
                    initialValues={{
                        username: "",
                        password: ""
                    }}
                    validationSchema={Yup.object().shape({
                        username: Yup.string().required("Username is required"),
                        password: Yup.string().required("Password is required")
                    })}
                    onSubmit={({username, password}, {setStatus, setSubmitting}) => {
                        setStatus();
                        authenticationService.login(username, password)
                            .then(
                                user => {
                                    const {from} = props.location.state || {from: {pathname: "/"}};
                                    props.history.push(from);
                                },
                                error => {
                                    setSubmitting(false);
                                    setStatus(error);
                                }
                            );
                    }}
                >
                    {(props) =>
                        <LoginForm
                            {...props}
                            classes={classes}
                        />
                    }
                </Formik>
            </div>
        </Container>
    );
}
