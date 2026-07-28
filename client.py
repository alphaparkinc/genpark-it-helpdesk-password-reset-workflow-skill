class HelpdeskWorkflowClient:
    def handle_reset(self, user_id: str, service: str) -> dict:
        return {
            "status": 'RESET_LINK_SENT'
        }
