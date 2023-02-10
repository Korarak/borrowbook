from django.shortcuts import render,redirect
from django.contrib  import messages
from bookapp.models import*
from django.db.models import Q
import datetime


# Create your views here.
def home(request):
    context = {'borrow_all':tb_borrow_book.objects.all()}  
    return render(request,'bookapp/all_list.html',context)

def search(request):
    if request.method == 'POST':
        if request.POST.get('search_nav'):
            search_key = request.POST.get('search_nav')
            search = tb_borrow_book.objects.filter(Q(b_id__b_name__icontains=search_key)
            |Q(m_user_id__m_name__icontains=search_key)
            |Q(b_id__b_id__icontains=search_key)
            )
            context = {'Search':search }
            return render(request,'bookapp/search.html',context)
        else:
            messages.warning(request,'ไม่พบ')
            context = {'Search':tb_borrow_book.objects.all()}  
            return render(request,'bookapp/search.html',context)  
    context = {'Search':tb_borrow_book.objects.all()}       
    return render(request,'bookapp/search.html',context)

def borrow(request):
    now_time = datetime.datetime.now()
    print(now_time)
    if request.method == "POST":
        if request.POST.get('m_user'):
            m_user = request.POST.get('m_user')
            b_id = request.POST.get('b_id')
            context2 = {
        'member2' : tb_member.objects.filter(m_user=m_user),
        'book2'   : tb_book.objects.filter(b_id=b_id),
        'nowtime2': now_time,
        
    }       
        else:
            messages.warning(request,'ไม่สำเร็จ')
            return redirect('/')
        return render(request,'bookapp/borrow.html',context2)
    messages.warning(request,'เลือกผู้ยืม')        
    context = {
        'member' : tb_member.objects.all(),
        'book'   : tb_book.objects.all(),
        'nowtime': now_time,
    }
    return render(request,'bookapp/borrow.html',context)

def confirm(request):
    if request.method == "POST":
        if request.POST.get('member_user'):
            now_time = datetime.datetime.now()
            print(now_time)
            print(request.POST.get('book_user'))
            print(request.POST.get('member_user'))
            table = tb_borrow_book()
            table.br_date_br = now_time
            table.b_id_id = request.POST.get('book_user')
            table.m_user_id = int(request.POST.get('member_user'))
            table.br_fine = 0
            table.save()
            messages.success(request,'บันทึกการยืมสำเร็จ')
            return redirect('/')
        else:
            messages.warning(request,'ไม่สำเร็จ')
            return redirect('/')
    return   render(request,'bookapp/all_list.html')

def returnbook(request):
    if request.method == 'POST':
        if request.POST.get('search_return'):
            search_key = request.POST.get('search_return')
            search = tb_borrow_book.objects.filter(Q(b_id__b_name__icontains=search_key)
            |Q(m_user_id__m_name__icontains=search_key)
            |Q(b_id__b_id__icontains=search_key)
            )
            context = {'Search':search }
            return render(request,'bookapp/returnbook.html',context)
        else:
            messages.warning(request,'ไม่พบ')
            context = {'Search':tb_borrow_book.objects.filter(br_date_rt=None)}  
            return render(request,'bookapp/returnbook.html',context)       
    context = {'Search':tb_borrow_book.objects.filter(br_date_rt=None)}  
    return render(request,'bookapp/returnbook.html',context)

def returnbookconfirm(request,id):
    now_time = datetime.datetime.now()
    context = tb_borrow_book.objects.get(br_id=id)
    context.br_date_rt = now_time
    context.save()
    messages.success(request,'คืนหนังสือสำเร็จ')
    return redirect('/returnbook')

def borrowstat(request):
    numbook = tb_book.objects.all().count()
    nummember = tb_member.objects.all().count()
    bookok = tb_borrow_book.objects.all().count()
    booklost = tb_borrow_book.objects.filter(br_date_rt=None).count()
    context = {'numbook':numbook,
                'nummember':nummember,
                'bookok':bookok,
                'booklost':booklost,
    }
    return render(request,'bookapp/borrowstat.html',context)