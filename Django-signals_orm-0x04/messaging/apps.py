from django.apps import AppConfig

class MessagingConfig(AppConfig):
    name = 'messaging' 

    def ready(self):
        """
        Override the ready method to import signal handlers.
        
        This ensures that the signal handlers are connected when the app is ready.
        """
        import messaging.signals  # Import signals to ensure they are registered
