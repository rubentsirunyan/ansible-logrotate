import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache_logrotate_file(host):
    f = host.file('/etc/logrotate.d/httpd')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_default_cron_daily_file_absence(host):
    f = host.file('/etc/cron.daily/logrotate')

    assert not f.exists


def test_line_exists_in_crontab(host):
    f = host.file('/etc/crontab')

    assert f.exists
    assert f.contains("/usr/sbin/logrotate -s")
