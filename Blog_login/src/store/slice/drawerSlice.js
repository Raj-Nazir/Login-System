import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  open_drawer: false,
};

export const drawerSlice = createSlice({
  name: "drawer",
  initialState,
  reducers: {
    setDrawer: (state, action) => {
      state.open_drawer = action.payload.open_drawer;
    },
    unsetDrawer: (state, action) => {
      state.open_drawer = action.payload.close_drawer;
    },
  },
});

export const { setDrawer, unsetDrawer } = drawerSlice.actions;

export default drawerSlice.reducer;
