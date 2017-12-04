import docker.client
import docker.errors
from containers.containers_api import *
from images.images_api import *
from client.client_api import *
import yaml
import json
import requests


# New a docker client.
# Config: save docker daemon url.
def new_docker_client(base_url):
    try:
        docker_client = docker.DockerClient(base_url=base_url)
        docker_client.ping()
    except requests.ConnectionError:
        print(requests.ConnectionError)
        return ""
    return docker_client


# Initialization config by environment.
# You can define a special config under conf folder.
def load_config(environment):
    global config
    with open('./conf/' + environment + '.config.yaml', 'r') as yaml_file:
        config = yaml.load(yaml_file)
    return config


# Show docker client detail information.
def show_docker_client_info(client):
    info = json.dumps(show_cli_info(client))
    return info


# Login to registry.
def login_registry(cli, user_name, password, email, registry):
    result_login = json.dumps(cli.api.login(username=user_name, password=password,
                                            email=email, registry=registry))
    return result_login


# Pull a image from docker registry.
def pull_docker_image(cli, name):
    return pull_docker_image_from_private(cli, image_name=name)


def search_image_from_public(cli, name):
    return json.dumps(search_image(cli, name=name))


def get_container_info(cli, container_id):
    return get_container(cli, container_id=container_id)
