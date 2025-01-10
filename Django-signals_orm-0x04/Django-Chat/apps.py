from django.apps import AppConfig

class DjangoChatConfig(AppConfig):
    name = 'Django-Chat'

    def ready(self):
        # Import the signals module to connect signal handlers
        import signals
