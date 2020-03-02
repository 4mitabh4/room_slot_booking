from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *

# testing different urls
class TestUrls(SimpleTestCase):

  def test_url_home(self):
    url = reverse('home')
    self.assertEquals(resolve(url).func, home)
  
  def test_url_profile(self):
    url = reverse('profile')
    self.assertEquals(resolve(url).func, profile)
    
  def test_url_user_book(self):
    url = reverse('user_book',args=['1'])
    self.assertEquals(resolve(url).func, book)
  
  def test_url_user_user_login(self):
    url = reverse('user_login')
    self.assertEquals(resolve(url).func, user_login)
  
  def test_url_user_book_delete(self):
    url = reverse('book_delete',args=['1'])
    self.assertEquals(resolve(url).func, old_book)
    
  def test_url_user_user_logout(self):
    url = reverse('user_logout')
    self.assertEquals(resolve(url).func, user_logout)
    
  def test_url_user_register(self):
    url = reverse('register')
    self.assertEquals(resolve(url).func,register)