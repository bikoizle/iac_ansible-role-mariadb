

def test_mariadb_is_working(host):
    cmd = host.run("mysql -e 'SHOW DATABASES;' -u root --password=insecure")
    assert cmd.rc == 0

def test_mariadb_test_user_is_gone(host):
    cmd = host.run("mysql -e 'SHOW DATABASES;'")
    assert cmd.rc == 1
