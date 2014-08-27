import sqlite3
import logging #for info logging
#logger setup
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)#adjust level to see different levels
'''General Class Setup Below'''

class nodes:
    def __init__(self, name, nodeType):
        self.Name = name
        self.Type = nodeType

class data:
    def __init__(self, name, dataType, data, date)
    self.Type = dataType
    self.data = data
    self.date = date




'''Run Order:
   makedb'''


def makedb():
    #db setup
    conn = sqlite3.connect('database.db')#intalizing db
    c = conn.cursor()
def makeTable(name):
    try:
        c.execute(''' SELECT * FROM ? ''', name)
        logger.info("Object under same name exists making changing name")
        name = name+"1"
        makeTable(name)
    except sqlite3.OperationalError:
        c.execute('''CREATE TABLE ?(Name text, valType text, description text, data text )''', name)

def addData():


def addConnection



def newNode(node):
    name = node.name
    nodetype = node.type
    makeTable(name)
