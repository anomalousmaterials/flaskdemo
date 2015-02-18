# flaskdemo
An Ansible playbook to get started with Flask, Apache and mod_wsgi.

What it does
------------

* Installs Apache and mod_wsgi packages.
* Adds an Apache config file.
* Creates a pair of trivial Hello World apps using Flask and bare WSGI.
* Restarts Apache.

Prerequisites
-------------
* CentOS / RHEL 6
* Ansible and the EPEL repository installed

Running on localhost
--------------------

ansible-playbook -i 'localhost,' -c local main.yml

After completion, the files can be found under /var/www/flaskdemo and the apps can be accessed at:

* http:/localhost/wsgi
* http:/localhost/flask


