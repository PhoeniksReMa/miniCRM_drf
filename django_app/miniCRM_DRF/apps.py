from django.apps import AppConfig


class CrmdrfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miniCRM_DRF'

    def ready(self):
        import miniCRM_DRF.signals