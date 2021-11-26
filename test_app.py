import unittest
import application

class BasicTestCase(unittest.TestCase):
    def test_logout_status_check(self):
        self.app = application.app.test_client()
        ans =self.app.get('/logout')
        self.assertEqual(ans.status_code,200) 

    def test_logout_return_check_success(self):
        self.app = application.app.test_client()
        ans =self.app.get('/logout')
        self.assertEqual(ans.data,b'success')     

    def test_logout_return_check_error(self):
        self.app = application.app.test_client()
        ans =self.app.get('/logout')
        self.assertNotEqual(ans.data,b'error')     
    
    def test_home(self):
        self.app = application.app.test_client()
        ans =self.app.get('/home')
        self.assertEqual(ans.status_code,302)

    def test_login(self):
        self.app = application.app.test_client()
        ans =self.app.get('/login')
        self.assertEqual(ans.status_code,200)

    def test_register(self):
        self.app = application.app.test_client()
        ans =self.app.get('/register')
        self.assertEqual(ans.status_code,200)
    
    def test_dashboard(self):
        self.app = application.app.test_client()
        ans =self.app.get('/dashboard')
        self.assertEqual(ans.status_code,200)

    def test_friends(self):
        self.app=application.app.test_client()
        ans=self.app.get('/friends')
        self.assertEqual(ans.status_code,200)

    def test_islive(self):
        self.app=application.app.test_client()
        ans=self.app.get('/')
        self.assertEqual(ans.status_code,302)

    def test_user_profile(self):
        self.app=application.app.test_client()
        ans=self.app.get('/user_profile')
        self.assertEqual(ans.status_code,302)

    def test_history(self):
        self.app=application.app.test_client()
        ans=self.app.get('/history')
        self.assertEqual(ans.status_code,500)

    def test_calories(self):
        self.app=application.app.test_client()
        ans=self.app.get('/calories')
        self.assertEqual(ans.status_code,302)

    def test_yoga(self):
        self.app=application.app.test_client()
        ans=self.app.get('/yoga')
        self.assertEqual(ans.status_code,302)

    def test_swim(self):
        self.app=application.app.test_client()
        ans=self.app.get('/swim')
        self.assertEqual(ans.status_code,302)

    def test_gym(self):
        self.app=application.app.test_client()
        ans=self.app.get('/gym')
        self.assertEqual(ans.status_code,302)

    def test_walk(self):
        self.app=application.app.test_client()
        ans=self.app.get('/walk')
        self.assertEqual(ans.status_code,302)

    def test_dance(self):
        self.app=application.app.test_client()
        ans=self.app.get('/dance')
        self.assertEqual(ans.status_code,302)

if __name__ == '__main__':
    unittest.main()
