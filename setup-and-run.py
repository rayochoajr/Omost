import subprocess
import sys
import os

def run_commands():
    project_path = os.path.dirname(os.path.abspath(__file__))
    venv_path = os.path.join(project_path, 'omost', 'Scripts', 'activate.bat' if os.name == 'nt' else 'activate')
    commands = [
        [sys.executable, '-m', 'venv', os.path.join(project_path, 'omost')],
        venv_path,
        [sys.executable, '-m', 'pip', 'install', 'torch', 'torchvision', '--index-url', 'https://download.pytorch.org/whl/cu121'],
        [sys.executable, '-m', 'pip', 'install', '-r', os.path.join(project_path, 'requirements.txt')],
        [sys.executable, os.path.join(project_path, 'gradio_app.py')]
    ]
    
    for command in commands:
        if isinstance(command, str):
            # Activate command needs to be run in shell mode but carefully
            command = f'call {command}' if os.name == 'nt' else f'source {command}'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=project_path)
        else:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=project_path)
        
        stdout, stderr = process.communicate()
        if stderr:
            print(f"Error while executing {' '.join(command) if isinstance(command, list) else command}:\n{stderr}")
        else:
            print(f"Output of {' '.join(command) if isinstance(command, list) else command}:\n{stdout}")

if __name__ == '__main__':
    run_commands()