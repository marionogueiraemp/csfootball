import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const CompetitionDetail = () => {
  const { id } = useParams();
  const [competition, setCompetition] = useState(null);
  const [standings, setStandings] = useState([]);
  const [matchFilter, setMatchFilter] = useState("ALL");
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  const getFilteredMatches = () => {
    if (matchFilter === "ALL") return competition.matches;
    return competition.matches.filter((match) => match.status === matchFilter);
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [competitionResponse, standingsResponse] = await Promise.all([
          axios.get(`${process.env.REACT_APP_API_URL}/competitions/${id}/`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }),
          axios.get(
            `${process.env.REACT_APP_API_URL}/competitions/${id}/standings/`,
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("access_token")}`,
              },
            }
          ),
        ]);

        setCompetition(competitionResponse.data);
        setStandings(standingsResponse.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  if (loading) return <div>Loading...</div>;
  if (!competition) return <div>Competition not found</div>;

  return (
    <div className="competition-detail">
      <h1>{competition.name}</h1>
      <div className="competition-info">
        <p>
          Start Date: {new Date(competition.start_date).toLocaleDateString()}
        </p>
        <p>End Date: {new Date(competition.end_date).toLocaleDateString()}</p>
        <p>Teams: {competition.team_count}</p>
      </div>

      <div className="standings-section">
        <h2>Standings</h2>
        <table className="standings-table">
          <thead>
            <tr>
              <th>Position</th>
              <th>Team</th>
              <th>MP</th>
              <th>W</th>
              <th>D</th>
              <th>L</th>
              <th>GF</th>
              <th>GA</th>
              <th>GD</th>
              <th>Pts</th>
            </tr>
          </thead>
          <tbody>
            {standings.map((team, index) => (
              <tr key={team.team}>
                <td>{index + 1}</td>
                <td>{team.team}</td>
                <td>{team.matches_played}</td>
                <td>{team.wins}</td>
                <td>{team.draws}</td>
                <td>{team.losses}</td>
                <td>{team.goals_scored}</td>
                <td>{team.goals_conceded}</td>
                <td>{team.goals_scored - team.goals_conceded}</td>
                <td>{team.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="matches-section">
        <h2>Matches</h2>
        <div className="match-filters">
          <button
            className={`filter-btn ${matchFilter === "ALL" ? "active" : ""}`}
            onClick={() => setMatchFilter("ALL")}
          >
            All Matches
          </button>
          <button
            className={`filter-btn ${matchFilter === "SCHEDULED" ? "active" : ""}`}
            onClick={() => setMatchFilter("SCHEDULED")}
          >
            Upcoming
          </button>
          <button
            className={`filter-btn ${matchFilter === "LIVE" ? "active" : ""}`}
            onClick={() => setMatchFilter("LIVE")}
          >
            Live
          </button>
          <button
            className={`filter-btn ${matchFilter === "COMPLETED" ? "active" : ""}`}
            onClick={() => setMatchFilter("COMPLETED")}
          >
            Completed
          </button>
        </div>
        {getFilteredMatches().map((match) => (
          <div
            key={match.id}
            className="match-card"
            onClick={() => navigate(`/matches/${match.id}`)}
            style={{ cursor: "pointer" }}
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

export default CompetitionDetail;
