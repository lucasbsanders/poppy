from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.modalview import ModalView
from kivy.garden.circulardatetimepicker import CircularTimePicker as CTP
from kivy.uix.button import Button

from kivy.metrics import sp, dp
from kivy.utils import rgba


class NewTask(ModalView):
    def __init__(self, **kw):
        super().__init__(**kw)

    def get_time(self):
        mv = ModalView(size_hint=[.8, .6])
        box = BoxLayout(orientation='vertical', size_hint=[.5, .5])
        mv.add_widget(box)

        cl = CTP(color=[1, 1, 1, 1])
        cl.bind(time=self.set_time)

        submit = Button(text='OK', background_normal='',
                        background_color=rgba('#ffffff'), color=rgba('#0e1574ff'), size_hint_y=.2)

        submit.bind(on_release=lambda x: self.update_time(cl.time, mv))
        box.add_widget(cl)
        box.add_widget(submit)
        mv.open()

    def set_time(self, inst, value):
        print(value)

    def update_time(self, time, mv):
        mv.dismiss()
        self.ids.task_time.text = str(time)


class NewButton(ButtonBehavior, BoxLayout):
    pass


class Task(ButtonBehavior, BoxLayout):
    name = StringProperty('')
    time = StringProperty('')
    date = StringProperty('')

    def __init__(self, **kw):
        super().__init__(**kw)


class Upcoming(Task):
    pass


class Today(Task):
    pass


class MainWindow (BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    def add_new(self):
        nt = NewTask()
        nt.open()

    def add_task(self, mv, xtask: tuple):
        error = False
        scroll_parent = self.ids.scroll_parent
        tw = self.ids.today_wrapper

        for t in xtask:
            if len(t.text) < 3:
                t.hint_text = 'Field required'
                t.hint.text_color = [1, 0, 0, 1]
                error = True
        if error:
            pass
        else:
            task = Today()
            task.name = xtask[0].text
            task.time = xtask[1].text
            task.date = xtask[2].text
            task.size_hint = (None, None)
            task.size = [scroll_parent.width/2.4, scroll_parent.height * .9]

            tw.add_widget(task)
            mv.dismiss()

            # check if we have enough tasks to show
            if len(tw.children) > 1:
                for child in tw.children:
                    if type(child) == NewButton:
                        tw.remove_widget(child)

    def auth_user(self, username, password):
        uname = username.text
        upass = password.text

        self.ids.scrn_mngr.current = 'scrn_main'
