import { apiConfig } from "../config/api";
import { handleApiError } from "../utils/errorHandler";
import axios from "axios";

const api = axios.create(apiConfig);

export const standingsService = {
  fetchStandings: async (competitionId) => {
    try {
      const response = await api.get(
        `/competitions/${competitionId}/standings/`
      );
      return response.data;
    } catch (error) {
      throw handleApiError(error);
    }
  },

  getTeams: async () => {
    try {
      const response = await api.get("/teams/");
      return response.data;
    } catch (error) {
      throw handleApiError(error);
    }
  },

  getTeam: async (id) => {
    try {
      const response = await api.get(`/teams/${id}/`);
      return response.data;
    } catch (error) {
      throw handleApiError(error);
    }
  },
};

export default standingsService;
