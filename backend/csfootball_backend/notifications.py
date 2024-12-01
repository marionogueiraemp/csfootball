from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from datetime import datetime
from .template_loader import EmailTemplateLoader


class TaskNotifications:
    @staticmethod
    def send_task_report(report):
        subject = f"Cache Monitoring Task Report - {datetime.now().date()}"
        recipients = [admin[1] for admin in settings.ADMINS]

        EmailTemplateLoader.send_templated_email(
            subject=subject,
            template_name='task_report',
            context={'report': report},
            recipients=recipients
        )

    @staticmethod
    def send_alert(alert_type, message):
        subject = f"Cache Monitoring Alert: {alert_type}"
        recipients = [admin[1] for admin in settings.ADMINS]

        alert_data = {
            'type': alert_type,
            'message': message,
            'timestamp': datetime.now()
        }

        EmailTemplateLoader.send_templated_email(
            subject=subject,
            template_name='alert',
            context={'alert': alert_data},
            recipients=recipients
        )
