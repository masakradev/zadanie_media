#!/usr/bin/env bash
MYSQL_PASSWORD="$1";
mysql -uroot -p"$MYSQL_PASSWORD" -h127.0.0.1 </docker/zad.sql;
