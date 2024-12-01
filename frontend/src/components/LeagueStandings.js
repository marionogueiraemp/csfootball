import React, { useEffect, useState } from "react";
import { standingsService } from "../services/standingsService";

const LeagueStandings = ({ competitionId }) => {
  const [standings, setStandings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadStandings = async () => {
      try {
        setLoading(true);
        const data = await standingsService.fetchStandings(competitionId);
        setStandings(data);
      } catch (err) {
        setError(err.message || "Failed to load standings");
      } finally {
        setLoading(false);
      }
    };

    loadStandings();
  }, [competitionId]);

  if (loading) {
    return <p>Loading standings...</p>;
  }

  if (error) {
    return <p className="error">{error}</p>;
  }

  return (
    <div className="league-standings">
      <h2>League Standings</h2>
      <table className="standings-table">
        <thead>
          <tr>
            <th>Position</th>
            <th>Team</th>
            <th>Matches Played</th>
            <th>Wins</th>
            <th>Draws</th>
            <th>Losses</th>
            <th>Goals Scored</th>
            <th>Goals Conceded</th>
            <th>Goal Difference</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {standings.map((team, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{team.team_name}</td>
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
  );
};

export default LeagueStandings;
