[15:43] == jakesyl [442d5d98@gateway/web/freenode/ip.68.45.93.152] has joined #python
[15:43] -ChanServ- [#python] Welcome to #python, puny fleshlings. Please see our website, http://pound-python.org/ , for information about the channel and Python.
[15:43] == Balliad [~textual@52D95C9B.cm-11-1b.dynamic.ziggo.nl] has quit [Client Quit]
[15:43] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 264 seconds]
[15:44] <Zeeh> gotta look at lsml i guess
[15:44] == nect [~nect@igate.tc.faa.gov] has quit [Read error: Connection reset by peer]
[15:44] <Zeeh> lxml*
[15:44] <jakesyl> hey guys, I've tried excluding, but does anyone know how i can stay out of applications dir in os.walk code: https://gist.github.com/jakesyl/da40ac2416bb2147068a
[15:45] == doctorpenguin [~doctorpen@dhcp-222-55.wireless.resnet.bloomu.edu] has joined #python
[15:45] == dvx [~dvx@igw.obsm.cz] has quit [Quit: dvx]
[15:46] == f13o [~f13o@2001:770:100:81da:626c:66ff:fe00:e353] has quit [Quit: Leaving]
[15:46] == rippa [~rippa@176.100.246.238] has quit [Quit: {#`%${%&`+'${`%&NO CARRIER]
[15:46] <jwhisnant> jakesyl: isn't applications a directory?  I don't think it will ever be in "files" (but it might be in dir_name)
[15:46] <jwhisnant> or sub_dirs
[15:46] == davi [davi@gnu/davi] has quit [Ping timeout: 272 seconds]
[15:46] <winny> whoever posted that link about radians and degrees thank you a whole lot. I didn't know anything about why we use radians
[15:47] <jakesyl> hmm I get what your saying but doesn't the for still loop through sub_dirs
[15:47] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[15:47] <Skarfejs> winny: could you paste link once again?
[15:47] <jakesyl> oh I think it's a subdir, but since I don't know is there a different path i can walk that includes everything but applications
[15:47] * winny looks for it
[15:47] <winny> http://betterexplained.com/articles/intuitive-guide-to-angles-degrees-and-radians/
[15:47] <Skarfejs> thanks
[15:47] <winny> computer just panicked so luckily i had it in browser history
[15:48] == SilentGhost [~SilentGho@h51580eb1.seluesp.dyn.perspektivbredband.net] has joined #python
[15:48] == H1FuelCell [~quassel@122.162.133.234] has quit [Quit: No Ping reply in 180 seconds.]
[15:48] == potato_farmer [~potato_fa@71-92-218-44.static.mtpk.ca.charter.com] has left #python []
[15:48] == H1FuelCell [~quassel@122.162.133.234] has joined #python
[15:49] <jakesyl> so can i just crawl everything files wise (not applications
[15:49] == iqualfragile [~iqualfrag@unaffiliated/iqualfragile] has joined #python
[15:50] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[15:50] == talldave [~talldave@c-24-5-80-57.hsd1.ca.comcast.net] has quit [Quit: ZZZZZZzzzzzzzz………]
[15:50] == StoneTab_ has changed nick to StoneTable
[15:50] == nonny_t [~nonny_t@host-89-242-65-81.as13285.net] has quit [Remote host closed the connection]
[15:51] == MGiberius [~mateusz@d32-10.icpnet.pl] has quit [Quit: Leaving.]
[15:51] == dickinsm [~dickinsm@cpc7-cmbg14-2-0-cust10.5-4.cable.virginm.net] has quit [Quit: dickinsm]
[15:51] == jjmarin [~jjmarin@84.125.149.19.dyn.user.ono.com] has joined #python
[15:51] == lamar [~Adium@p54981969.dip0.t-ipconnect.de] has joined #python
[15:51] <optix2> jakesyl: are content/f of the same type as excludes(=string)?
[15:52] == py0 [~sickle@cpe-74-78-176-27.twcny.res.rr.com] has quit [Quit: Leaving]
[15:52] == jvasallo [~Adium@63-144-124-93.dia.static.qwest.net] has joined #python
[15:52] <jakesyl> no f is files
[15:53] <bug_sniper> jakesyl, I'd just make the program continue if it "applications" is in the firpath
[15:53] <bug_sniper> dirpath
[15:53] == Nizumzen [~Nizumzen@cpc1-reig5-2-0-cust251.6-3.cable.virginm.net] has quit [Quit: KVIrc 4.2.0 Equilibrium http://www.kvirc.net/]
[15:53] <jakesyl> bug_sniper that's what i'm doing
[15:53] == throwinghammers [~hcs@unaffiliated/throwinghammers] has quit [Ping timeout: 240 seconds]
[15:53] <jakesyl> oh
[15:53] <jakesyl> wait
[15:53] <optix2> the search is not going to work with different data type
[15:53] <optix2> *object type
[15:53] == jvasallo [~Adium@63-144-124-93.dia.static.qwest.net] has quit [Client Quit]
[15:54] == acoyfellow [~acoyfello@c-68-81-123-233.hsd1.nj.comcast.net] has quit [Ping timeout: 240 seconds]
[15:54] <bug_sniper> it you need it to be more efficient and you have a lot of files to skip over, you can make your own recursive directory search function
[15:54] <four_o_four> sorry for bothering again, but can someone please explain decorators? I don't even understand then\m in the context of pyglet
[15:54] == unixist [~unixist@unaffiliated/unixist] has joined #python
[15:54] == Berra [~arch@c83-252-6-221.bredband.comhem.se] has joined #python
[15:54] <four_o_four> as far as I ca see they tell a method WHEN to go?
[15:54] == mwilson [~mwilson@ip174-65-132-161.sd.sd.cox.net] has joined #python
[15:54] == heavytull [~heavytull@nor87-h03-89-82-92-188.dsl.sta.abo.bbox.fr] has quit [Ping timeout: 240 seconds]
[15:55] <kevlarman> winny: that is actually a pretty horrible explanation
[15:55] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[15:55] == dasterin [dasterin@2600:3c00::f03c:91ff:feae:9b3a] has quit [Quit: Leaving]
[15:56] == dickinsm [~dickinsm@cpc7-cmbg14-2-0-cust10.5-4.cable.virginm.net] has joined #python
[15:56] == mijicd [~mijicd@cable-188-246-51-84.dynamic.kdsinter.net] has quit [Remote host closed the connection]
[15:56] == mlncn [~mlncn@18.111.14.36] has quit [Excess Flood]
[15:56] == mwilson [~mwilson@ip174-65-132-161.sd.sd.cox.net] has quit [Read error: Connection reset by peer]
[15:56] <bug_sniper> http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
[15:56] == jakesyl_mobile [~jakesyl_m@2601:c:3480:379:f569:150e:547f:cd81] has joined #python
[15:57] == mlncn [~mlncn@18.111.14.36] has joined #python
[15:57] <four_o_four> Actually .... it's the best damn thing I've read all day
[15:57] == jvasallo [~Adium@63-144-124-93.dia.static.qwest.net] has joined #python
[15:57] <jakesyl_mobile> Hey guys its jakesyl had to go downstairs for a minute
[15:57] <four_o_four> (maybe all month)
[15:57] <bug_sniper> I would have to review them myself
[15:57] == ecounysis [~echristen@67.110.116.150.ptr.us.xo.net] has quit [Read error: Connection reset by peer]
[15:57] == hoppi [~hoppi@irc.rddpool.com] has left #python ["Eating Food."]
[15:57] <jakesyl_mobile> My other question is how do I declare Unicode
[15:57] == kevinb [~europa-zn@99-166-106-52.lightspeed.tukrga.sbcglobal.net] has quit [Ping timeout: 240 seconds]
[15:57] == yeticry [~yeticry@60.168.89.120] has quit [Ping timeout: 240 seconds]
[15:58] == ecounysis [~echristen@67.110.116.150.ptr.us.xo.net] has joined #python
[15:58] <jakesyl_mobile> I need it for db interactions
[15:58] == nedbat [~nedbat@python/psf/nedbat] has joined #python
[15:58] == ojdo [~ojdo@unaffiliated/ojdo] has quit [Quit: WeeChat 0.4.2]
[15:58] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[15:58] <four_o_four> I don't know about you guys, but over here we learn that a circle just has 360 degrees .... then we learn about radians afterwards ...but I still haven't learnt about them, so now I get why they have 360 OMW -mindblown-
[15:58] == rustymyers [~rustymyer@mackenster.tlt.psu.edu] has quit [Quit: Lingo - http://www.lingoirc.com]
[15:58] <basheba> I fixed all the problems Wooble but color.RED will not print it only give me white bold b/c of the color.BOLD http://bpaste.net/show/eglKE9ELxXxjqHITcsEW/
[15:59] <therealfakemoot> four_o_four: yes, math is magical
[15:59] == yuhan [~yuhan@unaffiliated/yuhan] has joined #python
[15:59] == jvasallo [~Adium@63-144-124-93.dia.static.qwest.net] has quit [Client Quit]
[15:59] == arescorpio [~arescorpi@201-26-245-190.fibertel.com.ar] has joined #python
[15:59] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[15:59] <four_o_four> I'm glad I get excited about stuff like that
[15:59] <kevlarman> four_o_four: there's a bunch of straight up incorrect information there, and it doesn't go into the unit circle which it really should
[15:59] == thetet [~raggam-nl@178-190-149-123.adsl.highway.telekom.at] has joined #python
[16:00] == SpaghettiCat [~Spaghetti@stgt-5d843664.pool.mediaWays.net] has joined #python
[16:00] == yeticry [~yeticry@60.168.89.120] has joined #python
[16:00] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[16:00] <four_o_four> All the other twigs my age are smoking weed and getting pregnant (sometimes at the same time)
[16:00] <bug_sniper> So I think decorators are like code that assigns function calls using a function to replace that function.  Is that correct?
[16:01] == smccully [~smccully@192.65.45.20] has quit []
[16:01] <four_o_four> Yes, I know that , but it helped me make sene of all the other over-complicated articles
[16:01] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:01] <kevlarman> bug_sniper: @foo\ndef bar(): is syntactic sugar for def bar(): ... bar = foo(bar)
[16:01] == zzebelzz [~ebel@71.92.160.62] has joined #python
[16:02] <bug_sniper> kevin-brown, thanks for the answer
[16:02] <kevlarman> four_o_four: also calculus gets really tedious when using anything other than radians
[16:02] == Dambles [~Jeffrey_d@143.127.2.8] has quit [Ping timeout: 240 seconds]
[16:03] == position88 [~position8@92.246.1.130] has joined #python
[16:03] == yeticry [~yeticry@60.168.89.120] has quit [Client Quit]
[16:03] == Macuser [~textual@unaffiliated/macuser] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[16:03] <four_o_four> Lol South Africa has the second (or possibly the) worst maths and science education from a list of 150 .... dayum
[16:03] == OnkelTem [~onkeltem@pppoe-62-84-112-224.dubna.ru] has quit [Quit: WeeChat 0.3.7]
[16:03] == yuhan [~yuhan@unaffiliated/yuhan] has quit [Ping timeout: 256 seconds]
[16:03] == yeticry [~yeticry@60.168.89.120] has joined #python
[16:03] == krawchyk_ [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has quit [Quit: away]
[16:03] <jakesyl> anyone know how to make a python server, also for future use jakesyl_mobile is me
[16:04] <SpaghettiCat> jakesyl:  If you want something quick and temporary there's SimpleHTTPServer
[16:04] <four_o_four> :kevlarman: Are you from the US? At what age/grade did you start with calculus/radians/trig ?
[16:04] <jakesyl> no Sphagetticat i need something robust
[16:04] == slassh [~slassh@176.250.145.105] has joined #python
[16:04] == jorgev [~jorgev@rrcs-67-52-158-66.west.biz.rr.com] has joined #python
[16:04] <SpaghettiCat> jakesyl:  what do you mean Python server?
[16:04] <jakesyl> not http/web either a backend server kinda thing
[16:05] == jvasallo [~Adium@199.195.244.30] has joined #python
[16:05] <four_o_four> One that runs python?
[16:05] <kevlarman> four_o_four: we learn about what radians are somewhere around 8th/9th grade, then we forget about them until calculus
[16:05] <SpaghettiCat> you'll have to be a bit more specific
[16:05] <Pici> 'backend server'?
[16:05] == kevinb [~europa-zn@99-166-106-52.lightspeed.tukrga.sbcglobal.net] has joined #python
[16:05] <jakesyl> yes four_o_four
[16:05] == krawchyk [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has joined #python
[16:05] <kevlarman> four_o_four: most american students never learn calculus
[16:05] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 240 seconds]
[16:05] <four_o_four> :kevlarman: I'm 10th and I've never heard of them in school
[16:05] <gcbirzan> most * students don't learn calculus
[16:05] <jakesyl> pici, I mean the server does data processing with data from front end user
[16:05] <nedbat> four_o_four: "10th"?
[16:05] <four_o_four> calculus being derivatives and all that?
[16:06] <gcbirzan> close enough
[16:06] <kevlarman> gcbirzan: that's not really accurate, calculus wasn't optional for my parents growing up in the ussr
[16:06] == Johz [~Johz@cpc24-king9-2-0-cust525.19-1.cable.virginm.net] has joined #python
[16:06] * jakesyl
[16:06] <four_o_four> :nedbat: Yes, the grade one is in after successully completing the preceding nine grades
[16:06] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:06] <gcbirzan> kevlarman: It wasn't optional for me or my classmates, but I can assure you I didn't study it and they didn't learn it :P
[16:07] == position88 [~position8@92.246.1.130] has quit [Ping timeout: 240 seconds]
[16:07] == SpaghettiCat [~Spaghetti@stgt-5d843664.pool.mediaWays.net] has quit [Quit: Terminated]
[16:07] <nedbat> four_o_four: no need for snark, you didn't say "grade"! :)
[16:07] == mFacenet [~mFacenet@unaffiliated/mfacenet] has joined #python
[16:07] <four_o_four> I thought it was impliedsgithubgithub
[16:07] <nedbat> four_o_four: I missed an earlier message, my mistake! :)
[16:07] <four_o_four> I just had my eighth cuppa joe
[16:08] <four_o_four> all good
[16:08] == lvdz [~aa@109.133.185.250] has quit [Quit: lvdz]
[16:08] <four_o_four> srry
[16:08] == d1rkp1tt [~darin@119.224.34.137] has joined #python
[16:08] == sboudrias [~sboudrias@2601:9:3480:11b9:b81d:bf0d:2440:e235] has joined #pythonfads
[16:09] == shortdudey123 [~shortdude@c-67-180-84-163.hsd1.ca.comcast.net] has joined #python
[16:09] == pydsigner-work [~pydsigner@unaffiliated/pydsigner] has quit [Read error: No route to host]
[16:09] == mahmoudimus [~mahmoudim@199.241.202.154] has quit [Ping timeout: 240 seconds]
[16:09] == pydsigner-work [~pydsigner@unaffiliated/pydsigner] has joined #python
[16:10] == in_deep_thought [~alexmarsh@207.71.224.29] has quit [Quit: in_deep_thought]
[16:10] == ojdo [~ojdo@unaffiliated/ojdo] has joined #python
[16:10] <gcbirzan> kevlarman: also, it's absolutely insane to expect highschool kids to learn calculus, especially since half of them won't care about it at all, ever
[16:11] == sivy [~sivy@ip68-224-188-72.hr.hr.cox.net] has joined #python
[16:11] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 240 seconds]
[16:11] <four_o_four> We have mathematical literature - > Not to be rude, but you have to be mentally retarded to fail it.
[16:11] == mahmoudimus [~mahmoudim@199.241.202.154] has joined #python
[16:11] <four_o_four> The rest do 'Pure' math
[16:11] <four_o_four> Some do Ap
[16:12] == Balliad [~textual@52D95C9B.cm-11-1b.dynamic.ziggo.nl] has joined #python
[16:12] == elyezer_ [~elyezer@unaffiliated/elyezer] has joined #python
[16:12] == moted_ [~anonymous@c-71-193-182-37.hsd1.wa.comcast.net] has quit [Quit: moted_]
[16:12] == sboudrias [~sboudrias@2601:9:3480:11b9:b81d:bf0d:2440:e235] has quit [Ping timeout: 240 seconds]
[16:12] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:12] <kevlarman> gcbirzan: not really
[16:13] == nomic [~nomic@host86-139-151-69.range86-139.btcentralplus.com] has joined #python
[16:14] == Eyes [~eyes@WiseOS/Founder/NiaTeppelin] has joined #python
[16:14] == krawchyk [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has quit [Quit: bbye]
[16:14] == elyezer [~elyezer@unaffiliated/elyezer] has quit [Ping timeout: 240 seconds]
[16:15] == elyezer_ has changed nick to elyezer
[16:16] == cryptic0 [~cryptic0@fw.al.umces.edu] has joined #python
[16:16] == zivoni [~zivoni@ip-94-112-186-31.net.upcbroadband.cz] has quit [Ping timeout: 240 seconds]
[16:16] == Silkspire [~Silkspire@5-14-140-154.residential.rdsnet.ro] has quit [Quit: Leaving]
[16:17] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 260 seconds]
[16:17] == vsoftoiletpaper [~verysoftt@unaffiliated/softtoiletpaper] has quit []
[16:17] == bergin [~bergin@171.159.221.134] has joined #python
[16:17] == treehug88 [~treehug88@66.6.34.254] has joined #python
[16:17] == moted [~anonymous@c-71-193-182-37.hsd1.wa.comcast.net] has joined #python
[16:17] <nedbat> four_o_four: i wish you wou;dn
[16:17] <nedbat> four_o_four: i wish you wouldn't use that word that way