import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";
import { login } from "../store/slices/authSlice";
import axios from "axios";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const location = useLocation();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/token/`,
        {
          username,
          password,
        },
        {
          maxRedirects: 0,
          validateStatus: null,
        }
      );

      const { access, refresh } = response.data;
      const token = access;

      localStorage.setItem("access_token", access);
      localStorage.setItem("refresh_token", refresh);

      const userResponse = await axios.get(
        `${process.env.REACT_APP_API_URL}/users/me/`,
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      const { role } = userResponse.data;
      localStorage.setItem("user_role", role);

      dispatch(login({ token, user: userResponse.data, role }));

      const from = location.state?.from?.pathname || "/";
      navigate(from);
    } catch (err) {
      setError("Invalid credentials");
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username:</label>
          <input
            type="text"
            className="form-control"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            className="form-control"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
