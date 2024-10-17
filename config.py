import logging, sys
#Studio settings
def Settings():
    import os
    mDict = {
        "Server": {
            "Thread": None,
            "ListenPort": 8081, # Порт, по которому можно подключиться к демону
            "ListenURL": "0.0.0.0", # Сетевое расположение сервера демона
        },
        "Logger": None,
        "LoggerLevel": logging.INFO,
        "LoggerPathStr": "logs",
        "LoggerFileFormatStr": "%Y_%m_%d",
        "LoggerRowFormatStr": '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        "LoggerExtStr": 'log',
        "Storage": {
            "Robot_R01_help": "Robot data storage in orchestrator env",
            "Robot_R01": {}
        },
        "ProcessBitness": { #Section for robot init
            "Python32FullPath": "..\\Resources\\WPy32-3720\\python-3.7.2\\python.exe", #Set from user: "..\\Resources\\WPy32-3720\\python-3.7.2\\OpenRPARobotGUIx32.exe"
            "Python64FullPath": "..\\Resources\\WPy64-3720\\python-3.7.2.amd64\\python.exe", #Set from user
            "Python32ProcessName": "OpenRPAUIDesktopX32.exe", #Config set once
            "Python64ProcessName": "OpenRPAUIDesktopX64.exe" #Config set once
        }
    }
    return mDict