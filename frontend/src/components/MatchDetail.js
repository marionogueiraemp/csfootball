import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const MatchDetail = () => {
  const { id } = useParams();
  const [match, setMatch] = useState(null);
  const [playerStats, setPlayerStats] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMatchData = async () => {
      try {
        const [matchResponse, statsResponse] = await Promise.all([
          axios.get(
            `${process.env.REACT_APP_API_URL}/competitions/matches/${id}/`,
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("access_token")}`,
              },
            }
          ),
          axios.get(
            `${process.env.REACT_APP_API_URL}/competitions/matches/${id}/player-stats/`,
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("access_token")}`,
              },
            }
          ),
        ]);

        setMatch(matchResponse.data);
        setPlayerStats(statsResponse.data);
      } catch (error) {
        console.error("Error fetching match data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchMatchData();
  }, [id]);

  if (loading) return <div>Loading...</div>;
  if (!match) return <div>Match not found</div>;

  return (
    <div className="match-detail">
      <h1>Match Details</h1>
      <div className="match-header">
        <div className="team home">
          <h2>{match.home_team_name}</h2>
          {match.status === "COMPLETED" && (
            <div className="score">{match.home_score}</div>
          )}
        </div>
        <div className="vs">VS</div>
        <div className="team away">
          <h2>{match.away_team_name}</h2>
          {match.status === "COMPLETED" && (
            <div className="score">{match.away_score}</div>
          )}
        </div>
      </div>

      <div className="match-info">
        <p>Date: {new Date(match.match_date).toLocaleString()}</p>
        <p>Status: {match.status}</p>
      </div>

      <div className="player-stats">
        <h2>Player Statistics</h2>
        <table>
          <thead>
            <tr>
              <th>Player</th>
              <th>Goals</th>
              <th>Assists</th>
              <th>Yellow Cards</th>
              <th>Red Cards</th>
            </tr>
          </thead>
          <tbody>
            {playerStats.map((stat) => (
              <tr key={stat.id}>
                <td>{stat.player_name}</td>
                <td>{stat.goals}</td>
                <td>{stat.assists}</td>
                <td>{stat.yellow_cards}</td>
                <td>{stat.red_cards}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MatchDetail;
