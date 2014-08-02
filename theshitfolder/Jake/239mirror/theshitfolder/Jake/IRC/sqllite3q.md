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
[00:04] <KirkMcDonald> jakesyl: You could, for example, call cursor.feistchall() and check the length of the thing you get.
[00:04] <portablejim> JodaZ, It is to be a downloadable file, so mp3  currently king. For about 20-30 mins of audio we currently get (using a system which I am seeking to replace) a 2-3mb MP3 for dialup users, a ~8mb MP3 and an opus.
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
[00:26] <jakesyl> when i do call cursor.fetchall() do i use what i defined the cursor as or type cursor (KirkMcDonald)
[00:26] <spaceshiiiiiip> KirkMcDonald: http://pastebin.com/raw.php?i=1Mc9kDFU/
[00:26] <infobob> http://paste.pound-python.org/show/ooLrZtnNA28HbvVnzQ1K/ (repasted for spaceshiiiiiip)
[00:26] <KirkMcDonald> jakesyl: You call that on the same cursor object you called cursor.execute() on.
[00:27] == dougia [~dougia@S010684c9b250dc8c.gv.shawcable.net] has joined #python
[00:28] <jakesyl> and kirk do i do call cursor.fetchall('commands')
[00:28] <jakesyl> or do i do         clustery = c.execute('SELECT * FROM clusters WHERE contents = '+ path);
[00:28] <jakesyl> and then perform cursor.fetchall on clustery
[00:28] <KirkMcDonald> jakesyl: Yes, that. First you call c.execute, then you call c.fetchall() with no arguments.
[00:28] <KirkMcDonald> jakesyl: And fetchall() returns a list.
[00:29] <jakesyl> so not c.fetchall(clustery)
[00:29] <jakesyl> so do i even have to set the execute to a variable if I'm just seeing if its empty
[00:29] <KirkMcDonald> jakesyl: c.execute("SELECT * FROM clusters WHERE contents = ?", [path]); clusters = c.fetchall()
[00:29] <KirkMcDonald> jakesyl: You don't use the return value from c.execute() at all.
[00:30] == jontmorehouse [~jonmoreho@2605:e000:4202:dd00:9867:59bb:ee9e:fce1] has quit [Read error: Connection reset by peer]
[00:30] <jakesyl> well i was returning it by setting it to the var clustery
[00:30] == jontmorehouse [~jonmoreho@2605:e000:4202:dd00:9867:59bb:ee9e:fce1] has joined #python
[00:30] <jakesyl> so i set c.fetchall to a variable and if the length of that is zero then it found nothing, got it
[00:30] == ntio [~ntio@gateway/tor-sasl/ntio] has quit [Quit: WeeChat 0.4.3]
[00:31] == ntio [~ntio@gateway/tor-sasl/ntio] has joined #python
[00:31] == ValicekB [~tbox@dot.snat.baz.cz] has joined #python
[00:31] == ParokshaX [~ParokshaX@unaffiliated/parokshax] has quit [Ping timeout: 244 seconds]
[00:32] == dennisw [~dennis@104-10-140-195.lightspeed.hstntx.sbcglobal.net] has quit [Ping timeout: 240 seconds]
[00:32] == emperorcezar [~emperorce@24.14.228.224] has joined #python
[00:33] <jakesyl> KirkMcDonald, one more question if fetchal did return something in what format would thae data be returned
[00:33] <KirkMcDonald> jakesyl: A list of tuples.
[00:33] == spaceshiiiiiip [~spaceshii@unaffiliated/spaceshiiiiiip] has quit [Quit: Leaving.]
[00:34] <jakesyl> even if there's only one result
[00:34] == spaceshiiiiiip [~spaceshii@unaffiliated/spaceshiiiiiip] has joined #python
[00:34] <KirkMcDonald> jakesyl: Yes.
[00:34] <KirkMcDonald> jakesyl: If you're only expecting one result, you could call c.fetchone() instead.
[00:34] <KirkMcDonald> jakesyl: Which will either return the single tuple, or None if there is no data.
[00:34] == hiptobecubic [~john@unaffiliated/hiptobecubic] has quit [Ping timeout: 272 seconds]
[00:34] <jakesyl> does that stop after it gets one? (more effecient)
[00:35] <KirkMcDonald> jakesyl: It fetches a single result each time it is called, until there are no more results, when it will return None.
[00:36] <jakesyl> and, if there's only one result on a tuple it doesn't act as an array
[00:36] <KirkMcDonald> jakesyl: I am not sure what you mean.
[00:36] <jakesyl> so instead of setting it to clustery[0] I can simply set it to clustery
[00:36] <KirkMcDonald> jakesyl: No, if the tuple only has one element, you will still need to index the tuple to get that element.
[00:36] <jakesyl> so clustery[0]
[00:37] <Ofek> in tkinter can you, say, draw a circle or something WITHOUT creating a window? so it just appears on the screen somewhere?
[00:37] <KirkMcDonald> Yes.