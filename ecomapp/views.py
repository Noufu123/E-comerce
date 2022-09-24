from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def User_Home(request):
    return render(request,'user/home.html')

def User_Sign_page(request):
    return render(request,'user/signup.html')

def User_Login_Page(request):
    return render(request,'user/login.html')

def Load_catogory(request):
    return render(request,'admin/addcatogory.html')

def Load_prdct(request):
    catogory=catogoryModel.objects.all()
    context={'catogory':catogory}
    return render(request,'admin/adddprdct.html',context)

def Load_Admin_Home(request):
    return render(request,'admin/adminhome.html')

def Load_catgry(request):
    catogory=catogoryModel.objects.all()
    context={'catogory':catogory}
    return render(request,'admin/viewcatgry.html',context)

def Load_user(request):
    users=UserModel.objects.all()
    context={'users':users}
    return render(request,'admin/viewuser.html',context)

def Load_profile(request):
    users=UserModel.objects.get(User=request.user)
    context={'users':users}
    return render(request,'user/profile.html',context)

def Load_profile_edit(request):
    users=UserModel.objects.get(User=request.user)
    context={'users':users}
    return render(request,'user/profileedit.html',context)

def Load_View_Product(request):
    product=PrdctModel.objects.all()
    context={'product':product}
    return render(request,'admin/viewproduct.html',context)

def Load_Product(request):
    product=PrdctModel.objects.all()
    context={'prdct':product} # 'html page name' and variable  name
    return render(request,'user/product.html',context)


def User_SignUp(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        username=request.POST['username']
        address=request.POST['address']
        mail=request.POST['email']
        gender=request.POST['gender']
        age=request.POST['age']
        password=request.POST['password']
        com_password=request.POST['confirmpassword']

        # photo
        photo=request.FILES.get('photo')

        if password==com_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This Username Already Exists!')
                return redirect('User_Sign_page')

            elif User.objects.filter(email=mail).exists():
                messages.info(request,'This Email Already Exists!')
                return redirect('User_Sign_page')

            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=mail,username=username,password=password)
                user.save()
                messages.success(request,'SuccessFully Registred')
                print("Successed")

                data=User.objects.get(id=user.id)
                user_data=UserModel(User_Address=address,User_Gender=gender,User_Age=age,User_Photo=photo,User=data)
                user_data.save()
                messages.success(request,'SuccessFully Registred')
                print("Successed")
                return redirect('User_Login_Page')
        else:
            #messages info
            print("password is not Matching")
            return redirect('User_Sign_page')
        return redirect('User_Login')
    else:
        return render(request,'user/signup.html')

def User_Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)#variable and htmlpage name
        # request.session['uid']=user.id
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('Load_Admin_Home')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('User_Home')
        else:
            return redirect('User_Login')
    else:
        return redirect('login.html')

def User_Logout(request):
    auth.logout(request)
    return redirect('User_Home')

def Addcatogry(request):
    if request.method=='POST':
        catgry_Name=request.POST['Catogory_Name']

    
    data=catogoryModel(Catgory_Name=catgry_Name)
    data.save()
    return redirect('Load_catogory')

def AddProduct(request):
    if request.method == 'POST':
        PrdctName=request.POST['ProdctName']#html page name[]
        PrdctPrice=request.POST['ProductPrice']
        select=request.POST['select']
        Cat=catogoryModel.objects.get(id=select)
        data = PrdctModel(Prdct_Name=PrdctName,Prdct_Price=PrdctPrice,Catagory=Cat) #model name= variable name
        data.save()
        # messages.info(request, 'New prdct Added')
        return redirect('Load_prdct')

def user_dlt(request,pk):
    user=UserModel.objects.get(id=pk)
    user.delete()
    return redirect('Load_user')

# to edit user profile
def edit_user(request):
    if request.method == 'POST':
        member=UserModel.objects.get(User=request.user)
        member.User.first_name=request.POST['firstname']
        member.User.last_name=request.POST['lastname']
        member.User_Gender=request.POST['gender']
        member.User_Address=request.POST['address']
        member.User_Age=request.POST['age']
        # member.image=request.FILES['file']
        # if request .FILES.get('file') is not None:
        #     if not member.image == "/static/images/blank-profile-picture-973460_640.png":
        #         os.remove(member.image.path)
        #         member.image="/static/images/blank-profile-picture-973460_640.png"
        member.save()
        member.User.save()
        return redirect('Load_profile')
        
def product_dlt(request,pk):
    prdct=PrdctModel.objects.get(id=pk)
    prdct.delete()
    return redirect('Load_View_Product')

def edit_product_details(request,pk):
    if request.method=='POST':
        products = PrdctModel.objects.get(id=pk)
        products.Prdct_Name = request.POST['pname']
        products.Prdct_Price = request.POST['price']
        # products.image=request.FILES['file']
        products.save()
        return redirect('Load_View_Product')
    products=PrdctModel.objects.get(id=pk)
    return render(request,'admin/productedit.html',{'products':products})

# to add to cart product 
def add_caart(request,pk):
    product = PrdctModel.objects.get(id=pk)
    # user = adduser_model.objects.get(user=request.user)
    data = cartmodel(product=product,User=request.user)
    data.save()
    return redirect('Load_Product')

# to load cart page
def load_cart(request):
    products=cartmodel.objects.filter(User=request.user)
    context={'products':products}
    return render(request,'user/cart.html',context)

# to delete items in cart 
def del_item_cart(request,pk):
    product = cartmodel.objects.get(id=pk)
    product.delete()
    return redirect('load_cart')