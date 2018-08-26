# 封装任务函数
from celery_tasks.main import celery_app


@celery_app.task(name='send_sms_code')
def send_sms_code(a, b):
    print('任务函数被调用... a: %s, b: %s' % (a, b))
    # ...
