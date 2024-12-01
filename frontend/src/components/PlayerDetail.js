import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import playerService from "../services/playerService";
import { useMessage } from "../context/MessageContext";
import useDocumentMeta from "../hooks/useDocumentMeta";
import { validateSlug } from "../utils/urlValidator";
import NotFound from "./NotFound";

const PlayerDetail = () => {
  const { id, slug } = useParams();
  const [player, setPlayer] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { showMessage } = useMessage();
  const navigate = useNavigate();
  const [notFound, setNotFound] = useState(false);

  useDocumentMeta(
    player ? `${player.name}` : "Player Details",
    player
      ? `Player profile and statistics for ${player.name}`
      : "Loading player details"
  );

  useEffect(() => {
    const fetchPlayerDetails = async () => {
      try {
        const data = await playerService.getPlayer(id, slug);
        if (!data) {
          setNotFound(true);
          return;
        }
        if (!validateSlug(slug, data.name)) {
          navigate(`/players/${id}/${validateSlug(data.name)}`, {
            replace: true,
          });
          return;
        }
        setPlayer(data);
      } catch (error) {
        if (error.includes("not found")) {
          setNotFound(true);
        } else {
          setError(error);
          showMessage("Error loading player details", "danger");
        }
      } finally {
        setLoading(false);
      }
    };
    fetchPlayerDetails();
  }, [id, slug, navigate, showMessage]);

  if (notFound) return <NotFound />;
  if (loading) return <div className="text-center">Loading...</div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;
  if (!player) return <div>Player not found</div>;

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header bg-primary text-white">
          <h2>{player.name}</h2>
        </div>
        <div className="card-body">
          <div className="row">
            <div className="col-md-6">
              <h4>Player Information</h4>
              <p>
                <strong>Team:</strong> {player.team}
              </p>
              <p>
                <strong>Position:</strong> {player.position}
              </p>
              <p>
                <strong>Number:</strong> {player.number}
              </p>
              <p>
                <strong>Nationality:</strong> {player.nationality}
              </p>
            </div>
            <div className="col-md-6">
              <h4>Statistics</h4>
              <p>
                <strong>Games Played:</strong> {player.games_played}
              </p>
              <p>
                <strong>Goals:</strong> {player.goals}
              </p>
              <p>
                <strong>Assists:</strong> {player.assists}
              </p>
              <p>
                <strong>Yellow Cards:</strong> {player.yellow_cards}
              </p>
              <p>
                <strong>Red Cards:</strong> {player.red_cards}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PlayerDetail;
