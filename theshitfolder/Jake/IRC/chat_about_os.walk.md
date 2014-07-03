menu
Status #pythonX #wordpressX ##securityX ##javascriptX #jqueryX #wikipedia-enX
[NO LOL | NO PROJECT EULER | Don't paste, use http://bpaste.net/+python | 2.x or 3.x? http://bit.ly/py2vs3k | Tutorial: http://bit.ly/MCAhYx | New programmer? http://goo.gl/c170V | Find your nearest Python User Group: http://goo.gl/S1Zsq | #python-fr #python.dev #python-es #python.tw #python.pl #python-br #python-nl #python-ir #python-fi #python.it #python-india]
[21:24] == jakesyl [442d5d98@gateway/web/freenode/ip.68.45.93.152] has joined #python
[21:24] -ChanServ- [#python] Welcome to #python, puny fleshlings. Please see our website, http://pound-python.org/ , for information about the channel and Python.
[21:24] <Boingo> I have been searching for a while, just getting ideas.
[21:24] <nedbat> Boingo: what is the prez about?
[21:24] <jakesyl> hey guys sorry to interrupt anyone know of a tree shell application but in python
[21:25] == cknoettg [~Thunderbi@68.200.166.19] has left #python []
[21:25] == biergaizi has changed nick to biergaizi_AFK
[21:25] == DJJeff [~Guest_365@24.86.168.13] has quit [Read error: Connection reset by peer]
[21:25] <Boingo> nedbat: Not really important, but there is a weekly meeting I attened (not python related) that I wanted to make some cool (read eye-candy) presentaions that loop in the background.
[21:25] == DTVD [~DTVD@91.144.197.113.dy.bbexcite.jp] has quit [Ping timeout: 272 seconds]
[21:25] <Boingo> Maybe names of members, stats for the group for the week, etc.
[21:26] <Boingo> Possibly read the stats out of a file/db and then in a flasy way animate them on to the screen.
[21:26] <Boingo> Doesn't really have to be powerpoint.
[21:26] <nedbat> Boingo: d3.js makes cool looking things
[21:26] <Boingo> Could even be pre-renderd.
[21:26] == atheriel [~atheriel@d207-216-160-202.bchsia.telus.net] has joined #python
[21:26] <joelmo> Boingo, the language processing is made just for such stuff
[21:26] == innertracks [~Thunderbi@c-50-135-138-138.hsd1.wa.comcast.net] has quit [Quit: innertracks]
[21:26] == OverNord [~brn@host-091-097-165-032.ewe-ip-backbone.de] has quit [Quit: OverNord]
[21:26] == biergaizi_AFK has changed nick to biergaizi
[21:27] <jakesyl> so anyone know of anything like that  or something to interact with all files on a system
[21:27] == apg [~Thunderbi@unaffiliated/apg] has joined #python
[21:27] <Boingo> joelmo: Huh?  Did I miss a message?
[21:27] == kexmex [~kexmex@ool-4a586221.dyn.optonline.net] has quit [Quit: Computer has gone to sleep.]
[21:27] * jakesyl
[21:27] * jakesyl is cool
[21:27] * jakesyl needs help
[21:27] <joelmo> Boingo, see here https://www.processing.org/examples/
[21:27] == mathemancer [~mathemanc@50.23.131.235-static.reverse.softlayer.com] has quit [Ping timeout: 244 seconds]
[21:28] == sunya7a_ [~pryde@unaffiliated/sunya7a] has quit [Quit: leaving]
[21:28] <simpson> jakesyl: What are you building?
[21:28] == silphium [~jrjohnsto@173-81-201-66.chstcmtk02.res.dyn.suddenlink.net] has joined #python
[21:28] <Boingo> joelmo: Still confused as to what I am looking at on here.
[21:29] <jakesyl> simpson well its a cloud based storage service, but the first thing i need to do is index every file on the system and i thought i could modify some existing tree type application to do it,
[21:29] * sPiN- can talkin the 3rd person too!
[21:29] == gustavw [~gustavw@c213-89-120-93.bredband.comhem.se] has joined #python
[21:29] == fluter [~fluter@fedora/fluter] has joined #python
[21:29] == seanmcl [~seanmcl@cpe-74-73-230-234.nyc.res.rr.com] has joined #python
[21:31] <nedbat> jakesyl: os.walk is a good thing
[21:32] == Ariel_Calzada [~aricalso@186.82.232.130] has quit [Quit: Bye all]
[21:32] == seanmcl [~seanmcl@cpe-74-73-230-234.nyc.res.rr.com] has quit [Client Quit]
[21:32] == franzip [~Administr@2-226-58-214.ip179.fastwebnet.it] has quit [Quit: ...]
[21:32] == Corey84 [~Corey84@unaffiliated/corey84] has joined #python
[21:32] <jakesyl> nedbat is this basically what you mean: http://goo.gl/H7lPRL
[21:32] == joelmo [~joelmo@s213-103-207-206.cust.tele2.se] has quit [Quit: Leaving]
[21:32] == kaos01 [~kaos01@12.186.233.220.static.exetel.com.au] has joined #python
[21:33] == Maverous [~Ryan@rrcs-50-75-130-226.nys.biz.rr.com] has joined #python
[21:33] <nedbat> jakesyl: yes, though this page doesn't *look* like a trustworthy page.
[21:33] <jakesyl> sorry, i'm a big fan of third party documentation, i'm a php dev by trade so
[21:34] == gustavw [~gustavw@c213-89-120-93.bredband.comhem.se] has quit [Ping timeout: 255 seconds]
[21:34] <nedbat> jakesyl: third-party is fine, but the code should at least be monospaced....
[21:35] <jakesyl> oh true
 <nedbat> jakesyl: http://pymotw.com/2/os/index.html#walking-a-directory-tree
[21:36] == csotelo [~csotelo@190.41.210.210] has quit [Remote host closed the connection]
[21:36] == Bryson [~Bryson@184.2.174.149] has joined #python
[21:36] == sarodj [~pr0nstar@unaffiliated/sarodj] has joined #python
[21:37] <jakesyl> so i can do this from ~ out
[21:37] == sarodj_ [~pr0nstar@unaffiliated/sarodj] has quit [Ping timeout: 260 seconds]
[21:37] == jpadilla [~jpadilla@cvx-ppp-66-50-145-104.coqui.net] has joined #python
[21:38] <nedbat> jakesyl: sure.  os.path.expanduser() will help too
[21:36] <nedbat> jakesyl: http://pymotw.com/2/os/index.html#walking-a-directory-tree
[21:36] == csotelo [~csotelo@190.41.210.210] has quit [Remote host closed the connection]
[21:36] == Bryson [~Bryson@184.2.174.149] has joined #python
[21:36] == sarodj [~pr0nstar@unaffiliated/sarodj] has joined #python
[21:37] <jakesyl> so i can do this from ~ out
[21:37] == sarodj_ [~pr0nstar@unaffiliated/sarodj] has quit [Ping timeout: 260 seconds]
[21:37] == jpadilla [~jpadilla@cvx-ppp-66-50-145-104.coqui.net] has joined #python
[21:38] == jpadilla [~jpadilla@cvx-ppp-66-50-145-104.coqui.net] has quit [Client Quit]
[21:38] <nedbat> jakesyl: sure.  os.path.expanduser() will help too
[21:38] == l3lu3 [~l3lu3@unaffiliated/l3lu3] has left #python []
[21:38] <wescotte> Does Facebook no longer let you sync contacts in 4.4.2?
[21:39] == silphium [~jrjohnsto@173-81-201-66.chstcmtk02.res.dyn.suddenlink.net] has quit [Quit: Leaving.]
[21:39] == Bryson [~Bryson@184.2.174.149] has quit [Client Quit]
[21:40] == Wild_Cat [~Max@206-248-128-92.dsl.teksavvy.com] has joined #python
[21:40] == crc32 [crc32@nat/rackspace/x-uadvuquzcqolxljc] has quit [Quit: Textual IRC Client: www.textualapp.com]
[21:40] == zacts- [~AndChat41@freebsd/geek/zacts] has joined #python
[21:40] == sboudrias [~sboudrias@2601:9:3480:11b9:88b3:b4af:9dfc:8540] has quit [Ping timeout: 240 seconds]
[21:41] == ekinmur [~ekinmur@c-98-204-177-40.hsd1.va.comcast.net] has joined #python
[21:41] == nxiety [~nxiety@c-174-49-85-181.hsd1.ga.comcast.net] has quit [Quit: WeeChat 0.4.3]
[21:41] == darkbasic [~quassel@niko.linuxsystems.it] has quit [Remote host closed the connection]
[21:41] == comand [~comand@2620:79:0:164:1ec1:deff:fe33:c08d] has quit [Quit: Bye]
[21:41] <nedbat> wescotte: is that a python quesion?
[21:42] <jakesyl> nedbat: are there any diffs between the two
[21:42] <nedbat> jakesyl: two what?
[21:42] == darkbasic [~quassel@niko.linuxsystems.it] has joined #python
[21:42] <jakesyl> os.walk and os.expanduser()
[21:42] <nedbat> jakesyl: os.walk and os.path.expanduser do completely different things
[21:43] <jakesyl> which are, sorry I haven't had a chance to read through each one yet
[21:43] <nedbat> jakesyl: i'm not in a hurry, take your time :)
[21:43] == ePirat [~ePirat@unaffiliated/epirat] has quit [Quit: Palaver!]
