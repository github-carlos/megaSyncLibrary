from subprocess import Popen, PIPE, STDOUT
import os

def runCommandLine(command):
    resultofcommand = Popen(command, stdout=PIPE, stderr=STDOUT)
    # loop para esperar ate que todos comandos sejam executados
    while True:
        retcode = resultofcommand.poll()  # returns None while subprocess is running
        line = resultofcommand.stdout.readline()
        yield line
        if retcode is not None:
            break


def syncbooks(filesPath):
    pass


def filterNotUploadedFiles(__localfiles, __remotefiles):
    # convert to string
    __remotefiles = map(str, __remotefiles)

    filesInRootBiblioteca = map(lambda p: p[2:-3], filter(isInsideBibliotecaFolder, __remotefiles))
    for i in filesInRootBiblioteca:
        print(i)


def isInsideBibliotecaFolder(path):
    if str(path).__contains__('Biblioteca/'):
        return True
    return False


if __name__ == "__main__":
    remotefiles = runCommandLine("megals")
    listremotefiles = list(remotefiles)

    localfiles = os.listdir("/home/carlos/Documentos/Biblioteca")
    # for i in localfiles:
    #    print(i)
    filterNotUploadedFiles(localfiles, listremotefiles)
