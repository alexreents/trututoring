from django.shortcuts import get_object_or_404
from classroom.models import Lesson
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
 
 
@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment was successful
        lesson = get_object_or_404(Lesson, id=ipn.invoice)
 
        if ipn.mc_gross == 22.50:
            # mark the order as paid
            lesson.paid = True
            lesson.save()
