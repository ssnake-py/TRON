# TRON
a TRON like game based on Python


TRON Setup Tutorial (Arch Linux KDE)

1. Install Python

Open terminal and type:

sudo pacman -S python

Check if it works:

python --version

You should see something like:

Python 3.14.4


2. Install pygame

Type:

python -m pip install pygame


3. Create a folder called python

Type:

mkdir ~/python


4. Go into the folder

Type:

cd ~/python


5. Create an empty file called Tron.py

Type:

touch Tron.py


6. Open it in Kate

Type:

kate Tron.py


7. Paste the full TRON game script into the file

Save it with:

CTRL + S


8. Run the game

Type:

cd ~/python
python Tron.py


9. Add TRON to KDE Application Launcher

Create launcher file:

nano ~/.local/share/applications/tron.desktop


Paste this:

[Desktop Entry]
Name=TRON
Comment=Neon Tron Game
Exec=python /home/arch/python/Tron.py
Icon=applications-games
Terminal=false
Type=Application
Categories=Game;


10. Save nano file

Press:

CTRL + O
ENTER
CTRL + X


11. Make it executable

Type:

chmod +x ~/.local/share/applications/tron.desktop
chmod +x /home/arch/python/Tron.py


12. Refresh KDE launcher

Type:

kbuildsycoca6


Done.

Now open KDE Application Launcher, search:

TRON

Click it and the game will launch like a normal app.
