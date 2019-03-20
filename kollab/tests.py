from django.test import TestCase, Client
from kollab import models, views
from kollab.models import UserProfile
from kollab.views import rest_collab_initiate, get_first_collabs, profile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders


class ModelTests(TestCase):
    """ Tests run on the models where we have implemented changes not covered by the standard Django models """

    def test_userprofile(self):
        """ Tests whether a UserProfile, when passed a User, is created with the correct information """

        # First, a test user is created
        testuser = User.objects.create_user(username='test User Name',
                                            email='testemail@testemail.com',
                                            password='testPassword')
        testuser.save()

        # Then a UserProfile is created, and passed a User
        testuserprofile = UserProfile.objects.create(user=testuser)
        testuserprofile.save()

        # We would expect this to be true, as the string function of a UserProfile returns the username of the User
        self.assertTrue((str(testuserprofile) == 'test User Name'))


    def test_slug_creation(self):
        """ Tests whether a correct slug is created that can be used for urls"""

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
        """ Ensures that we can access static files """

        result = finders.find('images/354.jpg')
        self.assertIsNotNone(result)


class ViewTests(TestCase):


    def test_login_access(self):
        """ Tests that a page which has the @login required annotation cannot be accessed when not logged in"""

        testuser = User.objects.create_user(username='test User Name',
                                            email='testemail@testemail.com',
                                            password='testPassword')
        testuser.save()

        response = self.client.get(reverse('searchtags'))
        # should equal 302 as this would be a redirect to login page
        self.assertEqual(response.status_code, 302)

