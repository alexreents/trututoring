from django.apps import AppConfig


class ClassroomAppConfig(AppConfig):
    name = 'classroom'

    def ready(self):
        # import signal handlers
        import classroom.signals
