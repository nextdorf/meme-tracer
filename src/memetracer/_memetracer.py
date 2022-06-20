import praw
import os
import platform
import pathlib
from ._version import version

iniBotID = 'meme-tracer-bot'

def initIniFile():
  iniPath = pathlib.Path.cwd() / 'praw.ini'
  if not pathlib.Path.exists(iniPath):
    runningOS = platform.system()
    if runningOS == 'Windows':
      iniPath = pathlib.Path(os.environ.get('APPDATA')) / 'praw.ini'
    elif runningOS in ['Linux', 'Darwin']:
      iniPath = pathlib.Path(os.environ.get('HOME')) / '.config/praw.ini'
    else:
      runningOS = None
    if runningOS is None or not pathlib.Path.exists(iniPath):
      with open(iniPath, 'w+') as _:
        pass

  with open(iniPath, 'r') as f:
    l = True
    iniBotIDStr = f'[{iniBotID}]'
    while l:
      l = f.readline().strip()
      if l == iniBotIDStr:
        return iniPath

  with open(iniPath, 'a') as f:
    botID = 'Lh-56ml68XQvmT-eFaSXKw' #Since it's an installed app, it's OK to make this public
    f.write(f'[{iniBotID}]\nclient_id={botID}\n\n')
  return iniPath
  
iniPath = initIniFile()

useragent = f'Python:com.github.nextdorf.meme-tracer:ver{version} (by u/meme-tracer)'
reddit = praw.Reddit(iniBotID, user_agent=useragent, client_secret=None)
rMe = reddit.user.me()
reddit.config.user_agent

