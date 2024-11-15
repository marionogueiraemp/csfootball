import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const TeamPage = () => {
  const { teamId } = useParams();
  const [teamData, setTeamData] = useState(null);

  useEffect(() => {
    const fetchTeamData = async () => {
      const response = await axios.get(`/api/teams/${teamId}/`);
      setTeamData(response.data);
    };

    fetchTeamData();
  }, [teamId]);

  if (!teamData) return <div>Loading...</div>;

  return (
    <div>
      <h1>{teamData.team.name}</h1>
      <img src={teamData.team.logo} alt={`${teamData.team.name} logo`} />
      <h2>Players</h2>
      <ul>
        {teamData.players.map((player) => (
          <li key={player.id}>
            {player.username} - Goals: {player.goals}, Assists: {player.assists}
          </li>
        ))}
      </ul>
      <h2>Transfer History</h2>
      <ul>
        {teamData.transfers.map((transfer) => (
          <li key={transfer.id}>
            {transfer.player.username} transferred from {transfer.from_team} to{" "}
            {transfer.to_team}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeamPage;
