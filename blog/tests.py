import datetime

from django.test import TestCase
from django.utils import timezone

from blog.models import Post

class PostModeltest(TestCase):
    def test_is_working(self):
        print('i\'m working')

    def test_pub_in_future(self):
        print('second test')

