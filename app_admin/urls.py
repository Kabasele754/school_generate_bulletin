from django.urls import path
from .views import *

urlpatterns = [
   path("",DashbordardView.as_view(), name="admin_home"),
   path("admin_view_profile", admin_view_profile,
        name='admin_view_profile'),
    # year and period
   path("annee-scolaire/", SchoolYearView.as_view(),name="year"),
   path("annee-scolaire/edit/<str:sch_year_id>", edit_school_year,name="year_update"),
   path("periode/", PeriodView.as_view(),name="period"),
   path("periode/edit/<str:periode_id>", edit_period,name="period_edit"),
    # generate bulletin
    path('generate_bulletin', generate_bulletin, name="generate_bulletin"),
    
    path("generate_bulletin/view_eleve/<str:stud_id>",  detail_cls_stud_generate_bulletin,name="view_eleve"),
    path("generate_bulletin/print/<str:bulletin_id>",  generate_bulletin_print,name="stud_bulletin"),
    

   # student
   path('student/',StudentView.as_view(), name="student"),
   path("student/edit/<str:student_id>", edit_student, name='edit_student'),
   path("student/details/<str:student_id>", detail_student, name='detail_student'),
   path('student/cotes', cote_student, name="student_cote"),
   # staff
   path('staff/',StaffView.as_view(), name="staff"),
   path("staff/edit/<str:staff_id>", edit_staff, name='edit_staff'),
   path('staff/affecter',AffecterCoursView.as_view(), name="affecter"),
    path('staff/affecter/<pk>/update', AffecterCoursUpdateView.as_view(), name="affecte_update"),
   # class
   path('classe/',ClassView.as_view(), name="school_class"),
   path("classe/edit/<str:class_id>",
         edit_class, name='edit_class'),
   path('course/',CourseView.as_view(), name="book"),
   path("course/edit/<str:course_id>",
         edit_course, name='edit_course'),

    # Url Article Blog and Category

    path('article/', AddBlogView.as_view(), name="add_blog"),
    path('article/category/', AddCategoryView.as_view(),name="add_category"),
    path('article/category/edit/<str:cate_id>', edit_category, name="category_edit"),
    path('list-blog/', AllBlogs.as_view(), name="list_blog"),
    path('article/<pk>/edit/', ArticleUpdateView.as_view(), name="update"),
    #path('delete/<int:book_id>', views.delete_book)

   # inbox
   path('inbox/',InboxView.as_view(), name="inbox"),
   path('inbox/compose/',create_mail_view, name="compose"),
   path('bulletin/',BulletinView.as_view(), name="bulletin"),
   
   # system config
    path("systemconfig/",SystemConfigView.as_view(), name="logo"),
    path('systemconfig/<pk>/edit/', LogoUpdateView.as_view(), name="update_logo"),
    path("logo_admin/",LogoDashbordView.as_view(), name="logo_admin"),
    
    


]
