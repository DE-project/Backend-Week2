# apps/user/tests.py
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from apps.users.models import User

class TestUser(APITestCase):
    '''
        users app의 API 3개(회원가입, 로그인, 회원탈퇴) unit test
    '''
    def setUp(self):
        self.user = User(
            id         = 1,
            username   = "codestates",
            password   = make_password("123"),
            name       = "aaa",
            email      = "aaa@gmail.com",
            birth_date = "1984-07-07"
        )
        self.user.save()
        

    # 회원가입 성공 테스트
    def test_register_success(self):
        
        self.user_data = {
            "username"      : "codestates1",
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "gender"        : "Male",
            "birth_date"    : "1984-07-07",
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 회원가입 중복아이디 체크 실패
    def test_register_id_ckeck_fail(self):
        
        self.user_data = {
            "username"      : "codestates", # 중복아이디
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "gender"        : "Male",
            "birth_date"    : "1984-07-07",            
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    # 회원 가입시 패스워드 확인 실패
    def test_register_password_check_fail(self):
        
        self.user_data = {
            "username"      : "codestates112",
            "password"      : "111222333",
            "password_check": "111111111", # 패스워드 확인 오류
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "gender"        : "Male",
            "birth_date"    : "1984-07-07",            
            }

        self.register_url = "/api/users/sign-up/"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    # 로그인
    def test_login_success(self):
        self.login_url = "/api/users/sign-in/"
        data= {
                "username": "codestates",
                "password": "123",
            }
        response= self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 비밀번호 불일치
    def test_password_fail(self):
        self.login_url = "/api/users/sign-in/"
        data= {
                "username": "codestates",
                "password": "133",
            }
        response= self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'username': "{'detail': 'No active account found with the given credentials'}"})

    # 회원탈퇴
    def test_withdraw_success(self):
        self.withdraw_url = f"/api/users/{self.user.id}/withdraw/"

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.delete(self.withdraw_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)