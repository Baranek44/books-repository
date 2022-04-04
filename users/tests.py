from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):
    # Create test for a normal user in project
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='smith',
            email='smith@email.com',
            password='pawssword123'
        )
        self.assertEqual(user.username, 'smith')
        self.assertEqual(user.email, 'smith@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        # Create test for a super user in project
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='password123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)