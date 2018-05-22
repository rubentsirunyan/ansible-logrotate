Role: Logrotate
=========

An Ansible role for automating logrotate configuration for Apache HTTP server on RedHat family distributions.

Requirements
------------

None.

Role Variables
--------------

For variable descriptions see `defaults/main.yml`.

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: rubentsirunyan.logrotate
           logs_dir: /var/log/httpd
           old_dir: old
           rotate_frequency: daily
           rotate_retention: 45

License
-------

BSD

Author Information
------------------

This role was created by [Ruben Tsirunyan](https://github.com/rubentsirunyan)
