from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *

# testing different urls
class TestUrls(SimpleTestCase):

  def test_url_manager_signin(self):
    url = reverse('manager_signin')
    self.assertEquals(resolve(url).func, sign_in_up)

  def test_url_add(self):
    url = reverse('add')
    self.assertEquals(resolve(url).func, add_x)

  def test_url_room_data(self):
    url = reverse('room_data')
    self.assertEquals(resolve(url).func, rooms_data)

  def test_url_update_data(self):
    url = reverse('update_data',args=['1'])
    self.assertEquals(resolve(url).func, update)

  def test_url_delete_data(self):
    url = reverse('delete_data',args=['1'])
    self.assertEquals(resolve(url).func, delete)

  def test_url_manager_login(self):
    url = reverse('manager_login')
    self.assertEquals(resolve(url).func, manager_login)

  def test_url_manager_register(self):
    url = reverse('manager_register')
    self.assertEquals(resolve(url).func, manager_register)

  def test_url_manager_logout(self):
    url = reverse('manager_logout')
    self.assertEquals(resolve(url).func, manager_logout)

  def test_url_booked_rooms(self):
    url = reverse('booked_rooms')
    self.assertEquals(resolve(url).func, booked_rooms)

  def test_url_user_profile(self):
    url = reverse('user_profile',args=['1'])
    self.assertEquals(resolve(url).func, user_profile)