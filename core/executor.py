from .docker_client import DockerClient


def run_container(container_name: str, cmd: str, detach: bool = False):
    return DockerClient.containers.run(container_name, cmd, detach=detach)


def get_container_list():
    return DockerClient.containers.list()


def get_container(container_id: str):
    # container_id or name
    return DockerClient.containers.get(container_id)


def exec_run_python(container, code: str, user: str):
    result = container.exec_run(['python', '/usr/src/app/runcode.py', code], user=user)

    output = result.output.decode("utf-8")

    return output
