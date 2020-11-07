from . import json, GraphQLTestCase
from users.testCase.User import UserTestCase

class TipoUserTestCase(GraphQLTestCase):
                            
    def test_all_query(self):
        response = self.query(
            '''
            query {
                allTipoUser(first: 1){
                    edges{
                    node{
                        id
                        nome
                    }
                    }
                }
            }
            '''
        )

        content = json.loads(response.content)
        new = len(content['data']['allTipoUser']['edges'])
        self.assertResponseNoErrors(response)
        self.assertEqual(new,0)

    # Adicionar novo Tipo de Usuario
    def test_Add_mutation(self):
        UserTestCase.setUp(self)
        UserTestCase.test_TokenAuth_superUser(self)

        response = self.query(
        '''
           mutation($input: TipoUserMotationInput!){
                tipoUser(input: $input){
                    tipouser{
                        id
                        nome
                        user{
                            id
                            username
                        }
                    }
                }
            }
            ''',
            input_data={"nome": "Admin"}
            )

        content = json.loads(response.content)
        new = content['data']['tipoUser']['tipouser']
        self.assertResponseNoErrors(response)
        self.assertEqual(new['nome'],'Admin')
        return new

    # Editar Tipo de Usuario
    def test_Edit_mutation(self):
        oldContent = self.test_Add_mutation()

        response = self.query(
        '''
           mutation($input: TipoUserMotationInput!){
                tipoUser(input: $input){
                    tipouser{
                        id
                        nome
                        user{
                        id
                        username
                        }
                    }
                }
            }
            ''',
            input_data={"id": oldContent['id'], "nome": "Derone"}
            )

        content = json.loads(response.content)
        new = content['data']['tipoUser']['tipouser']
        self.assertResponseNoErrors(response)
        self.assertEqual(new['nome'],'Derone')
        return new


    # Eliminar Tipo de Usuario
    def test_Eliminar_mutation(self):
        oldContent = self.test_Edit_mutation()

        response = self.query(
        '''
            mutation($input: RemoveTipoUserInput!){
                removeTipoUser(input: $input){
                    tipouser{
                        id
                        nome
                        user{
                        id
                        username
                        }
                    }
                }
            }                                      
            ''',
            input_data={"id": oldContent['id']}
            )

        content = json.loads(response.content)
        new = content['data']['removeTipoUser']['tipouser']
        self.assertResponseNoErrors(response)
        self.assertEqual(new['nome'],oldContent['nome'])

