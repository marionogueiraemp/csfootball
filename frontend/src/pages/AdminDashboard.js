import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { fetchAdminDashboardData } from "../services/dashboardService";

const AdminDashboard = () => {
  const [data, setData] = useState(null);
  const token = useSelector((state) => state.auth.token);

  useEffect(() => {
    const fetchData = async () => {
      const dashboardData = await fetchAdminDashboardData(token);
      setData(dashboardData);
    };
    fetchData();
  }, [token]);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <p>Total Users: {data.total_users}</p>
      <p>Total Teams: {data.total_teams}</p>
      <p>Total Competitions: {data.total_competitions}</p>
    </div>
  );
};

export default AdminDashboard;
