from cx_Freeze import setup, Executable
base = None
executables = [Executable("E:/Programmation/visualstudio\python/notif_bureau/main.py",
                          base=base)]
##Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna", "psutil", "plyer", "time", "matplotlib.pyplot"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
##Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Battery Notification",
    options = options,
    version = "1.0",
    executables = executables
)