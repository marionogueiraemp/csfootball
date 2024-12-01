import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await axios.get(
          `${process.env.REACT_APP_API_URL}/teams/`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        setTeams(response.data);
        setLoading(false);
      } catch (err) {
        setError("Error loading teams");
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div>Loading teams...</div>;
  if (error) return <div className="error-message">{error}</div>;

  return (
    <div className="teams-container">
      <h1>Teams</h1>
      <div className="teams-grid">
        {teams.map((team) => (
          <div
            key={team.id}
            className="team-card"
            onClick={() => navigate(`/teams/${team.id}`)}
          >
            <h3>{team.name}</h3>
            <p>Players: {team.player_count}</p>
            <p>Matches: {team.matches_played}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Teams;
