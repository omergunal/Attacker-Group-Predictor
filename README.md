# Attacker-Group-Predictor
The tool predicts attacker groups from techniques and softwares used. It searches based on the MITRE ATT&CK™ framework

### How it works?

* 1- Collect data from mitre.org about attacker groups
* 2- Get data from user about attack
* 3- Compare data and create result

### Installation
```
git clone https://github.com/omergunal/Attacker-Group-Predictor.git
cd Attacker-Group-Predictor/
pip3 install -r requirements.txt
```


### Usage
```
python3 main.py
Fill the inputs
```

### Example
```
python3 main.py
  Techniques used (ID or Name) (Seperate with comma):Brute Force,Commonly used port,connection proxy,Credential dumping
  Softwares used (ID or Name) (Seperate with comma):Bankshot,mimikatz,Rawdisk

  Most probable groups:
    Lazarus Group
    APT33
    menuPass
    Threat Group-3390
    APT41


```

### ScreenShots

![example](https://github.com/omergunal/Attacker-Group-Predictor/blob/master/img/example.PNG)

