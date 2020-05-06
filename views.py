from django.shortcuts import render,get_object_or_404

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count

from django.http import HttpResponse
from .models import authors,blogs,categorys,Post,commissoner_message,comment,uploader,uploadergetimg,leaders,vacancy,resource_uploader,planning_uploader,reports_uploader
from .models import guidelines_uploader,rule_uploader,videup

from django.utils.timesince import timesince  
def blogsm(request):
      
     get=blogs.objects.filter(published=True).order_by('-published_date')[0:6]   
    
     cate=categorys.objects.all()
     getevent=blogs.objects.filter(published=True).order_by('-published_date')  
     paginator = Paginator(getevent,12)  # 3 posts in each page  #posts per page
     page = request.GET.get('page')
    
     try:
        queryset = paginator.page(page)
     except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
     except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)



       #posts per page
	   
		   

  
   # search = blogs.objects.filter(title__icontains='g')
    #query =request.GET.get('q')
    
    #if query:      

    # getevent=blogs.objects.filter(published=True)(title_icontains=query)
     #getevent=blogs.objects.all()
      
              
     context={
      'datao':getevent ,'datam':get,'catem':cate,"object_list":queryset,
    }
     return render (request,'blogm.html', context) 

#def get_queryset(self): # new
       # query = self.request.GET.get('q')
       # object_list = blogs.objects.filter(Q(title__icontains=query)
       # )
       # return object_list     
def getnow(request):
      getevent=blogs.objects.filter(published=True).order_by('-published_date') 
      getimg = uploadergetimg.objects.all()
      cate=categorys.objects.all()
      
      getv=leaders.objects.all()
      message_commi = commissoner_message.objects.all()   

      paginator = Paginator(getevent,3)  # 3 posts in each page  #posts per page
      page = request.GET.get('page')
    
      try:
        queryset = paginator.page(page)
      except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
      except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)
      context={
      'data':getevent,'messcom':message_commi,'uploaderget':getimg,'leaderpdc':getv,'get_list':queryset,'categ':cate,'getimga':getimg,'catem':cate, 
       
      }      
      
      return render(request,'get.html',context)   


def missionv(request):
  return render(request,'missionvision.html')

def duites(request):
  return render(request,'duites.html')

def contact(request):
  return render(request,'contactus.html')

def videos(request):
  return render(request,'videos.html')


def event(request):
  return render(request,'event.html')

def gallery(request):
  getimg=uploadergetimg.objects.all()
  getvideo =videup.objects.all()
  paginator = Paginator(getimg, 12)  # 3 posts in each page  #posts per page
  page = request.GET.get('page')
    
  try:
        queryset = paginator.page(page)
  except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
  except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)




  context={
    'uploaderget':getimg,'gallery_list':queryset,'videolist':getvideo,
  } 
  return render(request,'gallery.html',context)   
   

def vacancym(request):
    getvaca=vacancy.objects.all()
    context={
      'vacaget':getvaca,
    }
    return render(request,'vacancy.html',context)

def bid(request):
   return render(request,'bid.html')

def service(request):
   return render(request,'service.html')   


def reso(request):
    getfilo= resource_uploader.objects.filter(uploaded=True).order_by('-uploaded_date')
    
    paginator = Paginator(getfilo, 12)  # 3 posts in each page  #posts per page
    page = request.GET.get('page')
    
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)



    context={
      'getreso':getfilo,'get_list':queryset,
    }
    return render(request,'resource.html',context)



def planget(request):
    getfilo= planning_uploader.objects.filter(uploaded=True).order_by('-uploaded_date')
    
    paginator = Paginator(getfilo, 12)  # 3 posts in each page  #posts per page
    page = request.GET.get('page')
    
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)



    context={
      'getreso':getfilo,'get_list':queryset,
    }
    return render(request,'plandoc.html',context)


def report(request):
    getfilo= reports_uploader.objects.filter(uploaded=True).order_by('-uploaded_date')
    
    paginator = Paginator(getfilo, 12)  # 3 posts in each page  #posts per page
    page = request.GET.get('page')
    
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)



    context={
      'getreso':getfilo,'get_list':queryset,
    }
    return render(request,'report.html',context)







def guide(request):
    getfilo= guidelines_uploader.objects.filter(uploaded=True).order_by('-uploaded_date')
    
    paginator = Paginator(getfilo, 12)  # 3 posts in each page  #posts per page
    page = request.GET.get('page')
    
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)



    context={
      'getreso':getfilo,'get_list':queryset,
    }
    return render(request,'guidelines.html',context)





def rule(request):
    getfilo= rule_uploader.objects.filter(uploaded=True).order_by('-uploaded_date')
    
    paginator = Paginator(getfilo, 12)  # 3 posts in each page  #posts per page
    page = request.GET.get('page')
    
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)



    context={
      'getreso':getfilo,'get_list':queryset,
    }
    return render(request,'rule.html',context)

def organ(request):
  return render(request,'orgstra.html')




def topleader(request):    
   getv=leaders.objects.all()   
   context={   
     'leaderpdc':getv, 
   }       

   return render(request,'top_leaders.html',context)  


def post(request,pk):
  getm=blogs.objects.get(id=pk)        
  getm=blogs.objects.filter(id=pk)
  dis=comment.objects.filter(blogs=pk)
       
  getevent=blogs.objects.filter(published=True).order_by('-published_date')[0:3]
  cate=categorys.objects.all()
  getnew=get_object_or_404(blogs,id=pk)     
  upget=uploader.objects.filter(uploaded=True).order_by('-uploaded_date')

 
  #context={'get':getm   
  if request.method == 'POST':   

            if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
                post=comment()
                post.name= request.POST.get('name')
                post.email= request.POST.get('email')
                post.message=request.POST.get('message')
                
                post.blogs=getnew 
                post.save()  
                
                return render(request,'blog-details.html',{'blogs':getm,'data':getevent,'catem':cate,'getup':upget,'display':dis,})
  else:  
               return render(request,'blog-details.html',{'blogs':getm,'data':getevent,'catem':cate,'getup':upget,'display':dis,})  
  return render(request,'blog-details.html',{'blogs':getm,'data':getevent,'catem':cate,'getup':upget,'display':dis,})   


def cat(request,idm):
  #getm=blogs.objects.get(categorys=idm).count()             
  getm=blogs.objects.filter(categorys=idm).order_by('-published_date')
  #getm=blogs.objects.filter(published=True).order_by('-published_date')[0:3] 
  getevent=blogs.objects.filter(published=True).order_by('-published_date')[0:3] 
  cate=categorys.objects.all()
  paginator = Paginator(getm,12)  # 3 posts in each page  #posts per page
  page = request.GET.get('page')
    
  try:
        queryset = paginator.page(page)
  except PageNotAnInteger: 
            # If page is not an integer deliver the first page
        queryset = paginator.page(1)
  except EmptyPage:
        # If page is out of range deliver last page of results
         queryset = paginator.page(paginator.num_pages)


  
       
  #getml=blogs.objects.filter(pk.get('pk')) 
  #context={'get':getm  
 
 #Create your views here.
  
  return render(request,'blogm.html',{'blogs':getevent,'object_list':getm,'catem':cate,"object_list":queryset,}) 

                




  