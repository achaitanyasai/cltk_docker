#!/bin/bash

sudo docker run -d -it cltk bash
container_id=`sudo docker ps -a | awk 'FNR == 2 {print $1}'`
sudo docker cp tests/ $container_id:/
_command='nosetests --no-skip'
sudo docker exec $container_id $_command
