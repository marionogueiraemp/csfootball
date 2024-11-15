import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { fetchLeagueManagerDashboardData } from "../services/dashboardService";
import { generateFixtures, updateMatch } from "../services/competitionService";

const LeagueManagerDashboard = () => {
  const [data, setData] = useState(null);
  const token = useSelector((state) => state.auth.token);

  const handleGenerateFixtures = async (competitionId) => {
    try {
      await generateFixtures(token, competitionId);
      alert("Fixtures generated successfully!");
    } catch (error) {
      console.error("Error generating fixtures:", error);
      alert("Failed to generate fixtures.");
    }
  };

  const handleUpdateMatch = async (matchId, team1Score, team2Score) => {
    try {
      await updateMatch(token, matchId, { team1Score, team2Score });
      alert("Match updated successfully!");
    } catch (error) {
      console.error("Error updating match:", error);
      alert("Failed to update match.");
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      const dashboardData = await fetchLeagueManagerDashboardData(token);
      setData(dashboardData);
    };
    fetchData();
  }, [token]);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>League Manager Dashboard</h1>
      <p>Competitions:</p>
      <ul>
        {data.competitions.map((competition) => (
          <li key={competition.id}>
            {competition.name}
            <button onClick={() => handleGenerateFixtures(competition.id)}>
              Generate Fixtures
            </button>
            <ul>
              {competition.matches.map((match) => (
                <li key={match.id}>
                  {match.team1} vs {match.team2} - Score: {match.team1Score} :{" "}
                  {match.team2Score}
                  <button
                    onClick={() =>
                      handleUpdateMatch(
                        match.id,
                        match.team1Score + 1,
                        match.team2Score
                      )
                    }
                  >
                    Update Score
                  </button>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LeagueManagerDashboard;
