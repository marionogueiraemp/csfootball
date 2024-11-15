import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import axios from "axios";
import { Link } from "react-router-dom";

const LeagueManagerDashboard = () => {
  const [competitions, setCompetitions] = useState([]);
  const [teamApplications, setTeamApplications] = useState([]);
  const [playerTransfers, setPlayerTransfers] = useState([]);
  const [matches, setMatches] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const userToken = useSelector((state) => state.auth.token);

  useEffect(() => {
    const fetchDashboardData = async () => {
      setIsLoading(true);
      try {
        // Fetch competitions
        const competitionsResponse = await axios.get("/api/competitions/", {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        });
        setCompetitions(competitionsResponse.data);

        // Fetch team applications
        const teamApplicationsResponse = await axios.get(
          "/api/teams/applications/",
          {
            headers: {
              Authorization: `Bearer ${userToken}`,
            },
          }
        );
        setTeamApplications(teamApplicationsResponse.data);

        // Fetch player transfer requests
        const playerTransfersResponse = await axios.get(
          "/api/teams/transfers/",
          {
            headers: {
              Authorization: `Bearer ${userToken}`,
            },
          }
        );
        setPlayerTransfers(playerTransfersResponse.data);

        // Fetch matches
        const matchesResponse = await axios.get("/api/competitions/matches/", {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        });
        setMatches(matchesResponse.data);

        setIsLoading(false);
      } catch (error) {
        console.error("Error fetching dashboard data:", error);
        setIsLoading(false);
      }
    };

    fetchDashboardData();
  }, [userToken]);

  const handleApproveApplication = async (applicationId) => {
    try {
      await axios.post(
        `/api/teams/applications/${applicationId}/approve/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        }
      );
      alert("Application approved!");
      setTeamApplications((prev) =>
        prev.filter((app) => app.id !== applicationId)
      );
    } catch (error) {
      console.error("Error approving application:", error);
      alert("Failed to approve application.");
    }
  };

  const handleRejectApplication = async (applicationId) => {
    try {
      await axios.post(
        `/api/teams/applications/${applicationId}/reject/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        }
      );
      alert("Application rejected.");
      setTeamApplications((prev) =>
        prev.filter((app) => app.id !== applicationId)
      );
    } catch (error) {
      console.error("Error rejecting application:", error);
      alert("Failed to reject application.");
    }
  };

  const handleApproveTransfer = async (transferId) => {
    try {
      await axios.post(
        `/api/teams/transfers/${transferId}/approve/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        }
      );
      alert("Transfer approved!");
      setPlayerTransfers((prev) =>
        prev.filter((transfer) => transfer.id !== transferId)
      );
    } catch (error) {
      console.error("Error approving transfer:", error);
      alert("Failed to approve transfer.");
    }
  };

  const handleRejectTransfer = async (transferId) => {
    try {
      await axios.post(
        `/api/teams/transfers/${transferId}/reject/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        }
      );
      alert("Transfer rejected.");
      setPlayerTransfers((prev) =>
        prev.filter((transfer) => transfer.id !== transferId)
      );
    } catch (error) {
      console.error("Error rejecting transfer:", error);
      alert("Failed to reject transfer.");
    }
  };

  const generateFixtures = async (competitionId) => {
    try {
      await axios.post(
        `/api/competitions/${competitionId}/generate-fixtures/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${userToken}`,
          },
        }
      );
      alert("Fixtures generated successfully!");
    } catch (error) {
      console.error("Error generating fixtures:", error);
      alert("Failed to generate fixtures.");
    }
  };

  const updateMatch = async (matchId, matchData) => {
    try {
      await axios.put(`/api/competitions/matches/${matchId}/`, matchData, {
        headers: {
          Authorization: `Bearer ${userToken}`,
        },
      });
      alert("Match updated successfully!");
      setMatches((prev) =>
        prev.map((match) =>
          match.id === matchId ? { ...match, ...matchData } : match
        )
      );
    } catch (error) {
      console.error("Error updating match:", error);
      alert("Failed to update match.");
    }
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>League Manager Dashboard</h1>

      <section>
        <h2>Competitions</h2>
        {competitions.length > 0 ? (
          <ul>
            {competitions.map((competition) => (
              <li key={competition.id}>
                <Link to={`/competitions/${competition.id}`}>
                  {competition.name}
                </Link>
                <button onClick={() => generateFixtures(competition.id)}>
                  Generate Fixtures
                </button>
              </li>
            ))}
          </ul>
        ) : (
          <p>No competitions available.</p>
        )}
      </section>

      <section>
        <h2>Team Applications</h2>
        {teamApplications.length > 0 ? (
          <ul>
            {teamApplications.map((application) => (
              <li key={application.id}>
                <span>{application.team_name}</span>
                <button
                  onClick={() => handleApproveApplication(application.id)}
                >
                  Approve
                </button>
                <button onClick={() => handleRejectApplication(application.id)}>
                  Reject
                </button>
              </li>
            ))}
          </ul>
        ) : (
          <p>No team applications pending.</p>
        )}
      </section>

      <section>
        <h2>Player Transfer Requests</h2>
        {playerTransfers.length > 0 ? (
          <ul>
            {playerTransfers.map((transfer) => (
              <li key={transfer.id}>
                <span>
                  {transfer.player_name} from {transfer.current_team} to{" "}
                  {transfer.requested_team}
                </span>
                <button onClick={() => handleApproveTransfer(transfer.id)}>
                  Approve
                </button>
                <button onClick={() => handleRejectTransfer(transfer.id)}>
                  Reject
                </button>
              </li>
            ))}
          </ul>
        ) : (
          <p>No player transfer requests pending.</p>
        )}
      </section>

      <section>
        <h2>Matches</h2>
        {matches.length > 0 ? (
          <ul>
            {matches.map((match) => (
              <li key={match.id}>
                <span>
                  {match.home_team} vs {match.away_team}
                </span>
                <button
                  onClick={() => updateMatch(match.id, { status: "Completed" })}
                >
                  Mark as Completed
                </button>
              </li>
            ))}
          </ul>
        ) : (
          <p>No matches available.</p>
        )}
      </section>
    </div>
  );
};

export default LeagueManagerDashboard;
