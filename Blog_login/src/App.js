import logo from "./logo.svg";
import "./App.css";
import { Link, NavLink, Navigate, Route, Routes } from "react-router-dom";

import Navbar from "./Components/Navbar";
import RegisterLoginPage from "./Components/auth/RegisterLoginPage";
import SignUp from "./Components/auth/SignUp";
import Blog from "./page/Blog";
import { useSelector } from "react-redux";
import ProfileCom from "./page/Profile/ProfileCom";

// import { useDispatch } from "react-redux";

function App() {
  // const dispatch = useDispatch();
  const { access_token } = useSelector((state) => state.auth);

  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Blog />} />
        <Route path="/profile" element={<ProfileCom />} />
        <Route
          path="/register"
          element={
            !access_token ? (
              <RegisterLoginPage />
            ) : (
              <Navigate to={"/dashboard"} />
            )
          }
        />
        <Route
          path="/dashboard"
          element={access_token ? <Blog /> : <Navigate to={"/register"} />}
        />
      </Routes>
    </>
  );
}

export default App;
