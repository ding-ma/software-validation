from behave.__main__ import main as behave_main
import random
import glob
import os

names = ["({})".format(os.path.basename(x)) for x in glob.glob('./features/*.feature')]
random.shuffle(names)
for name in names:
    behave_main(["./features", "--include", name])
