import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Matches = () => {
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchMatches = async () => {
      try {
        const response = await axios.get(
          `${process.env.REACT_APP_API_URL}/matches/`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        setMatches(response.data);
        setLoading(false);
      } catch (err) {
        setError("Error loading matches");
        setLoading(false);
      }
    };

    fetchMatches();
  }, []);

  if (loading) return <div>Loading matches...</div>;
  if (error) return <div className="error-message">{error}</div>;

  return (
    <div className="matches-container">
      <h1>Matches</h1>
      <div className="matches-grid">
        {matches.map((match) => (
          <div
            key={match.id}
            className="match-card"
            onClick={() => navigate(`/matches/${match.id}`)}
          >
            <p>
              {match.home_team_name} vs {match.away_team_name}
            </p>
            <p>Date: {new Date(match.match_date).toLocaleDateString()}</p>
            <p>Status: {match.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Matches;
