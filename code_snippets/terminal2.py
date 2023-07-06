#https://stackoverflow.com/questions/14894993/running-windows-shell-commands-with-python
#https://stackoverflow.com/questions/11615455/python-start-new-command-prompt-on-windows-and-wait-for-it-finish-exit
#https://stackoverflow.com/questions/19308415/execute-terminal-command-from-python-in-new-terminal-window
#https://stackoverflow.com/questions/62349170/pyqt-terminal-emulator   !!!!!!!!!
#https://stackoverflow.com/questions/51975678/embedding-a-terminal-in-pyqt5

#https://www.pythonguis.com/tutorials/qprocess-external-programs/
import subprocess
def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)