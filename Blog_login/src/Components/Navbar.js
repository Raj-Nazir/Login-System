import React, { useState } from "react";
import { AppBar, Toolbar, Typography, Button, Avatar } from "@material-ui/core";
import { NavLink } from "react-router-dom";

import man from "E:/FullStack/Blog_Frontend/src/IMG/man.jpg";
import DrawerMenu from "../page/SideMenubar/DrawerMenu";
import { useDispatch } from "react-redux";
import { setDrawer } from "../store/slice/drawerSlice";

function Navbar() {
  const [open, setOpen] = useState(false);

  const dispatch = useDispatch();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          My App
        </Typography>
        <Button color="inherit" component={NavLink} to="/">
          Home
        </Button>
        <Button color="inherit" component={NavLink} to="/register">
          Register
        </Button>
        <Button color="inherit" component={NavLink} to="/dashboard">
          Dashboard
        </Button>
        <Button
          color="inherit"
          // onClick={() => dispatch(setDrawer({ open_drawer: true }))}
          component={NavLink}
          to="/profile"
        >
          <Avatar alt="Remy Sharp" src={man} />
          {/* <DrawerMenu /> */}
        </Button>
      </Toolbar>
      <DrawerMenu />
    </AppBar>
  );
}

export default Navbar;
