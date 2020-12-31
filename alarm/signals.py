# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Alarm, AlarmArchive
#
# @receiver(post_save, sender=AlarmArchive)
# def delete_alarm(sender, instance, created, model=Alarm, **kwargs):
#     if created:
#         print(f'MODEL    :::: {model}')
#         print(f'INSTANCE :::: {instance}')
#         print(f'SENDER   :::: {sender}')
#         alarm = Alarm.objects.get(pk=instance.id, alarm_date=instance.arcv_alarm_date)
#         print(f'ALARM    :::: {alarm}')
#         alarm.delete()
#         print(f'ALARM   AFTER CALL DELETE   ::::   {alarm}')
#         print(f'ALARM   AFTER CALL DELETE  TYPE   ::::   {type(alarm)}')

# @receiver(post_delete, sender=Alarm)
# def confirm_delete(sender, instance, **kwargs):
#     print('Alarm deleted????\n\n')
#     print(f'instance= {type(instance)}\n {instance}\n')
#     print(f'sender {type(sender)}\n {sender}\n')
#     print(f'kwargs  {type(kwargs)}\n {kwargs}\n')
    # Alarm.objects.get(id=instance.id, alarm_date=instance.arcv_alarm_date).delete()
