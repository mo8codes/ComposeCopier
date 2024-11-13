# Compose Copier
Copies docker-compose.y(a)ml files into ../export_cc for your server distro hopping needs.

Instructions:
Assuming this file structure:
> ~/docker/*
Where * are all the folders for each docker container.

Run one of these commands to get the cc.py 

> curl -O https://raw.githubusercontent.com/mo8codes/ComposeCopier/main/cc.py
Alpine doesn't have curl by default but it does have wget so if curl doesn't work try this:
> wget https://raw.githubusercontent.com/mo8codes/ComposeCopier/main/cc.py

Alpine doesn't have python3 either:
> apk add python3

You could also try this (untested and not reccomended):
> git clone https://github.com/mo8codes/ComposeCopier
> mv ./ComposeCopier/cc.py ./
> rm -rf ./ComposeCopier 

Finally
> python3 ./cc.py

Then all compose files should be in ~/export_cc