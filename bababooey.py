import random
import threading
import pathlib
import pygame
import sys
import shutil
from win32comext.shell import shell, shellcon

# https://stackoverflow.com/a/43618925
def get_startup_directory(common):
    """
    Copyright Tim Golden <winshell@timgolden.me.uk> 25th November 2003 - 2012
    Licensed under the (GPL-compatible) MIT License:
    http://www.opensource.org/licenses/mit-license.php
    """
    return pathlib.Path(shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0))

def copy_to_startup():
  current_file = pathlib.Path(sys.argv[0])
  file_in_startup = get_startup_directory(0) / current_file.name
  if not file_in_startup.exists():
    shutil.copy(current_file, get_startup_directory(0))

def main():
  copy_to_startup()
  script_directory = pathlib.Path(__file__).parent
  pygame.mixer.init()
  pygame.mixer.music.load(script_directory / 'bababooey.wav')
  pygame.mixer.music.set_volume(0.15)
  event = threading.Event()
  random.seed()
  secondsBetweenBababooey = random.randrange(900, 3600)

  while True:
    event.wait(secondsBetweenBababooey)
    pygame.mixer.music.play()
    secondsBetweenBababooey = random.randrange(900, 3600)

if __name__ == '__main__':
  main()