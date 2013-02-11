#echo "Please enter the password for postgres"
sudo su postgres -c "
psql -c \"DROP DATABASE jtg_test;\";
psql -c \"CREATE DATABASE jtg_test OWNER jtg;\""

