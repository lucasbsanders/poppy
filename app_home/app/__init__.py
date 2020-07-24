from kivy.app import App
from .view import MainWindow
# from android.permissions import request_permissions, Permission


class MainApp(App):
    def build(self):
        # request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
        #                      Permission.READ_EXTERNAL_STORAGE, Permission.CAMERA])
        return MainWindow()

    def on_pause(self, *args):
        return True

    def on_resume(self, *args):
        return True
