from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    verbose_name = "图片管理"

    def ready(self):
        # 导入信号处理器
        import images.signals