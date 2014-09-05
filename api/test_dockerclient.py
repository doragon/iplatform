import pytest
import dockerclient

class TestDockerClient:


    def __init__(self):
        print '[TestDockerClient.__init__]'
        self.dockerc = new DockerClient()

#     def build(self, path=None, tag=None, quiet=False, fileobj=None,
#         nocache=False, rm=False, stream=False,
#         timeout=None, custom_context=False, encoding=None):
#         print '[DockerClient.build]'
#         print '[TODO]'
#         return 'test'

    def test_containers(self, quiet=False, all=False, trunc=True,
        latest=False, since=None, before=None, limit=-1):
        print '[TestDockerClient.test_containers]'
        assert self.dockerc.containers() == 'test'


#     def create_container(self, image, command=None, hostname=None, user=None,
#         detach=False, stdin_open=False, tty=False, mem_limit=0,
#         ports=None, environment=None, dns=None, volumes=None,
#         volumes_from=None, network_disabled=False, name=None,
#         entrypoint=None, cpu_shares=None, working_dir=None,
#         memswap_limit=0):
#         print '[DockerClient.create_containers]'
#         print '[TODO]'
#         return 'test'

#     def images(self, name=None, quiet=False, all=False, viz=False):
#         print '[DockerClient.images]'
#         print '[TODO]'
#         return 'test'

#     def pull(self, repository, tag=None, stream=False):
#         print '[DockerClient.pull]'
#         print '[TODO]'
#         return 'test'

#     def remove_container(self, container, v=False, link=False):
#         print '[DockerClient.remove_container]'
#         print '[TODO]'
#         return 'test'

#     def remove_image(self, image):
#         print '[DockerClient.remove_image]'
#         print '[TODO]'
#         return 'test'

#     def start(self, container, binds=None, port_bindings=None, lxc_conf=None,
#         publish_all_ports=False, links=None, privileged=False,
#         dns=None, dns_search=None, volumes_from=None, network_mode=None, restart_policy=None):
#         print '[DockerClient.start]'
#         print '[TODO]'
#         return 'test'

#     def stop(self, container, timeout=10):
#         print '[DockerClient.stop]'
#         print '[TODO]'
#         return 'test'