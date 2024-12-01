import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const [competitions, setCompetitions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCompetitions = async () => {
      try {
        const response = await axios.get(
          `${process.env.REACT_APP_API_URL}/competitions/`,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        setCompetitions(response.data);
        setLoading(false);
      } catch (error) {
        setError("Failed to fetch competitions");
        setLoading(false);
      }
    };

    fetchCompetitions();
  }, []);

  if (loading) return <div>Loading competitions...</div>;
  if (error) return <div className="error">{error}</div>;

  const handleCompetitionClick = (id) => {
    navigate(`/competitions/${id}`);
  };

  return (
    <div className="home">
      <h1>Competitions</h1>
      <div className="competition-list">
        {competitions.map((competition) => (
          <div
            key={competition.id}
            className="competition-card"
            onClick={() => handleCompetitionClick(competition.id)}
            style={{ cursor: "pointer" }}
          >
            <h2>{competition.name}</h2>
            <div className="competition-stats">
              <p>Teams: {competition.team_count}</p>
              <p>Matches: {competition.matches.length}</p>
            </div>
            <div className="competition-dates">
              <p>
                Start: {new Date(competition.start_date).toLocaleDateString()}
              </p>
              <p>End: {new Date(competition.end_date).toLocaleDateString()}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
