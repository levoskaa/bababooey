<div align="center">

# Bababooey
</div>

This project was my way of pranking one of my roommates: once started, the script will play the ["bababooey"](https://www.youtube.com/watch?v=ia3Tc9FTgk0)
sound effect every 15-60 minutes. It's not often enough to make the victim suspicious of something at first, they might think that they misheard it or
that it was coming from elsewhere.

## Usage
If you want to prank someone as well, I recommend using one of the executables from the [releases](https://github.com/levoskaa/bababooey/releases). You can also
make the application start with Windows by copying the .exe file into the *C:\Users\\\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup*
folder. You should also rename the .exe file before starting it, so even if they start looking for it in the task manager the name won't stick out. I personally used
*Sink for asynchronous services.exe*.

## Creating your own version
The time intervals are easy to change and replacing the audio file with another one is pretty straightforward as well, so you can customize the script to your needs.

I used *pyinstaller* to bundle everything into an executable:
```
pyinstaller -w -F -i "NONE" --add-data "bababooey.wav;." --log-level "WARN" bababooey.py
```
