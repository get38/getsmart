from django.contrib import admin

from .models import blogs,authors,categorys,Post,comment,commissoner_message,uploader,uploadergetimg,leaders,vacancy,resource_uploader,planning_uploader,reports_uploader

from .models import guidelines_uploader,rule_uploader,videup                 
admin.site.register(vacancy)
admin.site.register(rule_uploader)
admin.site.register(reports_uploader)
admin.site.register(resource_uploader)
admin.site.register(guidelines_uploader)              
admin.site.register(videup)
class commentAdmin(admin.ModelAdmin):
    list_display=('name','email','message','blogs')
    list_filter=('message',)
admin.site.register(comment,commentAdmin)
   

class uploadergetimgAdmin(admin.ModelAdmin):
    list_display=('place',)
    list_filter=('place',)
admin.site.register(uploadergetimg,uploadergetimgAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
    list_filter = ('name',)

admin.site.register(Post, PostAdmin)

class blogsAdmin(admin.ModelAdmin):
    list_display = ('title','authors','image','published_date','published','categorys')
    list_filter = ('title','authors')
      

admin.site.register(blogs, blogsAdmin) 

class categorysAdmin(admin.ModelAdmin):
      list_display= ('cateoryname',)
     
admin.site.register(categorys,categorysAdmin)      
    
class authorsAdmin(admin.ModelAdmin):
    list_display =('username','images')
    list_filter=('username',)
       
admin.site.register(authors,authorsAdmin)

class commissoner_messageAdmin(admin.ModelAdmin):
    list_display =('message',)
admin.site.register(commissoner_message,commissoner_messageAdmin)


class uploaderAdmin(admin.ModelAdmin):
    list_display=('title','uploaded_date')
admin.site.register(uploader,uploaderAdmin)

class leadersAdmin(admin.ModelAdmin):
    list_display=('name','postion')
admin.site.register(leaders,leadersAdmin) 

class planning_uploaderAdmin(admin.ModelAdmin):
    list_display=('title_planning','desc','file_pdc_pl','uploaded_date','uploaded')
admin.site.register(planning_uploader,planning_uploaderAdmin)

admin.site.site_header="የፕላንና ልማት ኮምሽን ድህረ-ገጽ ማስተዳደርያ "
admin.site.site_title="ፕላንና ልማት ኮምሽን"  
 


