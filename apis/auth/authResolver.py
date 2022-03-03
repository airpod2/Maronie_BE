from flask_restx import Resource
from flask import request
from .authDTO import *
from . import authService

# 회원가입 email 유효성 검사
@Auth.route('/register/email=<string:email>')
class AuthRegisterCheckId(Resource):
    # @Auth.expect(checkIdDTO)
    @Auth.response(200, "Available email address")
    @Auth.response(404, "Not found")
    @Auth.response(500, "Unavailable email address")
    def get(self,email):
        '''회원가입시 ID유효성 검사'''
        return authService.idckeck(email)

# 회원가입 nickname 유효성 검사
@Auth.route('/register/nickname=<string:nickname>')
class AuthRegisterCheckNickname(Resource):
    # @Auth.expect(checkIdDTO)
    @Auth.response(200, "Available nickname address")
    @Auth.response(404, "Not found")
    @Auth.response(500, "Unavailable nickname address")
    def get(self,nickname):
        '''회원가입시 ID유효성 검사'''
        return authService.nicknameckeck(nickname)

# 회원가입 요청
@Auth.route('/register')
class AuthRegister(Resource):
    @Auth.expect(registerDTO)
    # @Auth.response(200, "Available id")
    # @Auth.response(500, "Unavailable id")
    def post(self):
        '''회원가입 성공시 DB에 저장'''
        email = request.json['email']
        nickname = request.json['nickname']
        password = request.json['password']
        return authService.userRegister(email,nickname,password)

# 로그인
@Auth.route('/login')
class AuthLogin(Resource):
    @Auth.expect(loginDTO)
    @Auth.response(200, "login Success")
    @Auth.response(404, "Not found")
    @Auth.response(500, "login Failed")
    def post(self):
        '''로그인 기능'''
        email = request.json['email']
        password = request.json['password']
        return authService.userLogin(email,password)

#비밀번호 변경

@Auth.route('/changepw')
class AuthChangepw(Resource):
    @Auth.expect(changepwDTO)
    @Auth.response(200, "password Changed")
    @Auth.response(404, "Not Found")
    @Auth.response(404, "Wrong Password")
    @Auth.response(500, "Password Change Fail")
    def post(self):
        '''유저 비밀번호 변경하기'''
        email = request.json['email']
        new_password = request.json['new_password']
        new_password_check = request.json['new_password_check']
        return authService.changepw(email,new_password,new_password_check)

# 로그아웃
@Auth.route('/logout')
class AuthLogout(Resource):
    def post(self):
        '''로그아웃 기능'''
        return authService.userLogout()
