import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import teamService from "../services/teamService";
import { useMessage } from "../context/MessageContext";
import useDocumentMeta from "../hooks/useDocumentMeta";
import { validateSlug } from "../utils/urlValidator";
import NotFound from "./NotFound";

const TeamDetail = () => {
  const { id, slug } = useParams();
  const [team, setTeam] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { showMessage } = useMessage();
  const navigate = useNavigate();
  const [notFound, setNotFound] = useState(false);

  useDocumentMeta(
    team ? `${team.name}` : "Team Details",
    team
      ? `View detailed statistics and information about ${team.name}`
      : "Loading team details"
  );

  useEffect(() => {
    const fetchTeamDetails = async () => {
      try {
        const data = await teamService.getTeam(id, slug);
        if (!data) {
          setNotFound(true);
          return;
        }
        if (!validateSlug(slug, data.name)) {
          navigate(`/teams/${id}/${validateSlug(data.name)}`, {
            replace: true,
          });
          return;
        }
        setTeam(data);
      } catch (error) {
        if (error.message.includes("not found")) {
          setNotFound(true);
        } else {
          setError(error.message);
          showMessage("Error loading team details", "danger");
        }
      } finally {
        setLoading(false);
      }
    };
    fetchTeamDetails();
  }, [id, slug, navigate, showMessage]);

  if (notFound) return <NotFound />;
  if (loading) return <div className="text-center">Loading...</div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;
  if (!team) return <div>Team not found</div>;

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header bg-primary text-white">
          <h2>{team.name}</h2>
        </div>
        <div className="card-body">
          <div className="row">
            <div className="col-md-6">
              <h4>Team Information</h4>
              <p>
                <strong>Ranking:</strong> {team.ranking}
              </p>
              <p>
                <strong>Description:</strong> {team.description}
              </p>
            </div>
            <div className="col-md-6">
              <h4>Statistics</h4>
              <p>
                <strong>Matches Played:</strong> {team.matches_played}
              </p>
              <p>
                <strong>Wins:</strong> {team.wins}
              </p>
              <p>
                <strong>Losses:</strong> {team.losses}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default TeamDetail;
