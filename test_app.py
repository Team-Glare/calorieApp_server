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
     

if __name__ == '__main__':
    unittest.main()
