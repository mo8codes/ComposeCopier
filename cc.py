import shutil
from pathlib import Path

# Create new folder "./exported_compose_files" if it doesn't already exist
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
                # Print to show that a docker-compose file was found
                #print(f"Found file: {compose_file}")
                
                # Define the destination path for the copied file
                destination = new_folder / dir_path / compose_file.name
                
                # Convert both paths to absolute paths to avoid issues with relative vs absolute paths
                if compose_file.resolve() != destination.resolve():
                    # Copy the file to the new folder
                    shutil.copy(compose_file, destination)
                    print(f"Copied {compose_file} to {destination}")
                else:
                    pass #print(f"Skipped copying {compose_file}, as it is already in the destination.")