# python-mirrorhub
Python3 module for interacting with the mirrorhub.io API and managing the mirror docker container


## Installation
You can either clone this repository and run the setup.py ...
```bash
git clone https://github.com/mirrorhub-io/python-mirrorhub.git
cd python-mirrorhub
python3 setup.py
```

... or install the module using pip.
```bash
pip3 install git+https://github.com/mirrorhub-io/python-mirrorhub.git
```

## shipped CLI tools
### init_container
Initscript will be executed, while starting the docker container, through the Dockerfile. It requires the ENV variable CLIENT_TOKEN to be set.
