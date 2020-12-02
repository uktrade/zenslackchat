from webapp import settings
from zenslackchat.zendesk_base_webhook import BaseWebHook
from zenslackchat.message import update_from_zendesk_email
from zenslackchat.message import update_with_comments_from_zendesk


class CommentsWebHook(BaseWebHook):
    """Handle Zendesk Comment Events.

    """    
    def handle_event(self, event, slack_client, zendesk_client):
        """Handle the comment trigger event we have been POSTed.

        Recover and update the comments with lastest from Zendesk.

        """
        update_with_comments_from_zendesk(event, slack_client, zendesk_client)


class EmailWebHook(BaseWebHook):
    """Handle Zendesk Email Events.

    """    
    def handle_event(self, event, slack_client, zendesk_client):
        """Handle the comment trigger event we have been POSTed.

        Recover and update the comments with lastest from Zendesk.

        """
        event['channel_id'] = settings.SRE_SUPPORT_CHANNEL
        event['zendesk_uri'] = settings.ZENDESK_REDIRECT_URI
        event['workspace_uri'] = settings.SLACK_WORKSPACE_URI

        update_from_zendesk_email(event, slack_client, zendesk_client)
