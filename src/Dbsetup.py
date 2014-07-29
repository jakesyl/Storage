'''
Creates database and subsequent tables on users computer
'''
import sqlite3
import logging #for info logging

def makedb():
    #logger setup
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)#adjust level to see different levels of stuff

    #db setup
    conn = sqlite3.connect('database.db')#intalizing db
    c = conn.cursor()
    #setting up all of the tables

    #test for fileMap
    try:
        c.execute(''' SELECT * FROM  fileMap''')#what the fuck is a file map
    except sqlite3.OperationalError:
    #files
        c.execute('''CREATE TABLE fileMap(fpath text, size text)''')
        logger.info("Table filemap doesn't exsist creating it")



    try:
        c.execute(''' SELECT * FROM  scan''')
    except sqlite3.OperationalError:
    #files
        c.execute('''CREATE TABLE scan(fpath text, accessDate integer)''')
        logger.debug("table scan doesn't exsist creating it")


    try:
        c.execute(''' SELECT * FROM  noUpload''')#catching crash
    except sqlite3.OperationalError:
    #no upload list
        c.execute('''CREATE TABLE noUpload(fpath text)''')
        logger.info("Table noUpload doesn't exsist creating it")



    try:
        c.execute(''' SELECT * FROM  noUpload''')#catching crash
    except sqlite3.OperationalError:
    #no upload
        c.execute('''CREATE TABLE noUpload(fpath text)''')
        logger.info("Table noUpload doesn't exsist creating it")




    try:
        c.execute(''' SELECT * FROM  extentions''')#catching crash
    except sqlite3.OperationalError:
    #extenstions
        c.execute('''CREATE TABLE extentions(ext text, count integer)''')
        logger.info("Table extenstions doesn't exsist creating it")






    # time to add all of the extions WOOT WOOT
    extentions = ("png", "jpg", "jpeg", "jfif", "jpeg2000", "ani","anim","apng","art","bmp","psd","bsave","cal","cin","cpc","cpt","dpx","ecw","exr","fits","flic","fpx","gif","hdri","hevc","icer","icns","ico","cur","ics","ilbm","jbig","jbig2","jng","jpeg-ls","jpegxr","mng","miff","pam","pbm","pgm","ppm","pnm","pcx","pgf","pictor","psb","psp","qtvr","ras","rbe","jpeg-hdr","sgi","tga","wbmp","webp","xbm","xcf","xpm","xwd","ciff","dng","ai","cdr","cgm","dxf","eva","emf","gerber","hvif","iges","pgml","svg","vml","wmf","xar","cdf","djvu","eps","pdf","pict","ps","swf","xaml","mpg","mov","wmv","rm","mp4","mpeg","mpg","mpe","mpeg","mpeg-1","mpeg-2","m1s","mpa","mp2","m2a","mp2v","m2v","m2s","avi","qt","asf","asx","wma","mkv","3gp","act","aiff","aac","amr","au","awb","dct","dss","dvf","flac","gsm","iklax","ivs","m4a","m4p","mmf","mp3","mpc","msv","ogg","oga","opus","ra","rm","raw","tta","vox","wave","wma","wv")
    count = 0
    for ext in extentions:
        ext = (ext, count, )
        c.execute('INSERT INTO extentions(ext, count) VALUES(?,?)',ext)
    conn.commit()
    logger.info("Completed table creation")








