import ConfigParser
def engine(path, time, size):
    config = ConfigParser.RawConfigParser()
    config.read('fTypes.cfg')
    pathTypes =  path.split('.')
    length = len(pathTypes)
    print length
    extention = pathTypes[length-1]
    print extention
engine("downloads/shit/tile.txt", "time", 100003)
