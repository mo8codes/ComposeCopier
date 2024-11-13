# Compose Copier
Copies docker-compose.y(a)ml files into ../export_cc for your server distro hopping needs.

Instructions:
Assuming this file structure:
> ~/docker/*

Where * are all the folders for each docker container.

Run one of these commands to get the cc.py 

> curl -O https://raw.githubusercontent.com/mo8codes/ComposeCopier/main/cc.py

or

> wget https://raw.githubusercontent.com/mo8codes/ComposeCopier/main/cc.py

Finally:
> python3 ./cc.py

Now all compose files are in ~/export_cc/*/docker-compose.y\*ml
![image](https://github.com/user-attachments/assets/7b7ad433-a334-4ac6-9717-3ddaceaa69b8)
