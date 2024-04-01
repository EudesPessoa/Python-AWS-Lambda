from chalice import Chalice

app = Chalice(app_name='consumers')

users = {
            "users": [
                {"name": "usuário1", "phone": "47999999991"},
                {"name": "usuário2", "phone": "47999999992"},
                {"name": "usuário3", "phone": "47999999993"},
            ]
        }


companies = {
                "companies": [
                    {"name": "empresa1", "telefone": "47999999994"},
                    {"name": "empresa2", "telefone": "47999999995"},
                    {"name": "empresa3", "telefone": "47999999996"},
                ]
            }

# PF
@app.route('/consumers/person', methods = ['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode" : 200,
        "body" : f"Usúario {requests_params} criado com sucesso!"
    }
    return response

@app.route('/consumers/person', methods = ['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode" : 200,
        "body" : f"Usúario {requests_params} atualizado com sucesso!"
    }
    return response

@app.route('/consumers/persons', methods = ['GET'])
def get_persons():
    response = {
        "statusCode" : 200,
        "body" : users
    }
    return response

@app.route('/consumers/person/{id}', methods = ['GET'])
def get_person(id):
    response = {
        "statusCode" : 200,
        "body" : {id: {"name": "usuário1", "telefone": "47999999999"}}
    }
    return response

@app.route('/consumers/person', methods = ['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode" : 200,
        "body" : f"Usúario {requests_params} deletado com sucesso!"
    }
    return response


# PJ
@app.route('/consumers/company', methods = ['POST'])
def create_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode" : 200,
        "body" : f"Empresa {requests_params} criado com sucesso!"
    }
    return response

@app.route('/consumers/company', methods = ['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode" : 200,
        "body" : f"Empresa {requests_params} atualizado com sucesso!"
    }
    return response

@app.route('/consumers/companies', methods = ['GET'])
def get_companies():
    response = {
        "statusCode" : 200,
        "body" : companies
    }
    return response

@app.route('/consumers/company/{id}', methods = ['GET'])
def get_company(id):
    response = {
        "statusCode" : 200,
        "body" : {id: {"name": "empresa1", "telefone": "47999999999"}}
    }
    return response

@app.route('/consumers/company', methods = ['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    response = {
        "statusCode" : 200,
        "body" : f"Empresa {requests_params} deletado com sucesso!"
    }
    return response



# https://egpcl0yqn9.execute-api.us-east-2.amazonaws.com/api/
