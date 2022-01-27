Faire les mises à jours du raspberry
```bash
sudo apt update
sudo apt upgrade
```
Installer python3
```bash
sudo apt install python3
sudo apt install python3-venv
```
Installer git et télécharger le site
```bash
sudo apt install git
sudo git clone https://github.com/Francesco-fr/sn.git
```
Aller dans le projet puis installer flask
```bash
cd sn
. venv/bin/activate
pip install Flask
```
Mettre le pays pour le wifi
```bash
sudo raspi-config nonint do_wifi_country FR
```
