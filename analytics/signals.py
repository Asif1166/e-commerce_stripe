from django.dispatch import Signal

object_viewed_signal = Signal()


# Define a function to send the signal with specific arguments
def send_object_viewed_signal(instance, request):
    object_viewed_signal.send(
        sender=instance.__class__, instance=instance, request=request
    )
