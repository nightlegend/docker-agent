# import package from here


# List all running container in current docker client.
def list_all_container(cli):
    containers = cli.containers.list(all=True)
    return containers


# Inspect a container information.
def get_container(cli, container_id):
    # cli = docker.DockerClient()
    container_info = cli.api.inspect_container(container=container_id)
    # container_info = cli.containers.get(container_id=container_id)
    return container_info
