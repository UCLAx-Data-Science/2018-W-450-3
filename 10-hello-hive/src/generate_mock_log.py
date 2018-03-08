#!/bin/python3
import random
import socket
import os
import datetime as dt
import pathlib

def message(user, file):
    timestamp = dt.datetime.now().strftime("%b %d %H:%M:%S")
    host = "host-"+socket.gethostname()
    pid = os.getpid()
    messages = [
    "INFO: Login successful.".format(user),
    "WARNING: Login failed.".format(user),
    "SEVERE: Received SEGFAULT signal from process {}.".format(str(random.randint(0,1000))),
    "INFO: Logout occurred.".format(user),
    "INFO: File {} accessed.".format(user, file),
    "INFO: Password updated.".format(user),
    "SEVERE: Disk write failure.",
    "SEVERE: Unable to complete transaction - Out of memory.",
    ]
    message = [timestamp, host, __name__ + "[{}]".format(pid), random.choice(messages), user]
    return ','.join(message)

files = ["ipod","conditioner","glasses","cinder-block","thread","cookie-jar","lip-gloss","toothbrush","door","sandal","flowers","pencil","pen","phone","spring","speakers","air-freshener","purse","desk","video-games","fake-flowers","plate","socks","rusty-nail","washing-machine","pillow","cat","ring","candy-wrapper","coasters"]
users = ["Emerald","Cody", "Daniel", "Mitsuko", "Berenice", "Johnna", "Alexis", "Elinor", "Todd", "Ellan", "John", "Fidela", "Jenna", "Serita", "Millard", "Britt", "Jestine", "Geraldo", "Romelia", "Loan", "Eli", "Su", "Shavonda", "Arianna", "Margo", "Jasper", "Samella", "Brady", "Kallie", "Mariko", "Jonell", "Sonja", "Shaneka", "Katie", "Doreatha", "Annis", "Sanford", "Ned", "Nancee", "Lynnette", "Marco", "Miguelina", "Sam", "Karlyn", "Abby", "Lyda", "Pansy", "Howard", "Mariam", "Margart"]

if __name__ == "__main__":
    pathlib.Path('data').mkdir(parents=True, exist_ok=True) 
    with open('data/mock.log', 'w') as log:
        for _ in range(1000000):
            user = random.choice(users)
            file = random.choice(files)
            print(message(user, file), file=log)