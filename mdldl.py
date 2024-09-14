import os
import json
import subprocess

def process(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json.mdl'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r') as f:
                        json_data = json.load(f)
                        
                    download_link = json_data.get("downloadLink")
                    download_method = json_data.get("prefferedDownloadMethod")

                    if download_link and download_method:
                        print(f"Processing {file} using {download_method}...")
                        
                        os.chdir(root)
                        
                        if download_method == "gdown":
                            command = f"gdown {download_link}"
                        elif download_method == "git":
                            command = f"git clone {download_link}"
                        elif download_method == "wget":
                            command = f"wget {download_link}"
                        else:
                            print(f"Unknown download method: {download_method} for {file}")
                            continue
                        
                        # Execute the command
                        try:
                            subprocess.run(command, shell=True, check=True)
                            print(f"Successfully processed {json_data.get('modName')} using {download_method}.")
                        except subprocess.CalledProcessError as e:
                            print(f"Failed to run {download_method} for {file}: {e}")
                    else:
                        print(f"Missing required fields in {file}")
                
                except Exception as e:
                    print(f"Failed to load or process {file}: {e}")


directory_path = './'
process(directory_path)
