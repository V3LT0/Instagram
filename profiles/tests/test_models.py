from django.test import TestCase

from profiles.models import UserProfiles, Follow
from django.contrib.auth.models import User

class UserProfileModelTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="john",
            email="john@lennon.com",
            password="password123"
        )

        self.user2 = User.objects.create_user(
            username="paul",
            email="paul@maccartney.com",
            password="password123"
        )

        self.profile1 = UserProfiles.objects.create(
            user=self.user1,
            bio="I'm a musician",
            birth_date="1940-10-09"
        )

        self.profile1 = UserProfiles.objects.create(
            user=self.user2,
            bio="I'm also a musician",
            birth_date="1942-06-18"
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.profile1.bio, "I'm a musician")
        self.assertEqual(self.user1.username,"john")
