# benchdb

Back-end database for benchmark tool

# Database Setup

```
sudo su
psql
>CREATE DATABASE bench_db;
>CREATE USER postgres WITH PASSWORD 'postgres';
>GRANT ALL PRIVILEGES ON DATABASE bench_db TO postgres;
>\q
exit
```  

# Python Setup

```
yum install -y postgresql-devel
python3 --version
python3 -m venv env
source env/bin/activate
pip install django psycopg2
python3 -m django --version
```
