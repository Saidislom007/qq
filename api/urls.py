from django.urls import path

from .views import (
    GetConference,
    GetOneConference,
    GetMaqola,
    GetOneMaqola,
    GetAboutShoba,
    GetOneAboutShoba,
    GetShoba,
    GetOneShoba,
    GetWordPart,
    GetOneWordPart,
    DownloadConferenceWordFileView
)


urlpatterns = [

    path(
        'conferences/',
        GetConference.as_view(),
        name='conference-list'
    ),

    path(
        'conferences/<slug:slug>/',
        GetOneConference.as_view(),
        name='conference-detail'
    ),


    path(
        'shobalar/',
        GetShoba.as_view(),
        name='shoba-list'
    ),

    path(
        'shobalar/<slug:slug>/',
        GetOneShoba.as_view(),
        name='shoba-detail'
    ),


    path(
        'maqolalar/',
        GetMaqola.as_view(),
        name='maqola-list'
    ),

    path(
        'maqolalar/<slug:slug>/',
        GetOneMaqola.as_view(),
        name='maqola-detail'
    ),


    path(
        'about-shoba/',
        GetAboutShoba.as_view(),
        name='about-shoba-list'
    ),

    path(
        'about-shoba/<slug:slug>/',
        GetOneAboutShoba.as_view(),
        name='about-shoba-detail'
    ),


    path(
        'word-parts/',
        GetWordPart.as_view(),
        name='word-part-list'
    ),

    path(
        'word-parts/<int:pk>/',
        GetOneWordPart.as_view(),
        name='word-part-detail'
    ),
    path('download-word-file/<int:id>/', 
         DownloadConferenceWordFileView.as_view(),
         name='download-word-file-by-id'),

]