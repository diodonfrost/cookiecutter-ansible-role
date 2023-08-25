ansible-role-{{ cookiecutter.role_name }}
=============

{{ cookiecutter.project_short_description }}

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: {{ cookiecutter.ansible_galaxy_user }}.{{ cookiecutter.role_name }}

Local Testing
-------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing.

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)
{%- if cookiecutter.freebsd_support or cookiecutter.openbsd_support or cookiecutter.windows_support %}
* [Libvirt](https://libvirt.org/) (If you test a system other than Linux)
* [Vagrant](https://www.vagrantup.com/downloads.html) (If you test a system other than Linux)
{%- endif %}

Testing with Docker
-------------------

```shell
# Install requirements
pip install -r requirements-dev.txt

# Test ansible role with ubuntu 22.04
molecule test

# Test ansible role with ubuntu 20.04
image=ansible-ubuntu:20.04 molecule test

# Test ansible role with alpine latest
image=ansible-alpine:latest molecule test

# Create centos 7 instance
image=ansible-centos:7 molecule create

# Apply role on centos 7 instance
image=ansible-centos:7 molecule converge

# Launch tests on centos 7 instance
image=ansible-centos:7 molecule verify
```

{% if cookiecutter.freebsd_support or cookiecutter.openbsd_support or cookiecutter.windows_support -%}
Testing with Vagrant and Libvirt
--------------------------------

```shell
{%- if cookiecutter.freebsd_support %}
# Test ansible role with FreeBSD
molecule test -s freebsd
{% endif -%}

{%- if cookiecutter.openbsd_support %}
# Test ansible role with OpenBSD
molecule test -s openbsd
{% endif -%}

{%- if cookiecutter.windows_support %}
# Test ansible role with Windows
molecule test -s windows
{%- endif %}
```

{% endif -%}
License
-------

{{ cookiecutter.license }}

Author Information
------------------

This role was created in 2023 by {{ cookiecutter.ansible_galaxy_user }}.
