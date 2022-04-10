import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nzbget_service(host):
    s = host.service('nzbget')

    assert s.is_enabled
    assert s.is_running
    assert s.systemd_properties['User'] == 'nzbget'


def test_nzbget_http(host):
    # ZNBGet has user nzbget with password tegbzn6789 set by default
    html = host.run('curl http://nzbget:tegbzn6789@localhost/nzbget/').stdout

    assert 'NZBGet' in html


def test_firewall(host):
    i = host.iptables

    assert (
        '-A INPUT -p tcp -m tcp --dport 80 '
        '-m conntrack --ctstate NEW,ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp -m tcp --sport 80 '
        '-m conntrack --ctstate ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')


def test_user(host):
    u = host.user('nzbget')

    assert u.exists
    assert 'nzbget' in u.groups
    assert 'media' in u.groups
    assert u.password == '!'
    assert u.shell == '/usr/bin/env nologin'
