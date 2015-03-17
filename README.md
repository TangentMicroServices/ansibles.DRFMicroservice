Role Name
=========

An opinionated deployment for a Django Rest Framework MicroService on an Ubuntu box.

* Stack is: Django REST Framework on Django running inside virtualenv. nginx, gunicorn and upstart for process management. 
* Will deploy to a domain of the format {{service_name}}.{{tld}} 
* Optionally create postgres databases with Ansibles.postgresql role
* ...

Requirements
------------

None

Role Variables
--------------

| Parameter           	| Required 	| Default             	| Choices                                                              	| Comment                                                                                                                                                                                             	|
|---------------------	|----------	|---------------------	|----------------------------------------------------------------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| service_name        	| yes      	|                     	|                                                                      	| The name of your microservice. Typically something along the lines of: userservice, customerservice ..etc. Will be used in a number of places. Importantly: domain will be {{service_name}}.{{tld}} 	|
| github_repo         	| yes      	|                     	|                                                                      	| The repo to pull this code from. Use the ssh form. e.g.: git@github.com:muusername/myproject.git                                                                                                    	|
| service_http_port   	| yes      	|                     	|                                                                      	| The http port to run this process on.                                                                                                                                                               	|
| service_db_password 	| yes      	|                     	|                                                                      	| A password for your database                                                                                                                                                                        	|
| tld                 	| yes      	|                     	|                                                                      	| Top level domain. For example: mysite.com                                                                                                                                                           	|
| python_version      	| no       	| "2.7"               	|                                                                      	| The python version to use in your virtualenv                                                                                                                                                        	|
| service_db_engine   	| no       	| postgresql_psycopg2 	| 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'. 	| Used for setting your django database connection                                                                                                                                                    	|
| services            	| no       	|                     	|                                                                      	|                                                                                                                                                                                                     	|

Dependencies
------------

* Ansibles.postgresql
* toast38coza.djangoserver


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      vars:
        service_name: libraryservice
        github_repo: git@github.com:TangentMicroServices/LibraryService.git
        service_http_port: 8011
        service_db_password: testtest    
    
      roles:
        - Ansibles.postgresql
        - toast38coza.djangoserver
        - toast38coza.DRFMicroservice
 

License
-------

MIT

