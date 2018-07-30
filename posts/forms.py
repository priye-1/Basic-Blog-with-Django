# coding= utf-8
"""used to create forms for the posts module"""
from django.forms import forms
from .models import Post
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


class PostForm(forms.Form):
    """Create and update form for Post DB model"""
    model = Postfields = ["title", "headline",
                          "content", "publisher", "is_draft"]



