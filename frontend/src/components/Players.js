import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Players = () => {
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPlayers = async () => {
      try {
        const response = await axios.get(
          `${process.env.REACT_APP_API_URL}/players/`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        setPlayers(response.data);
        setLoading(false);
      } catch (err) {
        setError("Error loading players");
        setLoading(false);
      }
    };

    fetchPlayers();
  }, []);

  if (loading) return <div>Loading players...</div>;
  if (error) return <div className="error-message">{error}</div>;

  return (
    <div className="players-container">
      <h1>Players</h1>
      <div className="players-grid">
        {players.map((player) => (
          <div
            key={player.id}
            className="player-card"
            onClick={() => navigate(`/players/${player.id}`)}
          >
            <h3>{player.name}</h3>
            <p>Team: {player.team}</p>
            <p>Position: {player.position}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Players;
