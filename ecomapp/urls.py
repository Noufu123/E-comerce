from ecomapp import views
from django.urls import path

urlpatterns=[
    path("",views.User_Home,name="User_Home"),
    path("User_Sign_page",views.User_Sign_page,name="User_Sign_page"),
    path("User_Login_Page",views.User_Login_Page,name="User_Login_Page"),
    path("User_SignUp",views.User_SignUp,name="User_SignUp"),
    path("User_Login",views.User_Login,name="User_Login"),
    path("User_Logout",views.User_Logout,name="User_Logout"),
    path("Load_catogory",views.Load_catogory,name="Load_catogory"),
    path("Load_prdct",views.Load_prdct,name="Load_prdct"),
    path("Addcatogry",views.Addcatogry,name="Addcatogry"),
    path("AddProduct",views.AddProduct,name="AddProduct"),
    path("Load_Admin_Home",views.Load_Admin_Home,name="Load_Admin_Home"),
    path("Load_catgry",views.Load_catgry,name="Load_catgry"),
    path("Load_user/",views.Load_user,name="Load_user"),
    path("user_dlt/<int:pk>",views.user_dlt,name="user_dlt"),
    path("Load_profile",views.Load_profile,name="Load_profile"),
    path("Load_profile_edit",views.Load_profile_edit,name="Load_profile_edit"),
    path("edit_user",views.edit_user,name="edit_user"),
    path("Load_View_Product",views.Load_View_Product,name="Load_View_Product"),
    path("product_dlt/<int:pk>",views.product_dlt,name="product_dlt"),
    path("Load_Product",views.Load_Product,name="Load_Product"),
    path("edit_product_details/<int:pk>",views.edit_product_details,name="edit_product_details"),
    path("add_caart/<int:pk>",views.add_caart,name="add_caart"),
    path("load_cart",views.load_cart,name="load_cart"),
    path("del_item_cart/<int:pk>",views.del_item_cart,name="del_item_cart"),

]