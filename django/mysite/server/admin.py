from django.contrib import admin

# Register your models here.
from .models import Scrap

from .models import Enquirie


admin.site.site_title="Admin"
admin.site.index_title = 'AR Enterprise'

admin.site.site_header = 'AR Enterprise'  


class EnquirieAdmin(admin.ModelAdmin):
    
    list_display=('name','email','companyname','contactnumber','address','gst','comments','status')
    list_display_links=['status']
    list_filter=['status']
    # list_editable = ['status']
      
    def has_add_permission(self,request):
        return False
    def changeform_view(self, request, obj_id, form_url, extra_context=None):
      extra_context={}
      extra_context["show_save_and_continue"]=False
      return super(EnquirieAdmin, self).changeform_view(request, obj_id, form_url, extra_context=extra_context)
admin.site.register(Enquirie,EnquirieAdmin)


class ScrapAdmin(admin.ModelAdmin):
  list_display = ('name','img','current_stock','Add_Stock','current_cost')

  list_editable = ('current_stock','Add_Stock','current_cost')
  def save_model(self, request, obj, form, change):
        additional_value = form.cleaned_data.get('Add_Stock')
        print(additional_value)
        if additional_value:
            obj.current_stock+= additional_value
            obj.Add_Stock=0
        obj.save()
  
admin.site.register(Scrap,ScrapAdmin)  