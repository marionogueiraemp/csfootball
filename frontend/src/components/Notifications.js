import React, { useEffect, useState } from "react";
import axios from "axios";

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);
  const [filter, setFilter] = useState("ALL");

  useEffect(() => {
    const fetchNotifications = async () => {
      const response = await axios.get("/api/notifications/", {
        params: filter !== "ALL" ? { category: filter } : {},
      });
      setNotifications(response.data);
    };

    fetchNotifications();
  }, [filter]);

  return (
    <div>
      <h1>Notifications</h1>
      <select onChange={(e) => setFilter(e.target.value)}>
        <option value="ALL">All</option>
        <option value="TRANSFER">Transfer</option>
        <option value="MATCH">Match</option>
        <option value="GENERAL">General</option>
      </select>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id}>{notification.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
