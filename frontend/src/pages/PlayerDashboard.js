import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { fetchPlayerDashboardData } from "../services/dashboardService";

const PlayerDashboard = () => {
  const [data, setData] = useState(null);
  const token = useSelector((state) => state.auth.token);

  useEffect(() => {
    const fetchData = async () => {
      const dashboardData = await fetchPlayerDashboardData(token);
      setData(dashboardData);
    };
    fetchData();
  }, [token]);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>Player Dashboard</h1>
      <p>Team Membership:</p>
      <ul>
        {data.team_membership.map((team) => (
          <li key={team.id}>{team.name}</li>
        ))}
      </ul>
      <p>Unread Notifications: {data.unread_notifications}</p>
    </div>
  );
};

export default PlayerDashboard;
