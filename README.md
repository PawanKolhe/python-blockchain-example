# Python Blockchain
This project is based on tutorial at [Tutorialpoint](https://www.tutorialspoint.com/python_blockchain/python_blockchain_developing_client.htm).

## Requirements
- [Python 3](https://www.python.org/downloads/)

## Notes
1. Use `python3` in terminal if `python` does not work.  
2. Make sure you are running python version 3 by entering following command: `python -V`  

## Environment Setup
#### 1. Clone project
```bash
git clone https://github.com/PawanKolhe/python-blockchain-example.git
cd ./python-blockchain-example
```

#### 2. Create and start a virtual environment
```bash
## Creating virtual environment
python -m venv .env
# or
python3 -m venv .env

## Starting virtual environment (use one of the following commands according to OS)

# Windows (PowerShell)
.env/Scripts/activate.ps1

# Windows (CMD)
.env/Scripts/activate.bat

# Linux/Mac
source .env/Scripts/activate
```
> _When dependencies are installed while virtual environment is activated, the dependencies will be stored in the .env folder and isolated from system dependencies._  
> Type `deactivate` to turn off virual environment  

#### 3. Install dependencies
```bash
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```
> This will install `pycryptodome` library

#### 4. Run app
```bash
python app.py
# or
python3 app.py
```
