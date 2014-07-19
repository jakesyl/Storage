'''
Creates database and subsequent tables on users computer
'''
import sqlite3
conn = sqlite3.connect('database.db')#intalizing db
c = conn.cursor()
#setting up all of the tables

#test for fileMap
try:
    c.execute(''' SELECT * FROM  fileMap''')#whaqt the fuck is a file map
except sqlite3.OperationalError:
#files
    c.execute('''CREATE TABLE fileMap(fpath text, size text)''')



try:
    c.execute(''' SELECT * FROM  scan''')
except sqlite3.OperationalError:
#files
    c.execute('''CREATE TABLE scan(fpath text, accessDate integer)''')



try:
    c.execute(''' SELECT * FROM  noUpload''')#catching crash
except sqlite3.OperationalError:
#no upload list
    c.execute('''CREATE TABLE noUpload(fpath text)''')



try:
    c.execute(''' SELECT * FROM  noUpload''')#catching crash
except sqlite3.OperationalError:
#no upload
    c.execute('''CREATE TABLE noUpload(fpath text)''')




try:
    c.execute(''' SELECT * FROM  extentions''')#catching crash
except sqlite3.OperationalError:
#extenstions
    c.execute('''CREATE TABLE extentions(ext text, count integer)''')





# time to add all of the extions WOOT WOOT
extentions = ("png", "jpg", "jpeg", "jfif", "jpeg2000", "ani","anim","apng","art","bmp","psd","bsave","cal","cin","cpc","cpt","dpx","ecw","exr","fits","flic","fpx","gif","hdri","hevc","icer","icns","ico","cur","ics","ilbm","jbig","jbig2","jng","jpeg-ls","jpegxr","mng","miff","pam","pbm","pgm","ppm","pnm","pcx","pgf","pictor","psb","psp","qtvr","ras","rbe","jpeg-hdr","sgi","tga","wbmp","webp","xbm","xcf","xpm","xwd","ciff","dng","ai","cdr","cgm","dxf","eva","emf","gerber","hvif","iges","pgml","svg","vml","wmf","xar","cdf","djvu","eps","pdf","pict","ps","swf","xaml","mpg","mov","wmv","rm","mp4","mpeg","mpg","mpe","mpeg","mpeg-1","mpeg-2","m1s","mpa","mp2","m2a","mp2v","m2v","m2s","avi","qt","asf","asx","wma","mkv","3gp","act","aiff","aac","amr","au","awb","dct","dss","dvf","flac","gsm","iklax","ivs","m4a","m4p","mmf","mp3","mpc","msv","ogg","oga","opus","ra","rm","raw","tta","vox","wave","wma","wv")
count = 0
for ext in extentions:
    ext = (ext, count, )
    c.execute('INSERT INTO extentions(ext, count) VALUES(?,?)',ext)
for row in c.execute('SELECT * FROM extentions WHERE ext = "mp4"'):
    if len(row) != 0:
        print "shit"













def engine(path, time, size):
    #getting file etentions
    pathTypes =  path.split('.')
    length = len(pathTypes)
    extention = pathTypes[length-1]
    extention = (extention,)
    print extention
    #checks for proper extetion
    for row in c.execute('SELECT * FROM extentions WHERE ext=?', extention):
        print row
        if len(row) != 0:
            # get readable date from file
            date = datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
            date = date.split(" ")
            date = date[0].split("-")
            # get current timestamp
            timestamp = int(time.time())
            #get date from current
            date1 = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
            date1 = date.split(" ")
            date1 = date[0].split("-")
            #check if it is within the month
            if date1[1] == date[1] and date1[0] == date[0]:
                #check if it is withn the last two days
                if date1[2] == date[2] or date1[2] == date[2]-1 or date1[2] == date[2]-2:
                    #if so dont upload
                    print"shit3"
                    return False
                #if not dont upload
                else:
                    print "shit2"
                    return True
                #if not within the month no need to check just upload
            else:
                print "shit1"
                return True
            #if not proper extention dont upload
        else:
            print "shit"
            return False
print engine("downloads/shit/tile.mp4", 1405738428, 10003)
