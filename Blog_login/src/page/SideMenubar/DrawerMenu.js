import {
  Button,
  Drawer,
  List,
  ListItem,
  ListItemText,
} from "@material-ui/core";
import { ListItemButton } from "@mui/material";
import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";
import { unsetDrawer } from "../../store/slice/drawerSlice";

const DrawerMenu = ({ open }) => {
  const { open_drawer } = useSelector((state) => state.drawerSlice);

  const dispatch = useDispatch();

  const Course = ["Profile", "Javascript", "CSS", "React JS", `python`];

  console.log(open_drawer, "drawer ");
  return (
    <>
      <Drawer
        anchor="right"
        open={open_drawer}
        onClose={() => dispatch(unsetDrawer({ close_drawer: false }))}
      >
        <List>
          {Course.map((item) => {
            return (
              <>
                <ListItemButton
                  onClick={() => dispatch(unsetDrawer({ close_drawer: false }))}
                >
                  <ListItemText primary={item} />
                </ListItemButton>
              </>
            );
          })}
        </List>
      </Drawer>
    </>
  );
};

export default DrawerMenu;
