from pathlib import Path
import sys
check = False;
for path in Path('src').rglob('*.js'):
    with open(path) as f:
        if '//Student Name: Reece Brown' in f.read():
            with open(path) as newF:
                if '//Student ID: 1365178' in newF.read():
                    check = True
                else:
                    check = False
                    sys.stdout.write('0')
                    sys.exit(0)
        else:
            check = False
            sys.stdout.write('0')
            sys.exit(0)
sys.stdout.write('1')
sys.exit(0)