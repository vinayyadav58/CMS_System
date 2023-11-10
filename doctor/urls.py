from django.urls import path
from doctor.views import *





urlpatterns = [
    path('add_doctor/',add_doctor ,name="add_doctor"),
    path('sc_doctor/',schedule_appointment ,name="sc_doctor"),
    path('ts/',todays_schedule ,name="ts_doctor"),
    path('deal/',deal_detail ,name="deal_detail"),
    path('admin_deal/',admin_deal ,name="admin_deal"),
    path('admin_deal_visit/',admin_deal_visit ,name="admin_deal_visit"),
    # path('tt_deal/',tt ,name="tt"),

]
