from django.urls import path

from . import views

# 添加命名空間，在模板中可用
# <!-- 在 polls.urls 的 url() 函数中通过 name 参数为 URL 定义了名字，你可以使用 {% url %} 标签代替它 -->
# <!-- 在 polls/urls.py 文件中稍作修改，加上 app_name 设置命名空间 -->
app_name = 'polls'
urlpatterns = [
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path(r'addQuestion/', views.addQuestion, name='addQuestion'),
]