from collections.abc import Iterable

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def message_handler(msg):
    """
    catches errors in message sender
    :param msg: Message object
    :return: boolean(status of message), string(error message)
    """
    error_message = ""
    status = False
    try:
        msg.send()
        status = True
    except Exception as e:
        error_message = str(e)
    return status, error_message


def prepare_emails(emails):
    if isinstance(emails, str) or not isinstance(emails, Iterable):
        emails = [emails]
    return emails


def prepare_name():
    name = ""
    if name:
        return '%s <%s>' % (name, settings.EMAIL_HOST_USER)
    return settings.EMAIL_HOST_USER


def send_html_message(emails, title, template_path, context):
    """
    Send email by text template
    :param title: title message
    :param emails: list of receivers
    :param template_path: path to template, from templates/emails folder
    :param context: some context for template
    :return: boolean( status of message), string(error message)
    Example : send_html_message(["iurii.ebs@gmail.com", ], "Title", "emails/template.html", {"text": "test"})
    """
    html = render_to_string(template_path, context)
    msg = EmailMessage(
        title,
        html,
        to=prepare_emails(emails),
        from_email=prepare_name()
    )
    msg.content_subtype = 'html'
    return message_handler(msg)


def send_text_message(emails, title, text):
    """
    Send email by text template
    :param title: title message
    :param emails: list of receivers
    :param text: text for email message
    :return: boolean( status of message), string(error message)
    Example : send_html_message(["iurii.ebs@gmail.com", ], "Title test", "test test test")
    """
    msg = EmailMultiAlternatives(
        title,
        text,
        bcc=prepare_emails(emails),
        from_email=prepare_name()
    )
    return message_handler(msg)
