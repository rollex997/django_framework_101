from __future__ import absolute_import , unicode_literals
#email related imports
from task1.email_send_file import *
#celery related imports
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
@shared_task(name="send_email_task")
def send_email_task(email_id,subject,message,attachment_name, attachment_content):
    logger.info("Mail Sent!!!")
    return send_email(email_id,subject,message,attachment_name, attachment_content)