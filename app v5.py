from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.progressbar import MDProgressBar
import mysql.connector
from kivy.clock import Clock
from kivy.uix.widget import Widget
import sqlite3
import time

mydb = sqlite3.connect("app2.db")

c = mydb.cursor()

jump = False
KV = '''
ScreenManager:
    id:rock
    Screen:
        name:"main"


        BoxLayout:
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
    def __init__(self, bar,**kwargs):
        super(ProgressList, self).__init__(**kwargs)
        self.bar = bar
        self.add_widget(self.bar)



class Test(MDApp):

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
        self.onetime = True
        self.listit = []
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
            print(self.romet2.text, x.text)
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
        c.execute("INSERT INTO  timer (name,hours,minutes,seconds,number) VALUES (?,?,?,?,?)",
                  (self.help.ids.frij.text, self.hour, self.minutes, self.seconds, self.ider))
        self.ider += 1
        mydb.commit()

    def screen3(self):
        # c.execute("DELETE FROM timer")

        c.execute("SELECT * FROM timer ORDER BY number DESC LIMIT 1 ")
        for i in c:
            # print(i,i[4])
            self.extracted_second = i[3]
            self.extracted_minute = i[2]
            self.added = self.extracted_minute * 60
        self.bar.max = self.extracted_second + self.added
        self.bar.value = self.extracted_second + self.added

        self.event = Clock.schedule_interval(self.pop, 1)
        # print(self.extracted_second)

    def pop(self, *args):
        # self.help.ids.counter.value = self.help.ids.counter.max
        pok = int(self.i.bar.value) - 1
        self.i.bar.value = pok

        if self.i.bar.value == 0:
            Clock.unschedule(self.event)

    def load_list(self):
        c.execute("SELECT * FROM timer ORDER BY number DESC LIMIT 1 ")
        for i in c:
            self.load_name = i[0]
            self.load_hours = i[1]
            self.load_minutes = i[2]
            self.load_seconds = i[3]
            self.Limit_for = True
            for i in range(8):
                if self.Limit_for == True:
                    self.bar = MDProgressBar(id="counter", max=26, value=26, size_hint=(0.7, 0),
                                             pos_hint={"center_x": 0.5, "center_y": 0.3})
                    lists = ProgressList(text=self.help.ids.frij.text,
                                         secondary_text=str(self.load_minutes) + ":" + str(self.load_seconds),
                                         tertiary_text=" ",
                                         bar=self.bar)
                    self.listit.append(lists)
                    self.help.ids.leep.add_widget(lists)
                    #c.execute("INSERT INTO  timer (lists,bar) VALUES (?,?)", (lists,self.bar,))
                    image = IconLeftWidget(icon="plus")
                    lists.add_widget(image)
                    self.Limit_for = False
                    self.help.ids.frij.text = ""

    def start_load_list(self):
        c.execute("SELECT * FROM timer ORDER BY number ASC")
        d = c.fetchall()
        # print(d[0])
        for t in d:
            # print(t[3])
            u = 0
            self.bar = MDProgressBar(id="counter", max=26, value=26, size_hint=(0.7, 0),
                                     pos_hint={"center_x": 0.5, "center_y": 0.3})
            lists = ProgressList(text=t[0],
                                 secondary_text=str(t[2]) + ":" + str(t[3]),
                                 tertiary_text=" ", bar=self.bar)
            self.help.ids.leep.add_widget(lists)
            image = IconLeftWidget(icon="plus")
            self.listit.append(lists)
            lists.add_widget(image)
            u += 1

    def screeble4(self):
        



        """
        for i in self.listit:
            self.sec = i.sec

            i.bar.max = self.sec
            self.value = i.bar.value
            self.event = Clock.schedule_interval(self.pop, 1)
            self.i = i

            
            self.sec = i.sec
            #self.addit = self.min * 60
            i.bar.max = self.sec
            #i.bar.value = self.sec + self.addit
            self.max = i.bar.max
            self.value = i.bar.value
            self.event = Clock.schedule_interval(self.pop, 1)
        """


Test().run()
