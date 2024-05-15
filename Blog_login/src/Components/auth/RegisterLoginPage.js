import React, { useEffect, useState } from "react";

import Avatar from "@mui/material/Avatar";
// import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
// import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";

import { Tab, Tabs, TextField, Button, Alert } from "@mui/material";
import SignUp from "./SignUp";
import LoginPage from "./LoginPage";
import { getToken } from "../../service/LocalStorageService";
import { useDispatch } from "react-redux";
import { setUserToken } from "../../store/slice/authSlice";

function Copyright(props) {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

// A custom component that renders a register and login page within one component
const RegisterLoginPage = () => {
  // State variables to store the current tab and the alert message
  const [tab, setTab] = useState(0);
  const [alert, setAlert] = useState(null);
  const dispatch = useDispatch();

  let { access_token } = getToken();

  useEffect(() => {
    dispatch(setUserToken({ access_token: access_token }));
  }, [access_token, dispatch]);

  // The handler function for changing the tab
  const handleChangeTab = (event, newValue) => {
    setTab(newValue);
    setAlert(null);
  };

  return (
    <div>
      <Container component="main" maxWidth="xs">
        <CssBaseline />

        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <Tabs value={tab} onChange={handleChangeTab}>
            <Tab label="Register" />
            <Tab label="Login" />
          </Tabs>
          {tab === 0 && <SignUp />}
          {tab === 1 && <LoginPage />}
        </Box>
      </Container>

      {/* {alert && <Alert severity={alert.type}>{alert.message}</Alert>} */}
    </div>
  );
};

export default RegisterLoginPage;
