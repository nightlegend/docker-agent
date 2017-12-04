from flask import Flask, request
from flask_cors import cross_origin, CORS
from utils.string_to_dict import *
import os
import main
import json


app = Flask(__name__, static_url_path='/static')
CORS(app)

# define a storage to store all new client.
client_session = {}


# Testing request.
@app.route('/', methods=['GET', 'POST'])
def request_test():
    return "testing...."


# Login to docker registry.
# Methods: POST
# Args: [client_id]:the client key;
#       [registry]: login docker registry url,eg: private.registry.com;
#       [user_name]: your login id;
#       [password]: your login password;
#       [email]: your register email address.
# Return: eg: "{\"IdentityToken\": \"\", \"Status\": \"Login Succeeded\"}"
@app.route('/login_registry', methods=['POST'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def login_registry():
    certs = parse_to_dict(request.json)
    client_id = certs['client_id']
    cli = client_session[client_id]
    login_result = main.login_registry(cli=cli, user_name=certs['user_name'], password=certs['password'],
                                       email=certs['email'], registry=certs['registry'])
    return json.dumps(login_result)


# Create a docker client object.
# Methods: POST
# Args:
#       [docker_daemon_url]: will connect to docker daemon.
#       [client_id]: new docker client id.(set by yourself)
# Returns:
#       fail or success
@app.route('/create_client', methods=['POST'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def create_new_client():
    dict_result = parse_to_dict(request.json)
    base_url = dict_result['docker_daemon_url']
    cli = main.new_docker_client(base_url=base_url)
    if cli == "":
        return 100
    client_session[dict_result['client_id']] = cli
    return 200


# Get docker client information.
# Methods: GET
# Args
#       [client_id]: create new client key.
# Return:
#       the client information.
@app.route('/show_docker_client_info/<client_id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def show_docker_info(client_id):
    cli = client_session[client_id]
    print(cli)
    cli_info = main.show_cli_info(cli)
    return json.dumps(cli_info)


# Pull image from docker registry.
# Methods: GET
# Args:
#       [client_id]: Recognize your docker client session.
#       [name]: pull image name, eg:(private.registry/com/os/centos:7).
# return:
#       pull result.
@app.route('/pull/<client_id>/<host>/<folder>/<name>/<tag>', methods=['GET'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def pull_image(client_id, host, folder, name, tag):
    cli = client_session[client_id]
    image_name = host + '/' + folder + '/' + name + ':' + tag
    pull_result = main.pull_docker_image(cli, image_name)
    return pull_result


# Start a server from here.
if __name__ == '__main__':
    # load env config
    env = os.environ.get("ENV")
    config = main.load_config(env)
    print("load env is:" + env)
    app.run(host=config['host'], port=config['port'])
