import sqlite3

from anvil.tables import app_tables
from kivymd.uix.boxlayout import MDBoxLayout
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
                                helper_text: "First Name"
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
                            id: text_input4
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
                        id: event1
                        text: "Select Event"
                        values: ["Select Event","Birthday Event", "Party Event", "Marriage Event"]
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
                        text: "  Exact No Of Guests"

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
                            id: text_input5
                            size_hint: None, None
                            size_hint_x: 0.91
                            multiline: False
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            line_color_normal: [1, 1, 1, 1]
                            line_color_focus: [1, 1, 1, 1]
                            font_name: "Roboto-Bold"
                            helper_text: "Enter Valid no of guests"
                            helper_text_mode: "on_focus"

                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(5)

                    MDLabel:
                        text: "  Type of event Hosting"

                    Spinner:
                        id: event2
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
                            id: text_input6
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
                        id: date
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
                        id: time
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
                            id: text_input7
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
                        id: text_input8
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
                        on_release: root.create_events(text_input1.text, text_input2.text, text_input3.text, text_input4.text, event.text, event1.text, event2.text, text_input5.text, text_input6.text, date.text, time.text, text_input7.text, text_input8.text)
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
                                id: container1
                                ThreeLineAvatarIconListItem:
                                    id: list1
                                    text: "White Rice "
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 30/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check1
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check1()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus1()
                                        MDTextField:
                                            id: text1
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus1()                   

                                ThreeLineAvatarIconListItem:
                                    id: list2
                                    text: "Lemon Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 60/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check2
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check2()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus2()
                                        MDTextField:
                                            id: text2
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus2()

                                ThreeLineAvatarIconListItem:
                                    id: list3
                                    text: "Tomato Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 60/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check3
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check3()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus3()
                                        MDTextField:
                                            id: text3
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus3()

                                ThreeLineAvatarIconListItem:
                                    id: list4
                                    text: "Brown Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 60/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check4
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check4()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus4()
                                        MDTextField:
                                            id: text4
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus4()

                                ThreeLineAvatarIconListItem:
                                    id: list5
                                    text: "Zeera Rice(Jilakarra Rice)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 60/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check5
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check5()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus5()
                                        MDTextField:
                                            id: text5
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus5()

                                ThreeLineAvatarIconListItem:
                                    id: list6
                                    text: "Veg Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check6
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check6()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus6()
                                        MDTextField:
                                            id: text6
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus6()
                            MDLabel:
                                text: "Veg Curry Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)

                            MDList:
                                id: container2
                                ThreeLineAvatarIconListItem:
                                    id: list7
                                    text: "Dal"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check7
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check7()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus7()
                                        MDTextField:
                                            id: text7
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus7()
                                ThreeLineAvatarIconListItem:
                                    id: list8
                                    text: "Brinjal Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check8
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check8()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus8()
                                        MDTextField:
                                            id: text8
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus8()
                                ThreeLineAvatarIconListItem:
                                    id: list9
                                    text: "Potato Curry (Aloo Curry)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check9
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check9()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus9()
                                        MDTextField:
                                            id: text9
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus9()
                                ThreeLineAvatarIconListItem:
                                    id: list10
                                    text: "Potato Fry "
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check10
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check10()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus10()
                                        MDTextField:
                                            id: text10
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus10()
                                ThreeLineAvatarIconListItem:
                                    id: list11
                                    text: "Ladies Finger Curry(Bhendakai)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check11
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check11()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus11()
                                        MDTextField:
                                            id: text11
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus11()
                                ThreeLineAvatarIconListItem:
                                    id: list12
                                    text: "Sambar"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check12
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check12()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus12()
                                        MDTextField:
                                            id: text12
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus12()
                                ThreeLineAvatarIconListItem:
                                    id: list13
                                    text: "Rasam"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check13
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check13()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus13()
                                        MDTextField:
                                            id: text13
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus13()
                                ThreeLineAvatarIconListItem:
                                    id: list14
                                    text: "Mustroom Curry "
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check14
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check14()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus14()
                                        MDTextField:
                                            id: text14
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus14()
                                ThreeLineAvatarIconListItem:
                                    id: list15
                                    text: "Kajju Panner Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check15
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check15()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus15()
                                        MDTextField:
                                            id: text15
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus15()
                                ThreeLineAvatarIconListItem:
                                    id: list16
                                    text: "DrumStick Curry (Mulakai)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check16
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check16()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus16()
                                        MDTextField:
                                            id: text16
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus16()
                                ThreeLineAvatarIconListItem:
                                    id: list17
                                    text: "Beams Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check17
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check17()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus17()
                                        MDTextField:
                                            id: text17
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus17()
                                ThreeLineAvatarIconListItem:
                                    id: list18
                                    text: "Peas Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check18
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check18()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus18()
                                        MDTextField:
                                            id: text18
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus18()
                                ThreeLineAvatarIconListItem:
                                    id: list19
                                    text: "Tomato Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check19
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check19()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus19()
                                        MDTextField:
                                            id: text19
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus19()
                                ThreeLineAvatarIconListItem:
                                    id: list20
                                    text: "Cabbage Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check20
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check20()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus20()
                                        MDTextField:
                                            id: text20
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus20()
                                ThreeLineAvatarIconListItem:
                                    id: list21
                                    text: "Cauliflower Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check21
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check21()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus21()
                                        MDTextField:
                                            id: text21
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus21()
                                ThreeLineAvatarIconListItem:
                                    id: list22
                                    text: "Avakaya chutney"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check22
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check22()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus22()
                                        MDTextField:
                                            id: text22
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus22()

                            MDLabel:
                                text: "Veg-FastFood Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container3
                                ThreeLineAvatarIconListItem:
                                    id: list23
                                    text: "Veg Fried Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check23
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check23()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus23()
                                        MDTextField:
                                            id: text23
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus23() 
                                ThreeLineAvatarIconListItem:
                                    id: list24
                                    text: "Veg Noodles"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check24
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check24()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus24()
                                        MDTextField:
                                            id: text24
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus24()
                                ThreeLineAvatarIconListItem:
                                    id: list25
                                    text: "Veg Manchuria"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check25
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check25()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus25()
                                        MDTextField:
                                            id: text25
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus25() 
                                ThreeLineAvatarIconListItem:
                                    id: list26
                                    text: "Manchuria Rice(Gobi Rice)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check26
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check26()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus26()
                                        MDTextField:
                                            id: text26
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus26()
                                ThreeLineAvatarIconListItem:
                                    id: list27
                                    text: "Manchuria Noodles (Gobi Noodles)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check27
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check27()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus27()
                                        MDTextField:
                                            id: text27
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus27()

            Tab : 
                title : 'Non Veg Items'
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
                                id: container4
                                ThreeLineAvatarIconListItem:
                                    id: list28
                                    text: "Chicken Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check28
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check28()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus28()
                                        MDTextField:
                                            id: text28
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus28() 
                                ThreeLineAvatarIconListItem:
                                    id: list29
                                    text: "Chicken Fried-Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check29
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check29()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus29()
                                        MDTextField:
                                            id: text29
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus29()
                                ThreeLineAvatarIconListItem:
                                    id: list30
                                    text: "Chicken Dum-Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check30
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check30()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus30()
                                        MDTextField:
                                            id: text30
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus30() 
                                ThreeLineAvatarIconListItem:
                                    id: list31
                                    text: "Mutton Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check31
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check31()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus31()
                                        MDTextField:
                                            id: text31
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus31()
                                ThreeLineAvatarIconListItem:
                                    id: list32
                                    text: "Mutton Fry-Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check32
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check32()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus32()
                                        MDTextField:
                                            id: text32
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus32()
                                ThreeLineAvatarIconListItem:
                                    id: list33
                                    text: "Prawns Biryani"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check33
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check33()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus33()
                                        MDTextField:
                                            id: text33
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus33()
                                ThreeLineAvatarIconListItem:
                                    id: list34
                                    text: "Normal Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check34
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check34()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus34()
                                        MDTextField:
                                            id: text34
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus34()
                            MDLabel:
                                text: "Non-veg Curry Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)
                            MDList:
                                id: container5
                                ThreeLineAvatarIconListItem:
                                    id: list35
                                    text: "Chicken Fry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check35
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check35()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus35()
                                        MDTextField:
                                            id: text35
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus35()
                                ThreeLineAvatarIconListItem:
                                    id: list36
                                    text: "Chicken Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check36
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check36()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus36()
                                        MDTextField:
                                            id: text36
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus36()
                                ThreeLineAvatarIconListItem:
                                    id: list37
                                    text: "Chicken 65"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check37
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check37()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus37()
                                        MDTextField:
                                            id: text37
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus37()
                                ThreeLineAvatarIconListItem:
                                    id: list38
                                    text: "Gongura chicken Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check38
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check38()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus38()
                                        MDTextField:
                                            id: text38
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus38()
                                ThreeLineAvatarIconListItem:
                                    id: list39
                                    text: "Mutton Fry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check39
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check39()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus39()
                                        MDTextField:
                                            id: text39
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus39()
                                ThreeLineAvatarIconListItem:
                                    id: list40
                                    text: "Mutton Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check40
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check40()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus40()
                                        MDTextField:
                                            id: text40
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus40()
                                ThreeLineAvatarIconListItem:
                                    id: list41
                                    text: "Gongura Mutton Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check41
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check41()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus41()
                                        MDTextField:
                                            id: text41
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus41()
                                ThreeLineAvatarIconListItem:
                                    id: list42
                                    text: "Fish Fry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check42
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check42()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus42()
                                        MDTextField:
                                            id: text42
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus42()
                                ThreeLineAvatarIconListItem:
                                    id: list43
                                    text: "Fish Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check43
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check43()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus43()
                                        MDTextField:
                                            id: text43
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus43()
                                ThreeLineAvatarIconListItem:
                                    id: list44
                                    text: "Prawns Fry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check44
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check44()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus44()
                                        MDTextField:
                                            id: text44
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus44()
                                ThreeLineAvatarIconListItem:
                                    id: list45
                                    text: "Prawns Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check45
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check45()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus45()
                                        MDTextField:
                                            id: text45
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus45()
                                ThreeLineAvatarIconListItem:
                                    id: list46
                                    text: "Crabs curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check46
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check46()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus46()
                                        MDTextField:
                                            id: text46
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus46()
                                ThreeLineAvatarIconListItem:
                                    id: list47
                                    text: "Egg Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check47
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check47()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus47()
                                        MDTextField:
                                            id: text47
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus47()
                                ThreeLineAvatarIconListItem:
                                    id: list48
                                    text: "Egg omlete"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check48
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check48()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus48()
                                        MDTextField:
                                            id: text48
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus48() 
                                ThreeLineAvatarIconListItem:
                                    id: list49
                                    text: "Egg roll"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check49
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check49()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus49()
                                        MDTextField:
                                            id: text49
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus49()
                                ThreeLineAvatarIconListItem:
                                    id: list50
                                    text: "Chicken roll"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check50
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check50()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus50()
                                        MDTextField:
                                            id: text50
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus50()
                                ThreeLineAvatarIconListItem:
                                    id: list51
                                    text: "Chicken Wings"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check51
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check51()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus51()
                                        MDTextField:
                                            id: text51
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus51()
                                ThreeLineAvatarIconListItem:
                                    id: list52
                                    text: "Chicken Leg-peaces"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check52
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check52()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus52()
                                        MDTextField:
                                            id: text52
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus52()
                                ThreeLineAvatarIconListItem:
                                    id: list53
                                    text: "Botii Curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check53
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check53()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus53()
                                        MDTextField:
                                            id: text53
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus53()
                            MDLabel:
                                text: "Non-Veg FastFood Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container6
                                ThreeLineAvatarIconListItem:
                                    id: list54
                                    text: "Chicken Fried Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check54
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check54()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus54()
                                        MDTextField:
                                            id: text54
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus54()
                                ThreeLineAvatarIconListItem:
                                    id: list55
                                    text: "Chicken Noodles"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check55
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check55()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus55()
                                        MDTextField:
                                            id: text55
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus55()
                                ThreeLineAvatarIconListItem:
                                    id: list56
                                    text: "chilli chicken"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check56
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check56()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus56()
                                        MDTextField:
                                            id: text56
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus56()
                                ThreeLineAvatarIconListItem:
                                    id: list57
                                    text: "Egg Noodles"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check57
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check57()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus57()
                                        MDTextField:
                                            id: text57
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus57()
                                ThreeLineAvatarIconListItem:
                                    id: list58
                                    text: "Egg Manchuria"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check58
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check58()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus58()
                                        MDTextField:
                                            id: text58
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus58()
                                ThreeLineAvatarIconListItem:
                                    id: list59
                                    text: "Manchuria Egg Rice"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check59
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check59()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus59()
                                        MDTextField:
                                            id: text59
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus59()
                                ThreeLineAvatarIconListItem:
                                    id: list60
                                    text: "Manchuria Egg Noodles"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check60
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check60()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus60()
                                        MDTextField:
                                            id: text60
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus60()  
                            MDLabel:
                                text: "Roti Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container7
                                ThreeLineAvatarIconListItem:
                                    id: list61
                                    text: "Butter non"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check61
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check61()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus61()
                                        MDTextField:
                                            id: text61
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus61()
                                ThreeLineAvatarIconListItem:
                                    id: list62
                                    text: "Tawa roti"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check62
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check62()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus62()
                                        MDTextField:
                                            id: text62
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus62() 
                                ThreeLineAvatarIconListItem:
                                    id: list63
                                    text: "Rumalli roti"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check63
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check63()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus63()
                                        MDTextField:
                                            id: text63
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus63()
                                ThreeLineAvatarIconListItem:
                                    id: list64
                                    text: "Makki roti"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check64
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check64()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus64()
                                        MDTextField:
                                            id: text64
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus64()
                                ThreeLineAvatarIconListItem:
                                    id: list65
                                    text: "Parota"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check65
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check65()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus65()
                                        MDTextField:
                                            id: text65
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus65()
                                ThreeLineAvatarIconListItem:
                                    id: list66
                                    text: "Sada Roti"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check66
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check66()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus66()
                                        MDTextField:
                                            id: text66
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus66()

                            MDLabel:
                                text: "curry For Roti Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)
                            ThreeLineAvatarIconListItem:
                                id: list67
                                text: "Egg Keema"
                                secondary_text: "Total Item Price : 0"
                                tertiary_text: "For Each Person 100/-"
                                on_size:
                                    self.ids._right_container.width = container.width + 200
                                    self.ids._right_container.x = container.width + 200

                                IconLeftWidget:
                                    id: check67
                                    icon: "checkbox-blank-outline"
                                    on_release: root.check67()

                                YourContainer:
                                    id: container

                                    MDIconButton:
                                        icon: "minus"
                                        on_release: root.minus67()
                                    MDTextField:
                                        id: text67
                                        size_hint: None, None
                                        size: "27dp", "27dp"
                                    MDIconButton:
                                        icon: "plus"   
                                        on_release: root.plus67()
                            ThreeLineAvatarIconListItem:
                                id: list68
                                text: "Egg Bhurji"
                                secondary_text: "Total Item Price : 0"
                                tertiary_text: "For Each Person 100/-"
                                on_size:
                                    self.ids._right_container.width = container.width + 200
                                    self.ids._right_container.x = container.width + 200

                                IconLeftWidget:
                                    id: check68
                                    icon: "checkbox-blank-outline"
                                    on_release: root.check68()

                                YourContainer:
                                    id: container

                                    MDIconButton:
                                        icon: "minus"
                                        on_release: root.minus68()
                                    MDTextField:
                                        id: text68
                                        size_hint: None, None
                                        size: "27dp", "27dp"
                                    MDIconButton:
                                        icon: "plus"   
                                        on_release: root.plus68()
                            ThreeLineAvatarIconListItem:
                                id: list69
                                text: "Butter chicken"
                                secondary_text: "Total Item Price : 0"
                                tertiary_text: "For Each Person 100/-"
                                on_size:
                                    self.ids._right_container.width = container.width + 200
                                    self.ids._right_container.x = container.width + 200

                                IconLeftWidget:
                                    id: check69
                                    icon: "checkbox-blank-outline"
                                    on_release: root.check69()

                                YourContainer:
                                    id: container

                                    MDIconButton:
                                        icon: "minus"
                                        on_release: root.minus69()
                                    MDTextField:
                                        id: text69
                                        size_hint: None, None
                                        size: "27dp", "27dp"
                                    MDIconButton:
                                        icon: "plus"   
                                        on_release: root.plus69()
                            ThreeLineAvatarIconListItem:
                                id: list70
                                text: "Afgani chicken"
                                secondary_text: "Total Item Price : 0"
                                tertiary_text: "For Each Person 100/-"
                                on_size:
                                    self.ids._right_container.width = container.width + 200
                                    self.ids._right_container.x = container.width + 200

                                IconLeftWidget:
                                    id: check70
                                    icon: "checkbox-blank-outline"
                                    on_release: root.check70()

                                YourContainer:
                                    id: container

                                    MDIconButton:
                                        icon: "minus"
                                        on_release: root.minus70()
                                    MDTextField:
                                        id: text70
                                        size_hint: None, None
                                        size: "27dp", "27dp"
                                    MDIconButton:
                                        icon: "plus"   
                                        on_release: root.plus70()
                            ThreeLineAvatarIconListItem:
                                id: list71
                                text: "Kajju curry"
                                secondary_text: "Total Item Price : 0"
                                tertiary_text: "For Each Person 100/-"
                                on_size:
                                    self.ids._right_container.width = container.width + 200
                                    self.ids._right_container.x = container.width + 200

                                IconLeftWidget:
                                    id: check71
                                    icon: "checkbox-blank-outline"
                                    on_release: root.check71()

                                YourContainer:
                                    id: container

                                    MDIconButton:
                                        icon: "minus"
                                        on_release: root.minus71()
                                    MDTextField:
                                        id: text71
                                        size_hint: None, None
                                        size: "27dp", "27dp"
                                    MDIconButton:
                                        icon: "plus"   
                                        on_release: root.plus71()
                            ThreeLineAvatarIconListItem:
                                id: list72
                                text: "Paneer Butter masala"
                                secondary_text: "Total Item Price : 0"
                                tertiary_text: "For Each Person 100/-"
                                on_size:
                                    self.ids._right_container.width = container.width + 200
                                    self.ids._right_container.x = container.width + 200

                                IconLeftWidget:
                                    id: check72
                                    icon: "checkbox-blank-outline"
                                    on_release: root.check72()

                                YourContainer:
                                    id: container

                                    MDIconButton:
                                        icon: "minus"
                                        on_release: root.minus72()
                                    MDTextField:
                                        id: text72
                                        size_hint: None, None
                                        size: "27dp", "27dp"
                                    MDIconButton:
                                        icon: "plus"   
                                        on_release: root.plus72()               

            Tab : 
                title : 'Sweet and hot Items'
                BoxLayout:
                    orientation: 'vertical'

                    MDScrollView:
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            MDLabel:
                                text: "Sweet Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container8
                                ThreeLineAvatarIconListItem:
                                    id: list73
                                    text: "Gulab Jamun"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check73
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check73()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus73()
                                        MDTextField:
                                            id: text73
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus73()
                                ThreeLineAvatarIconListItem:
                                    id: list74
                                    text: "Gajar ka Halwa (Carrot Halwa)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check74
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check74()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus74()
                                        MDTextField:
                                            id: text74
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus74() 
                                ThreeLineAvatarIconListItem:
                                    id: list75
                                    text: "Ras Malai (Cottage Cheese Balls in Clotted Cream)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check75
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check75()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus75()
                                        MDTextField:
                                            id: text75
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus75()
                                ThreeLineAvatarIconListItem:
                                    id: list76
                                    text: "Besan Ladoo (Roasted Gram Flour Balls)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check76
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check76()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus76()
                                        MDTextField:
                                            id: text76
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus76()
                                ThreeLineAvatarIconListItem:
                                    id: list77
                                    text: "Kalakand"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check77
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check77()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus77()
                                        MDTextField:
                                            id: text77
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus77()
                                ThreeLineAvatarIconListItem:
                                    id: list78
                                    text: "Peanut Chikki (Peanut Brittle)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check78
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check78()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus78()
                                        MDTextField:
                                            id: text78
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus78()
                                ThreeLineAvatarIconListItem:
                                    id: list79
                                    text: "Jalebi"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check79
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check79()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus79()
                                        MDTextField:
                                            id: text79
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus79()
                                ThreeLineAvatarIconListItem:
                                    id: list80
                                    text: "Soan Papdi"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check80
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check80()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus80()
                                        MDTextField:
                                            id: text80
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus80()
                                ThreeLineAvatarIconListItem:
                                    id: list81
                                    text: "Rice Kheer(Payasam)"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check81
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check81()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus81()
                                        MDTextField:
                                            id: text81
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus81()

                            MDLabel:
                                text: "Hot Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container9
                                ThreeLineAvatarIconListItem:
                                    id: list82
                                    text: "Masala Peanuts"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check82
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check82()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus82()
                                        MDTextField:
                                            id: text82
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus82()
                                ThreeLineAvatarIconListItem:
                                    id: list83
                                    text: "Samosa"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check83
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check83()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus83()
                                        MDTextField:
                                            id: text83
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus83() 
                                ThreeLineAvatarIconListItem:
                                    id: list84
                                    text: "Onion Pakodi"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check84
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check84()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus84()
                                        MDTextField:
                                            id: text84
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus84()
                                ThreeLineAvatarIconListItem:
                                    id: list85
                                    text: "Baggi"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check85
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check85()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus85()
                                        MDTextField:
                                            id: text85
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus85()
                                ThreeLineAvatarIconListItem:
                                    id: list86
                                    text: "Mixter"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check86
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check86()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus86()
                                        MDTextField:
                                            id: text86
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus86()
                                ThreeLineAvatarIconListItem:
                                    id: list87
                                    text: "Vada Pav"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check87
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check87()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus87()
                                        MDTextField:
                                            id: text87
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus87()
                                ThreeLineAvatarIconListItem:
                                    id: list88
                                    text: "Panipuri"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check88
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check88()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus88()
                                        MDTextField:
                                            id: text88
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus88()

            Tab :
                title : 'Soft Drinks'
                BoxLayout:
                    orientation: 'vertical'

                    MDScrollView:
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            MDLabel:
                                text: "Drink Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15) 
                            MDList:
                                id: container10
                                ThreeLineAvatarIconListItem:
                                    id: list89
                                    text: "Sprite"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check89
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check89()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus89()
                                        MDTextField:
                                            id: text89
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus89()
                                ThreeLineAvatarIconListItem:
                                    id: list90
                                    text: "Thumps up"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check90
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check90()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus90()
                                        MDTextField:
                                            id: text90
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus90() 
                                ThreeLineAvatarIconListItem:
                                    id: list91
                                    text: "Fanta"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check91
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check91()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus91()
                                        MDTextField:
                                            id: text91
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus91()
                                ThreeLineAvatarIconListItem:
                                    id: list92
                                    text: "Limka"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check92
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check92()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus92()
                                        MDTextField:
                                            id: text92
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus92()
                                ThreeLineAvatarIconListItem:
                                    id: list93
                                    text: "coco-cola"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check93
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check93()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus93()
                                        MDTextField:
                                            id: text93
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus93()
                                ThreeLineAvatarIconListItem:
                                    id: list94
                                    text: "Mirinda"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check94
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check94()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus94()
                                        MDTextField:
                                            id: text94
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus94()
                                ThreeLineAvatarIconListItem:
                                    id: list95
                                    text: "Mazza"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check95
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check95()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus95()
                                        MDTextField:
                                            id: text95
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus95()
                                ThreeLineAvatarIconListItem:
                                    id: list96
                                    text: "Apple Fizz"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check96
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check96()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus96()
                                        MDTextField:
                                            id: text96
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus96()
                                ThreeLineAvatarIconListItem:
                                    id: list97
                                    text: "Pulpi-Orange"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check97
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check97()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus97()
                                        MDTextField:
                                            id: text97
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus97()
                                ThreeLineAvatarIconListItem:
                                    id: list98
                                    text: "Mountaine Dew"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check98
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check98()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus98()
                                        MDTextField:
                                            id: text98
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus98()
                                ThreeLineAvatarIconListItem:
                                    id: list99
                                    text: "Red bull"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check99
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check99()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus99()
                                        MDTextField:
                                            id: text99
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus99()
                                ThreeLineAvatarIconListItem:
                                    id: list100
                                    text: "Artos"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check100
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check100()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus100()
                                        MDTextField:
                                            id: text100
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus100()                  

            Tab :
                title : 'Tiffins'
                BoxLayout:
                    orientation: 'vertical'

                    MDScrollView:
                        BoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: self.minimum_height
                            MDLabel:
                                text: "Tiffin Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container11
                                ThreeLineAvatarIconListItem:
                                    id: list102
                                    text: "Dosa"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check102
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check102()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus102()
                                        MDTextField:
                                            id: text102
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus102()
                                ThreeLineAvatarIconListItem:
                                    id: list103
                                    text: "Masala Dosa"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check103
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check103()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus103()
                                        MDTextField:
                                            id: text103
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus103()
                                ThreeLineAvatarIconListItem:
                                    id: list104
                                    text: "onion Dosa"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check104
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check104()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus104()
                                        MDTextField:
                                            id: text104
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus104()
                                ThreeLineAvatarIconListItem:
                                    id: list105
                                    text: "Egg Dosa"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check105
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check105()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus105()
                                        MDTextField:
                                            id: text105
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus105()
                                ThreeLineAvatarIconListItem:
                                    id: list106
                                    text: "Idly"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check106
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check106()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus106()
                                        MDTextField:
                                            id: text106
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus106()
                                ThreeLineAvatarIconListItem:
                                    id: list107
                                    text: "Ghee Idly"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check107
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check107()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus107()
                                        MDTextField:
                                            id: text107
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus107()
                                ThreeLineAvatarIconListItem:
                                    id: list108
                                    text: "Sambar Idly"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check108
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check108()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus108()
                                        MDTextField:
                                            id: text108
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus108()
                                ThreeLineAvatarIconListItem:
                                    id: list109
                                    text: "vada"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check109
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check109()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus109()
                                        MDTextField:
                                            id: text109
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus109()
                                ThreeLineAvatarIconListItem:
                                    id: list110
                                    text: "Mysore Bonda"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check110
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check110()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus110()
                                        MDTextField:
                                            id: text110
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus110()
                                ThreeLineAvatarIconListItem:
                                    id: list111
                                    text: "Upma"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check111
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check111()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus111()
                                        MDTextField:
                                            id: text111
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus111()
                                ThreeLineAvatarIconListItem:
                                    id: list112
                                    text: "chapati"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check112
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check112()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus112()
                                        MDTextField:
                                            id: text112
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus112() 
                                ThreeLineAvatarIconListItem:
                                    id: list113
                                    text: "puri"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check113
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check113()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus113()
                                        MDTextField:
                                            id: text113
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus113()
                                ThreeLineAvatarIconListItem:
                                    id: list114
                                    text: "Porota"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check114
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check114()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus114()
                                        MDTextField:
                                            id: text114
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus114()

                            MDLabel:
                                text: "Chatny Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                ThreeLineAvatarIconListItem:
                                    id: list115
                                    text: "Palli chutney"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check115
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check115()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus115()
                                        MDTextField:
                                            id: text115
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus115()
                                ThreeLineAvatarIconListItem:
                                    id: list116
                                    text: "red chutney"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check116
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check116()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus116()
                                        MDTextField:
                                            id: text116
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus116()
                                ThreeLineAvatarIconListItem:
                                    id: list117
                                    text: "Green Chutney"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check117
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check117()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus117()
                                        MDTextField:
                                            id: text117
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus117()
                                ThreeLineAvatarIconListItem:
                                    id: list118
                                    text: "Allu kurma curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check118
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check118()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus118()
                                        MDTextField:
                                            id: text118
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus118()
                                ThreeLineAvatarIconListItem:
                                    id: list119
                                    text: "Puri curry"
                                    secondary_text: "Total Item Price : 0"
                                    tertiary_text: "For Each Person 100/-"
                                    on_size:
                                        self.ids._right_container.width = container.width + 200
                                        self.ids._right_container.x = container.width + 200

                                    IconLeftWidget:
                                        id: check119
                                        icon: "checkbox-blank-outline"
                                        on_release: root.check119()

                                    YourContainer:
                                        id: container

                                        MDIconButton:
                                            icon: "minus"
                                            on_release: root.minus119()
                                        MDTextField:
                                            id: text119
                                            size_hint: None, None
                                            size: "27dp", "27dp"
                                        MDIconButton:
                                            icon: "plus"   
                                            on_release: root.plus119()


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


class YourContainer(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class FoodItems(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.text1.text = '0'
        self.white_rice = 30
        self.ids.text2.text = '0'
        self.lemon_rice = 60
        self.ids.text3.text = '0'
        self.tomato_rice = 60
        self.ids.text4.text = '0'
        self.brown_rice = 60
        self.ids.text5.text = '0'
        self.zeera_rice = 60
        self.ids.text6.text = '0'
        self.veg_biryani = 100
        self.ids.text7.text = '0'
        self.dal = 10
        self.ids.text8.text = '0'
        self.brinjal_curry = 10
        self.ids.text9.text = '0'
        self.potato_Curry = 10
        self.ids.text10.text = '0'
        self.potato_fry = 10
        self.ids.text11.text = '0'
        self.ladies_finger_curry = 10
        self.ids.text12.text = '0'
        self.sambar = 10
        self.ids.text13.text = '0'
        self.rasam = 10
        self.ids.text14.text = '0'
        self.mustroom = 20
        self.ids.text15.text = '0'
        self.kajju_panner = 30
        self.ids.text16.text = '0'
        self.drumstick = 20
        self.ids.text17.text = '0'
        self.beams = 10
        self.ids.text18.text = '0'
        self.peas = 20
        self.ids.text19.text = '0'
        self.tomato = 10
        self.ids.text20.text = '0'
        self.cabbage = 10
        self.ids.text21.text = '0'
        self.cauliflower = 10
        self.ids.text22.text = '0'
        self.avakaya_chutney = 20
        self.ids.text23.text = '0'
        self.veg_fried_rice = 30
        self.ids.text24.text = '0'
        self.veg_noodles = 30
        self.ids.text25.text = '0'
        self.veg_manchuria = 40
        self.ids.text26.text = '0'
        self.manchuria_rice = 40
        self.ids.text27.text = '0'
        self.manchuria_noodles = 40
        self.ids.text28.text = '0'
        self.chicken_biryani = 60
        self.ids.text29.text = '0'
        self.chicken_fried_biryani = 60
        self.ids.text30.text = '0'
        self.chicken_dum_biryani = 60
        self.ids.text31.text = '0'
        self.mutton_biryani = 110
        self.ids.text32.text = '0'
        self.mutton_fried_biryani = 110
        self.ids.text33.text = '0'
        self.prawns_biryani = 150
        self.ids.text34.text = '0'
        self.normal_rice = 30
        self.ids.text35.text = '0'
        self.chicken_fry = 50
        self.ids.text36.text = '0'
        self.chicken_curry = 50
        self.ids.text37.text = '0'
        self.chicken_65 = 50
        self.ids.text38.text = '0'
        self.gongura_chicken_curry = 80
        self.ids.text39.text = '0'
        self.mutton_fry = 120
        self.ids.text40.text = '0'
        self.mutton_curry = 120
        self.ids.text41.text = '0'
        self.gongura_mutton_curry = 150
        self.ids.text42.text = '0'
        self.fish_fry = 40
        self.ids.text43.text = '0'
        self.fish_curry = 30
        self.ids.text44.text = '0'
        self.prawns_fry = 50
        self.ids.text45.text = '0'
        self.prawns_curry = 50
        self.ids.text46.text = '0'
        self.crabs_curry = 80
        self.ids.text47.text = '0'
        self.egg_curry = 10
        self.ids.text48.text = '0'
        self.egg_omlet = 7
        self.ids.text49.text = '0'
        self.egg_roll = 12
        self.ids.text50.text = '0'
        self.chicken_roll = 20
        self.ids.text51.text = '0'
        self.chicken_wings = 20
        self.ids.text52.text = '0'
        self.chicken_leg_peaces = 30
        self.ids.text53.text = '0'
        self.botti_curry = 15
        self.ids.text54.text = '0'
        self.chicken_fried_rice = 30
        self.ids.text55.text = '0'
        self.chicken_noodles = 30
        self.ids.text56.text = '0'
        self.chilli_chicken = 35
        self.ids.text57.text = '0'
        self.egg_noodles = 20
        self.ids.text58.text = '0'
        self.egg_manchuria = 20
        self.ids.text59.text = '0'
        self.manchuria_egg_rice = '20'
        self.ids.text60.text = '0'
        self.manchuria_egg_noodles = 20
        self.ids.text61.text = '0'
        self.butter_non = 10
        self.ids.text62.text = '0'
        self.tawa_roti = 8
        self.ids.text63.text = '0'
        self.rumalli_roti = 10
        self.ids.text64.text = '0'
        self.makki_roti = 10
        self.ids.text65.text = '0'
        self.parota = 25
        self.ids.text66.text = '0'
        self.sada_roti = 5
        self.ids.text67.text = '0'
        self.egg_keema = 20
        self.ids.text68.text = '0'
        self.egg_burji = 20
        self.ids.text69.text = '0'
        self.butter_chicken = 20
        self.ids.text70.text = '0'
        self.afgani = 30
        self.ids.text71.text = '0'
        self.kajju_curry = 30
        self.ids.text72.text = '0'
        self.paneer_butter_masala = 30
        self.ids.text73.text = '0'
        self.gulab_jamun = 10
        self.ids.text74.text = '0'
        self.gajar_ka_halva = 10
        self.ids.text75.text = '0'
        self.ras_malai = 10
        self.ids.text76.text = '0'
        self.besan_ladoo = 10
        self.ids.text77.text = '0'
        self.kalakand = 10
        self.ids.text78.text = '0'
        self.peanut_chikki = 20
        self.ids.text79.text = '0'
        self.jalabi = 5
        self.ids.text80.text = '0'
        self.soan_papdi = 6
        self.ids.text81.text = '0'
        self.rice_kheer = 10
        self.ids.text82.text = '0'
        self.masala_peanuts = 10
        self.ids.text83.text = '0'
        self.samosa = 5
        self.ids.text84.text = '0'
        self.onion_pakodi = 5
        self.ids.text85.text = '0'
        self.bajji = 5
        self.ids.text86.text = '0'
        self.mixter = 10
        self.ids.text87.text = '0'
        self.vada_pav = 10
        self.ids.text88.text = '0'
        self.panipuri = 10
        self.ids.text89.text = '0'
        self.sprite = 20
        self.ids.text90.text = '0'
        self.thums_up = 20
        self.ids.text91.text = '0'
        self.fanta = 20
        self.ids.text92.text = '0'
        self.limka = 20
        self.ids.text93.text = '0'
        self.coco_cola = 20
        self.ids.text94.text = '0'
        self.mirinda = 20
        self.ids.text95.text = '0'
        self.mazza = 20
        self.ids.text96.text = '0'
        self.apple_fizz = 10
        self.ids.text97.text = '0'
        self.pulpi_orange = 25
        self.ids.text98.text = '0'
        self.mountain_due = 20
        self.ids.text99.text = '0'
        self.red_bull = 120
        self.ids.text100.text = '0'
        self.artos = 20
        self.ids.text102.text = '0'
        self.dosa = 10
        self.ids.text103.text = '0'
        self.masala_dosa = 15
        self.ids.text104.text = '0'
        self.onion_dosa = 15
        self.ids.text105.text = '0'
        self.egg_dosa = 12
        self.ids.text106.text = '0'
        self.idly = 10
        self.ids.text107.text = '0'
        self.ghee_idly = 15
        self.ids.text108.text = '0'
        self.sambar_idly = 15
        self.ids.text109.text = '0'
        self.vada = 5
        self.ids.text110.text = '0'
        self.mysore_bonda = 5
        self.ids.text111.text = '0'
        self.upma = 5
        self.ids.text112.text = '0'
        self.chapati = 5
        self.ids.text113.text = '0'
        self.puri = 8
        self.ids.text114.text = '0'
        self.parota = 10
        self.ids.text115.text = '0'
        self.palli_chutney = 0
        self.ids.text116.text = '0'
        self.red_chutney = 0
        self.ids.text117.text = '0'
        self.green_chutney = 0
        self.ids.text118.text = '0'
        self.allu_kurma = 5
        self.ids.text119.text = '0'
        self.puri_curry = 5

    def minus1(self):
        if self.ids.text1.text == '0':
            self.ids.text1.text = '0'
        else:
            self.ids.text1.text = str(int(self.ids.text1.text) - 1)
            self.ids.list1.secondary_text = 'Total Item Price : ' + str(self.white_rice * int(self.ids.text1.text))

    def plus1(self):
        self.ids.text1.text = str(int(self.ids.text1.text) + 1)
        self.ids.list1.secondary_text = 'Total Item Price : ' + str(self.white_rice * int(self.ids.text1.text))

    def check1(self):
        if self.ids.check1.icon == "checkbox-blank-outline":
            self.ids.check1.icon = 'checkbox-marked'
        else:
            self.ids.check1.icon = "checkbox-blank-outline"

    def minus2(self):
        if self.ids.text2.text == '0':
            self.ids.text2.text = '0'
        else:
            self.ids.text2.text = str(int(self.ids.text2.text) - 1)
            self.ids.list2.secondary_text = 'Total Item Price : ' + str(self.lemon_rice * int(self.ids.text2.text))

    def plus2(self):
        self.ids.text2.text = str(int(self.ids.text2.text) + 1)
        self.ids.list2.secondary_text = 'Total Item Price : ' + str(self.lemon_rice * int(self.ids.text2.text))

    def check2(self):
        if self.ids.check2.icon == "checkbox-blank-outline":
            self.ids.check2.icon = 'checkbox-marked'
        else:
            self.ids.check2.icon = "checkbox-blank-outline"

    def minus3(self):
        if self.ids.text3.text == '0':
            self.ids.text3.text = '0'
        else:
            self.ids.text3.text = str(int(self.ids.text3.text) - 1)
            self.ids.list3.secondary_text = 'Total Item Price : ' + str(self.tomato_rice * int(self.ids.text3.text))

    def plus3(self):
        self.ids.text3.text = str(int(self.ids.text3.text) + 1)
        self.ids.list3.secondary_text = 'Total Item Price : ' + str(self.tomato_rice * int(self.ids.text3.text))

    def check3(self):
        if self.ids.check3.icon == "checkbox-blank-outline":
            self.ids.check3.icon = 'checkbox-marked'
        else:
            self.ids.check3.icon = "checkbox-blank-outline"

    def minus4(self):
        if self.ids.text4.text == '0':
            self.ids.text4.text = '0'
        else:
            self.ids.text4.text = str(int(self.ids.text4.text) - 1)
            self.ids.list4.secondary_text = 'Total Item Price : ' + str(self.brown_rice * int(self.ids.text4.text))

    def plus4(self):
        self.ids.text4.text = str(int(self.ids.text4.text) + 1)
        self.ids.list4.secondary_text = 'Total Item Price : ' + str(self.brown_rice * int(self.ids.text4.text))

    def check4(self):
        if self.ids.check4.icon == "checkbox-blank-outline":
            self.ids.check4.icon = 'checkbox-marked'
        else:
            self.ids.check4.icon = "checkbox-blank-outline"

    def minus5(self):
        if self.ids.text5.text == '0':
            self.ids.text5.text = '0'
        else:
            self.ids.text5.text = str(int(self.ids.text5.text) - 1)
            self.ids.list5.secondary_text = 'Total Item Price : ' + str(self.zeera_rice * int(self.ids.text5.text))

    def plus5(self):
        self.ids.text5.text = str(int(self.ids.text5.text) + 1)
        self.ids.list5.secondary_text = 'Total Item Price : ' + str(self.zeera_rice * int(self.ids.text5.text))

    def check5(self):
        if self.ids.check5.icon == "checkbox-blank-outline":
            self.ids.check5.icon = 'checkbox-marked'
        else:
            self.ids.check5.icon = "checkbox-blank-outline"

    def minus6(self):
        if self.ids.text6.text == '0':
            self.ids.text6.text = '0'
        else:
            self.ids.text6.text = str(int(self.ids.text6.text) - 1)
            self.ids.list6.secondary_text = 'Total Item Price : ' + str(self.veg_biryani * int(self.ids.text6.text))

    def plus6(self):
        self.ids.text6.text = str(int(self.ids.text6.text) + 1)
        self.ids.list6.secondary_text = 'Total Item Price : ' + str(self.veg_biryani * int(self.ids.text6.text))

    def check6(self):
        if self.ids.check6.icon == "checkbox-blank-outline":
            self.ids.check6.icon = 'checkbox-marked'
        else:
            self.ids.check6.icon = "checkbox-blank-outline"

    def minus7(self):
        if self.ids.text7.text == '0':
            self.ids.text7.text = '0'
        else:
            self.ids.text7.text = str(int(self.ids.text7.text) - 1)
            self.ids.list7.secondary_text = 'Total Item Price : ' + str(self.dal * int(self.ids.text7.text))

    def plus7(self):
        self.ids.text7.text = str(int(self.ids.text7.text) + 1)
        self.ids.list7.secondary_text = 'Total Item Price : ' + str(self.dal * int(self.ids.text7.text))

    def check7(self):
        if self.ids.check7.icon == "checkbox-blank-outline":
            self.ids.check7.icon = 'checkbox-marked'
        else:
            self.ids.check7.icon = "checkbox-blank-outline"

    def minus8(self):
        if self.ids.text8.text == '0':
            self.ids.text8.text = '0'
        else:
            self.ids.text8.text = str(int(self.ids.text8.text) - 1)
            self.ids.list8.secondary_text = 'Total Item Price : ' + str(self.brinjal_curry * int(self.ids.text8.text))

    def plus8(self):
        self.ids.text8.text = str(int(self.ids.text8.text) + 1)
        self.ids.list8.secondary_text = 'Total Item Price : ' + str(self.brinjal_curry * int(self.ids.text8.text))

    def check8(self):
        if self.ids.check8.icon == "checkbox-blank-outline":
            self.ids.check8.icon = 'checkbox-marked'
        else:
            self.ids.check8.icon = "checkbox-blank-outline"

    def minus9(self):
        if self.ids.text9.text == '0':
            self.ids.text9.text = '0'
        else:
            self.ids.text9.text = str(int(self.ids.text9.text) - 1)
            self.ids.list9.secondary_text = 'Total Item Price : ' + str(self.potato_Curry * int(self.ids.text9.text))

    def plus9(self):
        self.ids.text9.text = str(int(self.ids.text9.text) + 1)
        self.ids.list9.secondary_text = 'Total Item Price : ' + str(self.potato_Curry * int(self.ids.text9.text))

    def check9(self):
        if self.ids.check9.icon == "checkbox-blank-outline":
            self.ids.check9.icon = 'checkbox-marked'
        else:
            self.ids.check9.icon = "checkbox-blank-outline"

    def minus10(self):
        if self.ids.text10.text == '0':
            self.ids.text10.text = '0'
        else:
            self.ids.text10.text = str(int(self.ids.text10.text) - 1)
            self.ids.list10.secondary_text = 'Total Item Price : ' + str(self.potato_fry * int(self.ids.text10.text))

    def plus10(self):
        self.ids.text10.text = str(int(self.ids.text10.text) + 1)
        self.ids.list10.secondary_text = 'Total Item Price : ' + str(self.potato_fry * int(self.ids.text10.text))

    def check10(self):
        if self.ids.check10.icon == "checkbox-blank-outline":
            self.ids.check10.icon = 'checkbox-marked'
        else:
            self.ids.check10.icon = "checkbox-blank-outline"

    def minus11(self):
        if self.ids.text11.text == '0':
            self.ids.text11.text = '0'
        else:
            self.ids.text11.text = str(int(self.ids.text11.text) - 1)
            self.ids.list11.secondary_text = 'Total Item Price : ' + str(
                self.ladies_finger_curry * int(self.ids.text11.text))

    def plus11(self):
        self.ids.text11.text = str(int(self.ids.text11.text) + 1)
        self.ids.list11.secondary_text = 'Total Item Price : ' + str(
            self.ladies_finger_curry * int(self.ids.text11.text))

    def check11(self):
        if self.ids.check11.icon == "checkbox-blank-outline":
            self.ids.check11.icon = 'checkbox-marked'
        else:
            self.ids.check11.icon = "checkbox-blank-outline"

    def minus12(self):
        if self.ids.text12.text == '0':
            self.ids.text12.text = '0'
        else:
            self.ids.text12.text = str(int(self.ids.text12.text) - 1)
            self.ids.list12.secondary_text = 'Total Item Price : ' + str(self.sambar * int(self.ids.text12.text))

    def plus12(self):
        self.ids.text12.text = str(int(self.ids.text12.text) + 1)
        self.ids.list12.secondary_text = 'Total Item Price : ' + str(self.sambar * int(self.ids.text12.text))

    def check12(self):
        if self.ids.check12.icon == "checkbox-blank-outline":
            self.ids.check12.icon = 'checkbox-marked'
        else:
            self.ids.check12.icon = "checkbox-blank-outline"

    def minus13(self):
        if self.ids.text13.text == '0':
            self.ids.text13.text = '0'
        else:
            self.ids.text13.text = str(int(self.ids.text13.text) - 1)
            self.ids.list13.secondary_text = 'Total Item Price : ' + str(self.rasam * int(self.ids.text13.text))

    def plus13(self):
        self.ids.text13.text = str(int(self.ids.text13.text) + 1)
        self.ids.list13.secondary_text = 'Total Item Price : ' + str(self.rasam * int(self.ids.text13.text))

    def check13(self):
        if self.ids.check13.icon == "checkbox-blank-outline":
            self.ids.check13.icon = 'checkbox-marked'
        else:
            self.ids.check13.icon = "checkbox-blank-outline"

    def minus14(self):
        if self.ids.text14.text == '0':
            self.ids.text14.text = '0'
        else:
            self.ids.text14.text = str(int(self.ids.text14.text) - 1)
            self.ids.list14.secondary_text = 'Total Item Price : ' + str(self.mustroom * int(self.ids.text14.text))

    def plus14(self):
        self.ids.text14.text = str(int(self.ids.text14.text) + 1)
        self.ids.list14.secondary_text = 'Total Item Price : ' + str(self.mustroom * int(self.ids.text14.text))

    def check14(self):
        if self.ids.check14.icon == "checkbox-blank-outline":
            self.ids.check14.icon = 'checkbox-marked'
        else:
            self.ids.check14.icon = "checkbox-blank-outline"

    def minus15(self):
        if self.ids.text15.text == '0':
            self.ids.text15.text = '0'
        else:
            self.ids.text15.text = str(int(self.ids.text15.text) - 1)
            self.ids.list15.secondary_text = 'Total Item Price : ' + str(self.kajju_panner * int(self.ids.text15.text))

    def plus15(self):
        self.ids.text15.text = str(int(self.ids.text15.text) + 1)
        self.ids.list15.secondary_text = 'Total Item Price : ' + str(self.kajju_panner * int(self.ids.text15.text))

    def check15(self):
        if self.ids.check15.icon == "checkbox-blank-outline":
            self.ids.check15.icon = 'checkbox-marked'
        else:
            self.ids.check15.icon = "checkbox-blank-outline"

    def minus16(self):
        if self.ids.text16.text == '0':
            self.ids.text16.text = '0'
        else:
            self.ids.text16.text = str(int(self.ids.text16.text) - 1)
            self.ids.list16.secondary_text = 'Total Item Price : ' + str(self.drumstick * int(self.ids.text16.text))

    def plus16(self):
        self.ids.text16.text = str(int(self.ids.text16.text) + 1)
        self.ids.list16.secondary_text = 'Total Item Price : ' + str(self.drumstick * int(self.ids.text16.text))

    def check16(self):
        if self.ids.check16.icon == "checkbox-blank-outline":
            self.ids.check16.icon = 'checkbox-marked'
        else:
            self.ids.check16.icon = "checkbox-blank-outline"

    def minus17(self):
        if self.ids.text17.text == '0':
            self.ids.text17.text = '0'
        else:
            self.ids.text17.text = str(int(self.ids.text17.text) - 1)
            self.ids.list17.secondary_text = 'Total Item Price : ' + str(self.beams * int(self.ids.text17.text))

    def plus17(self):
        self.ids.text17.text = str(int(self.ids.text17.text) + 1)
        self.ids.list17.secondary_text = 'Total Item Price : ' + str(self.beams * int(self.ids.text17.text))

    def check17(self):
        if self.ids.check17.icon == "checkbox-blank-outline":
            self.ids.check17.icon = 'checkbox-marked'
        else:
            self.ids.check17.icon = "checkbox-blank-outline"

    def minus18(self):
        if self.ids.text18.text == '0':
            self.ids.text18.text = '0'
        else:
            self.ids.text18.text = str(int(self.ids.text18.text) - 1)
            self.ids.list18.secondary_text = 'Total Item Price : ' + str(self.peas * int(self.ids.text18.text))

    def plus18(self):
        self.ids.text18.text = str(int(self.ids.text18.text) + 1)
        self.ids.list18.secondary_text = 'Total Item Price : ' + str(self.peas * int(self.ids.text18.text))

    def check18(self):
        if self.ids.check18.icon == "checkbox-blank-outline":
            self.ids.check18.icon = 'checkbox-marked'
        else:
            self.ids.check18.icon = "checkbox-blank-outline"

    def minus19(self):
        if self.ids.text19.text == '0':
            self.ids.text9.text = '0'
        else:
            self.ids.text19.text = str(int(self.ids.text19.text) - 1)
            self.ids.list19.secondary_text = 'Total Item Price : ' + str(self.tomato * int(self.ids.text19.text))

    def plus19(self):
        self.ids.text19.text = str(int(self.ids.text19.text) + 1)
        self.ids.list19.secondary_text = 'Total Item Price : ' + str(self.tomato * int(self.ids.text19.text))

    def check19(self):
        if self.ids.check19.icon == "checkbox-blank-outline":
            self.ids.check19.icon = 'checkbox-marked'
        else:
            self.ids.check19.icon = "checkbox-blank-outline"

    def minus20(self):
        if self.ids.text20.text == '0':
            self.ids.text20.text = '0'
        else:
            self.ids.text20.text = str(int(self.ids.text20.text) - 1)
            self.ids.list20.secondary_text = 'Total Item Price : ' + str(self.cabbage * int(self.ids.text20.text))

    def plus20(self):
        self.ids.text20.text = str(int(self.ids.text20.text) + 1)
        self.ids.list20.secondary_text = 'Total Item Price : ' + str(self.cabbage * int(self.ids.text20.text))

    def check20(self):
        if self.ids.check20.icon == "checkbox-blank-outline":
            self.ids.check20.icon = 'checkbox-marked'
        else:
            self.ids.check20.icon = "checkbox-blank-outline"

    def minus21(self):
        if self.ids.text21.text == '0':
            self.ids.text21.text = '0'
        else:
            self.ids.text21.text = str(int(self.ids.text21.text) - 1)
            self.ids.list21.secondary_text = 'Total Item Price : ' + str(self.cauliflower * int(self.ids.text21.text))

    def plus21(self):
        self.ids.text21.text = str(int(self.ids.text21.text) + 1)
        self.ids.list21.secondary_text = 'Total Item Price : ' + str(self.cauliflower * int(self.ids.text21.text))

    def check21(self):
        if self.ids.check21.icon == "checkbox-blank-outline":
            self.ids.check21.icon = 'checkbox-marked'
        else:
            self.ids.check21.icon = "checkbox-blank-outline"

    def minus22(self):
        if self.ids.text22.text == '0':
            self.ids.text22.text = '0'
        else:
            self.ids.text22.text = str(int(self.ids.text22.text) - 1)
            self.ids.list22.secondary_text = 'Total Item Price : ' + str(
                self.avakaya_chutney * int(self.ids.text22.text))

    def plus22(self):
        self.ids.text22.text = str(int(self.ids.text22.text) + 1)
        self.ids.list22.secondary_text = 'Total Item Price : ' + str(self.avakaya_chutney * int(self.ids.text22.text))

    def check22(self):
        if self.ids.check22.icon == "checkbox-blank-outline":
            self.ids.check22.icon = 'checkbox-marked'
        else:
            self.ids.check22.icon = "checkbox-blank-outline"

    def minus23(self):
        if self.ids.text23.text == '0':
            self.ids.text23.text = '0'
        else:
            self.ids.text23.text = str(int(self.ids.text23.text) - 1)
            self.ids.list23.secondary_text = 'Total Item Price : ' + str(
                self.veg_fried_rice * int(self.ids.text23.text))

    def plus23(self):
        self.ids.text23.text = str(int(self.ids.text23.text) + 1)
        self.ids.list23.secondary_text = 'Total Item Price : ' + str(self.veg_fried_rice * int(self.ids.text23.text))

    def check23(self):
        if self.ids.check23.icon == "checkbox-blank-outline":
            self.ids.check23.icon = 'checkbox-marked'
        else:
            self.ids.check23.icon = "checkbox-blank-outline"

    def minus24(self):
        if self.ids.text24.text == '0':
            self.ids.text24.text = '0'
        else:
            self.ids.text24.text = str(int(self.ids.text24.text) - 1)
            self.ids.list24.secondary_text = 'Total Item Price : ' + str(self.veg_noodles * int(self.ids.text24.text))

    def plus24(self):
        self.ids.text24.text = str(int(self.ids.text24.text) + 1)
        self.ids.list24.secondary_text = 'Total Item Price : ' + str(self.veg_noodles * int(self.ids.text24.text))

    def check24(self):
        if self.ids.check24.icon == "checkbox-blank-outline":
            self.ids.check24.icon = 'checkbox-marked'
        else:
            self.ids.check24.icon = "checkbox-blank-outline"

    def minus25(self):
        if self.ids.text25.text == '0':
            self.ids.text25.text = '0'
        else:
            self.ids.text25.text = str(int(self.ids.text25.text) - 1)
            self.ids.list25.secondary_text = 'Total Item Price : ' + str(self.veg_manchuria * int(self.ids.text25.text))

    def plus25(self):
        self.ids.text25.text = str(int(self.ids.text25.text) + 1)
        self.ids.list25.secondary_text = 'Total Item Price : ' + str(self.veg_manchuria * int(self.ids.text25.text))

    def check25(self):
        if self.ids.check25.icon == "checkbox-blank-outline":
            self.ids.check25.icon = 'checkbox-marked'
        else:
            self.ids.check25.icon = "checkbox-blank-outline"

    def minus26(self):
        if self.ids.text26.text == '0':
            self.ids.text26.text = '0'
        else:
            self.ids.text26.text = str(int(self.ids.text26.text) - 1)
            self.ids.list26.secondary_text = 'Total Item Price : ' + str(
                self.manchuria_rice * int(self.ids.text26.text))

    def plus26(self):
        self.ids.text26.text = str(int(self.ids.text26.text) + 1)
        self.ids.list26.secondary_text = 'Total Item Price : ' + str(self.manchuria_rice * int(self.ids.text26.text))

    def check26(self):
        if self.ids.check26.icon == "checkbox-blank-outline":
            self.ids.check26.icon = 'checkbox-marked'
        else:
            self.ids.check26.icon = "checkbox-blank-outline"

    def minus27(self):
        if self.ids.text27.text == '0':
            self.ids.text27.text = '0'
        else:
            self.ids.text27.text = str(int(self.ids.text27.text) - 1)
            self.ids.list27.secondary_text = 'Total Item Price : ' + str(
                self.manchuria_noodles * int(self.ids.text27.text))

    def plus27(self):
        self.ids.text27.text = str(int(self.ids.text27.text) + 1)
        self.ids.list27.secondary_text = 'Total Item Price : ' + str(self.manchuria_noodles * int(self.ids.text27.text))

    def check27(self):
        if self.ids.check27.icon == "checkbox-blank-outline":
            self.ids.check27.icon = 'checkbox-marked'
        else:
            self.ids.check27.icon = "checkbox-blank-outline"

    def minus28(self):
        if self.ids.text28.text == '0':
            self.ids.text28.text = '0'
        else:
            self.ids.text28.text = str(int(self.ids.text28.text) - 1)
            self.ids.list28.secondary_text = 'Total Item Price : ' + str(
                self.chicken_biryani * int(self.ids.text28.text))

    def plus28(self):
        self.ids.text28.text = str(int(self.ids.text28.text) + 1)
        self.ids.list28.secondary_text = 'Total Item Price : ' + str(self.chicken_biryani * int(self.ids.text28.text))

    def check28(self):
        if self.ids.check28.icon == "checkbox-blank-outline":
            self.ids.check28.icon = 'checkbox-marked'
        else:
            self.ids.check28.icon = "checkbox-blank-outline"

    def minus29(self):
        if self.ids.text29.text == '0':
            self.ids.text29.text = '0'
        else:
            self.ids.text29.text = str(int(self.ids.text29.text) - 1)
            self.ids.list29.secondary_text = 'Total Item Price : ' + str(
                self.chicken_fried_biryani * int(self.ids.text29.text))

    def plus29(self):
        self.ids.text29.text = str(int(self.ids.text29.text) + 1)
        self.ids.list29.secondary_text = 'Total Item Price : ' + str(
            self.chicken_fried_biryani * int(self.ids.text29.text))

    def check29(self):
        if self.ids.check29.icon == "checkbox-blank-outline":
            self.ids.check29.icon = 'checkbox-marked'
        else:
            self.ids.check29.icon = "checkbox-blank-outline"

    def minus30(self):
        if self.ids.text30.text == '0':
            self.ids.text30.text = '0'
        else:
            self.ids.text30.text = str(int(self.ids.text30.text) - 1)
            self.ids.list30.secondary_text = 'Total Item Price : ' + str(
                self.chicken_dum_biryani * int(self.ids.text30.text))

    def plus30(self):
        self.ids.text30.text = str(int(self.ids.text30.text) + 1)
        self.ids.list30.secondary_text = 'Total Item Price : ' + str(
            self.chicken_dum_biryani * int(self.ids.text30.text))

    def check30(self):
        if self.ids.check30.icon == "checkbox-blank-outline":
            self.ids.check30.icon = 'checkbox-marked'
        else:
            self.ids.check30.icon = "checkbox-blank-outline"

    def minus31(self):
        if self.ids.text31.text == '0':
            self.ids.text31.text = '0'
        else:
            self.ids.text31.text = str(int(self.ids.text31.text) - 1)
            self.ids.list31.secondary_text = 'Total Item Price : ' + str(
                self.mutton_biryani * int(self.ids.text31.text))

    def plus31(self):
        self.ids.text31.text = str(int(self.ids.text31.text) + 1)
        self.ids.list31.secondary_text = 'Total Item Price : ' + str(self.mutton_biryani * int(self.ids.text31.text))

    def check31(self):
        if self.ids.check31.icon == "checkbox-blank-outline":
            self.ids.check31.icon = 'checkbox-marked'
        else:
            self.ids.check31.icon = "checkbox-blank-outline"

    def minus32(self):
        if self.ids.text32.text == '0':
            self.ids.text32.text = '0'
        else:
            self.ids.text32.text = str(int(self.ids.text32.text) - 1)
            self.ids.list32.secondary_text = 'Total Item Price : ' + str(
                self.mutton_fried_biryani * int(self.ids.text32.text))

    def plus32(self):
        self.ids.text32.text = str(int(self.ids.text32.text) + 1)
        self.ids.list32.secondary_text = 'Total Item Price : ' + str(
            self.mutton_fried_biryani * int(self.ids.text32.text))

    def check32(self):
        if self.ids.check32.icon == "checkbox-blank-outline":
            self.ids.check32.icon = 'checkbox-marked'
        else:
            self.ids.check32.icon = "checkbox-blank-outline"

    def minus33(self):
        if self.ids.text33.text == '0':
            self.ids.text33.text = '0'
        else:
            self.ids.text33.text = str(int(self.ids.text33.text) - 1)
            self.ids.list33.secondary_text = 'Total Item Price : ' + str(
                self.prawns_biryani * int(self.ids.text33.text))

    def plus33(self):
        self.ids.text33.text = str(int(self.ids.text33.text) + 1)
        self.ids.list33.secondary_text = 'Total Item Price : ' + str(self.prawns_biryani * int(self.ids.text33.text))

    def check33(self):
        if self.ids.check33.icon == "checkbox-blank-outline":
            self.ids.check33.icon = 'checkbox-marked'
        else:
            self.ids.check33.icon = "checkbox-blank-outline"

    def minus34(self):
        if self.ids.text34.text == '0':
            self.ids.text34.text = '0'
        else:
            self.ids.text34.text = str(int(self.ids.text34.text) - 1)
            self.ids.list34.secondary_text = 'Total Item Price : ' + str(self.normal_rice * int(self.ids.text34.text))

    def plus34(self):
        self.ids.text34.text = str(int(self.ids.text34.text) + 1)
        self.ids.list34.secondary_text = 'Total Item Price : ' + str(self.normal_rice * int(self.ids.text34.text))

    def check34(self):
        if self.ids.check34.icon == "checkbox-blank-outline":
            self.ids.check34.icon = 'checkbox-marked'
        else:
            self.ids.check34.icon = "checkbox-blank-outline"

    def minus35(self):
        if self.ids.text35.text == '0':
            self.ids.text35.text = '0'
        else:
            self.ids.text35.text = str(int(self.ids.text35.text) - 1)
            self.ids.list35.secondary_text = 'Total Item Price : ' + str(self.chicken_fry * int(self.ids.text35.text))

    def plus35(self):
        self.ids.text35.text = str(int(self.ids.text35.text) + 1)
        self.ids.list35.secondary_text = 'Total Item Price : ' + str(self.chicken_fry * int(self.ids.text35.text))

    def check35(self):
        if self.ids.check35.icon == "checkbox-blank-outline":
            self.ids.check35.icon = 'checkbox-marked'
        else:
            self.ids.check35.icon = "checkbox-blank-outline"

    def minus36(self):
        if self.ids.text36.text == '0':
            self.ids.text36.text = '0'
        else:
            self.ids.text36.text = str(int(self.ids.text36.text) - 1)
            self.ids.list36.secondary_text = 'Total Item Price : ' + str(self.chicken_curry * int(self.ids.text36.text))

    def plus36(self):
        self.ids.text36.text = str(int(self.ids.text36.text) + 1)
        self.ids.list36.secondary_text = 'Total Item Price : ' + str(self.chicken_curry * int(self.ids.text36.text))

    def check36(self):
        if self.ids.check36.icon == "checkbox-blank-outline":
            self.ids.check36.icon = 'checkbox-marked'
        else:
            self.ids.check36.icon = "checkbox-blank-outline"

    def minus37(self):
        if self.ids.text37.text == '0':
            self.ids.text37.text = '0'
        else:
            self.ids.text37.text = str(int(self.ids.text37.text) - 1)
            self.ids.list37.secondary_text = 'Total Item Price : ' + str(self.chicken_65 * int(self.ids.text37.text))

    def plus37(self):
        self.ids.text37.text = str(int(self.ids.text37.text) + 1)
        self.ids.list37.secondary_text = 'Total Item Price : ' + str(self.chicken_65 * int(self.ids.text37.text))

    def check37(self):
        if self.ids.check37.icon == "checkbox-blank-outline":
            self.ids.check37.icon = 'checkbox-marked'
        else:
            self.ids.check37.icon = "checkbox-blank-outline"

    def minus38(self):
        if self.ids.text38.text == '0':
            self.ids.text38.text = '0'
        else:
            self.ids.text38.text = str(int(self.ids.text38.text) - 1)
            self.ids.list38.secondary_text = 'Total Item Price : ' + str(
                self.gongura_chicken_curry * int(self.ids.text38.text))

    def plus38(self):
        self.ids.text38.text = str(int(self.ids.text38.text) + 1)
        self.ids.list38.secondary_text = 'Total Item Price : ' + str(
            self.gongura_chicken_curry * int(self.ids.text38.text))

    def check38(self):
        if self.ids.check38.icon == "checkbox-blank-outline":
            self.ids.check38.icon = 'checkbox-marked'
        else:
            self.ids.check38.icon = "checkbox-blank-outline"

    def minus39(self):
        if self.ids.text39.text == '0':
            self.ids.text39.text = '0'
        else:
            self.ids.text39.text = str(int(self.ids.text39.text) - 1)
            self.ids.list39.secondary_text = 'Total Item Price : ' + str(self.mutton_fry * int(self.ids.text39.text))

    def plus39(self):
        self.ids.text39.text = str(int(self.ids.text39.text) + 1)
        self.ids.list39.secondary_text = 'Total Item Price : ' + str(self.mutton_fry * int(self.ids.text39.text))

    def check39(self):
        if self.ids.check39.icon == "checkbox-blank-outline":
            self.ids.check39.icon = 'checkbox-marked'
        else:
            self.ids.check39.icon = "checkbox-blank-outline"

    def minus40(self):
        if self.ids.text40.text == '0':
            self.ids.text40.text = '0'
        else:
            self.ids.text40.text = str(int(self.ids.text40.text) - 1)
            self.ids.list40.secondary_text = 'Total Item Price : ' + str(self.mutton_curry * int(self.ids.text40.text))

    def plus40(self):
        self.ids.text40.text = str(int(self.ids.text40.text) + 1)
        self.ids.list40.secondary_text = 'Total Item Price : ' + str(self.mutton_curry * int(self.ids.text40.text))

    def check40(self):
        if self.ids.check40.icon == "checkbox-blank-outline":
            self.ids.check40.icon = 'checkbox-marked'
        else:
            self.ids.check40.icon = "checkbox-blank-outline"

    def minus41(self):
        if self.ids.text41.text == '0':
            self.ids.text41.text = '0'
        else:
            self.ids.text41.text = str(int(self.ids.text41.text) - 1)
            self.ids.list41.secondary_text = 'Total Item Price : ' + str(
                self.gongura_mutton_curry * int(self.ids.text41.text))

    def plus41(self):
        self.ids.text41.text = str(int(self.ids.text41.text) + 1)
        self.ids.list41.secondary_text = 'Total Item Price : ' + str(
            self.gongura_mutton_curry * int(self.ids.text41.text))

    def check41(self):
        if self.ids.check41.icon == "checkbox-blank-outline":
            self.ids.check41.icon = 'checkbox-marked'
        else:
            self.ids.check41.icon = "checkbox-blank-outline"

    def minus42(self):
        if self.ids.text42.text == '0':
            self.ids.text42.text = '0'
        else:
            self.ids.text42.text = str(int(self.ids.text42.text) - 1)
            self.ids.list42.secondary_text = 'Total Item Price : ' + str(self.fish_fry * int(self.ids.text42.text))

    def plus42(self):
        self.ids.text42.text = str(int(self.ids.text42.text) + 1)
        self.ids.list42.secondary_text = 'Total Item Price : ' + str(self.fish_fry * int(self.ids.text42.text))

    def check42(self):
        if self.ids.check42.icon == "checkbox-blank-outline":
            self.ids.check42.icon = 'checkbox-marked'
        else:
            self.ids.check42.icon = "checkbox-blank-outline"

    def minus43(self):
        if self.ids.text43.text == '0':
            self.ids.text43.text = '0'
        else:
            self.ids.text43.text = str(int(self.ids.text43.text) - 1)
            self.ids.list43.secondary_text = 'Total Item Price : ' + str(self.fish_curry * int(self.ids.text43.text))

    def plus43(self):
        self.ids.text43.text = str(int(self.ids.text43.text) + 1)
        self.ids.list43.secondary_text = 'Total Item Price : ' + str(self.fish_curry * int(self.ids.text43.text))

    def check43(self):
        if self.ids.check43.icon == "checkbox-blank-outline":
            self.ids.check43.icon = 'checkbox-marked'
        else:
            self.ids.check43.icon = "checkbox-blank-outline"

    def minus44(self):
        if self.ids.text44.text == '0':
            self.ids.text44.text = '0'
        else:
            self.ids.text44.text = str(int(self.ids.text44.text) - 1)
            self.ids.list44.secondary_text = 'Total Item Price : ' + str(self.prawns_fry * int(self.ids.text44.text))

    def plus44(self):
        self.ids.text44.text = str(int(self.ids.text44.text) + 1)
        self.ids.list44.secondary_text = 'Total Item Price : ' + str(self.prawns_fry * int(self.ids.text44.text))

    def check44(self):
        if self.ids.check44.icon == "checkbox-blank-outline":
            self.ids.check44.icon = 'checkbox-marked'
        else:
            self.ids.check44.icon = "checkbox-blank-outline"

    def minus45(self):
        if self.ids.text45.text == '0':
            self.ids.text45.text = '0'
        else:
            self.ids.text45.text = str(int(self.ids.text45.text) - 1)
            self.ids.list45.secondary_text = 'Total Item Price : ' + str(self.prawns_curry * int(self.ids.text45.text))

    def plus45(self):
        self.ids.text45.text = str(int(self.ids.text45.text) + 1)
        self.ids.list45.secondary_text = 'Total Item Price : ' + str(self.prawns_curry * int(self.ids.text45.text))

    def check45(self):
        if self.ids.check45.icon == "checkbox-blank-outline":
            self.ids.check45.icon = 'checkbox-marked'
        else:
            self.ids.check45.icon = "checkbox-blank-outline"

    def minus46(self):
        if self.ids.text46.text == '0':
            self.ids.text46.text = '0'
        else:
            self.ids.text46.text = str(int(self.ids.text46.text) - 1)
            self.ids.list46.secondary_text = 'Total Item Price : ' + str(self.crabs_curry * int(self.ids.text46.text))

    def plus46(self):
        self.ids.text46.text = str(int(self.ids.text46.text) + 1)
        self.ids.list46.secondary_text = 'Total Item Price : ' + str(self.crabs_curry * int(self.ids.text46.text))

    def check46(self):
        if self.ids.check46.icon == "checkbox-blank-outline":
            self.ids.check46.icon = 'checkbox-marked'
        else:
            self.ids.check46.icon = "checkbox-blank-outline"

    def minus47(self):
        if self.ids.text47.text == '0':
            self.ids.text47.text = '0'
        else:
            self.ids.text47.text = str(int(self.ids.text47.text) - 1)
            self.ids.list47.secondary_text = 'Total Item Price : ' + str(self.egg_curry * int(self.ids.text47.text))

    def plus47(self):
        self.ids.text47.text = str(int(self.ids.text47.text) + 1)
        self.ids.list47.secondary_text = 'Total Item Price : ' + str(self.egg_curry * int(self.ids.text47.text))

    def check47(self):
        if self.ids.check47.icon == "checkbox-blank-outline":
            self.ids.check47.icon = 'checkbox-marked'
        else:
            self.ids.check47.icon = "checkbox-blank-outline"

    def minus48(self):
        if self.ids.text48.text == '0':
            self.ids.text48.text = '0'
        else:
            self.ids.text48.text = str(int(self.ids.text48.text) - 1)
            self.ids.list48.secondary_text = 'Total Item Price : ' + str(self.egg_omlet * int(self.ids.text48.text))

    def plus48(self):
        self.ids.text48.text = str(int(self.ids.text48.text) + 1)
        self.ids.list48.secondary_text = 'Total Item Price : ' + str(self.egg_omlet * int(self.ids.text48.text))

    def check48(self):
        if self.ids.check48.icon == "checkbox-blank-outline":
            self.ids.check48.icon = 'checkbox-marked'
        else:
            self.ids.check48.icon = "checkbox-blank-outline"

    def minus49(self):
        if self.ids.text49.text == '0':
            self.ids.text49.text = '0'
        else:
            self.ids.text49.text = str(int(self.ids.text49.text) - 1)
            self.ids.list49.secondary_text = 'Total Item Price : ' + str(self.egg_roll * int(self.ids.text49.text))

    def plus49(self):
        self.ids.text49.text = str(int(self.ids.text49.text) + 1)
        self.ids.list49.secondary_text = 'Total Item Price : ' + str(self.egg_roll * int(self.ids.text49.text))

    def check49(self):
        if self.ids.check49.icon == "checkbox-blank-outline":
            self.ids.check49.icon = 'checkbox-marked'
        else:
            self.ids.check49.icon = "checkbox-blank-outline"

    def minus50(self):
        if self.ids.text50.text == '0':
            self.ids.text50.text = '0'
        else:
            self.ids.text50.text = str(int(self.ids.text50.text) - 1)
            self.ids.list50.secondary_text = 'Total Item Price : ' + str(self.chicken_roll * int(self.ids.text50.text))

    def plus50(self):
        self.ids.text50.text = str(int(self.ids.text50.text) + 1)
        self.ids.list50.secondary_text = 'Total Item Price : ' + str(self.chicken_roll * int(self.ids.text50.text))

    def check50(self):
        if self.ids.check50.icon == "checkbox-blank-outline":
            self.ids.check50.icon = 'checkbox-marked'
        else:
            self.ids.check50.icon = "checkbox-blank-outline"

    def minus51(self):
        if self.ids.text51.text == '0':
            self.ids.text51.text = '0'
        else:
            self.ids.text51.text = str(int(self.ids.text51.text) - 1)
            self.ids.list51.secondary_text = 'Total Item Price : ' + str(self.chicken_wings * int(self.ids.text51.text))

    def plus51(self):
        self.ids.text51.text = str(int(self.ids.text51.text) + 1)
        self.ids.list51.secondary_text = 'Total Item Price : ' + str(self.chicken_wings * int(self.ids.text51.text))

    def check51(self):
        if self.ids.check51.icon == "checkbox-blank-outline":
            self.ids.check51.icon = 'checkbox-marked'
        else:
            self.ids.check51.icon = "checkbox-blank-outline"

    def minus52(self):
        if self.ids.text52.text == '0':
            self.ids.text52.text = '0'
        else:
            self.ids.text52.text = str(int(self.ids.text52.text) - 1)
            self.ids.list52.secondary_text = 'Total Item Price : ' + str(
                self.chicken_leg_peaces * int(self.ids.text52.text))

    def plus52(self):
        self.ids.text52.text = str(int(self.ids.text52.text) + 1)
        self.ids.list52.secondary_text = 'Total Item Price : ' + str(
            self.chicken_leg_peaces * int(self.ids.text52.text))

    def check52(self):
        if self.ids.check52.icon == "checkbox-blank-outline":
            self.ids.check52.icon = 'checkbox-marked'
        else:
            self.ids.check52.icon = "checkbox-blank-outline"

    def minus53(self):
        if self.ids.text53.text == '0':
            self.ids.text53.text = '0'
        else:
            self.ids.text53.text = str(int(self.ids.text53.text) - 1)
            self.ids.list53.secondary_text = 'Total Item Price : ' + str(self.botti_curry * int(self.ids.text53.text))

    def plus53(self):
        self.ids.text53.text = str(int(self.ids.text53.text) + 1)
        self.ids.list53.secondary_text = 'Total Item Price : ' + str(self.botti_curry * int(self.ids.text53.text))

    def check53(self):
        if self.ids.check53.icon == "checkbox-blank-outline":
            self.ids.check53.icon = 'checkbox-marked'
        else:
            self.ids.check53.icon = "checkbox-blank-outline"

    def minus54(self):
        if self.ids.text54.text == '0':
            self.ids.text54.text = '0'
        else:
            self.ids.text54.text = str(int(self.ids.text54.text) - 1)
            self.ids.list54.secondary_text = 'Total Item Price : ' + str(
                self.chicken_fried_rice * int(self.ids.text54.text))

    def plus54(self):
        self.ids.text54.text = str(int(self.ids.text54.text) + 1)
        self.ids.list54.secondary_text = 'Total Item Price : ' + str(
            self.chicken_fried_rice * int(self.ids.text54.text))

    def check54(self):
        if self.ids.check54.icon == "checkbox-blank-outline":
            self.ids.check54.icon = 'checkbox-marked'
        else:
            self.ids.check54.icon = "checkbox-blank-outline"

    def minus55(self):
        if self.ids.text55.text == '0':
            self.ids.text55.text = '0'
        else:
            self.ids.text55.text = str(int(self.ids.text55.text) - 1)
            self.ids.list55.secondary_text = 'Total Item Price : ' + str(
                self.chicken_noodles * int(self.ids.text55.text))

    def plus55(self):
        self.ids.text55.text = str(int(self.ids.text55.text) + 1)
        self.ids.list55.secondary_text = 'Total Item Price : ' + str(self.chicken_noodles * int(self.ids.text55.text))

    def check55(self):
        if self.ids.check55.icon == "checkbox-blank-outline":
            self.ids.check55.icon = 'checkbox-marked'
        else:
            self.ids.check55.icon = "checkbox-blank-outline"

    def minus56(self):
        if self.ids.text56.text == '0':
            self.ids.text56.text = '0'
        else:
            self.ids.text56.text = str(int(self.ids.text56.text) - 1)
            self.ids.list56.secondary_text = 'Total Item Price : ' + str(
                self.chilli_chicken * int(self.ids.text56.text))

    def plus56(self):
        self.ids.text56.text = str(int(self.ids.text56.text) + 1)
        self.ids.list56.secondary_text = 'Total Item Price : ' + str(self.chilli_chicken * int(self.ids.text56.text))

    def check56(self):
        if self.ids.check56.icon == "checkbox-blank-outline":
            self.ids.check56.icon = 'checkbox-marked'
        else:
            self.ids.check56.icon = "checkbox-blank-outline"

    def minus57(self):
        if self.ids.text57.text == '0':
            self.ids.text57.text = '0'
        else:
            self.ids.text57.text = str(int(self.ids.text57.text) - 1)
            self.ids.list57.secondary_text = 'Total Item Price : ' + str(self.egg_noodles * int(self.ids.text57.text))

    def plus57(self):
        self.ids.text57.text = str(int(self.ids.text57.text) + 1)
        self.ids.list57.secondary_text = 'Total Item Price : ' + str(self.egg_noodles * int(self.ids.text57.text))

    def check57(self):
        if self.ids.check57.icon == "checkbox-blank-outline":
            self.ids.check57.icon = 'checkbox-marked'
        else:
            self.ids.check57.icon = "checkbox-blank-outline"

    def minus58(self):
        if self.ids.text58.text == '0':
            self.ids.text58.text = '0'
        else:
            self.ids.text58.text = str(int(self.ids.text58.text) - 1)
            self.ids.list58.secondary_text = 'Total Item Price : ' + str(self.egg_manchuria * int(self.ids.text58.text))

    def plus58(self):
        self.ids.text58.text = str(int(self.ids.text58.text) + 1)
        self.ids.list58.secondary_text = 'Total Item Price : ' + str(self.egg_manchuria * int(self.ids.text58.text))

    def check58(self):
        if self.ids.check58.icon == "checkbox-blank-outline":
            self.ids.check58.icon = 'checkbox-marked'
        else:
            self.ids.check58.icon = "checkbox-blank-outline"

    def minus59(self):
        if self.ids.text59.text == '0':
            self.ids.text59.text = '0'
        else:
            self.ids.text59.text = str(int(self.ids.text59.text) - 1)
            self.ids.list59.secondary_text = 'Total Item Price : ' + str(
                self.manchuria_egg_rice * int(self.ids.text59.text))

    def plus59(self):
        self.ids.text59.text = str(int(self.ids.text59.text) + 1)
        self.ids.list59.secondary_text = 'Total Item Price : ' + str(
            self.manchuria_egg_rice * int(self.ids.text59.text))

    def check59(self):
        if self.ids.check59.icon == "checkbox-blank-outline":
            self.ids.check59.icon = 'checkbox-marked'
        else:
            self.ids.check59.icon = "checkbox-blank-outline"

    def minus60(self):
        if self.ids.text60.text == '0':
            self.ids.text60.text = '0'
        else:
            self.ids.text60.text = str(int(self.ids.text60.text) - 1)
            self.ids.list60.secondary_text = 'Total Item Price : ' + str(
                self.manchuria_egg_noodles * int(self.ids.text60.text))

    def plus60(self):
        self.ids.text60.text = str(int(self.ids.text60.text) + 1)
        self.ids.list60.secondary_text = 'Total Item Price : ' + str(
            self.manchuria_egg_noodles * int(self.ids.text60.text))

    def check60(self):
        if self.ids.check60.icon == "checkbox-blank-outline":
            self.ids.check60.icon = 'checkbox-marked'
        else:
            self.ids.check60.icon = "checkbox-blank-outline"

    def minus61(self):
        if self.ids.text61.text == '0':
            self.ids.text61.text = '0'
        else:
            self.ids.text61.text = str(int(self.ids.text61.text) - 1)
            self.ids.list61.secondary_text = 'Total Item Price : ' + str(self.butter_non * int(self.ids.text61.text))

    def plus61(self):
        self.ids.text61.text = str(int(self.ids.text61.text) + 1)
        self.ids.list61.secondary_text = 'Total Item Price : ' + str(self.butter_non * int(self.ids.text61.text))

    def check61(self):
        if self.ids.check61.icon == "checkbox-blank-outline":
            self.ids.check61.icon = 'checkbox-marked'
        else:
            self.ids.check61.icon = "checkbox-blank-outline"

    def minus62(self):
        if self.ids.text62.text == '0':
            self.ids.text62.text = '0'
        else:
            self.ids.text62.text = str(int(self.ids.text62.text) - 1)
            self.ids.list62.secondary_text = 'Total Item Price : ' + str(self.tawa_roti * int(self.ids.text62.text))

    def plus62(self):
        self.ids.text62.text = str(int(self.ids.text62.text) + 1)
        self.ids.list62.secondary_text = 'Total Item Price : ' + str(self.tawa_roti * int(self.ids.text62.text))

    def check62(self):
        if self.ids.check62.icon == "checkbox-blank-outline":
            self.ids.check62.icon = 'checkbox-marked'
        else:
            self.ids.check62.icon = "checkbox-blank-outline"

    def minus63(self):
        if self.ids.text63.text == '0':
            self.ids.text63.text = '0'
        else:
            self.ids.text63.text = str(int(self.ids.text63.text) - 1)
            self.ids.list63.secondary_text = 'Total Item Price : ' + str(self.rumalli_roti * int(self.ids.text63.text))

    def plus63(self):
        self.ids.text63.text = str(int(self.ids.text63.text) + 1)
        self.ids.list63.secondary_text = 'Total Item Price : ' + str(self.rumalli_roti * int(self.ids.text63.text))

    def check63(self):
        if self.ids.check63.icon == "checkbox-blank-outline":
            self.ids.check63.icon = 'checkbox-marked'
        else:
            self.ids.check63.icon = "checkbox-blank-outline"

    def minus64(self):
        if self.ids.text64.text == '0':
            self.ids.text64.text = '0'
        else:
            self.ids.text64.text = str(int(self.ids.text64.text) - 1)
            self.ids.list64.secondary_text = 'Total Item Price : ' + str(self.makki_roti * int(self.ids.text64.text))

    def plus64(self):
        self.ids.text64.text = str(int(self.ids.text64.text) + 1)
        self.ids.list64.secondary_text = 'Total Item Price : ' + str(self.makki_roti * int(self.ids.text64.text))

    def check64(self):
        if self.ids.check64.icon == "checkbox-blank-outline":
            self.ids.check64.icon = 'checkbox-marked'
        else:
            self.ids.check64.icon = "checkbox-blank-outline"

    def minus65(self):
        if self.ids.text65.text == '0':
            self.ids.text65.text = '0'
        else:
            self.ids.text65.text = str(int(self.ids.text65.text) - 1)
            self.ids.list65.secondary_text = 'Total Item Price : ' + str(self.parota * int(self.ids.text65.text))

    def plus65(self):
        self.ids.text65.text = str(int(self.ids.text65.text) + 1)
        self.ids.list65.secondary_text = 'Total Item Price : ' + str(self.parota * int(self.ids.text65.text))

    def check65(self):
        if self.ids.check65.icon == "checkbox-blank-outline":
            self.ids.check65.icon = 'checkbox-marked'
        else:
            self.ids.check65.icon = "checkbox-blank-outline"

    def minus66(self):
        if self.ids.text66.text == '0':
            self.ids.text66.text = '0'
        else:
            self.ids.text66.text = str(int(self.ids.text66.text) - 1)
            self.ids.list66.secondary_text = 'Total Item Price : ' + str(self.sada_roti * int(self.ids.text66.text))

    def plus66(self):
        self.ids.text66.text = str(int(self.ids.text66.text) + 1)
        self.ids.list66.secondary_text = 'Total Item Price : ' + str(self.sada_roti * int(self.ids.text66.text))

    def check66(self):
        if self.ids.check66.icon == "checkbox-blank-outline":
            self.ids.check66.icon = 'checkbox-marked'
        else:
            self.ids.check66.icon = "checkbox-blank-outline"

    def minus67(self):
        if self.ids.text67.text == '0':
            self.ids.text67.text = '0'
        else:
            self.ids.text67.text = str(int(self.ids.text67.text) - 1)
            self.ids.list67.secondary_text = 'Total Item Price : ' + str(self.egg_keema * int(self.ids.text67.text))

    def plus67(self):
        self.ids.text67.text = str(int(self.ids.text67.text) + 1)
        self.ids.list67.secondary_text = 'Total Item Price : ' + str(self.egg_keema * int(self.ids.text67.text))

    def check67(self):
        if self.ids.check67.icon == "checkbox-blank-outline":
            self.ids.check67.icon = 'checkbox-marked'
        else:
            self.ids.check67.icon = "checkbox-blank-outline"

    def minus68(self):
        if self.ids.text68.text == '0':
            self.ids.text68.text = '0'
        else:
            self.ids.text68.text = str(int(self.ids.text68.text) - 1)
            self.ids.list68.secondary_text = 'Total Item Price : ' + str(self.egg_burji * int(self.ids.text68.text))

    def plus68(self):
        self.ids.text68.text = str(int(self.ids.text68.text) + 1)
        self.ids.list68.secondary_text = 'Total Item Price : ' + str(self.egg_burji * int(self.ids.text68.text))

    def check68(self):
        if self.ids.check68.icon == "checkbox-blank-outline":
            self.ids.check68.icon = 'checkbox-marked'
        else:
            self.ids.check68.icon = "checkbox-blank-outline"

    def minus69(self):
        if self.ids.text69.text == '0':
            self.ids.text69.text = '0'
        else:
            self.ids.text69.text = str(int(self.ids.text69.text) - 1)
            self.ids.list69.secondary_text = 'Total Item Price : ' + str(
                self.butter_chicken * int(self.ids.text69.text))

    def plus69(self):
        self.ids.text69.text = str(int(self.ids.text69.text) + 1)
        self.ids.list69.secondary_text = 'Total Item Price : ' + str(self.butter_chicken * int(self.ids.text69.text))

    def check69(self):
        if self.ids.check69.icon == "checkbox-blank-outline":
            self.ids.check69.icon = 'checkbox-marked'
        else:
            self.ids.check69.icon = "checkbox-blank-outline"

    def minus70(self):
        if self.ids.text70.text == '0':
            self.ids.text70.text = '0'
        else:
            self.ids.text70.text = str(int(self.ids.text70.text) - 1)
            self.ids.list70.secondary_text = 'Total Item Price : ' + str(self.afgani * int(self.ids.text70.text))

    def plus70(self):
        self.ids.text70.text = str(int(self.ids.text70.text) + 1)
        self.ids.list70.secondary_text = 'Total Item Price : ' + str(self.afgani * int(self.ids.text70.text))

    def check70(self):
        if self.ids.check70.icon == "checkbox-blank-outline":
            self.ids.check70.icon = 'checkbox-marked'
        else:
            self.ids.check70.icon = "checkbox-blank-outline"

    def minus71(self):
        if self.ids.text71.text == '0':
            self.ids.text71.text = '0'
        else:
            self.ids.text71.text = str(int(self.ids.text71.text) - 1)
            self.ids.list71.secondary_text = 'Total Item Price : ' + str(self.kajju_curry * int(self.ids.text71.text))

    def plus71(self):
        self.ids.text71.text = str(int(self.ids.text71.text) + 1)
        self.ids.list71.secondary_text = 'Total Item Price : ' + str(self.kajju_curry * int(self.ids.text71.text))

    def check71(self):
        if self.ids.check71.icon == "checkbox-blank-outline":
            self.ids.check71.icon = 'checkbox-marked'
        else:
            self.ids.check71.icon = "checkbox-blank-outline"

    def minus72(self):
        if self.ids.text72.text == '0':
            self.ids.text72.text = '0'
        else:
            self.ids.text72.text = str(int(self.ids.text72.text) - 1)
            self.ids.list72.secondary_text = 'Total Item Price : ' + str(
                self.paneer_butter_masala * int(self.ids.text72.text))

    def plus72(self):
        self.ids.text72.text = str(int(self.ids.text72.text) + 1)
        self.ids.list72.secondary_text = 'Total Item Price : ' + str(
            self.paneer_butter_masala * int(self.ids.text72.text))

    def check72(self):
        if self.ids.check72.icon == "checkbox-blank-outline":
            self.ids.check72.icon = 'checkbox-marked'
        else:
            self.ids.check72.icon = "checkbox-blank-outline"

    def minus73(self):
        if self.ids.text73.text == '0':
            self.ids.text73.text = '0'
        else:
            self.ids.text73.text = str(int(self.ids.text73.text) - 1)
            self.ids.list73.secondary_text = 'Total Item Price : ' + str(self.gulab_jamun * int(self.ids.text73.text))

    def plus73(self):
        self.ids.text73.text = str(int(self.ids.text73.text) + 1)
        self.ids.list73.secondary_text = 'Total Item Price : ' + str(self.gulab_jamun * int(self.ids.text73.text))

    def check73(self):
        if self.ids.check73.icon == "checkbox-blank-outline":
            self.ids.check73.icon = 'checkbox-marked'
        else:
            self.ids.check73.icon = "checkbox-blank-outline"

    def minus74(self):
        if self.ids.text74.text == '0':
            self.ids.text74.text = '0'
        else:
            self.ids.text74.text = str(int(self.ids.text74.text) - 1)
            self.ids.list74.secondary_text = 'Total Item Price : ' + str(
                self.gajar_ka_halva * int(self.ids.text74.text))

    def plus74(self):
        self.ids.text74.text = str(int(self.ids.text74.text) + 1)
        self.ids.list74.secondary_text = 'Total Item Price : ' + str(self.gajar_ka_halva * int(self.ids.text74.text))

    def check74(self):
        if self.ids.check74.icon == "checkbox-blank-outline":
            self.ids.check74.icon = 'checkbox-marked'
        else:
            self.ids.check74.icon = "checkbox-blank-outline"

    def minus75(self):
        if self.ids.text75.text == '0':
            self.ids.text75.text = '0'
        else:
            self.ids.text75.text = str(int(self.ids.text75.text) - 1)
            self.ids.list75.secondary_text = 'Total Item Price : ' + str(self.ras_malai * int(self.ids.text75.text))

    def plus75(self):
        self.ids.text75.text = str(int(self.ids.text75.text) + 1)
        self.ids.list75.secondary_text = 'Total Item Price : ' + str(self.ras_malai * int(self.ids.text75.text))

    def check75(self):
        if self.ids.check75.icon == "checkbox-blank-outline":
            self.ids.check75.icon = 'checkbox-marked'
        else:
            self.ids.check75.icon = "checkbox-blank-outline"

    def minus76(self):
        if self.ids.text76.text == '0':
            self.ids.text76.text = '0'
        else:
            self.ids.text76.text = str(int(self.ids.text76.text) - 1)
            self.ids.list76.secondary_text = 'Total Item Price : ' + str(self.besan_ladoo * int(self.ids.text76.text))

    def plus76(self):
        self.ids.text76.text = str(int(self.ids.text76.text) + 1)
        self.ids.list76.secondary_text = 'Total Item Price : ' + str(self.besan_ladoo * int(self.ids.text76.text))

    def check76(self):
        if self.ids.check76.icon == "checkbox-blank-outline":
            self.ids.check76.icon = 'checkbox-marked'
        else:
            self.ids.check76.icon = "checkbox-blank-outline"

    def minus77(self):
        if self.ids.text77.text == '0':
            self.ids.text77.text = '0'
        else:
            self.ids.text77.text = str(int(self.ids.text77.text) - 1)
            self.ids.list77.secondary_text = 'Total Item Price : ' + str(self.kalakand * int(self.ids.text77.text))

    def plus77(self):
        self.ids.text77.text = str(int(self.ids.text77.text) + 1)
        self.ids.list77.secondary_text = 'Total Item Price : ' + str(self.kalakand * int(self.ids.text77.text))

    def check77(self):
        if self.ids.check77.icon == "checkbox-blank-outline":
            self.ids.check77.icon = 'checkbox-marked'
        else:
            self.ids.check77.icon = "checkbox-blank-outline"

    def minus78(self):
        if self.ids.text78.text == '0':
            self.ids.text78.text = '0'
        else:
            self.ids.text78.text = str(int(self.ids.text78.text) - 1)
            self.ids.list78.secondary_text = 'Total Item Price : ' + str(self.peanut_chikki * int(self.ids.text78.text))

    def plus78(self):
        self.ids.text78.text = str(int(self.ids.text78.text) + 1)
        self.ids.list78.secondary_text = 'Total Item Price : ' + str(self.peanut_chikki * int(self.ids.text78.text))

    def check78(self):
        if self.ids.check78.icon == "checkbox-blank-outline":
            self.ids.check78.icon = 'checkbox-marked'
        else:
            self.ids.check78.icon = "checkbox-blank-outline"

    def minus79(self):
        if self.ids.text79.text == '0':
            self.ids.text79.text = '0'
        else:
            self.ids.text79.text = str(int(self.ids.text79.text) - 1)
            self.ids.list79.secondary_text = 'Total Item Price : ' + str(self.jalabi * int(self.ids.text79.text))

    def plus79(self):
        self.ids.text79.text = str(int(self.ids.text79.text) + 1)
        self.ids.list79.secondary_text = 'Total Item Price : ' + str(self.jalabi * int(self.ids.text79.text))

    def check79(self):
        if self.ids.check79.icon == "checkbox-blank-outline":
            self.ids.check79.icon = 'checkbox-marked'
        else:
            self.ids.check79.icon = "checkbox-blank-outline"

    def minus80(self):
        if self.ids.text80.text == '0':
            self.ids.text80.text = '0'
        else:
            self.ids.text80.text = str(int(self.ids.text80.text) - 1)
            self.ids.list80.secondary_text = 'Total Item Price : ' + str(self.soan_papdi * int(self.ids.text80.text))

    def plus80(self):
        self.ids.text80.text = str(int(self.ids.text80.text) + 1)
        self.ids.list80.secondary_text = 'Total Item Price : ' + str(self.soan_papdi * int(self.ids.text80.text))

    def check80(self):
        if self.ids.check80.icon == "checkbox-blank-outline":
            self.ids.check80.icon = 'checkbox-marked'
        else:
            self.ids.check80.icon = "checkbox-blank-outline"

    def minus81(self):
        if self.ids.text81.text == '0':
            self.ids.text81.text = '0'
        else:
            self.ids.text81.text = str(int(self.ids.text81.text) - 1)
            self.ids.list81.secondary_text = 'Total Item Price : ' + str(self.rice_kheer * int(self.ids.text81.text))

    def plus81(self):
        self.ids.text81.text = str(int(self.ids.text81.text) + 1)
        self.ids.list81.secondary_text = 'Total Item Price : ' + str(self.rice_kheer * int(self.ids.text81.text))

    def check81(self):
        if self.ids.check81.icon == "checkbox-blank-outline":
            self.ids.check81.icon = 'checkbox-marked'
        else:
            self.ids.check81.icon = "checkbox-blank-outline"

    def minus82(self):
        if self.ids.text82.text == '0':
            self.ids.text82.text = '0'
        else:
            self.ids.text82.text = str(int(self.ids.text82.text) - 1)
            self.ids.list82.secondary_text = 'Total Item Price : ' + str(
                self.masala_peanuts * int(self.ids.text82.text))

    def plus82(self):
        self.ids.text82.text = str(int(self.ids.text82.text) + 1)
        self.ids.list82.secondary_text = 'Total Item Price : ' + str(self.masala_peanuts * int(self.ids.text82.text))

    def check82(self):
        if self.ids.check82.icon == "checkbox-blank-outline":
            self.ids.check82.icon = 'checkbox-marked'
        else:
            self.ids.check82.icon = "checkbox-blank-outline"

    def minus83(self):
        if self.ids.text83.text == '0':
            self.ids.text83.text = '0'
        else:
            self.ids.text83.text = str(int(self.ids.text83.text) - 1)
            self.ids.list83.secondary_text = 'Total Item Price : ' + str(self.samosa * int(self.ids.text83.text))

    def plus83(self):
        self.ids.text83.text = str(int(self.ids.text83.text) + 1)
        self.ids.list83.secondary_text = 'Total Item Price : ' + str(self.samosa * int(self.ids.text83.text))

    def check83(self):
        if self.ids.check83.icon == "checkbox-blank-outline":
            self.ids.check83.icon = 'checkbox-marked'
        else:
            self.ids.check83.icon = "checkbox-blank-outline"

    def minus84(self):
        if self.ids.text84.text == '0':
            self.ids.text84.text = '0'
        else:
            self.ids.text84.text = str(int(self.ids.text84.text) - 1)
            self.ids.list84.secondary_text = 'Total Item Price : ' + str(self.onion_pakodi * int(self.ids.text84.text))

    def plus84(self):
        self.ids.text84.text = str(int(self.ids.text84.text) + 1)
        self.ids.list84.secondary_text = 'Total Item Price : ' + str(self.onion_pakodi * int(self.ids.text84.text))

    def check84(self):
        if self.ids.check84.icon == "checkbox-blank-outline":
            self.ids.check84.icon = 'checkbox-marked'
        else:
            self.ids.check84.icon = "checkbox-blank-outline"

    def minus85(self):
        if self.ids.text85.text == '0':
            self.ids.text85.text = '0'
        else:
            self.ids.text85.text = str(int(self.ids.text85.text) - 1)
            self.ids.list85.secondary_text = 'Total Item Price : ' + str(self.bajji * int(self.ids.text85.text))

    def plus85(self):
        self.ids.text85.text = str(int(self.ids.text85.text) + 1)
        self.ids.list85.secondary_text = 'Total Item Price : ' + str(self.bajji * int(self.ids.text85.text))

    def check85(self):
        if self.ids.check85.icon == "checkbox-blank-outline":
            self.ids.check85.icon = 'checkbox-marked'
        else:
            self.ids.check85.icon = "checkbox-blank-outline"

    def minus86(self):
        if self.ids.text86.text == '0':
            self.ids.text86.text = '0'
        else:
            self.ids.text86.text = str(int(self.ids.text86.text) - 1)
            self.ids.list86.secondary_text = 'Total Item Price : ' + str(self.mixter * int(self.ids.text86.text))

    def plus86(self):
        self.ids.text86.text = str(int(self.ids.text86.text) + 1)
        self.ids.list86.secondary_text = 'Total Item Price : ' + str(self.mixter * int(self.ids.text86.text))

    def check86(self):
        if self.ids.check86.icon == "checkbox-blank-outline":
            self.ids.check86.icon = 'checkbox-marked'
        else:
            self.ids.check86.icon = "checkbox-blank-outline"

    def minus87(self):
        if self.ids.text87.text == '0':
            self.ids.text87.text = '0'
        else:
            self.ids.text87.text = str(int(self.ids.text87.text) - 1)
            self.ids.list87.secondary_text = 'Total Item Price : ' + str(self.vada_pav * int(self.ids.text87.text))

    def plus87(self):
        self.ids.text87.text = str(int(self.ids.text87.text) + 1)
        self.ids.list87.secondary_text = 'Total Item Price : ' + str(self.vada_pav * int(self.ids.text87.text))

    def check87(self):
        if self.ids.check87.icon == "checkbox-blank-outline":
            self.ids.check87.icon = 'checkbox-marked'
        else:
            self.ids.check87.icon = "checkbox-blank-outline"

    def minus88(self):
        if self.ids.text88.text == '0':
            self.ids.text88.text = '0'
        else:
            self.ids.text88.text = str(int(self.ids.text88.text) - 1)
            self.ids.list88.secondary_text = 'Total Item Price : ' + str(self.panipuri * int(self.ids.text88.text))

    def plus88(self):
        self.ids.text88.text = str(int(self.ids.text88.text) + 1)
        self.ids.list88.secondary_text = 'Total Item Price : ' + str(self.panipuri * int(self.ids.text88.text))

    def check88(self):
        if self.ids.check88.icon == "checkbox-blank-outline":
            self.ids.check88.icon = 'checkbox-marked'
        else:
            self.ids.check88.icon = "checkbox-blank-outline"

    def minus89(self):
        if self.ids.text89.text == '0':
            self.ids.text89.text = '0'
        else:
            self.ids.text89.text = str(int(self.ids.text89.text) - 1)
            self.ids.list89.secondary_text = 'Total Item Price : ' + str(self.sprite * int(self.ids.text89.text))

    def plus89(self):
        self.ids.text89.text = str(int(self.ids.text89.text) + 1)
        self.ids.list89.secondary_text = 'Total Item Price : ' + str(self.sprite * int(self.ids.text89.text))

    def check89(self):
        if self.ids.check89.icon == "checkbox-blank-outline":
            self.ids.check89.icon = 'checkbox-marked'
        else:
            self.ids.check89.icon = "checkbox-blank-outline"

    def minus90(self):
        if self.ids.text90.text == '0':
            self.ids.text90.text = '0'
        else:
            self.ids.text90.text = str(int(self.ids.text90.text) - 1)
            self.ids.list90.secondary_text = 'Total Item Price : ' + str(self.thums_up * int(self.ids.text90.text))

    def plus90(self):
        self.ids.text90.text = str(int(self.ids.text90.text) + 1)
        self.ids.list90.secondary_text = 'Total Item Price : ' + str(self.thums_up * int(self.ids.text90.text))

    def check90(self):
        if self.ids.check90.icon == "checkbox-blank-outline":
            self.ids.check90.icon = 'checkbox-marked'
        else:
            self.ids.check90.icon = "checkbox-blank-outline"

    def minus91(self):
        if self.ids.text91.text == '0':
            self.ids.text91.text = '0'
        else:
            self.ids.text91.text = str(int(self.ids.text91.text) - 1)
            self.ids.list91.secondary_text = 'Total Item Price : ' + str(self.fanta * int(self.ids.text91.text))

    def plus91(self):
        self.ids.text91.text = str(int(self.ids.text91.text) + 1)
        self.ids.list91.secondary_text = 'Total Item Price : ' + str(self.fanta * int(self.ids.text91.text))

    def check91(self):
        if self.ids.check91.icon == "checkbox-blank-outline":
            self.ids.check91.icon = 'checkbox-marked'
        else:
            self.ids.check91.icon = "checkbox-blank-outline"

    def minus92(self):
        if self.ids.text92.text == '0':
            self.ids.text92.text = '0'
        else:
            self.ids.text92.text = str(int(self.ids.text92.text) - 1)
            self.ids.list92.secondary_text = 'Total Item Price : ' + str(self.limka * int(self.ids.text92.text))

    def plus92(self):
        self.ids.text92.text = str(int(self.ids.text92.text) + 1)
        self.ids.list92.secondary_text = 'Total Item Price : ' + str(self.limka * int(self.ids.text92.text))

    def check92(self):
        if self.ids.check92.icon == "checkbox-blank-outline":
            self.ids.check92.icon = 'checkbox-marked'
        else:
            self.ids.check92.icon = "checkbox-blank-outline"

    def minus93(self):
        if self.ids.text93.text == '0':
            self.ids.text93.text = '0'
        else:
            self.ids.text93.text = str(int(self.ids.text93.text) - 1)
            self.ids.list93.secondary_text = 'Total Item Price : ' + str(self.coco_cola * int(self.ids.text93.text))

    def plus93(self):
        self.ids.text93.text = str(int(self.ids.text93.text) + 1)
        self.ids.list93.secondary_text = 'Total Item Price : ' + str(self.coco_cola * int(self.ids.text93.text))

    def check93(self):
        if self.ids.check93.icon == "checkbox-blank-outline":
            self.ids.check93.icon = 'checkbox-marked'
        else:
            self.ids.check93.icon = "checkbox-blank-outline"

    def minus94(self):
        if self.ids.text94.text == '0':
            self.ids.text94.text = '0'
        else:
            self.ids.text94.text = str(int(self.ids.text94.text) - 1)
            self.ids.list94.secondary_text = 'Total Item Price : ' + str(self.mirinda * int(self.ids.text94.text))

    def plus94(self):
        self.ids.text94.text = str(int(self.ids.text94.text) + 1)
        self.ids.list94.secondary_text = 'Total Item Price : ' + str(self.mirinda * int(self.ids.text94.text))

    def check94(self):
        if self.ids.check94.icon == "checkbox-blank-outline":
            self.ids.check94.icon = 'checkbox-marked'
        else:
            self.ids.check9.icon = "checkbox-blank-outline"

    def minus95(self):
        if self.ids.text95.text == '0':
            self.ids.text95.text = '0'
        else:
            self.ids.text95.text = str(int(self.ids.text95.text) - 1)
            self.ids.list95.secondary_text = 'Total Item Price : ' + str(self.mazza * int(self.ids.text95.text))

    def plus95(self):
        self.ids.text95.text = str(int(self.ids.text95.text) + 1)
        self.ids.list95.secondary_text = 'Total Item Price : ' + str(self.mazza * int(self.ids.text95.text))

    def check95(self):
        if self.ids.check95.icon == "checkbox-blank-outline":
            self.ids.check95.icon = 'checkbox-marked'
        else:
            self.ids.check95.icon = "checkbox-blank-outline"

    def minus96(self):
        if self.ids.text96.text == '0':
            self.ids.text96.text = '0'
        else:
            self.ids.text96.text = str(int(self.ids.text96.text) - 1)
            self.ids.list96.secondary_text = 'Total Item Price : ' + str(self.apple_fizz * int(self.ids.text96.text))

    def plus96(self):
        self.ids.text96.text = str(int(self.ids.text96.text) + 1)
        self.ids.list96.secondary_text = 'Total Item Price : ' + str(self.apple_fizz * int(self.ids.text96.text))

    def check96(self):
        if self.ids.check96.icon == "checkbox-blank-outline":
            self.ids.check96.icon = 'checkbox-marked'
        else:
            self.ids.check96.icon = "checkbox-blank-outline"

    def minus97(self):
        if self.ids.text97.text == '0':
            self.ids.text97.text = '0'
        else:
            self.ids.text97.text = str(int(self.ids.text97.text) - 1)
            self.ids.list97.secondary_text = 'Total Item Price : ' + str(self.pulpi_orange * int(self.ids.text97.text))

    def plus97(self):
        self.ids.text97.text = str(int(self.ids.text97.text) + 1)
        self.ids.list97.secondary_text = 'Total Item Price : ' + str(self.pulpi_orange * int(self.ids.text97.text))

    def check97(self):
        if self.ids.check97.icon == "checkbox-blank-outline":
            self.ids.check97.icon = 'checkbox-marked'
        else:
            self.ids.check97.icon = "checkbox-blank-outline"

    def minus98(self):
        if self.ids.text98.text == '0':
            self.ids.text98.text = '0'
        else:
            self.ids.text98.text = str(int(self.ids.text98.text) - 1)
            self.ids.list98.secondary_text = 'Total Item Price : ' + str(self.mountain_due * int(self.ids.text98.text))

    def plus98(self):
        self.ids.text98.text = str(int(self.ids.text98.text) + 1)
        self.ids.list98.secondary_text = 'Total Item Price : ' + str(self.mountain_due * int(self.ids.text98.text))

    def check98(self):
        if self.ids.check98.icon == "checkbox-blank-outline":
            self.ids.check98.icon = 'checkbox-marked'
        else:
            self.ids.check98.icon = "checkbox-blank-outline"

    def minus99(self):
        if self.ids.text99.text == '0':
            self.ids.text99.text = '0'
        else:
            self.ids.text99.text = str(int(self.ids.text99.text) - 1)
            self.ids.list99.secondary_text = 'Total Item Price : ' + str(self.red_bull * int(self.ids.text99.text))

    def plus99(self):
        self.ids.text99.text = str(int(self.ids.text99.text) + 1)
        self.ids.list99.secondary_text = 'Total Item Price : ' + str(self.red_bull * int(self.ids.text99.text))

    def check99(self):
        if self.ids.check99.icon == "checkbox-blank-outline":
            self.ids.check99.icon = 'checkbox-marked'
        else:
            self.ids.check99.icon = "checkbox-blank-outline"

    def minus100(self):
        if self.ids.text100.text == '0':
            self.ids.text100.text = '0'
        else:
            self.ids.text100.text = str(int(self.ids.text100.text) - 1)
            self.ids.list100.secondary_text = 'Total Item Price : ' + str(self.artos * int(self.ids.text100.text))

    def plus100(self):
        self.ids.text100.text = str(int(self.ids.text100.text) + 1)
        self.ids.list100.secondary_text = 'Total Item Price : ' + str(self.artos * int(self.ids.text100.text))

    def check100(self):
        if self.ids.check100.icon == "checkbox-blank-outline":
            self.ids.check100.icon = 'checkbox-marked'
        else:
            self.ids.check100.icon = "checkbox-blank-outline"

    def minus102(self):
        if self.ids.text102.text == '0':
            self.ids.text102.text = '0'
        else:
            self.ids.text102.text = str(int(self.ids.text102.text) - 1)
            self.ids.list102.secondary_text = 'Total Item Price : ' + str(self.dosa * int(self.ids.text102.text))

    def plus102(self):
        self.ids.text102.text = str(int(self.ids.text102.text) + 1)
        self.ids.list102.secondary_text = 'Total Item Price : ' + str(self.dosa * int(self.ids.text102.text))

    def check102(self):
        if self.ids.check102.icon == "checkbox-blank-outline":
            self.ids.check102.icon = 'checkbox-marked'
        else:
            self.ids.check102.icon = "checkbox-blank-outline"

    def minus103(self):
        if self.ids.text103.text == '0':
            self.ids.text103.text = '0'
        else:
            self.ids.text103.text = str(int(self.ids.text103.text) - 1)
            self.ids.list103.secondary_text = 'Total Item Price : ' + str(self.masala_dosa * int(self.ids.text103.text))

    def plus103(self):
        self.ids.text103.text = str(int(self.ids.text103.text) + 1)
        self.ids.list103.secondary_text = 'Total Item Price : ' + str(self.masala_dosa * int(self.ids.text103.text))

    def check103(self):
        if self.ids.check103.icon == "checkbox-blank-outline":
            self.ids.check103.icon = 'checkbox-marked'
        else:
            self.ids.check103.icon = "checkbox-blank-outline"

    def minus104(self):
        if self.ids.text104.text == '0':
            self.ids.text104.text = '0'
        else:
            self.ids.text104.text = str(int(self.ids.text104.text) - 1)
            self.ids.list104.secondary_text = 'Total Item Price : ' + str(self.onion_dosa * int(self.ids.text104.text))

    def plus104(self):
        self.ids.text104.text = str(int(self.ids.text104.text) + 1)
        self.ids.list104.secondary_text = 'Total Item Price : ' + str(self.onion_dosa * int(self.ids.text104.text))

    def check104(self):
        if self.ids.check104.icon == "checkbox-blank-outline":
            self.ids.check104.icon = 'checkbox-marked'
        else:
            self.ids.check104.icon = "checkbox-blank-outline"

    def minus105(self):
        if self.ids.text105.text == '0':
            self.ids.text105.text = '0'
        else:
            self.ids.text105.text = str(int(self.ids.text105.text) - 1)
            self.ids.list105.secondary_text = 'Total Item Price : ' + str(self.egg_dosa * int(self.ids.text105.text))

    def plus105(self):
        self.ids.text105.text = str(int(self.ids.text105.text) + 1)
        self.ids.list105.secondary_text = 'Total Item Price : ' + str(self.egg_dosa * int(self.ids.text105.text))

    def check105(self):
        if self.ids.check105.icon == "checkbox-blank-outline":
            self.ids.check105.icon = 'checkbox-marked'
        else:
            self.ids.check105.icon = "checkbox-blank-outline"

    def minus106(self):
        if self.ids.text106.text == '0':
            self.ids.text106.text = '0'
        else:
            self.ids.text106.text = str(int(self.ids.text106.text) - 1)
            self.ids.list106.secondary_text = 'Total Item Price : ' + str(self.idly * int(self.ids.text106.text))

    def plus106(self):
        self.ids.text106.text = str(int(self.ids.text106.text) + 1)
        self.ids.list106.secondary_text = 'Total Item Price : ' + str(self.idly * int(self.ids.text106.text))

    def check106(self):
        if self.ids.check106.icon == "checkbox-blank-outline":
            self.ids.check106.icon = 'checkbox-marked'
        else:
            self.ids.check106.icon = "checkbox-blank-outline"

    def minus107(self):
        if self.ids.text107.text == '0':
            self.ids.text10.text = '0'
        else:
            self.ids.text107.text = str(int(self.ids.text107.text) - 1)
            self.ids.list107.secondary_text = 'Total Item Price : ' + str(self.ghee_idly * int(self.ids.text107.text))

    def plus107(self):
        self.ids.text107.text = str(int(self.ids.text107.text) + 1)
        self.ids.list107.secondary_text = 'Total Item Price : ' + str(self.ghee_idly * int(self.ids.text107.text))

    def check107(self):
        if self.ids.check107.icon == "checkbox-blank-outline":
            self.ids.check107.icon = 'checkbox-marked'
        else:
            self.ids.check107.icon = "checkbox-blank-outline"

    def minus108(self):
        if self.ids.text108.text == '0':
            self.ids.text108.text = '0'
        else:
            self.ids.text108.text = str(int(self.ids.text108.text) - 1)
            self.ids.list108.secondary_text = 'Total Item Price : ' + str(self.sambar_idly * int(self.ids.text108.text))

    def plus108(self):
        self.ids.text108.text = str(int(self.ids.text108.text) + 1)
        self.ids.list108.secondary_text = 'Total Item Price : ' + str(self.sambar_idly * int(self.ids.text108.text))

    def check108(self):
        if self.ids.check108.icon == "checkbox-blank-outline":
            self.ids.check108.icon = 'checkbox-marked'
        else:
            self.ids.check108.icon = "checkbox-blank-outline"

    def minus109(self):
        if self.ids.text109.text == '0':
            self.ids.text109.text = '0'
        else:
            self.ids.text109.text = str(int(self.ids.text109.text) - 1)
            self.ids.list109.secondary_text = 'Total Item Price : ' + str(self.vada * int(self.ids.text109.text))

    def plus109(self):
        self.ids.text109.text = str(int(self.ids.text109.text) + 1)
        self.ids.list109.secondary_text = 'Total Item Price : ' + str(self.vada * int(self.ids.text109.text))

    def check109(self):
        if self.ids.check109.icon == "checkbox-blank-outline":
            self.ids.check109.icon = 'checkbox-marked'
        else:
            self.ids.check109.icon = "checkbox-blank-outline"

    def minus110(self):
        if self.ids.text110.text == '0':
            self.ids.text110.text = '0'
        else:
            self.ids.text110.text = str(int(self.ids.text110.text) - 1)
            self.ids.list110.secondary_text = 'Total Item Price : ' + str(
                self.mysore_bonda * int(self.ids.text110.text))

    def plus110(self):
        self.ids.text110.text = str(int(self.ids.text110.text) + 1)
        self.ids.list110.secondary_text = 'Total Item Price : ' + str(self.mysore_bonda * int(self.ids.text110.text))

    def check110(self):
        if self.ids.check110.icon == "checkbox-blank-outline":
            self.ids.check110.icon = 'checkbox-marked'
        else:
            self.ids.check110.icon = "checkbox-blank-outline"

    def minus111(self):
        if self.ids.text111.text == '0':
            self.ids.text111.text = '0'
        else:
            self.ids.text111.text = str(int(self.ids.text111.text) - 1)
            self.ids.list111.secondary_text = 'Total Item Price : ' + str(self.upma * int(self.ids.text111.text))

    def plus111(self):
        self.ids.text111.text = str(int(self.ids.text111.text) + 1)
        self.ids.list111.secondary_text = 'Total Item Price : ' + str(self.upma * int(self.ids.text111.text))

    def check111(self):
        if self.ids.check111.icon == "checkbox-blank-outline":
            self.ids.check111.icon = 'checkbox-marked'
        else:
            self.ids.check111.icon = "checkbox-blank-outline"

    def minus112(self):
        if self.ids.text112.text == '0':
            self.ids.text112.text = '0'
        else:
            self.ids.text112.text = str(int(self.ids.text112.text) - 1)
            self.ids.list112.secondary_text = 'Total Item Price : ' + str(self.chapati * int(self.ids.text112.text))

    def plus112(self):
        self.ids.text112.text = str(int(self.ids.text112.text) + 1)
        self.ids.list112.secondary_text = 'Total Item Price : ' + str(self.chapati * int(self.ids.text112.text))

    def check112(self):
        if self.ids.check112.icon == "checkbox-blank-outline":
            self.ids.check112.icon = 'checkbox-marked'
        else:
            self.ids.check112.icon = "checkbox-blank-outline"

    def minus113(self):
        if self.ids.text113.text == '0':
            self.ids.text113.text = '0'
        else:
            self.ids.text113.text = str(int(self.ids.text113.text) - 1)
            self.ids.list113.secondary_text = 'Total Item Price : ' + str(self.puri * int(self.ids.text113.text))

    def plus113(self):
        self.ids.text113.text = str(int(self.ids.text113.text) + 1)
        self.ids.list113.secondary_text = 'Total Item Price : ' + str(self.puri * int(self.ids.text113.text))

    def check113(self):
        if self.ids.check113.icon == "checkbox-blank-outline":
            self.ids.check113.icon = 'checkbox-marked'
        else:
            self.ids.check113.icon = "checkbox-blank-outline"

    def minus114(self):
        if self.ids.text114.text == '0':
            self.ids.text114.text = '0'
        else:
            self.ids.text114.text = str(int(self.ids.text114.text) - 1)
            self.ids.list114.secondary_text = 'Total Item Price : ' + str(self.parota * int(self.ids.text114.text))

    def plus114(self):
        self.ids.text114.text = str(int(self.ids.text114.text) + 1)
        self.ids.list114.secondary_text = 'Total Item Price : ' + str(self.parota * int(self.ids.text114.text))

    def check114(self):
        if self.ids.check114.icon == "checkbox-blank-outline":
            self.ids.check114.icon = 'checkbox-marked'
        else:
            self.ids.check114.icon = "checkbox-blank-outline"

    def minus115(self):
        if self.ids.text115.text == '0':
            self.ids.text115.text = '0'
        else:
            self.ids.text115.text = str(int(self.ids.text115.text) - 1)
            self.ids.list115.secondary_text = 'Total Item Price : ' + str(
                self.palli_chutney * int(self.ids.text115.text))

    def plus115(self):
        self.ids.text115.text = str(int(self.ids.text115.text) + 1)
        self.ids.list115.secondary_text = 'Total Item Price : ' + str(self.palli_chutney * int(self.ids.text115.text))

    def check115(self):
        if self.ids.check115.icon == "checkbox-blank-outline":
            self.ids.check115.icon = 'checkbox-marked'
        else:
            self.ids.check115.icon = "checkbox-blank-outline"

    def minus116(self):
        if self.ids.text116.text == '0':
            self.ids.text116.text = '0'
        else:
            self.ids.text116.text = str(int(self.ids.text116.text) - 1)
            self.ids.list116.secondary_text = 'Total Item Price : ' + str(self.red_chutney * int(self.ids.text116.text))

    def plus116(self):
        self.ids.text116.text = str(int(self.ids.text116.text) + 1)
        self.ids.list116.secondary_text = 'Total Item Price : ' + str(self.red_chutney * int(self.ids.text116.text))

    def check116(self):
        if self.ids.check116.icon == "checkbox-blank-outline":
            self.ids.check116.icon = 'checkbox-marked'
        else:
            self.ids.check116.icon = "checkbox-blank-outline"

    def minus117(self):
        if self.ids.text117.text == '0':
            self.ids.text117.text = '0'
        else:
            self.ids.text117.text = str(int(self.ids.text117.text) - 1)
            self.ids.list117.secondary_text = 'Total Item Price : ' + str(
                self.green_chutney * int(self.ids.text117.text))

    def plus117(self):
        self.ids.text117.text = str(int(self.ids.text117.text) + 1)
        self.ids.list117.secondary_text = 'Total Item Price : ' + str(self.green_chutney * int(self.ids.text117.text))

    def check117(self):
        if self.ids.check117.icon == "checkbox-blank-outline":
            self.ids.check117.icon = 'checkbox-marked'
        else:
            self.ids.check117.icon = "checkbox-blank-outline"

    def minus118(self):
        if self.ids.text118.text == '0':
            self.ids.text118.text = '0'
        else:
            self.ids.text118.text = str(int(self.ids.text118.text) - 1)
            self.ids.list118.secondary_text = 'Total Item Price : ' + str(self.allu_kurma * int(self.ids.text118.text))

    def plus118(self):
        self.ids.text118.text = str(int(self.ids.text118.text) + 1)
        self.ids.list118.secondary_text = 'Total Item Price : ' + str(self.allu_kurma * int(self.ids.text118.text))

    def check118(self):
        if self.ids.check118.icon == "checkbox-blank-outline":
            self.ids.check118.icon = 'checkbox-marked'
        else:
            self.ids.check118.icon = "checkbox-blank-outline"

    def minus119(self):
        if self.ids.text119.text == '0':
            self.ids.text119.text = '0'
        else:
            self.ids.text119.text = str(int(self.ids.text119.text) - 1)
            self.ids.list119.secondary_text = 'Total Item Price : ' + str(self.puri_curry * int(self.ids.text119.text))

    def plus119(self):
        self.ids.text119.text = str(int(self.ids.text119.text) + 1)
        self.ids.list119.secondary_text = 'Total Item Price : ' + str(self.puri_curry * int(self.ids.text119.text))

    def check119(self):
        if self.ids.check119.icon == "checkbox-blank-outline":
            self.ids.check119.icon = 'checkbox-marked'
        else:
            self.ids.check119.icon = "checkbox-blank-outline"

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
        date_label = self.ids.date
        date_label.text = f"{value}"

    def show_time_picker1(self):
        time_picker = MDTimePicker()
        time_picker.bind(on_save=self.on_time_selected)
        time_picker.open()

    def on_time_selected(self, instance, time):
        time_label = self.ids.time
        time_label.text = f"{time.strftime('%H:%M')}"

    def event_list_click(self):
        self.manager.current = "success"

    def create_events(self, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13):
        data = app_tables.create_event_table.search()
        id_list = []
        for i in data:
            id_list.append(i['event_id'])

        if len(id_list) == 0:
            event_id = 'EventID:100000'
        else:
            num =  int(id_list[-1].split(':')[-1]) + 1
            event_id = f'EventID:{num}'
        app_tables.create_event_table.add_row(customer_name=value1 + " " + value2, customer_email=value3,
                                              customer_numer=int(value4), expecting_guests=value5,
                                              event_type=value6, event_hosting_type=value7, no_of_guests=int(value8),
                                              customer_budget=int(value9),
                                              event_date=value10, event_time=value11, vanue_place=value12,
                                              other_details=value13, event_id=event_id)

class GuestInvitation(Screen):
    def gust_list_click(self):
        self.manager.current = "EventPlanning"
