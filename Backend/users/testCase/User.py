from django.test import TestCase
from django.contrib.auth.models import User
# from graphql_jwt.testcases import JSONWebTokenTestCase

from . import json, GraphQLTestCase


class UserTestCase(GraphQLTestCase,TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create_superuser(username='teste1',email='teste1@gmail.com',password='#1234567')
        self.user2 = User.objects.create_user(username='teste2',email='teste2@gmail.com',password='#1234567')
        return {
            "super_user":self.user1,
            "normal_user": self.user2
            }
        
    def test_TokenAuth_superUser(self):        
        response = self.query(
            '''
                mutation TokenAuth($input: ObtainJSONWebTokenInput!){
                    tokenAuth(input: $input){
                        payload
                        refreshExpiresIn
                        refreshToken
                        token
                        user{
                        id
                        username
                        email
                        }
                    }
                    }
            ''',
            input_data={
                "username": 'teste1',
		        "password": "#1234567"
            }
        )
        
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        new = content['data']['tokenAuth']
        self.assertEqual(new['user']['username'],'teste1')
    
        
    def test_TokenAuth_User(self):        
        response = self.query(
            '''
                mutation TokenAuth($input: ObtainJSONWebTokenInput!){
                    tokenAuth(input: $input){
                        payload
                        refreshExpiresIn
                        refreshToken
                        token
                        user{
                        id
                        username
                        email
                        }
                    }
                    }
            ''',
            input_data={
                "username": 'teste2',
		        "password": "#1234567"
            }
        )
        
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        new = content['data']['tokenAuth']
        self.assertEqual(new['user']['username'],'teste2')
 
  
    def test_all_query(self):
        response = self.query(
            '''
            query {
                allUsers{
                    edges{
                    node{
                        id
                        username
                        email
                        dateJoined
                        fullName
                        perfil{
                        sexo
                        bio
                        localizacao
                        avatar
                        }
                    }
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        new = len(content['data']['allUsers']['edges'])        
        self.assertNotEqual(new,0)


    # Adicionar Usuario
    def test_Add_mutation(self):
        response = self.query(
        '''
           mutation($input: UserMutationInput!){
            user(input: $input){
                user{
                id
                username
                perfil{
                    localizacao
                    bio
                }
            }
            errors{
                field
                messages
            }
            }
            }
            ''',
            input_data={
                "username": "dsderone",
                "email": "dercio@gmail.com",
                "password1": "#1234567",
                "password2": "#1234567"
            }
            )

        content = json.loads(response.content)
        new = content['data']['user']
        self.assertResponseNoErrors(response)
        self.assertEqual(new['errors'],None)
        self.assertEqual(new['user']['username'],'dsderone')
        return new['user']
       
        
    # Editar Usuario
    def test_Edit_mutation(self):
        oldContent = self.test_Add_mutation()

        response = self.query(
        '''
           mutation($input: UserMutationInput!){
                user(input: $input)
                {
                    user{
                    id
                    username
                    perfil{
                        localizacao
                        bio
                    }
                } errors{
                        field
                        messages
                    }
                }
            }
            ''',
            input_data={
                "id": oldContent['id'],
                "username": "dsderone2",
                "email": "dercio@gmail.com",
                "password1": "#1234567",
                "password2": "#1234567"
            }
            )

        content = json.loads(response.content)
        new = content['data']['user']
        self.assertResponseNoErrors(response)
        self.assertEqual(new['errors'],None)
        self.assertEqual(new['user']['username'],'dsderone2')
        return new['user']
   
   
    def test_get_query(self):
        oldContent = self.test_Edit_mutation()
        response = self.query(
        '''
            query($id: ID!){
            user(id: $id){
                id
                username
                email
            }
            }
        ''',
        variables={'id': oldContent['id'] }
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        new = content['data']['user']
        self.assertIsNot(new,None)
        self.assertEqual(new['username'],oldContent['username'])
    
    
    # Eliminar Usuario
    def test_Eliminar_mutation(self):
        self.test_TokenAuth_superUser()
        oldContent = self.test_Edit_mutation()

        response = self.query(
            '''
            mutation($input: RemoveUserInput!){
                removeUser(input: $input){
                user{
                    username
                    email
                }
                }
            }                          
            ''',
            input_data={"id": oldContent['id']}
            )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        new = content['data']['removeUser']['user']
        self.assertEqual(new['username'],oldContent['username'])
    
    def test_Eliminar_mutation2(self):
        return
        self.test_TokenAuth_User()
        oldContent = self.test_Edit_mutation()

        response = self.query(
            '''
            mutation($input: RemoveUserInput!){
                removeUser(input: $input){
                user{
                    username
                    email
                }
                }
            }                          
            ''',
            input_data={"id": oldContent['id']}
            )

        content = json.loads(response.content)
        self.assertResponseHasErrors(response)
        self.assertEqual(content['errors'][0]['message'],'You do not have permission to perform this action')