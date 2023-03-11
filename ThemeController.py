import json
from ThemeEnum import Theme

class ThemeController():
    
    def __init__(self):
        self.theme = Theme.Light
        
    @property
    def theme(self):
        return self.__theme
    
    @theme.setter
    def theme(self, theme):
        self.__theme = theme
        self.__json = open(self.__theme.value)
        self.__colors: dict[str, str] = json.load(self.__json)
        self.__json.close()

    #Применение темы к QSS файлу
    def ApplyThemeToQSS(self, qssFile: str):
        for key in self.__colors:
            qssFile = qssFile.replace(key, self.__colors[key])
        return qssFile
    

    

    



        