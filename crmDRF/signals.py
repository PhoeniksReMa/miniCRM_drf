import logging
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Deal


@receiver(pre_save, sender=Deal)
def deal_stage_changed(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.stage != instance.stage:
            print(notify_user(instance, old_instance.stage, instance.stage))

def notify_user(instance, old_stage, new_stage):
    message = f"""
        Сделка "{instance.name}" была перемещена:
        Старый этап: {old_stage}
        Новый этап: {new_stage}
        """
    return message