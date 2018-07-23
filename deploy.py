from fabric.api import *
from fabric.contrib.files import exists
from fabric.operations import open_shell

from avocado.crypt_key import KEY

### TEST PASSED ###
def deploy_postgresql(self):
    run('sudo apt-get update')
    run('sudo apt-get install libpq-dev postgresql postgresql-contrib')

    with cd('/etc/postgresql/9.5/main'):
        run("vim +\":%s/#listen_addresses = 'localhost'/listen_addresses = '*'/g | wq\" postgresql.conf")
        run("vim +\"%s/127.0.0.1\/32/0.0.0.0\/0   /g | %s/::1\/128/::\/0/g | wq\" pg_hba.conf")
    # start, enable and restart postgresql service
    # run('sudo systemctl start postgresql.service')
    run('sudo systemctl enable postgresql.service')
    run('sudo systemctl restart postgresql.service')

    # create database table and user if they do not exist already
    with settings(warn_only=True):
        run('sudo -i -u postgres psql -c "CREATE DATABASE {};"'.format('avocado'))
    with settings(warn_only=True):
        run("sudo -i -u postgres psql -c \"CREATE USER {0} WITH PASSWORD '{1}';\"".format('avocado', 'veggieavocado2018'))
    run("sudo -i -u postgres psql -c \"ALTER ROLE {} SET client_encoding TO 'utf8';\"".format('avocado'))
    run("sudo -i -u postgres psql -c \"ALTER ROLE {} SET default_transaction_isolation TO 'read committed';\"".format('avocado'))
    run("sudo -i -u postgres psql -c \"ALTER ROLE {} SET timezone TO 'UTC';\"".format('avocado'))
    run("sudo -i -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE {0} TO {1};\"".format('avocado', 'avocado'))
    return True
