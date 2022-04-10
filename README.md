# nzbget role

[![CI](https://github.com/coaxial/ansible-role-nzbget/actions/workflows/ci.yml/badge.svg)](https://github.com/coaxial/ansible-role-nzbget/actions/workflows/ci.yml)

Galaxy: https://galaxy.ansible.com/coaxial/nzbget

## Variables and their defaults

| variable name       | default value  | description                                                                             |
| ------------------- | -------------- | --------------------------------------------------------------------------------------- |
| nzbget\_\_username  | `nzbget`       | Username under which to run NZBGet                                                      |
| nzbget\_\_password  | `!` (disabled) | NZBGet user's password                                                                  |
| nzbget\_\_group     | `media`        | NZBGet user's group                                                                     |
| nzbget\_\_use_nginx | `yes`          | Whether to install and configure nginx (`no` if you're installing/managing it yourself) |
