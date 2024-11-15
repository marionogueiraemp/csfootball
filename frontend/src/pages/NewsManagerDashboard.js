import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { fetchNewsManagerDashboardData } from "../services/dashboardService";

const NewsManagerDashboard = () => {
  const [data, setData] = useState(null);
  const token = useSelector((state) => state.auth.token);

  useEffect(() => {
    const fetchData = async () => {
      const dashboardData = await fetchNewsManagerDashboardData(token);
      setData(dashboardData);
    };
    fetchData();
  }, [token]);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h1>News Manager Dashboard</h1>
      <p>News Posts: {data.news_posts}</p>
      <p>Interviews: {data.interviews}</p>
      <p>Historical Events: {data.historical_events}</p>
    </div>
  );
};

export default NewsManagerDashboard;
