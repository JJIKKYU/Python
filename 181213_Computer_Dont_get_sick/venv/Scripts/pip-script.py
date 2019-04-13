#!"C:\Users\jjikk\OneDrive - 홍익대학교\00_ 홍익대학교\2학년 2학기\3_ 게임프로토타입연구\3_ Final Project\2_ Develop\venv\Scripts\python.exe" -x
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==10.0.1','console_scripts','pip'
__requires__ = 'pip==10.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==10.0.1', 'console_scripts', 'pip')()
    )
