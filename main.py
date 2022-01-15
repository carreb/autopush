import os
import git
from git import Repo
import glob
from github import Github
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
info = config['info']
repo_name = info['repo_name']
owner_username = info['owner_username']
token = info['token']
branch = info['branch']
push_auto = info['push_automatically']
repo = Repo("./" + repo_name)


def main():
    while True:
        ft = "\*"
        f = glob.glob("./"+repo_name+ft)
        lf = str(max(f, key=os.path.getmtime))
        m = os.path.getmtime(lf)
        lf2 = lf.replace("./"+repo_name+"\\", "")
        t = time.time()
        if int(m) <= int(t) <= int(m) + 3:
            print("Modified! Attempting to commit...")
            try:
                repo.index.add([lf2])
                repo.index.commit("[AUTOMATED] " + "Commit " + lf2 + " from autopush")
                print("Successfully commited to head!")
                o = repo.remote('origin')
                if push_auto == "true".lower():
                    o.push()
                    print("Successfully pushed!")
            except:
                print("Failed to push!")
        time.sleep(2)

main()