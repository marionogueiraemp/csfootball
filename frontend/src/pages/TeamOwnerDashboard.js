import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { fetchTeamOwnerDashboardData } from "../services/dashboardService";

const TeamOwnerDashboard = () => {
  const [data, setData] = useState(null);
  const token = useSelector((state) => state.auth.token);

  useEffect(() => {
    const fetchData = async () => {
      const dashboardData = await fetchTeamOwnerDashboardData(token);
      setData(dashboardData);
    };
    fetchData();
  }, [token]);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>Team Owner Dashboard</h1>
      {data.teams.length > 0 ? (
        <div>
          <h2>Your Team:</h2>
          <ul>
            {data.teams.map((team) => (
              <li key={team.id}>
                <strong>{team.name}</strong>
                <img
                  src={team.logo}
                  alt={`${team.name} logo`}
                  style={{ width: "50px" }}
                />
              </li>
            ))}
          </ul>
          <p>Manage your team above.</p>
        </div>
      ) : (
        <p>
          You currently do not own a team.{" "}
          <a href="/create-team">Create a Team</a>
        </p>
      )}
      <p>Pending Transfer Requests: {data.pending_transfer_requests}</p>
    </div>
  );
};

export default TeamOwnerDashboard;
