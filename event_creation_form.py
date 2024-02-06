import sqlite3

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

KV = '''
<EventPlanning>

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(25)
        padding: dp(5)

        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                spacing: dp(25)
                padding: dp(20)
                height: dp(1500)
                MDLabel:
                    text: "Event Creation Form"
                    font_size: 65
                    halign: 'center'
                    bold: True

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)
                    MDLabel:
                        text: "   Full Name"
                    MDBoxLayout:
                        orientation: 'horizontal'
                        spacing: dp(10)
                        MDFloatLayout:
                            size_hint: 1, None
                            size: "150dp", "40dp"  
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            size_hint_x: 1
                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, 1
                                RoundedRectangle:
                                    pos: self.pos
                                    size: self.size
                                    radius: [10, 10, 10, 10]

                                Color:
                                    rgba: 0, 0, 0, 1

                                Line:
                                    rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                                    width: 1 

                            MDTextField:
                                id: text_input1
                                size_hint: None, None
                                size_hint_x: 0.91
                                multiline: False
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                line_color_normal: [1, 1, 1, 1]
                                line_color_focus: [1, 1, 1, 1]
                                font_name: "Roboto-Bold"
                                helper_text: "Last Name"
                                helper_text_mode: "on_focus"

                        MDFloatLayout:
                            size_hint: 1, None
                            size: dp(150), dp(40)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            size_hint_x: 1
                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, 1
                                RoundedRectangle:
                                    pos: self.pos
                                    size: self.size
                                    radius: [10, 10, 10, 10]

                                Color:
                                    rgba: 0, 0, 0, 1

                                Line:
                                    rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                                    width: 1 

                            MDTextField:
                                id: text_input2
                                size_hint: None, None
                                size_hint_x: 0.91
                                multiline: False
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                line_color_normal: [1, 1, 1, 1]
                                line_color_focus: [1, 1, 1, 1]
                                font_name: "Roboto-Bold"
                                helper_text: "Last Name"
                                helper_text_mode: "on_focus"

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  Contact Email"

                    MDFloatLayout:
                        size_hint: 1, None
                        size: "150dp", "40dp"  
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: 1
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [10, 10, 10, 10]

                            Color:
                                rgba: 0, 0, 0, 1

                            Line:
                                rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                                width: 1 

                        MDTextField:
                            id: text_input3
                            size_hint: None, None
                            size_hint_x: 0.91
                            multiline: False
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            line_color_normal: [1, 1, 1, 1]
                            line_color_focus: [1, 1, 1, 1]
                            font_name: "Roboto-Bold"
                            helper_text: "Contact Email"
                            helper_text_mode: "on_focus"

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  Contact Phone"

                    MDFloatLayout:
                        size_hint: 1, None
                        size: "150dp", "40dp"  
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: 1
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [10, 10, 10, 10]

                            Color:
                                rgba: 0, 0, 0, 1

                            Line:
                                rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                                width: 1 

                        MDTextField:
                            id: text_input3
                            size_hint: None, None
                            size_hint_x: 0.91
                            multiline: False
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            line_color_normal: [1, 1, 1, 1]
                            line_color_focus: [1, 1, 1, 1]
                            font_name: "Roboto-Bold"
                            helper_text: "Phone Number"
                            helper_text_mode: "on_focus"

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  Type of event"

                    Spinner:
                        id: event
                        text: "Select Event"
                        values: ["", "", ""]
                        multiline: False
                        size_hint: 1, None
                        height: "40dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)           

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  How Many Guests are expecting"

                    Spinner:
                        id: event
                        text: "Select Guest List"
                        values: ["1-50", "50-150", "150-250", "250-450", "500-800", "800-1200"]
                        multiline: False
                        size_hint: 1, None
                        height: "40dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15) 

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  Type of event Hosting"

                    Spinner:
                        id: event
                        text: "Select Event Hosting"
                        values: ["Indoor", "Outdoor", "Any of the above"]
                        multiline: False
                        size_hint: 1, None
                        height: "40dp"
                        background_color: 0, 0, 0, 0
                        background_normal: ''
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15) 

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  Your event Budget"

                    MDFloatLayout:
                        size_hint: 1, None
                        size: "150dp", "40dp"  
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_x: 1
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
                                radius: [10, 10, 10, 10]

                            Color:
                                rgba: 0, 0, 0, 1

                            Line:
                                rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                                width: 1 

                        MDTextField:
                            id: text_input3
                            size_hint: None, None
                            size_hint_x: 0.91
                            multiline: False
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            line_color_normal: [1, 1, 1, 1]
                            line_color_focus: [1, 1, 1, 1]
                            font_name: "Roboto-Bold"
                            helper_text_mode: "on_focus"

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(18)

                    MDLabel:
                        text: "Please provide more details about the event, such as the desired theme food and drinks"

                    MDTextField:
                        id: text_input3
                        size_hint: 1 , None
                        mode: 'rectangle'
                        max_text_length: 100                  
                        multiline: False
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        line_color_normal: [0, 0, 0, 1]
                        line_color_focus: [0, 0, 0, 1]
                        font_name: "Roboto-Bold"
                        helper_text: "Enter your text here"
                        helper_text_mode: "on_focus"
                MDGridLayout:
                    cols: 2
                    spacing: 30
                    padding: 20
                    size_hint: 1, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                    MDRaisedButton:
                        text: "Create Event"
                        md_bg_color: 38/255, 40/255, 41/255, 1
                        on_release: app.root.current = "ForecloseDetails"
                        size_hint: 1, None

'''

Builder.load_string(KV)


class EventPlanning(Screen):
    pass


