import { slugify } from "../utils/slugify";
import { apiConfig } from "../config/api";
import axios from "axios";

const api = axios.create(apiConfig);

export const playerService = {
  getPlayers: async () => {
    try {
      const response = await api.get("/players/");
      return response.data.map((player) => ({
        ...player,
        slug: slugify(player.name),
      }));
    } catch (error) {
      throw error;
    }
  },

  getPlayer: async (id, slug) => {
    try {
      const response = await api.get(`/players/${id}/${slug}/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default playerService;
