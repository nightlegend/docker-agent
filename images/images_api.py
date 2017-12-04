# import package from here.
import docker.errors


# List all image in current docker client.
# return image list.
def list_all_images(cli):
    image_list = cli.images.list(all=True)
    return image_list


# Pull a image from private registry.
# image_name: eg: http://xxx.xxx/app/name:tagn
def pull_docker_image_from_private(cli, image_name):
    try:
        result = cli.images.pull(image_name)
        print(result)
    except docker.errors.NotFound:
        return "Not found."
    except docker.errors:
        print(docker.errors)
        return "Server exception, please try later..."
    return "pull done"


# Pull a image from public registry(docker hub).
# image_name: eg: busybox, will get latest tag image from docker hub.
def pull_docker_image_from_public(cli, image_name):
    result = cli.images.pull(image_name, stream=True)
    return result


# Search image from public registry.
# name: search pattern, string type.
def search_image(cli, name):
    search_result = cli.images.search(name)
    return search_result
