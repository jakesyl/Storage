[00:01] <jakesyl> Hey guys in sqllite3 how do i tell if the SELECT returned nothing in an if statement
[00:02] == sboudrias [~sboudrias@2601:9:3480:11b9:5cec:aeac:a5c5:18eb] has joined #python
[00:02] <KirkMcDonald> toothe: Given a single-character byte-string, it returns the integer value of that byte.
[00:02] == WeiJunLi [~juiuk@a85-138-2-144.cpe.netcabo.pt] has quit []
[00:02] <KirkMcDonald> toothe: Given a unicode string of length 1, it returns the value of the code point as an integer.
[00:03] <toothe> KirkMcDonald: ohhh....
[00:03] <toothe> KirkMcDonald: Suddenly the documentation make sense
[00:03] <jakesyl> anyone know sqllite3
[00:03] == E1ven [~E1ven@SQ7/ProjectLead/E1ven] has quit [Quit: Quit]
[00:03] <toothe> I don't
[00:04] == wolrah_ [~wolrah@24.239.210.140] has joined #python
[00:04] <KirkMcDonald> JodaZ: You could, for example, call cursor.fetchall() and check the length of the thing you get.
[00:04] <KirkMcDonald> Bah
[00:04] <KirkMcDonald> jakesyl: You could, for example, call cursor.fetchall() and check the length of the thing you get.
[00:04] <portablejim> JodaZ, It is to be a downloadable file, so mp3 is currently king. For about 20-30 mins of audio we currently get (using a system which I am seeking to replace) a 2-3mb MP3 for dialup users, a ~8mb MP3 and an opus.
[00:04] == wolrah [~wolrah@24.239.210.140] has quit [Ping timeout: 252 seconds]
[00:04] == gshmu [~saas@58.247.132.250] has joined #python
[00:05] <jakesyl> oh can i just do len of a returned string
[00:05] <JodaZ> portablejim, system sounds fine, if it even has opus
[00:05] <jakesyl> c.execute and then length of that
[00:06] == bearman [79d3740b@gateway/web/freenode/ip.121.211.116.11] has joined #python
[00:06] <KirkMcDonald> jakesyl: The return value of cursor.execute() is not specified by the Python DB API.
[00:06] == BigOrangeSU [~bigorange@pool-108-24-49-84.cmdnnj.fios.verizon.net] has joined #python
[00:06] == ntio [~ntio@gateway/tor-sasl/ntio] has quit [Quit: WeeChat 0.4.3]
[00:06] == sboudrias [~sboudrias@2601:9:3480:11b9:5cec:aeac:a5c5:18eb] has quit [Ping timeout: 240 seconds]
[00:06] <KirkMcDonald> jakesyl: Though some modules do return the number of rows returned/affected.
[00:06] <jakesyl> okay thanks