import sqlite3
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


KV = '''
<EventPlanning>

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(25)
        padding: dp(5)
        MDIconButton:
            icon: 'arrow-left'
            on_release: root.event_list_click()
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
                MDGridLayout:
                    cols: 2
                    padding: dp(10)
                    MDTextField:
                        id: date_label
                        hint_text: "Event Date"
                        helper_text: 'YYYY-MM-DD'
                        font_name: "Roboto-Bold"
                        hint_text_color: 0, 0, 0, 1

                    MDIconButton:
                        icon: 'calendar-check'
                        on_press: root.show_date_picker()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                MDGridLayout:
                    cols: 2
                    padding: dp(10)
                    MDTextField:
                        id: time_label
                        hint_text: "Event Time"
                        helper_text: 'YYYY-MM-DD'
                        font_name: "Roboto-Bold"
                        hint_text_color: 0, 0, 0, 1

                    MDIconButton:
                        icon: 'clock'
                        on_press: root.show_time_picker1()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(15)

                    MDLabel:
                        text: "  Venue Place"

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
                            helper_text: "Venue"
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
                        on_release: app.root.current = "GuestInvitation"
                        size_hint: 1, None
<GuestInvitation>
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(35)
        padding: dp(20)
        MDIconButton:
            icon: 'arrow-left'
            on_release: root.gust_list_click()
        MDLabel:
            text: "Guest List Invitation Form"
            font_size: 50
            halign: 'center'
            bold: True
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(15)

            MDLabel:
                text: "  Full Name"

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
                    helper_text: "Full Name"
                    helper_text_mode: "on_focus"
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(15)

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
            spacing: dp(15)

            MDLabel:
                text: "  Phone Number"

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
                    helper_text: "Enter valid phone number"
                    helper_text_mode: "on_focus"            



        GridLayout:
            cols: 2
            spacing: dp(10)
            padding: dp(10)            
            MDRaisedButton:
                text: "Add"
                md_bg_color: 38/255, 40/255, 41/255, 1
                font_name: "Roboto-Bold.ttf"
                size_hint: 1, None
                text_color: 1, 1, 1, 1 

            MDRaisedButton:
                text: "Save&Next"
                md_bg_color: 38/255, 40/255, 41/255, 1
                on_release: app.root.current = "FoodItems"
                font_name: "Roboto-Bold.ttf"
                size_hint: 1, None
                text_color: 1, 1, 1, 1 

<FoodItems>:

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "FOOD ITEMS"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_menu_button_press()]]

        MDTabs:
            id: tabs
            Tab :
                title : 'Veg Items'
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDScrollView:
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            MDLabel:
                                text: "Rice / Biryani Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)
                            
                            MDList:
                                id: container
                                ListItemWithCheckbox:
                                    id: check1
                                    text: "White Rice"
                                    
                                ListItemWithCheckbox:
                                    text: "Lemon Rice"
                                ListItemWithCheckbox:
                                    text: "Tomato Rice"
                                ListItemWithCheckbox:
                                    text: "Brown Rice"
                                ListItemWithCheckbox:
                                    text: "Zeera Rice(Jilakarra Rice)"
                                ListItemWithCheckbox:
                                    text: "Veg Biryani"
                            MDLabel:
                                text: "Curry Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)
                            
                            MDList:
                                id: container1
                                ListItemWithCheckbox:
                                    id: check1
                                    text: "White Rice"
                                ListItemWithCheckbox:
                                    text: "Lemon Rice"
                                ListItemWithCheckbox:
                                    text: "Tomato Rice"
                                ListItemWithCheckbox:
                                    text: "Brown Rice"
                                ListItemWithCheckbox:
                                    text: "Zeera Rice(Jilakarra Rice)"
                                ListItemWithCheckbox:
                                    text: "Veg Biryani"
                                
            Tab : 
                title : 'Non Veg Items'
            Tab : 
                title : 'Sweet and hot Items'
            Tab :
                title : 'Soft Drinks'
            Tab :
                title : 'Tiffins'
                
<ListItemWithCheckbox>:

    RightCheckbox:
'''

Builder.load_string(KV)


class Tab(MDFloatLayout, MDTabsBase):
    pass
class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class FoodItems(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.ids.check1)
    def on_menu_button_press(self):
        self.manager.current = "GuestInvitation"


class EventPlanning(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_date_picker(self):
        date_picker = MDDatePicker()
        date_picker.bind(on_save=self.on_date_selected)
        date_picker.open()

    def on_date_selected(self, instance, value, date_range):
        date_label = self.ids.date_label
        date_label.text = f"{value}"

    def show_time_picker1(self):
        time_picker = MDTimePicker()
        time_picker.bind(on_save=self.on_time_selected)
        time_picker.open()

    def on_time_selected(self, instance, time):
        time_label = self.ids.time_label
        time_label.text = f"{time.strftime('%H:%M')}"

    def event_list_click(self):
        self.manager.current = "success"


class GuestInvitation(Screen):
    def gust_list_click(self):
        self.manager.current = "EventPlanning"



