from django.test import TestCase, Client
from kollab import models, views
from kollab.models import UserProfile
from kollab.views import rest_collab_initiate, get_first_collabs, profile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.contrib.staticfiles import finders




class ModelTests(TestCase):

    def test_userprofile(self):
        testuser = User.objects.create_user(username='test User Name',
                                            email='testemail@testemail.com',
                                            password='testPassword')
        testuser.save()

        testuserprofile = UserProfile.objects.create(user=testuser)
        testuserprofile.save()
        #print(testuserprofile)
        self.assertTrue((str(testuserprofile) == 'test User Name'))


    def test_slug_creation(self):
        testuser = User.objects.create_user(username='test User Name',
                                            email='testemail@testemail.com',
                                            password='testPassword')

        testuser.save()

        testuserprofile = UserProfile.objects.create(user=testuser,
                                                     firstname='testname',
                                                     lastname='mctestname',
                                                     lat=55.87473302,
                                                     lon=4.28724289,
                                                     selfinfo='blah blah blah')

        testuserprofile.save()

        self.assertEqual(testuserprofile.slug, 'test-user-name')


class ServeStaticFiles(TestCase):

    def test_serving_static_files(self):

        result = finders.find('images/354.jpg')
        self.assertIsNotNone(result)


class ViewTests(TestCase):


    def test_login_access(self):

        testuser = User.objects.create_user(username='test User Name',
                                            email='testemail@testemail.com',
                                            password='testPassword')

        testuser.save()

        response = self.client.get(reverse('searchtags'))
        # should equal 302 as this would be a redirect to login page
        self.assertEqual(response.status_code, 302)


    # def test_login_access_reverse(self):
    #
    #     testuser = User.objects.create_user(username='testuser')
    #     testuser.set_password('testPassword')
    #
    #     testuser.save()
    #
    #     c = Client()
    #     logged_in = c.login(username='testuser', password='testPassword')
    #     response = self.client.get(reverse('buildprofile'))
    #     self.assertEqual(response.status_code, 200)

