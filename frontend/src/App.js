import React from "react";
import { Provider } from "react-redux";
import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import store from "./store";
import { MessageProvider } from "./context/MessageContext";
import PageTransition from "./components/PageTransition";
import NavigationProgress from "./components/NavigationProgress";
import Breadcrumb from "./components/Breadcrumb";
import Navbar from "./components/Navbar";
import Notifications from "./components/Notifications";
import ProtectedRoute from "./components/ProtectedRoute";
import LeagueStandings from "./components/LeagueStandings";
import Matches from "./components/Matches";
import MatchDetail from "./components/MatchDetail";
import Players from "./components/Players";
import CompetitionDetail from "./components/CompetitionDetail";
import PlayerDetail from "./components/PlayerDetail";
import Teams from "./components/Teams";
import TeamDetail from "./components/TeamDetail";
import NotFound from "./components/NotFound";
import ErrorBoundary from "./components/ErrorBoundary";
import AdminDashboard from "./pages/AdminDashboard";
import LeagueManagerDashboard from "./pages/LeagueManagerDashboard";
import TeamOwnerDashboard from "./pages/TeamOwnerDashboard";
import PlayerDashboard from "./pages/PlayerDashboard";
import Login from "./pages/Login";
import Home from "./pages/Home";

const router = createBrowserRouter([
  {
    element: (
      <Provider store={store}>
        <ErrorBoundary>
          <MessageProvider>
            <div>
              <NavigationProgress />
              <Navbar />
              <div className="container mt-4">
                <Breadcrumb />
                <PageTransition>
                  <Outlet />
                </PageTransition>
              </div>
            </div>
          </MessageProvider>
        </ErrorBoundary>
      </Provider>
    ),
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/admin",
        element: (
          <ProtectedRoute role="ADMIN">
            <AdminDashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: "/league-manager",
        element: (
          <ProtectedRoute role="LEAGUE_MANAGER">
            <LeagueManagerDashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: "/team-owner",
        element: (
          <ProtectedRoute role="TEAM_OWNER">
            <TeamOwnerDashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: "/player",
        element: (
          <ProtectedRoute role="PLAYER">
            <PlayerDashboard />
          </ProtectedRoute>
        ),
      },
      {
        path: "/notifications",
        element: <Notifications />,
      },
      {
        path: "/teams",
        element: <Teams />,
      },
      {
        path: "/teams/:id",
        element: <TeamDetail />,
      },
      {
        path: "/matches",
        element: <Matches />,
      },
      {
        path: "/matches/:id",
        element: <MatchDetail />,
      },
      {
        path: "/players",
        element: <Players />,
      },
      {
        path: "/players/:id",
        element: <PlayerDetail />,
      },
      {
        path: "/standings/:competitionId",
        element: <LeagueStandings />,
      },
      {
        path: "/competitions",
        element: <Home />,
      },
      {
        path: "/competitions/:id",
        element: <CompetitionDetail />,
      },
      {
        path: "*",
        element: <NotFound />,
      },
    ],
  },
]);

const App = () => {
  return <RouterProvider router={router} />;
};

export default App;
