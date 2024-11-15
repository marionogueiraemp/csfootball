import React, { useEffect, useState } from "react";

const MatchLive = ({ matchId }) => {
  const [matchData, setMatchData] = useState(null);

  useEffect(() => {
    const socket = new WebSocket(`ws://127.0.0.1:8000/ws/matches/${matchId}/`);

    socket.onopen = () => {
      console.log(`WebSocket connected for match: ${matchId}`);
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("Match Update:", data);
      setMatchData(data); // Update the UI with the latest match data
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed.");
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    return () => {
      socket.close();
    };
  }, [matchId]);

  if (!matchData) return <div>Loading match data...</div>;

  return (
    <div>
      <h1>
        {matchData.team1} vs {matchData.team2}
      </h1>
      <p>
        Score: {matchData.team1_score} - {matchData.team2_score}
      </p>
    </div>
  );
};

export default MatchLive;
