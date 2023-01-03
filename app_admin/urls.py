from django.urls import path
from .views import *

urlpatterns = [
   path('',admin_home, name="admin_home"),
   path("admin_view_profile", admin_view_profile,
        name='admin_view_profile'),
   # student
   path('student/',StudentView.as_view(), name="student"),
   path("student/edit/<int:student_id>",
        edit_student, name='edit_student'),
   # staff
   path('staff/',StaffView.as_view(), name="staff"),
   path("staff/edit/<int:staff_id>", edit_staff, name='edit_staff'),
   path('staff/affecter',AffecterCoursView.as_view(), name="affecter"),
   # class
   path('classe/',ClassView.as_view(), name="school_class"),
   path("classe/edit/<int:class_id>",
         edit_class, name='edit_class'),
   path('course/',CourseView.as_view(), name="book"),
   path("course/edit/<int:course_id>",
         edit_course, name='edit_course'),

    # Url Article Blog and Category
    path('add-category', AddCategoryView.as_view(),name="add_category"),
    path('add-blog', AddBlogView.as_view(), name="add_blog"),
    path('list-blog', AllBlogs.as_view(), name="list_blog"),
    path('update/<int:article_id>', update_article, name="update"),
    #path('delete/<int:book_id>', views.delete_book)

   # inbox
   path('inbox/',InboxView.as_view(), name="inbox"),
   path('inbox/compose/',ComposeView.as_view(), name="compose"),
   path('bulletin/',BulletinView.as_view(), name="bulletin"),


]
