from typing import Any
import unittest
import application

from unittest.mock import Mock, patch, MagicMock


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

    def test_home_session_email(self):
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = 'test@gmail.com'
            ans = c.get('/home')
            self.assertEqual(ans.status_code,302)     

    @patch("application.mongo")
    @patch("bcrypt.checkpw")
    def test_login_redirect_to_dashboard(self, mock_bcrypt, mock_find):
        temp = dict(email = "test@gmail.com", pwd = "abc")
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None
            mock_find.db.user.find_one.return_value = temp  
            mock_bcrypt.return_value = True    
            ans = c.post('/login', data = dict(email = "test@gmail.com", password = "abc"))
            self.assertEqual(ans.status_code,302)  

    def test_login_redirect_to_home(self):
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = 'test@gmail.com'   
            ans = c.get('/login')
            self.assertEqual(ans.status_code,302)  

    @patch("application.mongo")
    @patch("bcrypt.checkpw")
    def test_login_unsuccessful(self, mock_bcrypt, mock_find):
        temp = None
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None
            mock_find.db.user.find_one.return_value = temp  
            mock_bcrypt.return_value = False    
            ans = c.post('/login', data = dict(email = "test@gmail.com", password = "abc"))
            self.assertEqual(ans.status_code,200)                  

    def test_register_render_template(self):
        self.app = application.app.test_client()
        ans =self.app.get('/register')
        self.assertEqual(ans.status_code,200)

    @patch("application.mongo")
    def test_register_success(self, mock_find):
        temp = dict(username = "dummy", email = "test@gmail.com", password = "abc", confirm_password = "abc", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None  
            ans = c.post('/register', data = temp)
            self.assertEqual(ans.status_code,302) 

    def test_register_redirect_to_home(self):
        temp = dict(username = "dummy", email = "test@gmail.com", password = "abc", confirm_password = "abc", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com" 
            ans = c.post('/register', data = temp)
            self.assertEqual(ans.status_code,302)     

    @patch("application.mongo")
    def test_calories_update(self, mock_find):
        form_data = dict(food = "ABC 100", burnout = 50, submit = True)
        temp = dict(calories = 100, burnout = 100)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.calories.find_one.return_value = temp   
            mock_find.db.calories.update.return_value = Any
            ans = c.post('/calories', data = form_data)
            self.assertEqual(ans.status_code,302)

    @patch("application.mongo")
    def test_calories_insert(self, mock_find):
        form_data = dict(food = "ABC 100", burnout = 50, submit = True)
        temp = None
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.calories.find_one.return_value = temp   
            mock_find.db.calories.insert.return_value = Any
            ans = c.post('/calories', data = form_data)
            self.assertEqual(ans.status_code,302)  

    def test_calories_session_none(self):
        form_data = dict(food = "ABC 100", burnout = 50, submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None
            ans = c.post('/calories', data = form_data)
            self.assertEqual(ans.status_code,302)  

    def test_user_profile(self):
        self.app=application.app.test_client()
        ans=self.app.get('/user_profile')
        self.assertEqual(ans.status_code,302)       

    @patch("application.mongo")
    def test_user_profile_update(self, mock_find):
        form_data = dict(weight = 100, height = 50, goal = "Test", target_weight = 100, submit = True)
        temp = dict(weight = 100, height = 50, goal = "Test", target_weight = 100)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.profile.find_one.return_value = temp   
            mock_find.db.profile.update.return_value = Any
            ans = c.post('/user_profile', data = form_data)
            self.assertEqual(ans.status_code,302)  

    @patch("application.mongo")
    def test_user_profile_insert(self, mock_find):
        form_data = dict(weight = 100, height = 50, goal = "Test", target_weight = 100, submit = True)
        temp = None
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.profile.find_one.return_value = temp   
            mock_find.db.profile.insert.return_value = Any
            ans = c.post('/user_profile', data = form_data)
            self.assertEqual(ans.status_code,302)                                            
    
    def test_dashboard(self):
        self.app = application.app.test_client()
        ans =self.app.get('/dashboard')
        self.assertEqual(ans.status_code,200)


    @patch("application.mongo")
    def test_friends(self, mock_find):
        myFriends  = [{ 'sender':"test1", 'receiver':"test2", 'accept': True },{
		'sender':"test2", 'receiver':"test3", 'accept': False}]
        allUsers = [{ 'name':"test1", 'email':"test2"}]

        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.friends.find.return_value = myFriends   
            mock_find.db.user.find.return_value = allUsers
            ans = c.get('/friends')
            self.assertEqual(ans.status_code,200)    

    def test_islive(self):
        self.app=application.app.test_client()
        ans=self.app.get('/')
        self.assertEqual(ans.status_code,302)

    def test_history(self):
        self.app=application.app.test_client()
        ans=self.app.get('/history')
        self.assertEqual(ans.status_code,500)

    def test_history_session_email(self):
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = 'test@gmail.com'
            ans= c.get('/history')    
            self.assertEqual(ans.status_code,200)   

    @patch("application.mongo")
    def test_ajaxhistory_session_found(self, mock_find):
        form_data = dict(date = "11/11/2021", submit = True)
        temp = dict(date = "11/11/2021", email = "test@gmail.com", burnout = 100, calories = 100)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.calories.find_one.return_value = temp   
            ans = c.post('/ajaxhistory', data = form_data)
            self.assertEqual(ans.status_code,200) 

    @patch("application.mongo")
    def test_ajaxhistory_session_not_found(self, mock_find):
        form_data = dict(date = "11/11/2021", submit = True)
        temp = None
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.calories.find_one.return_value = temp   
            ans = c.post('/ajaxhistory', data = form_data)
            self.assertEqual(ans.status_code,200)                     

    def test_yoga_redirect_to_dashboard(self):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None   
            ans = c.post('/yoga', data = form_data)
            self.assertEqual(ans.status_code,302) 

    @patch("application.mongo")
    def test_yoga_enroll_success(self, mock_find):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.user.insert.return_value = Any   
            ans = c.post('/yoga', data = form_data)
            self.assertEqual(ans.status_code,200)            

    def test_swim_redirect_to_dashboard(self):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None   
            ans = c.post('/swim', data = form_data)
            self.assertEqual(ans.status_code,302) 

    @patch("application.mongo")
    def test_swim_enroll_success(self, mock_find):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.user.insert.return_value = Any   
            ans = c.post('/swim', data = form_data)
            self.assertEqual(ans.status_code,200)     

    def test_gym_redirect_to_dashboard(self):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None   
            ans = c.post('/gym', data = form_data)
            self.assertEqual(ans.status_code,302) 

    @patch("application.mongo")
    def test_gym_enroll_success(self, mock_find):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.user.insert.return_value = Any   
            ans = c.post('/gym', data = form_data)
            self.assertEqual(ans.status_code,200)     

    def test_walk_redirect_to_dashboard(self):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None   
            ans = c.post('/walk', data = form_data)
            self.assertEqual(ans.status_code,302) 

    @patch("application.mongo")
    def test_walk_enroll_success(self, mock_find):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.user.insert.return_value = Any   
            ans = c.post('/walk', data = form_data)
            self.assertEqual(ans.status_code,200)     

    def test_dance_redirect_to_dashboard(self):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None   
            ans = c.post('/dance', data = form_data)
            self.assertEqual(ans.status_code,302) 

    @patch("application.mongo")
    def test_dance_enroll_success(self, mock_find):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.user.insert.return_value = Any   
            ans = c.post('/dance', data = form_data)
            self.assertEqual(ans.status_code,200)     

    @patch("application.mongo")
    def test_ajaxapproverequest_success(self, mock_find):
        form_data = dict(receiver = "test", submit = True)
        temp = dict(success = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.friends.update_one.return_value = temp  
            mock_find.db.friends.insert_one.return_value = Any 
            ans = c.post('/ajaxapproverequest', data = form_data)
            self.assertEqual(ans.status_code,200) 

    @patch("application.mongo")
    def test_ajaxapproverequest_failure(self, mock_find):
        form_data = dict(date = "11/11/2021", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None 
            ans = c.post('/ajaxapproverequest', data = form_data)
            self.assertEqual(ans.status_code,500)     

    def test_hrx_redirect_to_dashboard(self):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None   
            ans = c.post('/hrx', data = form_data)
            self.assertEqual(ans.status_code,302) 

    @patch("application.mongo")
    def test_hrx_enroll_success(self, mock_find):
        form_data = dict(password = "123", confirm_password = "123", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.user.insert.return_value = Any   
            ans = c.post('/hrx', data = form_data)
            self.assertEqual(ans.status_code,200)      
        

    @patch("application.mongo")
    def test_ajaxcancelrequest_success(self, mock_find):
        form_data = dict(receiver = "test", submit = True)
        temp = dict(success = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.friends.delete_one.return_value = temp   
            ans = c.post('/ajaxcancelrequest', data = form_data)
            self.assertEqual(ans.status_code,200) 

    @patch("application.mongo")
    def test_ajaxcancelrequest_failure(self, mock_find):
        form_data = dict(date = "11/11/2021", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None 
            ans = c.post('/ajaxcancelrequest', data = form_data)
            self.assertEqual(ans.status_code,500)    

    @patch("application.mongo")
    def test_ajaxsendrequest_success(self, mock_find):
        form_data = dict(receiver = "test", submit = True)
        temp = dict(success = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = "test@gmail.com"
            mock_find.db.friends.insert_one.return_value = temp   
            ans = c.post('/ajaxsendrequest', data = form_data)
            self.assertEqual(ans.status_code,200) 

    @patch("application.mongo")
    def test_ajaxsendrequest_failure(self, mock_find):
        form_data = dict(date = "11/11/2021", submit = True)
        with application.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['email'] = None 
            ans = c.post('/ajaxsendrequest', data = form_data)
            self.assertEqual(ans.status_code,500)     


if __name__ == '__main__':
    unittest.main()
