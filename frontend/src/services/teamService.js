import { slugify } from "../utils/slugify";
import { apiConfig } from "../config/api";
import axios from "axios";

const api = axios.create(apiConfig);

export const teamService = {
  getTeams: async () => {
    try {
      const response = await api.get("/teams/");
      return response.data.map((team) => ({
        ...team,
        slug: slugify(team.name),
      }));
    } catch (error) {
      throw error;
    }
  },

  getTeam: async (id, slug) => {
    try {
      const response = await api.get(`/teams/${id}/${slug}/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default teamService;
