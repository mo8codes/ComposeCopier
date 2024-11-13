# Compose Copier
Copies docker-compose.y(a)ml files into "./exported_compose_files" for your server distro hopping needs.

Reccomended usage instructions: (Currently untested just preparing for my own Copy-&-Pasting pleasures.)
Assuming this file structure
~/docker/*
Where * are all the folders for each docker container.

Run one of these commands to get the cc.py 

> curl -O https://raw.githubusercontent.com/mo8codes/ComposeCopier/main/cc.py

You could also try this:
> git clone https://github.com/mo8codes/ComposeCopier
> mv ./ComposeCopier/cc.py ./
> rm -rf ./ComposeCopier 

Finally
> python3 ./cc.py