import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache_logrotate_file(host):
    f = host.file('/etc/logrotate.d/httpd')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
