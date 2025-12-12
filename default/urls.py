from django.urls import path
from .views import polll_list ,PollList,PollView ,PollVote, PollCreate, PollEdit, OptionCreate

urlpatterns=[
    #path("", polll_list),
    path("", PollList.as_view(), name = 'poll_list'),
    path("<int:pk>/",PollView.as_view(), name='poll_view'),
    path('<int:oid>/vote/',PollVote.as_view(),name='poll_vote'),
    path('add',PollCreate.as_view(),name='poll_create'),
    path("<int:pk>/edit",PollEdit.as_view(), name="poll_edit"),
    path("<int:pid>/add", OptionCreate.as_view(),name="option ")
]

