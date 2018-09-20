#!/bin/bash
service apache2 stop
a2enconf wsgi
/usr/sbin/apache2ctl -DFOREGROUND