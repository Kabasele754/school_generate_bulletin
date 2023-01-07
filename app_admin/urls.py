from django.urls import path
from .views import *

urlpatterns = [
   path("",admin_home, name="admin_home"),
   path("admin_view_profile", admin_view_profile,
        name='admin_view_profile'),
    # year and period
   path("annee-scolaire/", SchoolYearView.as_view(),name="year"),
   path("annee-scolaire/edit/<int:sch_year_id>", edit_school_year,name="year_update"),
   path("periode/", PeriodView.as_view(),name="period"),
   path("periode/edit/<int:periode_id>", edit_period,name="period_edit"),
    # generate bulletin
    path('generate_bulletin', generate_bulletin, name="generate_bulletin"),

   # student
   path('student/',StudentView.as_view(), name="student"),
   path("student/edit/<int:student_id>", edit_student, name='edit_student'),
   path("student/details/<int:student_id>", detail_student, name='detail_student'),
   path('student/cotes', cote_student, name="student_cote"),
   # staff
   path('staff/',StaffView.as_view(), name="staff"),
   path("staff/edit/<int:staff_id>", edit_staff, name='edit_staff'),
   path('staff/affecter',AffecterCoursView.as_view(), name="affecter"),
    path('staff/affecter/<pk>/update', AffecterCoursUpdateView.as_view(), name="affecte_update"),
   # class
   path('classe/',ClassView.as_view(), name="school_class"),
   path("classe/edit/<int:class_id>",
         edit_class, name='edit_class'),
   path('course/',CourseView.as_view(), name="book"),
   path("course/edit/<int:course_id>",
         edit_course, name='edit_course'),

    # Url Article Blog and Category

    path('article/', AddBlogView.as_view(), name="add_blog"),
    path('article/category/', AddCategoryView.as_view(),name="add_category"),
    path('article/category/edit/<int:cate_id>', edit_category, name="category_edit"),
    path('list-blog/', AllBlogs.as_view(), name="list_blog"),
    path('article/edit/<int:article_id>', update_article, name="update"),
    #path('delete/<int:book_id>', views.delete_book)

   # inbox
   path('inbox/',InboxView.as_view(), name="inbox"),
   path('inbox/compose/',create_mail_view, name="compose"),
   path('bulletin/',BulletinView.as_view(), name="bulletin"),


]
