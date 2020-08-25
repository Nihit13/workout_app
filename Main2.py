from kivy.lang import Builder
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem
import mysql.connector
from kivy.clock import  Clock
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
        MDRaisedButton:
            text:"ADD"
            on_press:
                rock.current = "selecttime"
        MDProgressBar:
            id:counter
            max:26
            value:26
            pos_hint:{"center_x":0.5,"center_y":0.5}
        
                
    Screen:
        name:"selecttime"
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.2,"center_y":0.7}
            size_hint:(0.2,0.8) 
            MDLabel:
                pos_hint:{"center_x":0.7,"center_y":0.8}
                text:"HOURS"
            ScrollView:
                MDList:
                    id:box
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.5,"center_y":0.7}
            size_hint:(0.2,0.8) 
            MDLabel:
                pos_hint:{"center_x":0.7,"center_y":0.8}
                text:"MINUTES" 
            ScrollView:
                MDList:
                    id:boo
        BoxLayout:
            orientation:"vertical"
            pos_hint:{"center_x":0.8,"center_y":0.7}
            size_hint:(0.2,0.8) 
            MDLabel:
                pos_hint:{"center_x":0.7,"center_y":0.8}
                text:"SECONDS"
            ScrollView:
                MDList:
                    id:move
        MDRaisedButton:
            text:"CONFIRM"
            pos_hint:{"center_x":0.5,"center_y":0.2}
            on_press:
                rock.current = "main"
                app.store_data()
                app.screen3()
            
                
                    
    
    
'''

screen = Screen()
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
        for i in range(23):
            self.items = OneLineListItem(text=str(i+1),size_hint=(0.1,0.1),on_release= lambda x:self.callbacker(x))
            self.help.ids.box.add_widget(self.items)
        for i in range(59):
            items1 = OneLineListItem(text=str(i+1),size_hint=(0.1,0.1),on_release= lambda x:self.callbacker2(x))
            self.help.ids.boo.add_widget(items1)
        for i in range(59):
            self.items2 = OneLineListItem(text=str(i + 1), size_hint=(0.1, 0.1),on_release= lambda x:self.callbacker3(x))
            self.help.ids.move.add_widget(self.items2)
    def callbacker(self,x):
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
    def callbacker2(self,x):
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
            print(self.romet2.text,x.text)
            if self.romet2 == x:
                self.minutes = 0
        if self.iteretion2 >= 1 and jump == True:
            x.bg_color = (0, 0, 255, 0.4)
            self.earlyx3.bg_color = (225, 225, 225, 0.3)
            self.earlyx3 = x
            self.minutes = x.text
    def callbacker3(self,x):
        jump = True
        if self.iteretion == 0:
            self.earlyx = x
            x.bg_color = (0, 0, 255,0.4)
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
        c.execute("INSERT INTO  timer (name,hours,minutes,seconds,number) VALUES (?,?,?,?,?)" ,("crunches",self.hour,self.minutes,self.seconds,self.ider))
        self.ider += 1
        mydb.commit()
    def screen3(self):
        #c.execute("DELETE FROM timer")

        c.execute("SELECT * FROM timer ORDER BY number DESC LIMIT 1 ")
        for i in c:
            print(i,i[4])
            self.extracted_second = i[3]
            self.extracted_minute = i[2]
        self.help.ids.counter.max = self.extracted_second
        self.help.ids.counter.value = self.extracted_second

        self.event = Clock.schedule_interval(self.pop, 1)
        #print(self.extracted_second)
    def pop(self,*args):
        #self.help.ids.counter.value = self.help.ids.counter.max
        pok = int(self.help.ids.counter.value) - 1
        self.help.ids.counter.value = pok
        if self.help.ids.counter.value == 0:
            Clock.unschedule(self.event)




Test().run()