MariaDB Role
============

Configures a mariadb server based on Fedora with CustomOS settings:

- Root password given as role parameter.
- Mysql basic secure settings, equivalent to mysql_secure_installation script.

Requirements
------------

A Fedora system.

Role Variables
--------------

root_password: 'insecure'

Static variables like packages list or configuration file settings
can be found in vars/ directory.

Dependencies
------------

This role has iac_ansible-role-server as dependency, configured in ansible-galaxy .requirements file.

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: iac_ansible-role-mariadb }
```

License
-------

GPL3

Author Information
--------------

