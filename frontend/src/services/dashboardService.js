import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/dashboard";

export const fetchAdminDashboardData = async (token) => {
  const response = await axios.get(`${API_URL}/admin/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};

export const fetchLeagueManagerDashboardData = async (token) => {
  const response = await axios.get(`${API_URL}/league-manager/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};

export const fetchNewsManagerDashboardData = async (token) => {
  const response = await axios.get(`${API_URL}/news-manager/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};

export const fetchTeamOwnerDashboardData = async (token) => {
  const response = await axios.get(`${API_URL}/team-owner/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};

export const fetchPlayerDashboardData = async (token) => {
  const response = await axios.get(`${API_URL}/player/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};
