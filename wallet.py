import sqlite3

from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

KV = '''
<EventWallet>
    MDTopAppBar:
        pos_hint: {'top': 1}
        elevation: 2

        BoxLayout:
            orientation: 'horizontal'

            MDIconButton:
                icon: 'arrow-left'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "Event Wallet"
                font_size: dp(20)
                theme_text_color: "Primary"
                halign: 'left'
                valign: 'middle'
                size_hint_y: None
                height: dp(46)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                bold: True

            MDIconButton:
                icon: 'help-circle-outline'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(2)
            padding: dp(20)  
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

            MDLabel:
                text: 'Welcome Back To Event Wallet'
                halign: 'center'
                font_size: "20dp"
                font_name: "Roboto-Bold"
            MDIcon:
                icon: "shield-lock"
                theme_text_color: "Custom"
                text_color: 245/255, 206/255, 78/255, 1
                pos_hint: {"center_x": 0.5, "top": 1} 
                font_size: dp(50)
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(20)

            MDLabel:
                text: "Please DO NOT expose to strangers. We do not have access to your password, and WILL NOT be able to restore it."
                halign: 'center'

            MDFloatLayout:
                MDTextField:
                    id: Wallet
                    hint_text: "Wallet Password"
                    password: True
                    helper_text: "Enter your password"
                    helper_text_mode: "on_focus"
                    icon_left: "lock"
                    pos_hint: {"center_x": 0.5, "top": 1}   

                MDIconButton:
                    id: icon1
                    icon: 'eye'
                    pos_hint: {"right": 1, "top": 1}
                    on_release: root.password_change()
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Continue"
                    md_bg_color: 50/255, 51/255, 59/255, 1 
                    pos_hint: {'right': 1, 'y': 0.5}
                    on_release: app.root.current = 'ActivateWallet'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 
<ActivateWallet>
    MDTopAppBar:
        pos_hint: {'top': 1}
        elevation: 2

        BoxLayout:
            orientation: 'horizontal'

            MDIconButton:
                icon: 'arrow-left'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "Event Wallet"
                font_size: dp(20)
                theme_text_color: "Primary"
                halign: 'left'
                valign: 'middle'
                size_hint_y: None
                height: dp(46)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                bold: True

            MDIconButton:
                icon: 'help-circle-outline'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(30)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(30)
            padding: dp(30)
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 # Dull background color
                Line:
                    width: 0.7  # Border width
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(50)
            MDIcon:
                icon: "wallet-plus-outline"
                theme_text_color: "Custom"
                text_color: 60/255, 3/255, 166/255, 1
                pos_hint: {"center_x": 0.5, "top": 1} 
                font_size: dp(50)
            MDLabel:
                text:"Balance:"
                size_hint_y: None
                height:dp(20)
                halign: 'center'

            MDFillRoundFlatIconButton:
                text: "0"
                font_size: dp(22)
                text_color: 60/255, 3/255, 166/255, 1 
                icon: "currency-inr"
                icon_color: 60/255, 3/255, 166/255, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 1, 1, 1, 1      
            Widget:
                size_hint_y: None
                height: dp(2) 
                canvas:
                    Color:
                        rgba: 0, 0, 1, 1
                    Line:
                        width: dp(0.6)  # Set the width of the line to make it bold
                        points: self.x, self.y, self.x + self.width, self.y

            MDLabel:
                text:"Activate Your Wallet"
                size_hint_y: None
                height:dp(10)
                bold: True
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(15)
            MDLabel:
                text:"Your Wallet has been inactive for the last 12 months.Upgrade to the New Event Wallet by activating.Terms and conditions apply."
                size_hint_y: None
                height:dp(10)
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(5)
            GridLayout:
                cols: 1
                spacing:dp(30)
                padding: [0, "30dp", 0, 0]

                MDRaisedButton:
                    text: "Activate Wallet"
                    md_bg_color: 38/255, 40/255, 41/255, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    on_release: app.root.current = 'WalletBasicDetails'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(25)


<WalletBasicDetails> 
    MDTopAppBar:
        pos_hint: {'top': 1}
        elevation: 2

        BoxLayout:
            orientation: 'horizontal'

            MDIconButton:
                icon: 'arrow-left'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "Event Wallet"
                font_size: dp(20)
                theme_text_color: "Primary"
                halign: 'left'
                valign: 'middle'
                size_hint_y: None
                height: dp(46)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                bold: True

            MDIconButton:
                icon: 'help-circle-outline'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(20)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(2)
            padding: dp(20)  
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            BoxLayout:
                orientation: 'horizontal'
                spacing: 20
                padding: 10
                MDLabel:
                    text: 'Basic Details'
                    font_size: dp(20)
                    size_hint_y: None
                    height: dp(2)

                MDIcon:
                    icon: 'close'
        MDBoxLayout:
            orientation: 'horizontal'
            spacing: 20
            padding: 10
            MDLabel:
                text: 'Documents'
                font_size: dp(20)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(20)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
            MDTextField:
                id: pan_id
                hint_text: 'Enter Pan ID'
                multiline: False
                helper_text: "Enter Valid PAN ID"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                height:self.minimum_height
            MDTextField:
                id: pan_name
                hint_text: 'Enter Pan Holder Name'
                multiline: False
                helper_text: "Enter Valid PAN Holder Name"
                helper_text_mode: 'on_focus'
                font_name: "Roboto-Bold"
                height:self.minimum_height
        GridLayout:
            cols: 1
            spacing:dp(30)
            padding: [0, "30dp", 0, 0]

            MDRaisedButton:
                text: "Submit"
                md_bg_color: 38/255, 40/255, 41/255, 1
                pos_hint: {'right': 1, 'y': 0.5}
                on_release: app.root.current = 'TopUpWallet'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold" 
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(150)  

<TopUpWallet> 
    MDTopAppBar:
        pos_hint: {'top': 1}
        elevation: 2

        BoxLayout:
            orientation: 'horizontal'

            MDIconButton:
                icon: 'arrow-left'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "Event Wallet"
                font_size: dp(20)
                theme_text_color: "Primary"
                halign: 'left'
                valign: 'middle'
                size_hint_y: None
                height: dp(46)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                bold: True

            MDIconButton:
                icon: 'help-circle-outline'
                on_release: root.go_to_dashboard()
                font_size: dp(20)
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(20)
        padding: dp(25)
        MDLabel:
            text:""
            size_hint_y: None
            height:dp(50)
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(2)
            padding: dp(20)  
            size_hint_y: None
            height: dp(150) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 10)

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Total Wallet Balance"
                    size_hint_y: None
                    height:dp(50)
                    bold: True

                MDIcon:
                    icon: 'wallet-bifold-outline'
            MDLabel:
                text:""
                size_hint_y: None
                height:dp(50)
            MDBoxLayout:
                orientation: 'horizontal'
                size_hint: None, None
                width: "190dp"
                height: "10dp"
                pos_hint: {'center_x': 0.4, 'center_y': 0.2}

                MDIcon:
                    icon: 'currency-inr'
                    halign: 'left'
                    bold: True
                MDLabel:
                    id: total_amount
                    halign: 'left'
                    bold: True
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            width: 1
                            points: [self.x, self.y - dp(5), self.x + self.width, self.y - dp(5)]

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(2)
            padding: dp(20) 
            size_hint_y: None
            height: dp(280) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDLabel:
                text: "Add Money to wallet"
                bold: True 
            MDLabel:
                text:''
                size_hint_y: None
                height: dp(20) 
            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
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
                        rgba: 0, 0, 0, 1  # Set border color to black

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width
                MDBoxLayout:
                    orientation: 'horizontal'
                    size_hint: None, None
                    width: "250dp"  
                    height: "5dp"  
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}  

                    MDIcon:
                        icon: 'currency-inr'
                        halign: 'left'
                        bold: True
                        font_size: dp(22)

                    MDTextField:
                        id: money
                        pos_hint: {'center_x': 0.5, 'center_y': 2.59}
                        line_color_normal: [1, 1, 1, 1]
                        line_color_focus: [1, 1, 1, 1]
                        font_name: "Roboto-Bold"



            MDLabel:
                text:''
                size_hint_y: None
                height: dp(20)
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: dp(10)
                size_hint: 1, 1
                width: "250dp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                MDFillRoundFlatIconButton:
                    text: "100"
                    text_color: 60/255, 3/255, 166/255, 1 
                    pos_hint: {'center_x': 0.3, 'center_y': 0.5}
                    icon: "plus"
                    icon_color: 60/255, 3/255, 166/255, 1
                    size_hint_x: 1
                MDFillRoundFlatIconButton:
                    text: "1000"
                    text_color: 60/255, 3/255, 166/255, 1 
                    pos_hint: {'center_x': 0.3, 'center_y': 0.5}
                    icon: "plus"
                    icon_color: 60/255, 3/255, 166/255, 1
                    size_hint_x: 1

            MDLabel:
                text:''
                size_hint_y: None
                height: dp(60)     

            MDBoxLayout:
                orientation: 'horizontal'

                MDRaisedButton:
                    text: "Deposit"
                    md_bg_color: 38/255, 40/255, 41/255, 1
                    pos_hint: {'right': 1, 'y': 0.5}
                    on_release: app.root.current = 'TopUpWallet'
                    text_color: 1, 1, 1, 1
                    size_hint: 1, None
                    height: "50dp"
                    font_name: "Roboto-Bold" 
            MDLabel:
                text:'Total Amount you need to pay'
                size_hint_y: None
                height: dp(20)

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  # Set background color to white
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  # Set border color to black

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width


                MDFlatButton:
                    text: "Pay"
                    pos_hint: {'center_x': 0.9, 'center_y': 0.5}
                    theme_text_color: "Custom"
                    text_color:6/255, 143/255, 236/255, 1
                    font_name: "Roboto-Bold"


        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(2)
            padding: dp(20) 
            size_hint_y: None
            height: dp(150) 
            md_bg_color:253/255, 254/255, 254/255, 1
            canvas:
                Color:
                    rgba: 174/255, 214/255, 241/255, 1 
                Line:
                    width: 0.7  
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "View History"
                    bold: True

                MDIcon:
                    icon: 'history'                        



'''
Builder.load_string(KV)


class EventWallet(Screen):
    pass


class WalletBasicDetails(Screen):
    def go_to_dashboard(self):
        self.manager.current = 'EventWallet'


class ActivateWallet(Screen):
    def go_to_dashboard(self):
        self.manager.current = 'EventWallet'


class TopUpWallet(Screen):
    def go_to_dashboard(self):
        self.manager.current = 'EventWallet'












