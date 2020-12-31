# from django.db.models.signals import pre_save, post_save
# from django.dispatch import receiver
# from .models import Tickets
#
# @receiver(post_save, sender=Tickets)
# def create_ticket(sender, instance, created, **kwargs):
#     if created:
#         Tickets.objects.create(ticketsytem=instance)
#
# @receiver(post_save, sender=Tickets)
# def save_ticket(sender, instance, **kwargs):
#     instance.ticketsytem.save()
