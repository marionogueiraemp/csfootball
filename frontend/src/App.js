import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Components
import AdminDashboard from "./pages/AdminDashboard";
import LeagueManagerDashboard from "./pages/LeagueManagerDashboard";
import TeamOwnerDashboard from "./pages/TeamOwnerDashboard";
import PlayerDashboard from "./pages/PlayerDashboard";
import Notifications from "./components/Notifications";
import TeamPage from "./pages/TeamPage";
import MatchLive from "./components/MatchLive";
import ProtectedRoute from "./components/ProtectedRoute";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route
          path="/admin"
          element={
            <ProtectedRoute role="ADMIN">
              <AdminDashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/league-manager"
          element={
            <ProtectedRoute role="LEAGUE_MANAGER">
              <LeagueManagerDashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/team-owner"
          element={
            <ProtectedRoute role="TEAM_OWNER">
              <TeamOwnerDashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/player"
          element={
            <ProtectedRoute role="PLAYER">
              <PlayerDashboard />
            </ProtectedRoute>
          }
        />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/teams/:teamId" element={<TeamPage />} />
        <Route path="/matches/:matchId" element={<MatchLive />} />
        <Route path="/" element={<div>Welcome to CSFootball</div>} />
      </Routes>
    </Router>
  );
};

export default App;
