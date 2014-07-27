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
conn.commit()
print "yes"









