from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget,IconRightWidget
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock
from kivy.uix.widget import Widget
import sqlite3
mydb = sqlite3.connect("app2.db")


c = mydb.cursor()
from kivy.core.audio import SoundLoader

sound = SoundLoader.load('point.wav')
jump = False
KV = '''
ScreenManager:
    id:rock
    Screen:
        name:"main"
        BoxLayout:
            id:piki
            orientation:"vertical"
            size_hint:(0.9,0.8)
            pos_hint:{"center_y":0.6}
            ScrollView:
                MDList:
                    id:leep
        MDRaisedButton:
            text:"ADD"
            pos_hint:{"center_x":0.2,"center_y":0.15}
            on_press:
                rock.current = "selecttime"
        MDRaisedButton:
            text:"START"
            pos_hint:{"center_x":0.8,"center_y":0.15}
            on_press:
                app.screeble4()
    Screen:
        name:"selecttime"
        MDTextField:
            id:frij
            hint_text:"Enter the name of the task"
            pos_hint:{"center_x":0.5,"center_y":0.9}
            size_hint:(0.7,0.1)
        MDLabel:
            pos_hint:{"center_x":0.6,"center_y":0.75}
            text:"HOURS" 
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.2,"center_y":0.5}
            size_hint:(0.2,0.4)                     
            ScrollView:
                MDList:
                    id:box
        MDLabel:
            pos_hint:{"center_x":0.9,"center_y":0.75}
            text:"MINUTES" 
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            size_hint:(0.2,0.4)                     
            ScrollView:
                MDList:
                    id:boo
        MDLabel:
            pos_hint:{"center_x":1.2,"center_y":0.75}
            text:"SECONDS" 
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.8,"center_y":0.5}
            size_hint:(0.2,0.4)                     
            ScrollView:
                MDList:
                    id:move
        MDRaisedButton:
            text:"CONFIRM"
            pos_hint:{"center_x":0.5,"center_y":0.2}
            on_press:
                rock.current = "main"
                app.store_data()
                app.load_list()
'''

screen = Screen()


class ProgressList(ThreeLineAvatarIconListItem, Widget):
    def __init__(self, bar, **kwargs):
        super(ProgressList, self).__init__(**kwargs)
        self.bar = bar
        self.add_widget(self.bar)


class SquentialTimer(MDApp):

    def build(self):
        self.help = Builder.load_string(KV)
        return self.help

    def on_start(self):
        self.iteretion = 0
        self.iteretion2 = 0
        self.iteretion3 = 0
        self.romet = 0
        self.romet2 = 0
        self.romet3 = 0
        self.prob = False
        self.prob2 = False
        self.prob3 = False
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        self.ider = 0
        self.Limit_for = True
        self.iu = 0
        self.u = 0
        self.onetime = True
        self.listit = []
        self.listitdown = []
        self.oneiter = True
        self.ij = 0
        self.secondtime = True
        self.iter = 0
        self.iteration = 0
        for i in range(23):
            self.items = OneLineListItem(text=str(i + 1), size_hint=(0.3, 0.5), on_release=lambda x: self.callbacker(x))
            self.help.ids.box.add_widget(self.items)

        for i in range(59):
            items1 = OneLineListItem(text=str(i + 1), size_hint=(0.3, 0.5), on_release=lambda x: self.callbacker2(x))
            self.help.ids.boo.add_widget(items1)

        for i in range(59):
            self.items2 = OneLineListItem(text=str(i + 1), size_hint=(0.1, 0.1),
                                          on_release=lambda x: self.callbacker3(x))
            self.help.ids.move.add_widget(self.items2)
        c.execute("SELECT * FROM timer ORDER BY number DESC LIMIT 1")
        for y in c:
            number = y[4]
            self.ider = number
            self.u = self.ider
        self.start_load_list()
    def callbacker(self, x):
        jump = True
        if self.iteretion3 == 0:
            self.earlyx2 = x
            x.bg_color = (0, 0, 255, 0.4)
            self.iteretion3 += 1
            self.hour = x.text
            jump = False
        if self.prob3 == True:
            self.romet3 = x
        if self.prob3 == True:
            self.prob3 = True

            if self.romet3 == x:
                self.hour = 0
        if self.iteretion3 >= 1 and jump == True:
            x.bg_color = (0, 0, 255, 0.4)
            self.earlyx2.bg_color = (225, 225, 225, 0.3)
            self.earlyx2 = x
            self.hour = x.text

    def callbacker2(self, x):
        jump = True
        if self.iteretion2 == 0:
            self.earlyx3 = x
            x.bg_color = (0, 0, 255, 0.4)
            self.iteretion2 += 1
            self.minutes = x.text
            jump = False
        if self.prob2 == True:
            self.romet2 = x
        if self.prob2 == True:
            self.prob2 = True
            if self.romet2 == x:
                self.minutes = 0
        if self.iteretion2 >= 1 and jump == True:
            x.bg_color = (0, 0, 255, 0.4)
            self.earlyx3.bg_color = (225, 225, 225, 0.3)
            self.earlyx3 = x
            self.minutes = x.text

    def callbacker3(self, x):
        jump = True
        if self.iteretion == 0:
            self.earlyx = x
            x.bg_color = (0, 0, 255, 0.4)
            self.iteretion += 1
            self.seconds = x.text
            jump = False
        if self.prob == True:
            self.romet = x
        if self.prob == True:
            self.prob = True
            if self.romet == x:
                self.seconds = 0
        if self.iteretion >= 1 and jump == True:
            x.bg_color = (0, 0, 255, 0.4)
            self.earlyx.bg_color = (225, 225, 225, 0.3)
            self.earlyx = x
            self.seconds = x.text

        jump = True
        self.prob = True

    def store_data(self):
        if self.onetime == True:
            self.ider += 1
            self.onetime = False
        self.bar = MDProgressBar(id="counter", max=26, value=26, size_hint=(0.7, 0),
                                 pos_hint={"center_x": 0.5, "center_y": 0.3})
        self.lists = ProgressList(text=self.help.ids.frij.text,
                                  secondary_text=str(self.minutes) + ":" + str(self.seconds),
                                  tertiary_text=" ",
                                  bar=self.bar)
        self.listitdown.append(self.lists)
        for i in self.listitdown:
            if self.oneiter == True:
                self.inserter = i
                c.execute("INSERT INTO  timer (name,hours,minutes,seconds,number,lists) VALUES (?,?,?,?,?,?)",
                          (self.help.ids.frij.text, self.hour, self.minutes, self.seconds, self.ider,
                           "self.listitdown[" + str(self.u) + "]"))
                self.oneiter = False
                self.u += 1
        self.ider += 1
        mydb.commit()
        self.oneiter = True


    def pop(self, *args):
        c.execute("SELECT * FROM timer ORDER BY number ASC  ")
        e = c.fetchall()
        self.pro = self.pro - 1
        self.pb.value = self.pro
        if self.pb.value == 0:
            c.execute("SELECT * FROM timer ORDER BY number DESC LIMIT 1 ")
            r = c.fetchall()
            self.ij += 1
            if self.ij != r[0][4]:
                Clock.unschedule(self.event)
                sound.play()
                self.screeble4()
            elif self.ij == r[0][4]:
                self.secondtime = False



    def load_list(self):
        c.execute("SELECT * FROM timer ORDER BY number DESC LIMIT 1 ")
        for i in c:
            self.load_name = i[0]
            self.load_hours = i[1]
            self.load_minutes = i[2]
            self.load_seconds = i[3] + self.load_minutes*60
            self.Limit_for = True
            for i in range(8):
                if self.Limit_for == True:
                    self.listit.append(self.lists)
                    self.help.ids.leep.add_widget(self.lists)
                    image = IconLeftWidget(icon="plus")
                    imageright = IconRightWidget(icon="minus")
                    self.lists.add_widget(image)
                    self.lists.add_widget(imageright)
                    imageright.bind(on_press=lambda x: self.delete_row((imageright.parent.parent)))
                    self.Limit_for = False
                    self.help.ids.frij.text = ""

    def start_load_list(self):
        c.execute("SELECT * FROM timer ORDER BY number ASC")
        d = c.fetchall()
        for t in d:
            u = 0
            self.bar = MDProgressBar(id="counter", max=t[3], value=t[3], size_hint=(0.7, 0),
                                     pos_hint={"center_x": 0.5, "center_y": 0.3})
            lists = ProgressList(text=t[0],
                                 secondary_text=str(self.bar.value//60) + ":" + str(self.bar.value)+str(self.bar.value),
                                 tertiary_text=" ", bar=self.bar)
            self.help.ids.leep.add_widget(lists)
            image = IconLeftWidget(icon="plus")
            self.image2 = IconRightWidget(icon="minus",on_press=lambda x: self.delete_row(x.parent.parent))
            self.listitdown.append(lists)
            lists.add_widget(self.image2)
            lists.add_widget(image)
            u += 1


    def screeble4(self):
        c.execute("SELECT * FROM timer")
        d = c.fetchall()
        if self.secondtime == True:
            self.pb = eval(d[self.ij][5]).bar
            self.addit = d[self.ij][2] * 60
            self.sce = d[self.ij][3]
            self.num = d[self.ij][4]
            self.pb.value = d[self.ij][2]*60+d[self.ij][3]
            self.pb.max = d[self.ij][2]*60+d[self.ij][3]
            self.pro = d[self.ij][2]*60+d[self.ij][3]
            self.pb.value = self.pro
            self.event = Clock.schedule_interval(self.pop, 1)
        else:
            c.execute("SELECT * FROM timer")
            e = c.fetchall()
            helpit = 0
            for i in self.listitdown:
                i.bar.value = e[helpit][2] * 60 + e[helpit][3]
                i.bar.max = i.bar.value
                self.secondtime = True
                self.ij = 0
    def delete_row(self,row):
        itere = 1
        self.root.ids.leep.remove_widget(row)
        c.execute("DELETE FROM timer WHERE name=?", (row.text,))
        mydb.commit()
        for i in self.listitdown:
            if i.text == row.text:
                self.listitdown.remove(i)
        for y in self.listitdown:
            c.execute("UPDATE timer SET lists=? WHERE name=?",
                      ("self.listitdown[" + str(self.iteration) + "]", y.text,))
            c.execute("UPDATE timer SET  number=? WHERE name = ? ",(itere,y.text,))
            itere +=1
            self.ider = itere
            mydb.commit()
            self.iteration += 1
        self.u = self.iteration
        self.iteration = 0





SquentialTimer().run()