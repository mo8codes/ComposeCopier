import shutil
from pathlib import Path

# Create new folder "./export_cc" if it doesn't already exist
new_folder = Path('../export_cc')
new_folder.mkdir(parents=True, exist_ok=True)

# Get the current working directory
current_directory = Path.cwd()

# Loop through all folders and subfolders
for dir_path in current_directory.rglob('*'):
    if dir_path.is_dir():
        # Check if there is a docker-compose.yml or docker-compose.yaml file in the folder
        for compose_file in dir_path.glob('docker-compose.y*ml'):
            if compose_file.is_file():    
                # Make new folder in export_cc with the same name as the folder where the compose file is currently stored
                destination_folder = new_folder / dir_path.relative_to(current_directory)
                destination_folder.mkdir(parents=True, exist_ok=True)
                
                # Define the destination path for the copied file
                destination = destination_folder / compose_file.name
                
                # Convert both paths to absolute paths to avoid issues with relative vs absolute paths
                if compose_file.resolve() != destination.resolve():
                    # Copy the file to the new folder
                    shutil.copy(compose_file, destination)
                    print(f"Copied {compose_file} to {destination}")
