from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('workhol/', views.workhol_site, name='workhol_site'),
    path('language_study/', views.language_study_site, name='language_study_site'),
    path('intern/', views.intern_site, name='intern_site'),
    path('<str:site_name>/<str:category_name>/post/', views.create_post, name='create_post'),
    path('<str:site_name>/<str:category_name>/', views.post_list, name='post_list'),
    path('<str:site_name>/<str:category_name>/<int:id>', views.post_detail, name='post_detail'),
    path('<str:site_name>/<str:category_name>/<int:id>/update/', views.post_update, name='post_update'),
    path('<str:site_name>/<str:category_name>/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('pressLike/<int:pk>/', views.press_like, name='press_like'),  # 좋아요 누르기 URL 추가
    path('comments/<int:pk>', views.create_comments, name='create_comments'),
    path('delcomments/<int:pk>',views.delete_comments, name='delete_comments'),
    path('upcomments/<int:pk>',views.update_comments,name = 'update_comments')
]
