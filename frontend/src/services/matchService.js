import { slugify } from "../utils/slugify";
import { apiConfig } from "../config/api";
import axios from "axios";

const api = axios.create(apiConfig);

export const matchService = {
  getMatches: async () => {
    try {
      const response = await api.get("/matches/");
      return response.data.map((match) => ({
        ...match,
        slug: slugify(`${match.home_team}-vs-${match.away_team}`),
      }));
    } catch (error) {
      throw error;
    }
  },

  getMatch: async (id, slug) => {
    try {
      const response = await api.get(`/matches/${id}/${slug}/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default matchService;
