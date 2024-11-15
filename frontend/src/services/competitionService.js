import axios from "axios";

const API_URL = "/api/competitions";

export const getCompetitions = async () => {
  const response = await axios.get(`${API_URL}/`);
  return response.data;
};

export const getCompetitionDetails = async (id) => {
  const response = await axios.get(`${API_URL}/${id}`);
  return response.data;
};

export const createCompetition = async (data) => {
  const response = await axios.post(`${API_URL}/`, data);
  return response.data;
};

export const updateCompetition = async (id, data) => {
  const response = await axios.put(`${API_URL}/${id}/`, data);
  return response.data;
};

export const deleteCompetition = async (id) => {
  const response = await axios.delete(`${API_URL}/${id}/`);
  return response.data;
};
