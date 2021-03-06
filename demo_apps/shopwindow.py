"""
Copyright (c) 2019 Ivanov Yuri

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.

"""

from kivy.app import App    
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

from kivymd import demos_assets_path

from .basedialog import BaseDialogForDemo

from database import DataBase#cambios futuro 
screen_shop_window = """

#:import toast kivymd.toast.toast
<PreviousDialog>
    size_hint: 0, 0
    email: email
    
    BoxLayout:
        padding: dp(10)

        Image:
            source: root.icon


<MyRecycleView@RecycleView>
    key_viewclass: 'viewclass'
    key_size: 'height'

    RecycleBoxLayout:
        padding: dp(10)
        spacing: dp(10)
        default_size: None, dp(48)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'

#mofificacion clase para el caso del gestor de productos
<CardItemForCartAdmin@MDCard>
    orientation: 'vertical'
    spacing: dp(20)
    padding: dp(10)
    product_image: ''
    txtCabecera: ''
    idProducto:''
    price: ''
    description:''
    BoxLayout:
        spacing: dp(10)

        Image:
            source: root.product_image
            size_hint: None, None
            size: dp(75), dp(150)

        BoxLayout:
            orientation: 'vertical'

            MDLabel:
                idr:root.id
                theme_text_color: 'Primary'
                font_style: 'Subtitle1'
                # text: '\\n' + 'Casio CVD-12L'
                text: root.txtCabecera
                height: self.texture_size[1]
                size_hint_y: None
                bold: True

            MDLabel:
                theme_text_color: 'Primary'
                # text: 'Number: 1234567890'
                text: root.idProducto
                height: self.texture_size[1]
                size_hint_y: None
            
            MDLabel:
                theme_text_color: 'Primary'
                text: root.description
                height: self.texture_size[1]
                size_hint_y: None

            Widget:

            MDLabel:
                theme_text_color: 'Primary'
                font_style: 'Subtitle1'
                # text: 'Price - 850 $'
                text: root.price
                height: self.texture_size[1]
                size_hint_y: None
                bold: True

        MDIconButton:
            idProducto:root.id
            icon: 'close'
            pos_hint: {'top': 1}
            on_release: app.get_cardDeleteProduct(self)
        
        MDIconButton:
            idProducto:root.id
            icon: 'pencil-outline'
            pos_hint: {'top': 1}
            on_release: app.getProduct(self)
        
        
            
<CardItemForCart@MDCard>
    orientation: 'vertical'
    spacing: dp(20)
    padding: dp(10)
    product_image: ''
    txtCabecera: ''
    description: ''
    idProd: ''
    price : ''

    BoxLayout:
        spacing: dp(10)

        Image:
            source: root.product_image
            size_hint: None, None
            size: dp(75), dp(150)

        BoxLayout:
            orientation: 'vertical'

            # MDLabel:
            #     theme_text_color: 'Primary'
            #     font_style: 'Subtitle1'
            #     # text: '\\n' + 'Casio CVD-12L'
            #     text: root.description
            #     height: self.texture_size[1]
            #     size_hint_y: None
            #     bold: True

            MDLabel:
                theme_text_color: 'Primary'
                # text: 'Number: 1234567890'
                text: root.idProd
                height: self.texture_size[1]
                size_hint_y: None
             
            MDLabel:
                theme_text_color: 'Primary'
                # text: 'Number: 1234567890'
                text: root.txtCabecera
                height: self.texture_size[1]
                size_hint_y: None
            
            MDLabel:
                theme_text_color: 'Primary'
                text: root.description
                height: self.texture_size[1]
                size_hint_y: None                



            Widget:

            MDLabel:
                theme_text_color: 'Primary'
                font_style: 'Subtitle1'
                # text: 'Price - 850 $'
                text: root.price
                height: self.texture_size[1]
                size_hint_y: None
                bold: True

        MDIconButton:
            idProd:root.idProd
            icon: 'close'
            pos_hint: {'top': 1}
            on_release: app.get_cardDelete(self)
            

<CardItemForShopWindow@MDCard>
    orientation: 'vertical'
    spacing: dp(10)
    padding: dp(5)
    icon: ''
    idProd1:''
    name:''
    previous_dialog: None
    # on_release:  root.hide_menu_animation1()
     

    AnchorLayout:
        anchor_x: 'right'
        size_hint_y: None
        height: dp(30)

    

    
        MDIconButton:
            icon: 'heart-outline'
            idProd1: root.idProd1
            theme_text_color: 'Custom'
            text_color: app.theme_cls.primary_color
            on_press:
                self.icon = 'heart' if self.icon == 'heart-outline' else 'heart-outline'
            on_release:  
                app.get_card(self)
            
    MDCustomRoundIconButton:
        source: root.icon
        size_hint: None, None
        height: self.width
        pos_hint: {'center_x': .5}
        # on_release: root.previous_dialog(icon=root.icon).open()
        on_release: print('d')
        

    MDLabel:
        font_style: 'Subtitle1'
        theme_text_color: 'Primary'
        text: root.name
        height: self.texture_size[1]
        halign: 'center'
        size_hint_y: None

    MDSeparator:

    MDFlatButton:
        text: 'Quick View'
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
        pos_hint: {'center_x': .5}
        idProd1: root.idProd1
        on_release: app.getViewProduct(self)





<CardsBoxForShopWindowSearch@BoxLayout>
    spacing: dp(10)
    text:''
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        MDIconButton:
            icon: 'magnify'
      
        MDTextField:
            id:emailUsr
            size_hint: 1, None
            height: dp(48)
            # icon: 'search_field'
            hint_text: 'Search'
            on_text: app.SearchProduct(self.text,2,0)#seteado filtro

<CardsBoxForShopWindowPagNum@BoxLayout>
    spacing: dp(10)
    text:''
    BoxLayout:
        FloatLayout:
            MDDropDownItem: 
                id: dropdown_Pag
                pos_hint: {'center_x': 0.4, 'center_y': 0.6} 
                items: ["2","4","6"] 
                dropdown_bg: [1, 1, 1, 1]

            MDFloatingActionButton: 
                icon: "eye"
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}  
                md_bg_color: app.theme_cls.primary_color
                on_release: app.filtrado(dropdown_Pag.current_item)



<CardsBoxForShopWindowPag@BoxLayout>      
    FloatLayout:
        

        MDRaisedButton:
            pos_hint: {"center_x": 0.4, "center_y": 0.6}
            text: "Back"
            on_release: app.decrementContadorPag()
        
        MDRaisedButton:
            pos_hint: {"center_x": 0.6, "center_y": 0.6}
            text: "Next"
            on_release: app.incrementContadorPag()




<CardsBoxForShopWindowPagSpace@BoxLayout>
    spacing: dp(10)
    text:''   
 
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        padding: dp(10)






<CardsBoxForShopWindow@BoxLayout>
    spacing: dp(10)
    product_image: ''
    product_image2: ''
    previous_dialog: None
    idProd1: ''
    name:''
    
    CardItemForShopWindow:        
        icon: root.product_image
        previous_dialog: root.previous_dialog
        idProd1: root.idProd1
        name: root.name
        #on_release: print('fdf')

        
        

    # CardItemForShopWindow:
    #     icon: root.product_image2
    #     previous_dialog: root.previous_dialog


<CartScreen@BoxLayout>
    orientation: 'vertical'
    spacing: dp(5)
    padding: dp(5)

    MyRecycleView:
        id: rv_cart
        # on_release: print('fdf')

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        padding: dp(10)

        canvas.before:
            Color:
                rgba: 0, 0, 0, .1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [10,]

        MDFillRoundFlatButton
            text: 'Make a purchase'
            on_release: app.make_purchase()

        Widget:

        MDLabel:
            id: totalCompra
            theme_text_color: 'Primary'
            font_style: 'Subtitle1'
            text: ''
            height: self.texture_size[1]
            size_hint_y: None
            pos_hint: {'center_y': .5}
            bold: True


<MainScreen@BoxLayout>
    orientation: 'vertical'

    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)

        canvas.before:
            Color:
                rgba:
                    app.theme_cls.bg_light
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            size_hint_y: None
            height: dp(48)
            spacing: dp(10)

            MDIconButton:
                icon: 'key-variant'

            MDLabel:
                font_style: 'H6'
                theme_text_color: 'Primary'
                halign: 'left'
                text: 'Login'

        MDSeparator:

        Widget:
            size_hint_y: None
            height: dp(5)

        BoxLayout:
            spacing: dp(5)
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id:txtlogin
                size_hint: 1, None                
                height: dp(48)
                hint_text: 'example@gmail.com'
                cursor_color: app.theme_cls.primary_color
                
        BoxLayout:
            spacing: dp(35)
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id: txtpwd
                hint_text: 'Password'
                icon_left: 'lock-outline'
                icon_type: 'left'
                password: True # hide password

        Widget:
            size_hint_y: None
            height: dp(5)

        MDLabel:
            markup: True

        Widget:
        Widget:
        Widget:

        BoxLayout:
            spacing: dp(2)
            size_hint_y: None
            height: dp(35)

            MDRaisedButton:
                text: 'Sign In'
                on_release: app.login()

            MDFlatButton:
                text: 'Sign Up'
                on_release: app.loginOut()


# <MainScreen@BoxLayout>

#     BoxLayout:

#         TextInput:
#             id: login
#         TextInput:
#             id: passw
#             password: True # hide password
    
#         Button:
#             text: "go"
#             on_release: app.login(self)


   


<AdminUserScreen@BoxLayout>
    orientation: 'vertical'

    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)

        canvas.before:
            Color:
                rgba:
                    app.theme_cls.bg_light
            Rectangle:
                pos: self.pos
                size: self.size

        BoxLayout:
            size_hint_y: None
            height: dp(48)
            spacing: dp(10)

            MDIconButton:
                icon: 'key-variant'

            MDLabel:
                font_style: 'H6'
                theme_text_color: 'Primary'
                halign: 'left'
                text: 'Registration'

        MDSeparator:

        Widget:
            size_hint_y: None
            height: dp(5)

        BoxLayout:
            spacing: dp(35)
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id:emailUsr
                size_hint: 1, None
                height: dp(48)
                hint_text: 'example@gmail.com'
                cursor_color: app.theme_cls.primary_color

        BoxLayout:
            spacing: dp(35)
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id: pwdUsr
                hint_text: 'Password'
                icon_left: 'lock-outline'
                password: True # hide password
                icon_type: 'left'
                # on_release: print('jamon')
        BoxLayout:
            orientation: 'vertical'
            
            MDLabel:
                font_style: 'H6'
                theme_text_color: 'Primary'
                halign: 'center'
                text: 'Type  User'  
                
        BoxLayout:
            FloatLayout:
                
                MDDropDownItem:
                    id: dropdown_item
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}
                    items: ["admin","normal"]
                    default_item:["Admin"]
                    dropdown_bg: [1, 1, 1, 1]
                    # on_release: root.select('item1')
                
                MDRaisedButton:
                    pos_hint: {"center_x": 0.5, "center_y": 0.3}
                    text: "Save User"
                    # on_release: toast(dropdown_item.current_item)
                    on_release: app.saveUser(dropdown_item.current_item)

<AdminProductScreen@BoxLayout>
    orientation: 'vertical'
    idProd: ''
    BoxLayout:
        orientation: 'vertical'
        padding: dp(15)
        spacing: dp(10)

        canvas.before:
            Color:
                rgba:
                    app.theme_cls.bg_light
            Rectangle:
                pos: self.pos
                size: self.size
        Widget:
            size_hint_y: None
            height: dp(5)

        BoxLayout:
            spacing: dp(35)
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id:nameProd
                size_hint: 1, None
                height: dp(48)
                hint_text: 'Name'
                cursor_color: app.theme_cls.primary_color

        BoxLayout:
            spacing: dp(35)
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id: catProd
                hint_text: 'Category'
                icon_left: 'lock-outline'
                icon_type: 'left'
                # on_release: print('jamon')

        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id: descripProd
                hint_text: 'Description'
                icon_left: 'lock-outline'
                icon_type: 'left'
                # on_release: print('jamon')
        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            MDTextField:
                id: priceProd
                hint_text: 'price'
                icon_left: 'lock-outline'
                icon_type: 'left'
                # on_release: print('jamon')
                
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(48)

            # MDTextField:
            #     id: imgProd
            #     hint_text: 'imagen'
            #     icon_left: 'lock-outline'
            #     icon_type: 'left'
            #     # on_release: print('jamon')
            MDRoundFlatIconButton:
                id: imgProd
                text: "Open manager"
                icon: "folder"
                pos_hint: {'center_x': .5, 'center_y': .6}
                on_release: app.file_manager_open()

        # MDRaisedButton:
        #     id:''
        #     pos_hint: {"center_x": 0.5, "center_y": 0.3}
        #     text: "Save/Edit"
        #     on_release: app.guardarProduct(self)              
     
        # MDRaisedButton:
        #     pos_hint: {"center_x": 0.5, "center_y": 0.3}
        #     text: "Clear"
        #     on_release: app.clearEdit(self)     
        

        BoxLayout:
            spacing: dp(2)
            size_hint_y: None
            height: dp(35)

            MDRaisedButton:
                text: "Save/Edit"
                on_release: app.guardarProduct(self) 

            MDFlatButton:
                text: "Clear"
                on_release: app.clearEdit(self) 



        BoxLayout:            
            MyRecycleView:
                id: rv_product   
      
#seccion principal
<ShopWindow>
    name: 'shop window'
    
    on_enter:
        root.hideRole()
        root.set_list_shop()
        # root.set_list_cart() render carrito
        root.set_list_product()#carga productos 
        app.main_widget.ids.toolbar.title = 'Shop window'
        app.main_widget.ids.toolbar.right_action_items = []
    on_leave: app.set_chevron_back_screen()

    MDBottomNavigation:

        MDBottomNavigationItem:
            id: main
            name: 'main'
            text: 'Main'
            icon: 'home-variant'

            MainScreen:
                id:menulogin          


        MDBottomNavigationItem:
            id: view_list
            name: 'view list'
            text: 'Catalog'
            icon: 'view-list'         


        
            


            MyRecycleView:
                id: rv_main        



        MDBottomNavigationItem:
            id: cart
            name: 'cart'
            text: 'Cart'
            icon: 'cart'

            CartScreen:
                id: cart_screen

        #ONLY ADMIN VIEW
        MDBottomNavigationItem:
            id: admin
            name: 'admin'
            text: 'admin Users'
            icon: 'account-circle'

            AdminUserScreen:
                id: adminuser_screen
        
        #ONLY ADMIN VIEW
        MDBottomNavigationItem:
            id: productAdmin
            name: 'productAdmin'
            text: 'productAdmin'
            icon: 'file-eye'

            AdminProductScreen:
                id: adminproduct_screen

"""


class ShopWindow(Screen):
    def set_list_shop(self):
        db = DataBase()
        # Busu
        App.get_running_app().main_widget.ids.scr_mngr.get_screen(
                        "shop window"
                    ).ids.rv_main.data.append(
                        {
                            "viewclass": "CardsBoxForShopWindowSearch",
                            "text": 'kiubo'
                        }
                    )     
        #producto                    
        for i, val in enumerate(db.getProducts()): 
            App.get_running_app().main_widget.ids.scr_mngr.get_screen(
                "shop window"
            ).ids.rv_main.data.append(
                {
                    "viewclass": "CardsBoxForShopWindow",
                    "height": dp(300),
                    'name': val.name,
                    "product_image": val.img,
                    "previous_dialog": dialog,
                    'idProd1':str(val.id)
                }
            )
            #paginado     
            App.get_running_app().main_widget.ids.scr_mngr.get_screen(
                "shop window"
            ).ids.rv_main.data.append(
                {
                    "viewclass": "CardsBoxForShopWindowPag",
                    "text": 'pago'
                }
            )   

        pass
    def get_card(self, instance):
            # self.shop
            #consultar el listado de compra de base de datos y pasar 
            pass
    
    #productos render productos
    def set_list_product(self):
        db = DataBase()
        for i, val in enumerate(db.getProducts()): 
            print (i, ",",val)
            App.get_running_app().main_widget.ids.scr_mngr.get_screen("shop window"
            ).ids.adminproduct_screen.ids.rv_product.data.append(
                    {
                        "viewclass": "CardItemForCartAdmin",
                        "height": dp(150),
                        # "product_image": f"{demos_assets_path}clock-%d.png" % i,
                        # "product_image": val.img,
                        # "product_image": f"{demos_assets_path}" +val.img.replace('/', '') + "" ,
                        "product_image": val.img,
                        "id":str(val.id),
                        "idProducto":str(val.id),
                        "txtCabecera":val.name,
                        "description":val.description,
                        "price":  str(val.price)
                    }
                )
            var = App.get_running_app().main_widget.ids.scr_mngr.get_screen("shop window").ids.adminproduct_screen.ids.rv_product.data
        pass
    #ocultar por rol
    def hideRole(self):
        App.get_running_app().main_widget.ids.scr_mngr.get_screen("shop window").ids.adminuser_screen.disabled= True
        App.get_running_app().main_widget.ids.scr_mngr.get_screen("shop window").ids.adminproduct_screen.disabled= True
        # valor = App.get_running_app().main_widget.ids.scr_mngr.get_screen("shop window").ids.adminuser_screen.disabled= True
        pass
 
    
class PreviousDialog(BaseDialogForDemo):
    icon = StringProperty()
    
    def on_open(self):
        Animation(size_hint=(0.7, 0.7), d=0.2, t="in_out_elastic").start(self)


dialog = PreviousDialog
