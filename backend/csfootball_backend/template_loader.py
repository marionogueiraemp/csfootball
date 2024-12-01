from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


class EmailTemplateLoader:
    @staticmethod
    def render_task_report(report_data):
        html_content = render_to_string(
            'notifications/task_report.html',
            {'report': report_data}
        )
        text_content = render_to_string(
            'notifications/task_report.txt',
            {'report': report_data}
        )
        return html_content, text_content

    @staticmethod
    def send_templated_email(subject, report_data, recipients):
        html_content, text_content = EmailTemplateLoader.render_task_report(
            report_data)

        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            recipients
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
