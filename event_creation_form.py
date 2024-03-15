import sqlite3

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
                                ThreeLineAvatarIconListItem:
                                    id: list8
                                    text: "Brinjal Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list9
                                    text: "Potato Curry (Aloo Curry)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list10
                                    text: "Potato Fry "
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
                                ThreeLineAvatarIconListItem:
                                    id: list11
                                    text: "Ladies Finger Curry(Bhendakai)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list12
                                    text: "Sambar"
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
                                ThreeLineAvatarIconListItem:
                                    id: list13
                                    text: "Rasam"
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
                                ThreeLineAvatarIconListItem:
                                    id: list14
                                    text: "Mustroom Curry "
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
                                ThreeLineAvatarIconListItem:
                                    id: list15
                                    text: "Kajju Panner Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list16
                                    text: "DrumStick Curry (Mulakai)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list17
                                    text: "Beams Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list18
                                    text: "Peas Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list19
                                    text: "Tomato Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list20
                                    text: "Cabbage Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list21
                                    text: "Cauliflower Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list22
                                    text: "avakaya chutney"
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
                                ThreeLineAvatarIconListItem:
                                    id: list24
                                    text: "Veg Noodles"
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
                                ThreeLineAvatarIconListItem:
                                    id: list25
                                    text: "Veg Manchuria"
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
                                ThreeLineAvatarIconListItem:
                                    id: list26
                                    text: "Manchuria Rice(Gobi Rice)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list27
                                    text: "Manchuria Noodles (Gobi Noodles)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list29
                                    text: "Chicken Fried-Biryani"
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
                                ThreeLineAvatarIconListItem:
                                    id: list30
                                    text: "Chicken Dum-Biryani"
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
                                ThreeLineAvatarIconListItem:
                                    id: list31
                                    text: "Mutton Biryani"
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
                                ThreeLineAvatarIconListItem:
                                    id: list32
                                    text: "Mutton Fry-Biryani"
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
                                ThreeLineAvatarIconListItem:
                                    id: list33
                                    text: "Prawns Biryani"
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
                                ThreeLineAvatarIconListItem:
                                    id: list34
                                    text: "Normal Rice"
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
                                ThreeLineAvatarIconListItem:
                                    id: list36
                                    text: "Chicken Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list37
                                    text: "Chicken 65"
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
                                ThreeLineAvatarIconListItem:
                                    id: list38
                                    text: "Gongura chicken Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list39
                                    text: "Mutton Fry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list40
                                    text: "Mutton Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list41
                                    text: "Gongura Mutton Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list42
                                    text: "Fish Fry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list43
                                    text: "Fish Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list44
                                    text: "Prawns Fry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list45
                                    text: "Prawns Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list46
                                    text: "Crabs curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list47
                                    text: "Egg Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list48
                                    text: "Egg omlete"
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
                                ThreeLineAvatarIconListItem:
                                    id: list49
                                    text: "Egg roll"
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
                                ThreeLineAvatarIconListItem:
                                    id: list50
                                    text: "Chicken roll"
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
                                ThreeLineAvatarIconListItem:
                                    id: list51
                                    text: "Chicken Wings"
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
                                ThreeLineAvatarIconListItem:
                                    id: list52
                                    text: "Chicken Leg-peaces"
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
                                ThreeLineAvatarIconListItem:
                                    id: list53
                                    text: "Botii Curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list55
                                    text: "Chicken Noodles"
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
                                ThreeLineAvatarIconListItem:
                                    id: list56
                                    text: "chilli chicken"
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
                                ThreeLineAvatarIconListItem:
                                    id: list57
                                    text: "Egg Noodles"
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
                                ThreeLineAvatarIconListItem:
                                    id: list58
                                    text: "Egg Manchuria"
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
                                ThreeLineAvatarIconListItem:
                                    id: list59
                                    text: "Manchuria Egg Rice"
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
                                ThreeLineAvatarIconListItem:
                                    id: list60
                                    text: "Manchuria Egg Noodles"
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
                                ThreeLineAvatarIconListItem:
                                    id: list62
                                    text: "Tawa roti"
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
                                ThreeLineAvatarIconListItem:
                                    id: list63
                                    text: "Rumalli roti"
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
                                ThreeLineAvatarIconListItem:
                                    id: list64
                                    text: "Makki roti"
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
                                ThreeLineAvatarIconListItem:
                                    id: list65
                                    text: "Parota"
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
                                ThreeLineAvatarIconListItem:
                                    id: list66
                                    text: "Sada Roti"
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
                            ThreeLineAvatarIconListItem:
                                id: list68
                                text: "Egg Bhurji"
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
                            ThreeLineAvatarIconListItem:
                                id: list69
                                text: "Butter chicken"
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
                            ThreeLineAvatarIconListItem:
                                id: list70
                                text: "Afgani chicken"
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
                            ThreeLineAvatarIconListItem:
                                id: list71
                                text: "Kajju curry"
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
                            ThreeLineAvatarIconListItem:
                                id: list72
                                text: "Paneer Butter masala"
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
                                ThreeLineAvatarIconListItem:
                                    id: list74
                                    text: "Gajar ka Halwa (Carrot Halwa)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list75
                                    text: "Ras Malai (Cottage Cheese Balls in Clotted Cream)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list76
                                    text: "Besan Ladoo (Roasted Gram Flour Balls)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list77
                                    text: "Kalakand"
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
                                ThreeLineAvatarIconListItem:
                                    id: list78
                                    text: "Peanut Chikki (Peanut Brittle)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list79
                                    text: "Jalebi"
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
                                ThreeLineAvatarIconListItem:
                                    id: list80
                                    text: "Soan Papdi"
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
                                ThreeLineAvatarIconListItem:
                                    id: list81
                                    text: "Rice Kheer(Payasam)"
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
                                ThreeLineAvatarIconListItem:
                                    id: list83
                                    text: "Samosa"
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
                                ThreeLineAvatarIconListItem:
                                    id: list84
                                    text: "Onion Pakodi"
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
                                ThreeLineAvatarIconListItem:
                                    id: list85
                                    text: "Baggi"
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
                                ThreeLineAvatarIconListItem:
                                    id: list86
                                    text: "Mixter"
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
                                ThreeLineAvatarIconListItem:
                                    id: list87
                                    text: "Vada Pav"
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
                                ThreeLineAvatarIconListItem:
                                    id: list88
                                    text: "Panipuri"
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
                                ThreeLineAvatarIconListItem:
                                    id: list90
                                    text: "Thumps up"
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
                                ThreeLineAvatarIconListItem:
                                    id: list91
                                    text: "Fanta"
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
                                ThreeLineAvatarIconListItem:
                                    id: list92
                                    text: "Limka"
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
                                ThreeLineAvatarIconListItem:
                                    id: list93
                                    text: "coco-cola"
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
                                ThreeLineAvatarIconListItem:
                                    id: list94
                                    text: "Mirinda"
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
                                ThreeLineAvatarIconListItem:
                                    id: list95
                                    text: "Mazza"
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
                                ThreeLineAvatarIconListItem:
                                    id: list96
                                    text: "Apple Fizz"
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
                                ThreeLineAvatarIconListItem:
                                    id: list97
                                    text: "pulpi-orange"
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
                                ThreeLineAvatarIconListItem:
                                    id: list98
                                    text: "Mountaine Dew"
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
                                ThreeLineAvatarIconListItem:
                                    id: list99
                                    text: "Red bull"
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
                                ThreeLineAvatarIconListItem:
                                    id: list101
                                    text: "Artos"
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
                                ThreeLineAvatarIconListItem:
                                    id: list103
                                    text: "Masala Dosa"
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
                                ThreeLineAvatarIconListItem:
                                    id: list104
                                    text: "onion Dosa"
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
                                ThreeLineAvatarIconListItem:
                                    id: list105
                                    text: "Egg Dosa"
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
                                ThreeLineAvatarIconListItem:
                                    id: list106
                                    text: "Idly"
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
                                ThreeLineAvatarIconListItem:
                                    id: list107
                                    text: "Ghee Idly"
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
                                ThreeLineAvatarIconListItem:
                                    id: list108
                                    text: "sambar Idly"
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
                                ThreeLineAvatarIconListItem:
                                    id: list109
                                    text: "vada"
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
                                ThreeLineAvatarIconListItem:
                                    id: list110
                                    text: "Mysore Bonda"
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
                                ThreeLineAvatarIconListItem:
                                    id: list111
                                    text: "Upma"
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
                                ThreeLineAvatarIconListItem:
                                    id: list112
                                    text: "chapati"
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
                                ThreeLineAvatarIconListItem:
                                    id: list113
                                    text: "puri"
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
                                ThreeLineAvatarIconListItem:
                                    id: list114
                                    text: "Porota"
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
                                ThreeLineAvatarIconListItem:
                                    id: list116
                                    text: "red chutney"
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
                                ThreeLineAvatarIconListItem:
                                    id: list117
                                    text: "Green Chutney"
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
                                ThreeLineAvatarIconListItem:
                                    id: list118
                                    text: "Allu kurma curry"
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
                                ThreeLineAvatarIconListItem:
                                    id: list119
                                    text: "Puri curry"
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
        self.ids.text2.text = '0'
        self.ids.text3.text = '0'
        self.ids.text4.text = '0'
        self.ids.text5.text = '0'
        self.ids.text6.text = '0'
        self.white_rice = 30
        self.tomato_rice = 60
        self.lemon_rice = 60
        self.brown_rice = 60
        self.zeera_rice = 60
        self.veg_biryani = 100

    def minus1(self):
        if self.ids.text1.text == '0':
            self.ids.text1.text = '0'
        else:
            self.ids.text1.text = str(int(self.ids.text1.text) -1)
            self.ids.list1.secondary_text = 'Total Item Price : ' + str(self.white_rice * int(self.ids.text1.text))
    def plus1(self):
        self.ids.text1.text = str(int(self.ids.text1.text) +1)
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
            self.ids.text2.text = str(int(self.ids.text2.text) -1)
            self.ids.list2.secondary_text = 'Total Item Price : ' + str(self.lemon_rice * int(self.ids.text2.text))
    def plus2(self):
        self.ids.text2.text = str(int(self.ids.text2.text) +1)
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
            self.ids.text3.text = str(int(self.ids.text3.text) -1)
            self.ids.list3.secondary_text = 'Total Item Price : ' + str(self.tomato_rice * int(self.ids.text3.text))
    def plus3(self):
        self.ids.text3.text = str(int(self.ids.text3.text) +1)
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
            self.ids.text4.text = str(int(self.ids.text4.text) -1)
            self.ids.list4.secondary_text = 'Total Item Price : ' + str(self.brown_rice * int(self.ids.text4.text))
    def plus4(self):
        self.ids.text4.text = str(int(self.ids.text4.text) +1)
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
            self.ids.text5.text = str(int(self.ids.text5.text) -1)
            self.ids.list5.secondary_text = 'Total Item Price : ' + str(self.zeera_rice * int(self.ids.text5.text))
    def plus5(self):
        self.ids.text5.text = str(int(self.ids.text5.text) +1)
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
            self.ids.text6.text = str(int(self.ids.text6.text) -1)
            self.ids.list6.secondary_text = 'Total Item Price : ' + str(self.veg_biryani * int(self.ids.text6.text))
    def plus6(self):
        self.ids.text6.text = str(int(self.ids.text6.text) +1)
        self.ids.list6.secondary_text = 'Total Item Price : ' + str(self.veg_biryani * int(self.ids.text6.text))
    def check6(self):
        if self.ids.check6.icon == "checkbox-blank-outline":
            self.ids.check6.icon = 'checkbox-marked'
        else:
            self.ids.check6.icon = "checkbox-blank-outline"
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
