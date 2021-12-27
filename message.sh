#! /bin/bash

code=`ss -ntl | grep 3344`
if [ -z "$code" ]; then
	 python message/main.py
else
	echo "正在运行"
fi
