import logging
from datetime import datetime

logger = logging.getLogger('panel_monitoring')


class PanelLogger:
    @staticmethod
    def log_panel_event(event_type, details, user=None):
        logger.info(f"Panel Event: {event_type} | User: {user} | {details}")

    @staticmethod
    def log_panel_error(error_type, error_message, user=None):
        logger.error(f"Panel Error: {error_type} | User: {
                     user} | {error_message}")

    @staticmethod
    def log_panel_access(panel_id, user=None):
        logger.info(f"Panel Access: {panel_id} | User: {
                    user} | Time: {datetime.now()}")
