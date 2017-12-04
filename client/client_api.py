import docker


# cli = docker.DockerClient()
def show_cli_info(cli):
    result = cli.api.info()
    return result
