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
                                TwoLineAvatarIconListItem:
                                    text: "One-line "
                                    secondary_text: "Price"
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
                               
                                TwoLineAvatarIconListItem:
                                    text: "Lemon Rice"
                                    secondary_text: "Price"
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
                                            
                                TwoLineAvatarIconListItem:
                                    text: "Tomato Rice"
                                    secondary_text: "Price"
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
                                            
                                TwoLineAvatarIconListItem:
                                    text: "Brown Rice"
                                    secondary_text: "Price"
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
                                    
                                TwoLineAvatarIconListItem:
                                    text: "Zeera Rice(Jilakarra Rice)"
                                    secondary_text: "Price"
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
                                    
                                TwoLineAvatarIconListItem:
                                    text: "Veg Biryani"
                                    secondary_text: "Price"
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
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Dal"
                                ListItemWithCheckbox:
                                    text: "Brinjal Curry"
                                ListItemWithCheckbox:
                                    text: "Potato Curry (Aloo Curry)"
                                ListItemWithCheckbox:
                                    text: "Potato Fry "
                                ListItemWithCheckbox:
                                    text: "Ladies Finger Curry(Bhendakai)"
                                ListItemWithCheckbox:
                                    text: "Sambar"
                                ListItemWithCheckbox:
                                    text: "Rasam"
                                ListItemWithCheckbox:
                                    text: " Mustroom Curry "
                                ListItemWithCheckbox:
                                    text: "Kajju Panner Curry"
                                ListItemWithCheckbox:
                                    text: "DrumStick Curry (Mulakai)"
                                ListItemWithCheckbox:
                                    text: "Beams Curry"
                                ListItemWithCheckbox:
                                    text: "Peas Curry"
                                ListItemWithCheckbox:
                                    text: "Tomato Curry"
                                ListItemWithCheckbox:
                                    text: " Cabbage Curry "
                                ListItemWithCheckbox:
                                    text: "Cauliflower Curry"
                                ListItemWithCheckbox:
                                    text: "avakaya chutney"
                            
                            MDLabel:
                                text: "Veg-FastFood Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Veg Fried Rice"   
                                ListItemWithCheckbox:
                                    text: "Veg Noodles" 
                                ListItemWithCheckbox:
                                    text: "Veg Manchuria" 
                                ListItemWithCheckbox:
                                    text: "Manchuria Rice(Gobi Rice)" 
                                ListItemWithCheckbox:
                                    text: "Manchuria Noodles (Gobi Noodles)" 
          
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
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Chicken Biryani"   
                                ListItemWithCheckbox:
                                    text: "Chicken Fried-Biryani " 
                                ListItemWithCheckbox:
                                    text: "Chicken Dum-Biryani" 
                                ListItemWithCheckbox:
                                    text: "Mutton Biryani" 
                                ListItemWithCheckbox:
                                    text: "Mutton Fry-Biryani" 
                                ListItemWithCheckbox:
                                    text: "Prawns Biryani" 
                                ListItemWithCheckbox:
                                    text: "Normal Rice" 
                            MDLabel:
                                text: "Non-veg Curry Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)
                            MDList:
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Chicken Fry"   
                                ListItemWithCheckbox:
                                    text: "Chicken Curry" 
                                ListItemWithCheckbox:
                                    text: "Chicken 65" 
                                ListItemWithCheckbox:
                                    text: "Gongura chicken Curry" 
                                ListItemWithCheckbox:
                                    text: "Mutton Fry" 
                                ListItemWithCheckbox:
                                    text: "Mutton Curry" 
                                ListItemWithCheckbox:
                                    text: "Gongura Mutton Curry" 
                                ListItemWithCheckbox:
                                    text: "Fish Fry" 
                                ListItemWithCheckbox:
                                    text: "Fish Curry" 
                                ListItemWithCheckbox:
                                    text: "Prawns Fry" 
                                ListItemWithCheckbox:
                                    text: "Prawns Curry" 
                                ListItemWithCheckbox:
                                    text: "Crabs curry" 
                                ListItemWithCheckbox:
                                    text: "Egg Curry" 
                                ListItemWithCheckbox:
                                    text: "Egg omlete" 
                                ListItemWithCheckbox:
                                    text: "Egg roll"        
                                ListItemWithCheckbox:
                                    text: "Chicken roll" 
                                ListItemWithCheckbox:
                                    text: "Chicken Wings" 
                                ListItemWithCheckbox:
                                    text: "Chicken Leg-peaces" 
                                ListItemWithCheckbox:
                                    text: "Botii Curry" 
                            MDLabel:
                                text: "Non-Veg FastFood Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Chicken Fried Rice"   
                                ListItemWithCheckbox:
                                    text: "Chicken Noodles" 
                                ListItemWithCheckbox:
                                    text: "chilli chicken" 
                                ListItemWithCheckbox:
                                    text: "Egg Noodles" 
                                ListItemWithCheckbox:
                                    text: "Egg Manchuria" 
                                ListItemWithCheckbox:
                                    text: "Manchuria Egg Rice" 
                                ListItemWithCheckbox:
                                    text: "Manchuria Egg Noodles"  
                            MDLabel:
                                text: "Roti Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Butter non"   
                                ListItemWithCheckbox:
                                    text: "Tawa roti" 
                                ListItemWithCheckbox:
                                    text: "Rumalli roti" 
                                ListItemWithCheckbox:
                                    text: "Makki roti" 
                                ListItemWithCheckbox:
                                    text: "Parota" 
                                ListItemWithCheckbox:
                                    text: "Sada Roti" 
                                        
                            MDLabel:
                                text: "curry For Roti Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)         
                            ListItemWithCheckbox:
                                text: "Egg Keema" 
                            ListItemWithCheckbox:
                                text: "Egg Bhurji" 
                            ListItemWithCheckbox:
                                text: "Butter chicken" 
                            ListItemWithCheckbox:
                                text: "Afgani chicken" 
                            ListItemWithCheckbox:
                                text: "Kajju curry" 
                            ListItemWithCheckbox:
                                text: "Paneer Butter masala"                 
                        
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
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Gulab Jamun"   
                                ListItemWithCheckbox:
                                    text: "Gajar ka Halwa (Carrot Halwa)" 
                                ListItemWithCheckbox:
                                    text: "Ras Malai (Cottage Cheese Balls in Clotted Cream)" 
                                ListItemWithCheckbox:
                                    text: "Besan Ladoo (Roasted Gram Flour Balls)" 
                                ListItemWithCheckbox:
                                    text: "Kalakand" 
                                ListItemWithCheckbox:
                                    text: "Peanut Chikki (Peanut Brittle)" 
                                ListItemWithCheckbox:
                                    text: "Jalebi" 
                                ListItemWithCheckbox:
                                    text: "Soan Papdi" 
                                ListItemWithCheckbox:
                                    text: "Rice Kheer(Payasam)" 
                                    
                            MDLabel:
                                text: "Hot Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Masala Peanuts"   
                                ListItemWithCheckbox:
                                    text: "Samosa" 
                                ListItemWithCheckbox:
                                    text: "Onion Pakodi" 
                                ListItemWithCheckbox:
                                    text: "Baggi" 
                                ListItemWithCheckbox:
                                    text: "Mixter" 
                                ListItemWithCheckbox:
                                    text: "Vada Pav" 
                                ListItemWithCheckbox:
                                    text: "Panipuri" 
                                
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
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Sprite"   
                                ListItemWithCheckbox:
                                    text: "Thumps up" 
                                ListItemWithCheckbox:
                                    text: "Fanta" 
                                ListItemWithCheckbox:
                                    text: "Limka" 
                                ListItemWithCheckbox:
                                    text: "coco-cola" 
                                ListItemWithCheckbox:
                                    text: "Mirinda" 
                                ListItemWithCheckbox:
                                    text: "Mazza" 
                                ListItemWithCheckbox:
                                    text: "Apple Fizz" 
                                ListItemWithCheckbox:
                                    text: "pulpi-orange" 
                                ListItemWithCheckbox:
                                    text: "Mountaine Dew" 
                                ListItemWithCheckbox:
                                    text: "Red bull" 
                                ListItemWithCheckbox:
                                    text: "Artos"                    
                                
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
                                id: container1
                                ListItemWithCheckbox:
                                    text: "Dosa"   
                                ListItemWithCheckbox:
                                    text: "Masala Dosa" 
                                ListItemWithCheckbox:
                                    text: "onion Dosa" 
                                ListItemWithCheckbox:
                                    text: "Egg Dosa" 
                                ListItemWithCheckbox:
                                    text: "Idly" 
                                ListItemWithCheckbox:
                                    text: "Ghee Idly" 
                                ListItemWithCheckbox:
                                    text: "sambar Idly" 
                                ListItemWithCheckbox:
                                    text: "vada" 
                                ListItemWithCheckbox:
                                    text: "Mysore Bonda" 
                                ListItemWithCheckbox:
                                    text: "Upma" 
                                ListItemWithCheckbox:
                                    text: "chapati" 
                                ListItemWithCheckbox:
                                    text: "puri" 
                                ListItemWithCheckbox:
                                    text: "Porota" 
                            
                            MDLabel:
                                text: "Chatny Items: "
                                size_hint_y: None
                                height: dp(50)
                                bold: True
                                haligh: 'center'
                                padding: dp(15)        
                            MDList:
                                ListItemWithCheckbox:
                                    text: "Palli chutney" 
                                ListItemWithCheckbox:
                                    text: "red chutney"        
                                ListItemWithCheckbox:
                                    text: "Green Chutney" 
                                ListItemWithCheckbox:
                                    text: "Allu kurma curry" 
                                ListItemWithCheckbox:
                                    text: "Puri curry" 
                                
                
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

    def minus1(self):
        if self.ids.text1.text == '0':
            self.ids.text1.text = '0'
        else:
            self.ids.text1.text = str(int(self.ids.text1.text) -1)
    def plus1(self):
        self.ids.text1.text = str(int(self.ids.text1.text) +1)
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
    def plus2(self):
        self.ids.text2.text = str(int(self.ids.text2.text) +1)
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
    def plus3(self):
        self.ids.text3.text = str(int(self.ids.text3.text) +1)
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
    def plus4(self):
        self.ids.text4.text = str(int(self.ids.text4.text) +1)
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
    def plus5(self):
        self.ids.text5.text = str(int(self.ids.text5.text) +1)
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
    def plus6(self):
        self.ids.text6.text = str(int(self.ids.text6.text) +1)
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



