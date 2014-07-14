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
[16:07] <four_o_four> I thought it was implied
[16:07] <nedbat> four_o_four: I missed an earlier message, my mistake! :)
[16:07] <four_o_four> I just had my eighth cuppa joe
[16:08] <four_o_four> all good
[16:08] == lvdz [~aa@109.133.185.250] has quit [Quit: lvdz]
[16:08] <four_o_four> srry
[16:08] == d1rkp1tt [~darin@119.224.34.137] has joined #python
[16:08] == sboudrias [~sboudrias@2601:9:3480:11b9:b81d:bf0d:2440:e235] has joined #python
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
[16:18] == sivy [~sivy@ip68-224-188-72.hr.hr.cox.net] has quit [Remote host closed the connection]
[16:18] == optix2 [~quassel@port-92-202-34-130.dynamic.qsc.de] has quit [Remote host closed the connection]
[16:18] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:18] <pydsigner-work> gcbirzan, I'd recommend Calculus to anyone.
[16:18] <gcbirzan> pydsigner-work: why?
[16:19] == ompaul [~ompaul@unaffiliated/ompaul] has quit [Quit: and zebedee said its time for other stuff]
[16:19] == vsoftoiletpaper [~verysoftt@unaffiliated/softtoiletpaper] has joined #python
[16:19] == sboudrias [~sboudrias@2601:9:3480:11b9:ec52:1c63:5d39:9616] has joined #python
[16:19] <ssbr_at_work> gcbirzan: calculus is important for understanding physics and finance
[16:19] <pydsigner-work> ^
[16:19] <ssbr_at_work> most people care about at least one of those in their day to day life
[16:19] <basheba> it works.  I picked another color so BASH ansi is WRONG
[16:19] <basheba> red doesn't work
[16:20] <gcbirzan> when was the last time, in your day to day life, you cared about calculus?
[16:20] <ssbr_at_work> well. specifically, limits and differentiation are important. integrals can die in a fire of course
[16:20] <basheba> oh wait you know what?  lemme check my terminal colors maybe it was assigned to white
[16:20] <ssbr_at_work> gcbirzan: I have been looking over my finances for the past few weeks, so, yesterday?
[16:20] <gcbirzan> ssbr_at_work: yeah, you were using a calculator :P
[16:20] == rafacv [~rafacv@187-53-134-7.gnale700.dsl.brasiltelecom.net.br] has joined #python
[16:20] <pydsigner-work> Just the thrill of understanding all the physics motion equations was worth it for me.
[16:20] <kevlarman> gcbirzan: calculus is required to understand linear algebra, linear algebra is required to understand 3d graphics
[16:20] <ssbr_at_work> gcbirzan: no, I was reading a book that talked briefly about efficient frontiers
[16:21] <nanonyme> ssbr_at_work, why do you hate integrals, you integral-hating integral hater?
[16:21] <ssbr_at_work> kevlarman: you don't need any calculus to understand linear algebra
[16:21] <pydsigner-work> gcbirzan, calculator or no, you still have to understand what you're doing
[16:21] <jwhisnant> kevlarman: ^^
[16:21] <Hodapp> kevlarman: Calculus is not required for linear algebra.
[16:21] <bergin> Does anyone have experience with Flask-Principal? I've been trying to unit test a Flask app that uses Flask-Principal. I've been able to get the get requests to work but not the post requests.
[16:21] <gcbirzan> kevlarman: oh, so the people who do 3d graphics need it. next?
[16:21] <ssbr_at_work> gcbirzan: calculators are pretty unhelpful for doing finances, really
[16:21] <Hodapp> ssbr_at_work: so is a soul, sometimes.
[16:21] == jj995_ [420380d2@gateway/web/freenode/ip.66.3.128.210] has quit [Ping timeout: 246 seconds]
[16:21] <ssbr_at_work> like, balancing your chequebook is a pretty trivial affair
[16:22] <gcbirzan> ssbr_at_work: okay, maybe, but I still doubt you need a deep understanding of it, to get by. I might be wrong, since I have a vague understanding of it, but *shrugs*
[16:22] <ssbr_at_work> calculus is more used for balancing your investments
[16:22] == yordan [~user@91.92.178.129] has joined #python
[16:22] <Hodapp> Calculus is why I have money TO invest.
[16:22] <ssbr_at_work> gcbirzan: an intuitive understanding is good enough for nearly anything that doesn't literally involve performing calculus on a page
[16:22] == H1FuelCell [~quassel@122.162.133.234] has quit [Ping timeout: 264 seconds]
[16:22] <ssbr_at_work> even with the physics
[16:23] * jwhisnant returns to /topic.
[16:23] == BPL [53a5f532@gateway/web/freenode/ip.83.165.245.50] has quit [Quit: Page closed]
[16:23] <ssbr_at_work> gcbirzan: as far as programming goes, understanding calculus is handy, but not as handy as linear algebra, sure
[16:23] <pydsigner-work> jwhisnant, "boring"
[16:23] == sboudrias [~sboudrias@2601:9:3480:11b9:ec52:1c63:5d39:9616] has quit [Ping timeout: 240 seconds]
[16:23] <ssbr_at_work> the concepts of linear independence, eigenvectors, etc.... are so useful so many places
[16:23] == bus3rr0r [~bus3rr0r@unaffiliated/bus3rr0r] has quit [Quit: Leaving]
[16:24] == Ariel_Calzada [~aricalso@181.136.103.229] has quit [Quit: Bye all]
[16:24] <ssbr_at_work> geometric interpretations come in handy in computer graphics, but the operators themselves are useful for modeling
[16:24] == atula [~neobreed@c-98-217-193-202.hsd1.ma.comcast.net] has quit [Quit: This computer has gone to sleep]
[16:25] <kevlarman> gcbirzan: and just understanding math is really useful for programming
[16:25] == deSilva [~deSilva@c83-254-213-203.bredband.comhem.se] has quit []
[16:25] == evildmp [~evildmp@django/committer/EvilDMP] has quit [Read error: Connection reset by peer]
[16:25] <kevlarman> gcbirzan: i had a coworker who had trouble with determining if 2 date ranges overlap
[16:25] <gcbirzan> kevlarman: I never said it's not. I just said, for the majority of people, it's not.
[16:25] <kmtsun> hello
[16:25] <gcbirzan> kevlarman: the majority of people are NOT programmers.
[16:26] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[16:26] <ssbr_at_work> The majority of people don't know enough math.
[16:26] == bluedreams [~bluedream@24-205-95-34.dhcp.psdn.ca.charter.com] has quit [Remote host closed the connection]
[16:26] == cnj [cnj@unaffiliated/cnj] has quit [Ping timeout: 240 seconds]
[16:26] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:26] == az4gh4l [~az4gh4l@78.24.93.79.rev.sfr.net] has quit [Remote host closed the connection]
[16:26] <ssbr_at_work> gcbirzan: subjects that are only brought up in calculus, in the US -- like the exponential function -- are so widely misunderstood as to actually hurt people.
[16:26] == Balliad [~textual@52D95C9B.cm-11-1b.dynamic.ziggo.nl] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[16:26] <gcbirzan> yes. and they don't need to. we started from saying people in highschool learn calculus, and I said it's insane to require it...
[16:26] <ssbr_at_work> see also: personal finance.
[16:26] == aep000 [62ddf6cf@gateway/web/freenode/ip.98.221.246.207] has joined #python
[16:27] <ssbr_at_work> gcbirzan: They don't "need to", but they are much worse off for it.
[16:27] == decoponio [~decoponio@pon059-128.kcn.ne.jp] has quit [Quit: Leaving...]
[16:27] <ssbr_at_work> gcbirzan: it's sort of like nobody "needs" dental care.
[16:27] == desophos [~desophos@108-205-152-216.lightspeed.irvnca.sbcglobal.net] has joined #python
[16:27] <gcbirzan> ssbr_at_work: to not know it? yeah, I guess. I never really missed not giving a crap and just learning as little as I can
[16:27] <ssbr_at_work> A good grounding in basic analysis is very helpful for navigating the world of personal finance. I can't stress it enough.
[16:27] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[16:28] <ssbr_at_work> gcbirzan: well, most people do as little as possible, and it hurts them
[16:28] <gcbirzan> ssbr_at_work: when I wanted to learn something, I got a book and studied it myself
[16:28] <Hodapp> Those who have considerable influence on legislation and budgeting do not benefit from people understanding math well.
[16:28] <ssbr_at_work> gcbirzan: that's why it should be required in school.
[16:28] <nedbat> ssbr_at_work: i don't know if i have that or not.  Do you have an example of a guide that covers the topic to the depth you're talking about?
[16:28] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:28] <ssbr_at_work> nedbat: if you know how exponentials work and you know the concept of marginal returns / differentiation, that's all I really mean.
[16:29] == sayan [~sayan@fedora/sayan] has quit [Ping timeout: 240 seconds]
[16:29] == Kayra [~Kayra@95.149.176.223] has joined #python
[16:29] == TekhnoLife [~Dmitry@31.180.138.104] has joined #python
[16:29] <nedbat> ssbr_at_work: can you give an example of how that applies to personal finance?
[16:29] == russw [~russ@bas1-ottawa01-1177967421.dsl.bell.ca] has quit [Ping timeout: 260 seconds]
[16:29] == Eyes has changed nick to Eyess
[16:30] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[16:30] <ssbr_at_work> nedbat: for example, many people invest in savings with fees of around 4%. This doesn't seem large, because it's 4%! But someone aware of how compounding interest works knows that this grows every year.
[16:31] <ssbr_at_work> it eats 4% of your first year's returns, but those fees eat 19% of your first five years of returns
[16:31] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:31] == DTVD [~DTVD@230.115.100.220.dy.bbexcite.jp] has joined #python
[16:31] <ssbr_at_work> (eh, 18.5%, but whatever)
[16:31] <ssbr_at_work> ehhhh, this isn't the right way to phrase it.
[16:31] <ssbr_at_work> it eats that much of your fifth year's returns compared to 0% fees
[16:31] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has quit [Ping timeout: 240 seconds]
[16:32] <aep000> Would socket communication be the best way to do file transfer or is there another method that is more effective
[16:32] == jjmarin [~jjmarin@84.125.149.19.dyn.user.ono.com] has left #python []
[16:32] == sr [~smrgr@shellium/member/samruger] has quit [Remote host closed the connection]
[16:32] == kermit [unknown@pdpc/supporter/bronze/kermit] has quit [Ping timeout: 260 seconds]
[16:33] == cnj [cnj@unaffiliated/cnj] has joined #python
[16:33] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has joined #python
[16:33] == Maratich [~Maratich@5.149.219.191] has joined #python
[16:33] <nedbat> aep000: what about using an existing thing like ftp?
[16:33] == sr [~smrgr@shellium/member/samruger] has joined #python
[16:33] <aep000> okay how would I go about thaty
[16:33] <Yhg1s> Not FTP, please.
[16:33] == turdidae [~je@ip68-224-89-5.lv.lv.cox.net] has joined #python
[16:33] <jwhisnant> aep000: or perhaps even sftp ...
[16:33] <Yhg1s> it's really not a thing to use.
[16:34] <nedbat> aep000: Yhg1s will have a recommendation :)
[16:34] <aep000> Yhg1s: ?
[16:34] <aep000> what should I use
[16:34] == Maratich [~Maratich@5.149.219.191] has quit [Client Quit]
[16:34] == circuit [~daniel@bas1-newmarket85-3096615903.dsl.bell.ca] has joined #python
[16:34] == CodeLicker [~CodeLicke@177.157.108.61.dynamic.adsl.gvt.net.br] has quit [Ping timeout: 240 seconds]
[16:34] <Bryson> I don't understand why this @property and @p.setter combination is throwing an exception on the @setter. Help is appreciated. http://bpaste.net/show/0lQFwqU77UQX733O2G0a/
[16:34] <Yhg1s> It depends on the usecase. HTTP is fine, as is SFTP. There's also rsync or webdav depending on your actual needs.
[16:35] <Yhg1s> Bryson: you forgot to subclass object.
[16:35] <Hodapp> ssbr_at_work: What is the 4% you're talking about? Most savings accounts - around here at least - don't have any fees, but they don't do anything for you either.
[16:35] == Back2Basics [~jeremy@cpe-173-175-53-12.hot.res.rr.com] has quit [Quit: Leaving.]
[16:35] <Hodapp> ssbr_at_work: so they sit there and lose value to inflation, because they're only making < 1% in interest.
[16:35] <Yhg1s> Bryson: you also really, really don't want to use a mutable default like on line 10.
[16:35] == rojem [~rojem@199.4.160.10] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[16:35] == DTVD [~DTVD@230.115.100.220.dy.bbexcite.jp] has quit [Ping timeout: 260 seconds]
[16:36] == johnnyb [~johnnyb@2a00:1028:8388:70e6:bc6d:789c:f626:23a9] has quit [Remote host closed the connection]
[16:36] <Bryson> Yhg1s: Error is the same with (object) or without. It isn't in there currently as this is python 3.4.1, so it isn't required because it subclasses (object) by default (right? or do i have that backwards, it's required in 3?)
[16:36] <aep000> Yhg1s: I need to have clients upload images, videos, audio etc to my server
[16:36] == wilornel [081a9d80@gateway/web/freenode/ip.8.26.157.128] has joined #python
[16:36] <wilornel> Hey guys! I have a script A doing `from B.C import D`. D is in the same directoy as E. When from D, I do `import E`, python says 'No module named E'
[16:36] == kermit [unknown@pdpc/supporter/bronze/kermit] has joined #python
[16:36] <wilornel> And now, I have no idea how exactly to investigate this issue
[16:36] <Bryson> Yhg1s: regarding the mutable default, pylint is complaining about it also so it's on my list of things to refactor, but outside the scope of this question
[16:36] <ssbr_at_work> Hodapp: that's the same problem from another angle. Not appreciating the difference between .1% interest and 10% is huge.
[16:37] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[16:37] <ssbr_at_work> differences between interest rates is nonlinear
[16:37] == Rudisimo [~Rudisimo@c-50-150-171-142.hsd1.fl.comcast.net] has quit [Ping timeout: 240 seconds]
[16:37] <jakesyl> aep000 i don't think sftp is the best solution
[16:37] <ssbr_at_work> the human mind doesn't really appreciate nonlinear things, I think?
[16:37] <jakesyl> isn't it deprecated anyway
[16:38] <Pici> jakesyl: SFTP != FTPS
[16:38] <bug_sniper> wilornel, what happens if you write import B.C.E?
[16:38] <jakesyl_mobile> Difference?
[16:38] <Pici> FTPS is terrible and no one should use it ever.
[16:38] == soiitaire [~soiitaire@123.114.55.8] has joined #python
[16:38] <Hodapp> ssbr_at_work: Banks have tons of money, and no incentive to have well-informed customers. They've likely been responsible for blocking plenty of initiatives that would have led to an overall higher education level.
[16:38] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:38] <maslen> How can I change  where the text is relative to the checkbox for a Tkinter `Checkbutton`?
[16:38] <jakesyl> well what about sftp
[16:38] <wilornel> bug_sniper: Nope, doesn't work!
[16:38] <Hodapp> ssbr_at_work: that's certainly not the only problem, but it's a big one.
[16:38] <nedbat> Bryson: can a setter take two args like that? What does that mean?
[16:38] == bergin [~bergin@171.159.221.134] has quit []
[16:38] <jakesyl> For the record, me and aep000 are working together on this project
[16:38] <wilornel> bug_sniper: I've also tried from B.C import E
[16:39] == jimmybot [~jimmybot@64.124.192.210] has quit [Remote host closed the connection]
[16:39] <ssbr_at_work> Hodapp: pfft, don't be ridiculous. Kids shouldn't learn complicated things like calculus. :)
[16:39] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has quit [Remote host closed the connection]
[16:39] == atula [~neobreed@c-98-217-193-202.hsd1.ma.comcast.net] has joined #python
[16:39] <Bryson> nedbat: What does what mean? I don't know if a setter can/can't take two args, but the error is the same with only one arg named `value` as well.
[16:39] == Balliad [~textual@52D95C9B.cm-11-1b.dynamic.ziggo.nl] has joined #python
[16:39] <nedbat> Bryson: oh, that's your problem:  n.outbound(x,y) is like:    o = n.outbound;  o(x,y)
[16:39] <nedbat> Bryson: setters don't work like that.
[16:39] <Hodapp> ssbr_at_work: most of them would agree with you.
[16:39] == firecat53 [~firecat53@c-98-225-17-95.hsd1.wa.comcast.net] has joined #python
[16:39] <bug_sniper> wilornel, what happens if you try to run the file D.py from its own directory?
[16:39] <nedbat> Bryson: the setter should be used like:   n.outbound = x
[16:39] <four_o_four> you wot?
[16:40] == VeXocide [vexocide@unaffiliated/vexocide] has joined #python
[16:40] == ioggstream [~rpolli@93-45-42-187.ip100.fastwebnet.it] has joined #python
[16:40] <nedbat> four_o_four: if you are talking to me, i meant that I would rather you didn't use "retarded" flippantly
[16:41] <aep000> Can anyone link me to material on a good file transfer method and some sample code in python
[16:41] <four_o_four> <nedbat> four_o_four: i wish you wouldn't use that word that way ----> ?
[16:41] <four_o_four> O
[16:41] == CatMtKing [~CatMtKing@ed-uluka.dyn.ucr.edu] has joined #python
[16:41] == kmtsun [~chatzilla@8.22.213.244] has quit [Read error: Connection reset by peer]
[16:41] == thelinuxkid [~thelinuxk@static-108-0-187-37.lsanca.fios.verizon.net] has quit [Quit: Leaving.]
[16:42] <jakesyl> chill retard doesn't even mean mental defect anymore
[16:42] == lad13371 [~Adium@212.12.46.3] has joined #python
[16:42] == russw [~russ@bas1-ottawa01-1177967421.dsl.bell.ca] has joined #python
[16:42] == dj_pi [~dj@c-107-5-25-243.hsd1.mi.comcast.net] has joined #python
[16:42] <Hodapp> um, what?
[16:42] <jakesyl> it has multiple definitions, it's kind of like being insulted when someone calls you gay and means happy
[16:42] <Bryson> nedbat: AH damn, so i'm just calling it incorrectly! bonehead mistake. Thanks.
[16:42] <four_o_four> They mean ou're a raging homosexual
[16:42] <four_o_four> except they don't
[16:43] <nedbat> jakesyl: you mean kind of like the way "gay" can mean "bad"? :(
[16:43] == soiitaire [~soiitaire@123.114.55.8] has quit [Ping timeout: 264 seconds]
[16:43] <four_o_four> Of course, all homos aren't gay
[16:43] == Liam` [liam@liam.ml] has quit [Ping timeout: 260 seconds]
[16:43] <Hodapp> jakesyl: What is an instance in which "mentally retarded" is used in a non-derogatory sense?
[16:43] <jakesyl> no nedbat, I mean someone interpreting you calling them happy instead of homosexual
[16:43] <nedbat> four_o_four: let's drop this, ok?
[16:43] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 240 seconds]
[16:43] <jakesyl> cool with me
[16:43] == ghostlines [~ghostline@92.109.90.61] has quit [Quit: My MacBook has gone to sleep. ZZZzzz…]
[16:43] <four_o_four> That dog is mentally retarded
[16:43] <four_o_four> give it ritalin
[16:44] <Hodapp> ...
[16:44] <wilornel> bug_sniper: no issues
[16:44] <four_o_four> There^
[16:44] == kyheo [~kyheo@190.188.185.158] has quit [Quit: Leaving.]
[16:44] == in_deep_thought [~alexmarsh@207.71.224.29] has joined #python
[16:44] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:44] <Yhg1s> jakesyl: unfortunately we can't know what you meant, and can't really infer it either, so we prefer you just use unambiguous language.
[16:44] <bug_sniper> wilornel, then the difficulty is navigating the directory structures
[16:44] <four_o_four> nedbat is like the ________  of #python
[16:44] == samfalkner [~samfalkne@inet-aumc10-o.oracle.com] has quit [Remote host closed the connection]
[16:44] <Pici> four_o_four: can we move on please?
[16:45] == mode/#python [+o Yhg1s] by ChanServ
[16:45] == jvasallo [~Adium@199.195.244.30] has left #python []
[16:45] <wilornel> bug_sniper: How could I know where in the "modules structure" I am located?
[16:45] == mode/#python [+b *!*290dd025@*.41.13.208.37] by Yhg1s
[16:45] == four_o_four was kicked from #python by Yhg1s [Come back when you can behave.]
[16:45] == mode/#python [-o Yhg1s] by Yhg1s
[16:45] <jakesyl> YHg1s I wasn't the original maker of that comment
[16:45] == mode/#python [+o infobob] by ChanServ
[16:45] == mode/#python [+b $a:four_O_four] by infobob
[16:45] == mode/#python [-b *!*290dd025@*.41.13.208.37] by infobob
[16:45] == Ariel_Calzada [~aricalso@186.82.232.130] has joined #python
[16:45] <nedbat> four_o_four, jakesyl: i'd be glad to talk to you in private it about it if you have more thoughts.
[16:45] == lad1337 [~Adium@212.12.46.3] has quit [Ping timeout: 240 seconds]
[16:45] == cap3lla [~cap3lla@unaffiliated/cap3lla] has quit []
[16:45] <Hodapp> nedbat: you'll need to send that one to four_o_four in private as he was kicked by the time you said it.
[16:46] == cap3lla [~cap3lla@unaffiliated/cap3lla] has joined #python
[16:46] == p0sixpscl [~p0sixpscl@p5B15C965.dip0.t-ipconnect.de] has quit [Ping timeout: 240 seconds]
[16:46] <Yhg1s> wilornel: you look at how modules are imported.
[16:46] <jakesyl> in any case the dir_names solution didn't work code:https://gist.github.com/jakesyl/05c7a450effebe67990f this is in refference to the os.walking the application directory
[16:46] == epoitras [~Thunderbi@CPE009400809a9c-CMb89bc9d2e1a5.cpe.net.cable.rogers.com] has quit [Quit: epoitras]
[16:46] <Yhg1s> wilornel: are you using Python 2.x or 3.x?
[16:46] == lad13371 [~Adium@212.12.46.3] has quit [Ping timeout: 264 seconds]
[16:47] == epoitras [~Thunderbi@CPE009400809a9c-CMb89bc9d2e1a5.cpe.net.cable.rogers.com] has joined #python
[16:47] <bug_sniper> wilornel, you might have to paste in your D.py file contents into pastebin
[16:48] <Yhg1s> jakesyl: the error means you have non-ASCII bytestrings that you are trying to insert into a text field.
[16:48] == superflat [~ayush@49.14.131.164] has quit [Read error: Connection reset by peer]
[16:48] <Yhg1s> jakesyl: the simple solution may be to make 'root' unicode, then everything os.walk returns will be unicode, too.
[16:48] <Yhg1s> jakesyl: but that'll only work if you have a sensible filesystem encoding (and Python knows about it)
[16:48] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[16:48] <wilornel> bug_sniper, Yhg1s: Give me a minute
[16:48] == jakesyl_mobile [~jakesyl_m@2601:c:3480:379:f569:150e:547f:cd81] has quit [Read error: Connection reset by peer]
[16:49] == inad922 [~inad925@193.61.9.77] has quit [Quit: Leaving]
[16:49] == aep000 [62ddf6cf@gateway/web/freenode/ip.98.221.246.207] has quit [Ping timeout: 246 seconds]
[16:49] == jimmybot [~jimmybot@64.124.192.210] has joined #python
[16:49] == jakesyl_mobile [~jakesyl_m@c-68-45-93-152.hsd1.nj.comcast.net] has joined #python
[16:49] == eeriegeek [~eeriegeek@c-98-244-112-229.hsd1.va.comcast.net] has joined #python
[16:50] == SilentGhost [~SilentGho@h51580eb1.seluesp.dyn.perspektivbredband.net] has quit [Quit: WeeChat 0.4.3]
[16:50] == krawchyk [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has joined #python
[16:50] == mode/#python [-o infobob] by infobob
[16:50] == agjacome [~agjacome@97.223.11.37.dynamic.jazztel.es] has quit [Quit: Lost terminal]
[16:50] == epoitras [~Thunderbi@CPE009400809a9c-CMb89bc9d2e1a5.cpe.net.cable.rogers.com] has quit [Client Quit]
[16:51] == ColdKeyboard [~coldkeybo@cable-188-2-9-220.dynamic.sbb.rs] has quit []
[16:51] == evildmp [~evildmp@django/committer/EvilDMP] has joined #python
[16:52] == sboudrias [~sboudrias@2601:9:3480:11b9:fd4a:b2fb:1f46:ae32] has joined #python
[16:52] == jakesyl_mobile [~jakesyl_m@c-68-45-93-152.hsd1.nj.comcast.net] has quit [Read error: Connection reset by peer]
[16:52] <Yhg1s> jakesyl: you may want to read or watch bit.ly/unipain if you haven't already, by the way.
[16:53] <jakesyl> YHg1s the output at the bottom is unrelated
[16:53] == nutzz [~chatzilla@84.117.60.106] has joined #python
[16:53] <jakesyl> I solved that problem with text factory
[16:53] <jakesyl> do you have any idea how to fix the os.walk error
[16:53] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[16:54] == five_o [290dd025@gateway/web/freenode/ip.41.13.208.37] has joined #python
[16:54] == ASUChander [~asuchande@ip68-3-149-68.ph.ph.cox.net] has quit [Remote host closed the connection]
[16:54] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has joined #python
[16:54] <five_o> wow
[16:55] <nutzz> is it possible to dynamically select fields in psycopg, like cur.execute("SELECT %(field_name)s FROM foo WHERE bar=baz", {"field_name: user_age"})?
[16:55] <jakesyl>  hey guys, I've tried excluding, but does anyone know how i can stay out of applications dir in os.walk code: https://gist.github.com/jakesyl/05c7a450effebe67990f
[16:55] == lamar [~Adium@p54981969.dip0.t-ipconnect.de] has quit [Ping timeout: 272 seconds]
[16:55] == five_o [290dd025@gateway/web/freenode/ip.41.13.208.37] has left #python []
[16:56] == sboudrias [~sboudrias@2601:9:3480:11b9:fd4a:b2fb:1f46:ae32] has quit [Ping timeout: 240 seconds]
[16:56] <ssbr_at_work> jakesyl: remove it from the sub_dirs list
[16:56] <nedbat> jakesyl: you can modify the sub_dirs list
[16:56] == four_0_four [290dd025@gateway/web/freenode/ip.41.13.208.37] has joined #python
[16:57] <jakesyl> nedbat how?
[16:57] <nedbat> jakesyl: (not with an assignment statement, with a .remove() call)
[16:57] <jakesyl> and ssbr okay
[16:57] == FortySix2 [~FortySix2@h204-246-2-62.mdsnwi.tisp.static.tds.net] has quit [Remote host closed the connection]
[16:57] <Yhg1s> jakesyl: what is 'the os.walk error', sorry?
[16:57] <jakesyl> so sub_dirs.remove(name)
[16:57] <Yhg1s> jakesyl: you can skip directories that way, yes.
[16:57] == p0sixpscl [~p0sixpscl@p5B15C965.dip0.t-ipconnect.de] has joined #python
[16:57] == ustunozgur [~ustunozgu@78.171.81.205] has joined #python
[16:57] <Greener> nutzz: Do you mean pass a variable into that execute statement?
[16:57] <nutzz> yes
[16:57] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has quit [Remote host closed the connection]
[16:58] <nutzz> in the place of a field
[16:58] <Yhg1s> nutzz: yes, but not with parameterization like that. you have to do string formatting.
[16:58] <Yhg1s> nutzz: you probably want to use a query builder instead, like SQLAlchemy's
[16:58] <Greener> Yes, and there's a way with psycopg to do it
[16:58] <jakesyl> where would i put this, the os.walk is a for loop, I'm not removing it every time am i?
[16:58] <Greener> Are you using psycopg2?
[16:58] <nutzz> yes
[16:58] == [nsh] [~unf@wikipedia/nsh] has joined #python
[16:58] <Greener> http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries
[16:58] == al1o [~al1o@p4FF57645.dip0.t-ipconnect.de] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[16:58] <Yhg1s> jakesyl: you put it in the loop, when it is in the iteration for the directory containing the directory you want to skip.
[16:59] == mrueg [~mrueg@gentoo/developer/mrueg] has quit [Remote host closed the connection]
[16:59] <four_0_four> Are there any alternatives to pyglet for making GUIs? maybe even simpler?
[16:59] == FortySix2 [~FortySix2@h204-246-2-62.mdsnwi.tisp.static.tds.net] has joined #python
[16:59] <nutzz> Greener: thanks
[16:59] <Yhg1s> Greener: parameterization doesn't work for SQL data, like column names, just for SQL data.
[16:59] == sivy [~sivy@ip68-224-188-72.hr.hr.cox.net] has joined #python
[16:59] <four_0_four> is PyGame suitable?
[16:59] == fzombie [gplgeek@pdpc/supporter/student/GPLGeek] has joined #python
[17:00] == yuhan [~yuhan@unaffiliated/yuhan] has joined #python
[17:00] == krawchyk [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has quit [Quit: away]
[17:00] <jakesyl> and since applications is in the root, all I have to do is type .remove(Applications)
[17:00] <Yhg1s> jakesyl: in the first iteration.
[17:00] == mrueg [~mrueg@gentoo/developer/mrueg] has joined #python
[17:00] <Yhg1s> four_0_four: you realize you're violating freenode's terms of service by evading bans, yes?
[17:01] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 256 seconds]
[17:01] <Greener> nutzz: Yhg1s is right, this won't do what you want
[17:01] <Greener> At least for columns
[17:01] == andtorg [~andtorg@host146-17-dynamic.52-79-r.retail.telecomitalia.it] has quit [Quit: WeeChat 0.4.3]
[17:01] == eden [~eden@unaffiliated/eden] has joined #python
[17:02] <jakesyl> sub_dirs.remove(Applications) returns https://gist.github.com/jakesyl/25c71917254ce61cb79f
[17:02] == aquinas [~aquinas_@unaffiliated/aquinas] has quit [Remote host closed the connection]
[17:02] == jackneill [~jackneill@unaffiliated/jackneill] has quit [Ping timeout: 264 seconds]
[17:02] == lyles [~lscott@unaffiliated/lyles] has quit [Remote host closed the connection]
[17:02] == aquinas [~aquinas_@unaffiliated/aquinas] has joined #python
[17:02] == roentgen [~none@openvpn/community/support/roentgen] has joined #python
[17:02] == agjacome [~agjacome@97.223.11.37.dynamic.jazztel.es] has joined #python
[17:02] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:02] <kingplusplus> please is it possible to print out sha1 password? I am doing it for testing sake, when a user logged in i am trying to use session[] to print the password just as  i printed the username but it doesn't print anything
[17:03] <bug_sniper> jakesyl, maybe Applications should be inside quotes as a string
[17:03] <nutzz> so, is there any solution to generate the column names dynamically or should I hard code them? Maybe I can build the query string before calling the cur() method?
[17:03] == LiquidSwordsman [1816d3bc@gateway/web/freenode/ip.24.22.211.188] has joined #python
[17:03] <four_0_four> Where can I find the terms of service?  Just out of curiousity.
[17:03] == dickinsm [~dickinsm@cpc7-cmbg14-2-0-cust10.5-4.cable.virginm.net] has quit [Quit: dickinsm]
[17:03] == jimmybot [~jimmybot@64.124.192.210] has quit [Remote host closed the connection]
[17:03] <dmbaturin> kingplusplus: Your sha1 object doesn't implement str()?
[17:04] == Pharaoh2 [~Pharaoh2@182.48.244.234] has quit [Read error: Connection reset by peer]
[17:04] <four_0_four> And I didn't know, but now I do. I'll leave. How long do bans last, though?
[17:04] == hockeynu_ [~hockeynut@72.32.115.231] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[17:04] == moted [~anonymous@c-71-193-182-37.hsd1.wa.comcast.net] has quit [Ping timeout: 260 seconds]
[17:04] == yuhan [~yuhan@unaffiliated/yuhan] has quit [Ping timeout: 240 seconds]
[17:04] == rojem [~rojem@pool-173-76-204-21.bstnma.fios.verizon.net] has joined #python
[17:05] == mode/#python [+o ssbr_at_work] by ChanServ
[17:05] <@ssbr_at_work> four_0_four: ask #freenode
[17:05] <therealfakemoot> four_0_four: however long they were set for
[17:05] == mode/#python [+b *!*@gateway/web/freenode/ip.41.13.208.37] by ssbr_at_work
[17:05] == four_0_four was kicked from #python by ssbr_at_work [four_0_four]
[17:05] <jakesyl> that seems to have worked but I get a remove error, I'm obviously not referring to the right applications dir traceback: https://gist.github.com/jakesyl/5d560340bb56138832fe
[17:05] == sboudrias [~sboudrias@2601:9:3480:11b9:3055:24a4:b05d:8bfd] has joined #python
[17:05] == mode/#python [-o ssbr_at_work] by ChanServ
[17:05] == mode/#python [+o infobob] by ChanServ
[17:05] == mode/#python [+b $a:five_o] by infobob
[17:05] == mode/#python [-b *!*@gateway/web/freenode/ip.41.13.208.37] by infobob
[17:05] == mgrouchy_ [~mgrouchy@CPE68b6fc44a453-CM68b6fc44a450.cpe.net.cable.rogers.com] has quit [Quit: My MacBook has gone to sleep. ZZZzzz…]
[17:05] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:06] == jimmybot [~jimmybot@64.124.192.210] has joined #python
[17:06] == nutzz [~chatzilla@84.117.60.106] has quit [Quit: ChatZilla 0.9.90.1 [Firefox 30.0/20140608211132]]
[17:06] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has joined #python
[17:06] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:06] == thetet [~raggam-nl@178-190-149-123.adsl.highway.telekom.at] has quit [Ping timeout: 256 seconds]
[17:06] == Vivekananda_y510 [~vvikramjh@c-68-49-141-134.hsd1.md.comcast.net] has quit [Ping timeout: 264 seconds]
[17:06] == vsoftoiletpaper [~verysoftt@unaffiliated/softtoiletpaper] has quit []
[17:06] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:07] == rodfersou [~RoADRuNNE@177.157.35.149] has quit [Remote host closed the connection]
[17:07] <Hodapp> Bah, that's no way to ban-evade. You either lay low, or you come in with a whole messload about how the op who did it was outside of his right to do so.
[17:07] == Cuppa_coffee [~Beast@5ED4E377.cm-7-5d.dynamic.ziggo.nl] has quit [Quit: Leaving]
[17:07] == jimmybot [~jimmybot@64.124.192.210] has quit [Remote host closed the connection]
[17:07] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:07] <jakesyl> which hodapp is often the case
[17:08] <circuit> normal people usually don't get banned to begin with
[17:08] == Pharaoh2 [~Pharaoh2@1.186.101.70] has joined #python
[17:08] <jakesyl> maybe not in #python
[17:08] <Hodapp> circuit: Ops do sometimes go on power trips.
[17:09] <jakesyl> anyway, putting it in quotes didn't help I don't think im referencing the applications dir the right way
[17:09] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:09] == sboudrias [~sboudrias@2601:9:3480:11b9:3055:24a4:b05d:8bfd] has quit [Ping timeout: 240 seconds]
[17:09] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has quit [Remote host closed the connection]
[17:10] == CatMtKing [~CatMtKing@ed-uluka.dyn.ucr.edu] has quit [Quit: This computer has gone to sleep]
[17:10] == roentgen [~none@openvpn/community/support/roentgen] has quit [Remote host closed the connection]
[17:10] == mode/#python [-o infobob] by infobob
[17:10] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:11] == SoftwareMaven [~Thunderbi@c-67-177-48-118.hsd1.ut.comcast.net] has quit [Ping timeout: 260 seconds]
[17:12] == vsoftoiletpaper [~verysoftt@unaffiliated/softtoiletpaper] has joined #python
[17:12] == Bryson [~Bryson@184.2.174.149] has quit [Quit: Bryson]
[17:13] == roentgen [~none@openvpn/community/support/roentgen] has joined #python
[17:13] <Yhg1s> jakesyl: what are you doing and how is it failing?
[17:13] == thelinuxkid [~thelinuxk@static-108-0-187-37.lsanca.fios.verizon.net] has joined #python
[17:13] == bwreilly [~bwreilly@c-71-231-109-148.hsd1.wa.comcast.net] has quit [Remote host closed the connection]
[17:14] == cerivera [~Adium@cpe-72-182-112-199.austin.res.rr.com] has joined #python
[17:14] == gelignite [~gelignite@i528C332F.versanet.de] has quit [Quit: http://bit.ly/nkczDT]
[17:14] == wgreenberg [~wgreenber@204.28.125.50] has joined #python
[17:14] <cerivera> when do you convert your dates from UTC to client's time zone?
[17:14] <cerivera> in the browser?
[17:15] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 240 seconds]
[17:15] == badams [~badams@207.250.189.4] has quit [Ping timeout: 260 seconds]
[17:15] <jwhisnant> cerivera: perhaps you should keep all times as UTC and only present them in a the appropriate timezone on displaying them (subtle distinction, but may make your life easier)
[17:16] == ZyX-I [~ZyX-I@broadband-77-37-224-207.nationalcablenetworks.ru] has quit [Ping timeout: 240 seconds]
[17:16] == cryptic0 [~cryptic0@fw.al.umces.edu] has quit [Quit: Computer has gone to sleep.]
[17:16] <cerivera> jwhisnant: only problem right now is that i'm displaying them in an input field
[17:17] <cerivera> i guess i have to convert back to UTC on form submit
[17:17] <Yhg1s> cerivera: by 'UTC', do you mean 'a string representation of a date, in UTC', or do you just mean 'seconds since the epoch'?
[17:17] <cerivera> string rep of a date
[17:17] == sunya7a [~pryde@unaffiliated/sunya7a] has quit [Ping timeout: 264 seconds]
[17:18] <cerivera> with gmt +0
[17:18] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:18] <Yhg1s> then it's more common not to have that at all, unless the user wants to see UTC.
[17:18] == Bryson [~Bryson@184.2.174.149] has joined #python
[17:18] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:18] <cerivera> Yhg1s: you're talking about only storing timestamp?
[17:18] <cerivera> err
[17:18] <cerivera> seconds from epoch
[17:19] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:19] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:20] <Yhg1s> cerivera: or some other convenient format, yes.
[17:20] == nickpresta [~nickprest@204.225.158.34] has quit [Quit: Computer has gone to sleep.]
[17:20] <Yhg1s> (like a datetime object.)
[17:20] == aarose [~aarose@vmfarms-1.itcanada.com] has quit [Remote host closed the connection]
[17:20] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:21] == alexcepoi [~alexcepoi@a83-163-98-141.adsl.xs4all.nl] has quit []
[17:21] == NomadJim [~NomadJim@pdpc/supporter/active/nomadjim] has quit [Read error: Connection reset by peer]
[17:22] == NomadJim [~NomadJim@pdpc/supporter/active/nomadjim] has joined #python
[17:22] == Alumin [~alumin@unaffiliated/alumin] has joined #python
[17:22] == obscured [~obscured@ool-18e492de.dyn.optonline.net] has quit [Quit: leaving]
[17:22] == evanz [~evanz@dhcp162-84.netlab.uky.edu] has quit [Ping timeout: 240 seconds]
[17:23] == jvasallo [~Adium@63-144-124-93.dia.static.qwest.net] has joined #python
[17:23] == whg has changed nick to zz_whg
[17:23] == Oxyd [~oxyd@pdpc/supporter/student/oxyd] has quit [Quit: Stop saying you're stupid. Start *feeling* you're stupid!]
[17:23] == AaronMT [~AaronMT@CPE0088654f39bd-CM602ad0738a5c.cpe.net.cable.rogers.com] has quit [Quit: Textual IRC Client: www.textualapp.com]
[17:23] == krawchyk [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has joined #python
[17:23] <Alumin> when I use "pydoc -w", the HTML pages that it generates contain the full (local filesystem) path to the source files.  In addition to being irrelevant when the pages are uploaded to a public Web server, I'd also rather not tell the world about my local directory structure.  Is there any way to customize pydoc's output such that that information isn't printed?
[17:24] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:24] <Yhg1s> Alumin: the usual choice is to use sphinx instead.
[17:24] == mrkz [~mark@187.244.9.117] has joined #python
[17:24] <Yhg1s> pydoc -w is really just a quick hack.
[17:24] == Oxyd [~oxyd@pdpc/supporter/student/oxyd] has joined #python
[17:24] == skimbrel [~skimbrel@192-195-80-114-TWIL.static.monkeybrains.net] has quit [Read error: Connection reset by peer]
[17:24] == CatMtKing [~CatMtKing@ed-uluka.dyn.ucr.edu] has joined #python
[17:24] == kermit [unknown@pdpc/supporter/bronze/kermit] has quit [Quit: Leaving.]
[17:24] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:24] == skimbrel [~skimbrel@192-195-80-114-TWIL.static.monkeybrains.net] has joined #python
[17:25] == uehtesham90 [uid35565@gateway/web/irccloud.com/x-yosancheaqhpmwss] has quit [Quit: Connection closed for inactivity]
[17:25] <Alumin> Yhg1s: cool, I shall investigate
[17:25] == kermit [unknown@pdpc/supporter/bronze/kermit] has joined #python
[17:25] == mahmoudimus [~mahmoudim@199.241.202.154] has quit [Ping timeout: 240 seconds]
[17:26] == cerivera [~Adium@cpe-72-182-112-199.austin.res.rr.com] has left #python []
[17:26] == sboudrias [~sboudrias@2601:9:3480:11b9:e8df:9844:90b6:d4ab] has joined #python
[17:26] <Alumin> if pydoc -w is a quick hack I can't wait to see what the real deal is :)
[17:27] <therealfakemoot> it's more effort for sure
[17:27] <therealfakemoot> but such is the nature of life
[17:27] == mrkz [~mark@187.244.9.117] has quit [Client Quit]
[17:27] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has joined #python
[17:27] == neataroni [~neataroni@c-67-171-200-129.hsd1.or.comcast.net] has joined #python
[17:28] <pydsigner-work> Alumin, the real deal (Sphinx) is standard Python documentation style.
[17:28] == Uvoa [~caw@24-107-214-94.dhcp.stls.mo.charter.com] has quit [Ping timeout: 264 seconds]
[17:28] <Yhg1s> Alumin: docs.python.org/lib uses sphinx. So do many, many Python projects on readthedocs.org
[17:28] == beardtree [~dan@gateway/tor-sasl/beardtree] has joined #python
[17:28] <pydsigner-work> A more custom version is CherryPy's, which has a red theme.
[17:28] == jimmybot [~jimmybot@64.124.192.210] has joined #python
[17:28] <beardtree> How do I make sure something matches but is not captured within a ?P<> group?
[17:28] == lad1337 [~Adium@pD9F771B2.dip0.t-ipconnect.de] has joined #python
[17:28] == muraii [~danielbla@unaffiliated/muraii] has quit [Read error: Connection reset by peer]
[17:28] <Yhg1s> beardtree: why would you give it a name if you don't want to capture it?
[17:29] <beardtree> Yhg1s: I do want to capture it, but only parts of it
[17:29] <beardtree> And I can't take the non-capturing part out of the group
[17:29] <ssbr_at_work> beardtree: lookahead/lookbehind assertions, I suppose.
[17:29] == nedbat [~nedbat@python/psf/nedbat] has quit []
[17:29] <beardtree> Because otherwise I would need to have two groups with the same name
[17:29] == mescalinum [~m@unaffiliated/mescalinum] has quit [Max SendQ exceeded]
[17:29] <ssbr_at_work> beardtree: if those aren't flexible enough, then regexp if-then-else
[17:29] == merica [~merica@66-215-213-203.dhcp.rvsd.ca.charter.com] has joined #python
[17:29] <Yhg1s> beardtree: I don't understand, sorry. Do you want to capture that group or not? If you don't want to capture that group, why do you want to give it a name?
[17:29] <Yhg1s> (the answer is "no, you can't both give it a name and not capture it.")
[17:29] == cap3lla [~cap3lla@unaffiliated/cap3lla] has quit [Quit: protect yourself! --> www.govspy.com <-- be informed, share that!]
[17:30] <ssbr_at_work> beardtree: you can have two groups with different names and then unify them after the fact
[17:30] <ssbr_at_work> bit of a pain to verify that they can't both match though
[17:30] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:30] == nonny_t [~nonny_t@host-89-242-65-81.as13285.net] has joined #python
[17:30] == sedeki [~textual@gateway/tor-sasl/sedeki] has joined #python
[17:30] == jonascj [~jonas@ip-52-91.bnaa.dk] has joined #python
[17:30] == Eyess [~eyes@WiseOS/Founder/NiaTeppelin] has quit [Ping timeout: 240 seconds]
[17:30] == sboudrias [~sboudrias@2601:9:3480:11b9:e8df:9844:90b6:d4ab] has quit [Ping timeout: 240 seconds]
[17:30] <jakesyl> hey guys, how do i make os.walk in this progarm skip the applications directory: https://gist.github.com/jakesyl/0f642124a18c400ffdb3
[17:30] == yak [~yak@isper-224-24.isper.sk] has joined #python
[17:31] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has quit [Ping timeout: 240 seconds]
[17:31] == stangeland [~bdi@12.195.152.2] has joined #python
[17:31] <Yhg1s> jakesyl: the Applications subdirectory of of any directory, or just of the toplevel directory?
[17:32] == DTVD [~DTVD@230.115.100.220.dy.bbexcite.jp] has joined #python
[17:32] <LiquidSwordsman> So I have an algorithm I can't figure out. Given a set of coordinates in a 2d list and knowing a chunk represents a 3x3 section of it how do I find out what chunk the coordinates are in if the chunks are ordered sequentially (in a )
[17:32] <jakesyl> Yhg1s, not quite sure what that means I want to crawl nothing in ~/Applications
[17:32] == dapz [~textual@c-67-180-23-154.hsd1.ca.comcast.net] has joined #python
[17:32] == dj_pi [~dj@c-107-5-25-243.hsd1.mi.comcast.net] has quit [Ping timeout: 256 seconds]
[17:32] <jakesyl> I think i mean the top level dir though
[17:32] <LiquidSwordsman> in a 150 x 150 array, the chunks would be numbered 0-2499
[17:32] <Yhg1s> jakesyl: ok, so _just_ the Applications subdirectory of the root directory you give to os.walk?
[17:32] <jakesyl> yes
[17:33] <Yhg1s> jakesyl: then you have to remove Applications from the 'sub_dirs' list in the first iteration. When 'dir_name' is 'root'.
[17:33] <stangeland> hi, anybody knows how to run a class method on an ipengine when using ipython parallel? Basically i have a for loop, in each iteration an object is created and data is stored in the object. What i then want is to run a function on that object remotely which has access to the data in the object. How do i do that?
[17:33] == Huvet [~Adium@c-b2c6e555.07-131-73746f39.cust.bredbandsbolaget.se] has joined #python
[17:33] == evanz_ has changed nick to evanz
[17:33] <VooDooNOFX> jakesyl: ~/Applications is the user's relative home directory. You want to remove that one, or the system wide /Applications root folder?
[17:33] == jvasallo [~Adium@63-144-124-93.dia.static.qwest.net] has quit [Quit: Leaving.]
[17:34] <kevlarman> stangeland: python or not, what you're describing is impossible
[17:34] <jakesyl> that's what i did, i think in the first for loop did you see my code
[17:34] == terminalmage [~terminalm@terminalmage.net] has joined #python
[17:34] <bug_sniper> LiquidSwordsman, can't you just divide the index by 150 to get the row, and modulo the index to get the column?
[17:34] <stangeland> kevlarman, why?
[17:34] <jakesyl> VooDooNOFX the systemwide  I guess whatever contains .app files
[17:34] <frostschutz> LiquidSwordsman, somearray[y/3*150+x/3]?
[17:34] <beardtree> Yhg1s: I want to capture the group, but only parts of it
[17:34] <stangeland> kevlarman, its just a matter of serializing the object?
[17:34] == fletom [~Adium@192.222.133.163] has joined #python
[17:34] <beardtree> I tried using ?: but it's matching that part too
[17:34] <Yhg1s> beardtree: I'm afraid that's not how groups work.
[17:34] == roentgen [~none@openvpn/community/support/roentgen] has quit [Ping timeout: 260 seconds]
[17:34] == jwhisnant [~jwhisnant@unaffiliated/jwhisnant] has quit [Read error: Connection reset by peer]
[17:34] <kevlarman> stangeland: you can't mutate the same object in parallel and expect it to work
[17:34] == roentgen [~none@openvpn/community/support/roentgen] has joined #python
[17:34] <Yhg1s> beardtree: you can't capture parts of a group. You can have a non-capturing group contain more groups that are capturing, though.
[17:35] <stangeland> kevlarman, why not?
[17:35] <Yhg1s> beardtree: perhaps you should show us the actual regular expression.
[17:35] <beardtree> Yhg1s: you don't want to see it
[17:35] <_habnabit> kevlarman, what are you talking about? mmap an nfs file
[17:35] == dlman [~dlman@c-50-137-77-122.hsd1.ma.comcast.net] has joined #python
[17:35] == krawchyk [~textual@50-198-150-254-static.hfc.comcastbusiness.net] has quit [Quit: bbye]
[17:35] <Yhg1s> jakesyl: that's not what your code does, no.
[17:35] <fletom> What's the best way to make an iterable of strings look like a file? (i.e. .read(n) can be called on it).
[17:35] <beardtree> I just need to capture *parts* of a group
[17:35] <kevlarman> _habnabit: "and expect it to work"
[17:35] <_habnabit> fletom, use a StringIO
[17:35] <Yhg1s> jakesyl: your code tries to remove it from any directory, and then does more work if that fails.
[17:35] <Yhg1s> (but not more work if it succeeds.)
[17:35] <terminalmage> I'm going through some old code trying to clean it up and optimize where applicable. I came across the following line: open(testcase_filedest).read().split('\n')"
[17:35] <kevlarman> _habnabit: it will do something, just not what you want it to
[17:35] <terminalmage> would this leave an open filehandle?
[17:35] == wgreenberg [~wgreenber@204.28.125.50] has left #python ["Leaving"]
[17:35] <therealfakemoot> terminalmage: eh.
[17:35] <_habnabit> terminalmage, no, python cleans them up
[17:35] <stangeland> kevlarman, seems like this guy didnt find it impossible: http://www.reddit.com/r/IPython/comments/1hz5o1/parallel_examples_using_classes/ :)
[17:35] <jakesyl> so how do I remove it from the original directory
[17:35] <_habnabit> terminalmage, but it's a bad idea anyway. use a with block
[17:36] <beardtree> How do I make sure something matches but is not captured within a (?P<>) group?
[17:36] <fletom> _habnabit: That's for a single string == one file. I'm talking about lots of strings that together look like one big file.
[17:36] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has joined #python
[17:36] <Yhg1s> jakesyl: you call sub_dirs.remove(...) only when dir_name is root.
[17:36] <beardtree> I tried using (?:) but it is still matching in the group
[17:36] == throwinghammers [~hcs@unaffiliated/throwinghammers] has joined #python
[17:36] == t4nk [~name@gateway/tor-sasl/t4nk] has quit [Ping timeout: 264 seconds]
[17:36] <Alumin> whoa, OK...this Sphinx is a completely different beast than running pydoc
[17:36] <_habnabit> fletom, yes, join the strings together into one file
[17:36] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 272 seconds]
[17:36] <jakesyl> YHG1S since it doens't help anything I'm going to revert before that catch and paste it again
[17:36] <_habnabit> fletom, er into one string
[17:36] == buck1 [~buck1@72-18-233-166.static-ip.telepacific.net] has quit [Ping timeout: 240 seconds]
[17:36] == DTVD [~DTVD@230.115.100.220.dy.bbexcite.jp] has quit [Ping timeout: 260 seconds]
[17:36] <terminalmage> _habnabit: I figured it should be in a with block, but whoever wrote this was trying to be clever and passed that monstrosity into a function call
[17:36] <fletom> _habnabit: With ''.join? I need this to take an iterable and consume it lazily.
[17:36] == mja [~viktor@92-247-228-158.spectrumnet.bg] has quit [Ping timeout: 240 seconds]
[17:37] == ioggstream [~rpolli@93-45-42-187.ip100.fastwebnet.it] has quit [Ping timeout: 240 seconds]
[17:37] == vbabiy [~vbabiy@cpe-098-024-041-201.carolina.res.rr.com] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[17:37] <_habnabit> fletom, why do you need it to be lazy? do you need seeking as well?
[17:37] <Yhg1s> beardtree: (?:non-capturing (?P<foo>capturing) non-capturing) matches 'non-capturing capturing non-capturing' and only captures 'capturing'
[17:37] <terminalmage> _habnabit: as an argument
[17:37] <LiquidSwordsman> frostschutz: no, In a 9 x 9 array given the coordinates 4, 4 it returns ten instead of 4
[17:37] == kexmex [~kexmex@88.128.80.28] has joined #python
[17:37] == deSilva [~deSilva@c83-254-213-203.bredband.comhem.se] has joined #python
[17:38] <beardtree> Yhg1s: the thing is, I need to do an | within P<foo>
[17:38] <kmcguire> fletom: write your own StringIO like class that reads from the iterable?
[17:38] == quintus [~quintus@unaffiliated/quintus] has joined #python
[17:38] == kexmex [~kexmex@88.128.80.28] has quit [Max SendQ exceeded]
[17:38] <kmcguire> fletom: i dont understand why your doing that though
[17:38] <Yhg1s> beardtree: ok? What's stopping you from doing so?
[17:38] * basheba is now following nedbat on github
[17:38] <fletom> _habnabit: No, I don't need seeking. (Forward seeking would be nice to stay consistent though.) I just need f.read(500) to work.
[17:38] == qtrain [~qtrain@2601:b:be00:90e:1451:435b:cefd:8900] has quit [Quit: Ex-Chat]
[17:38] == mescalinum [~m@unaffiliated/mescalinum] has joined #python
[17:39] <beardtree> Yhg1s: each part of the | needs to have a non-capturing clause
[17:39] == lvdz [~aa@109.133.185.250] has joined #python
[17:39] <kevlarman> fletom: why does it need to be lazy?
[17:39] <quintus> Hi folks. I'm integrating a bash script which uses GNU find pretty heavily into a python program. Should I use subprocess to call GNU find and deal with the output in Python, or is there some better, more native way to do this?
[17:39] <Yhg1s> beardtree: ok? And do you want to match the whole group or not?
[17:39] <Yhg1s> eh
[17:39] <Yhg1s> capture the whole group or not
[17:39] == dlman [~dlman@c-50-137-77-122.hsd1.ma.comcast.net] has quit [Ping timeout: 240 seconds]
[17:39] == hzopak [~hzopak@i-like-irc.hzopak.com] has quit [Ping timeout: 240 seconds]
[17:39] <beardtree> Yhg1s: no, just parts of it
[17:39] <beardtree> There are two cases I need to capture under one name
[17:39] <kevlarman> quintus: depends on what find is doing
[17:39] <Yhg1s> beardtree: then you don't want to make the outer group a capturing group.
[17:39] <VooDooNOFX> quintus: You can do either, but you should use os.walk to walk a subtree, looking for items that match what you're looking for.
[17:39] <fletom> kmcguire: I'm downloading encrypted chunks of a file from Amazon S3, decrypting them, and generating a .zip on the fly while streaming this as an HTTP response to a browser. I modified ZipStream to take an iterable of files but my files are currently not themselves lazily constructed from the decrypted chunks. Does that make sense?
[17:40] <Yhg1s> beardtree: you can't capture multiple groups under the same name.
[17:40] <ssbr_at_work> beardtree: you can use if-then-else to move stuff that's conditional on what matches internally, to be conditional outside of the capturing group. Or you can use lookahead assertions to match without consuming anything.
[17:40] <beardtree> I am aware
[17:40] <Yhg1s> you'd have to make it a single group.
[17:40] == hzopak [~hzopak@i-like-irc.hzopak.com] has joined #python
[17:40] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has quit [Remote host closed the connection]
[17:40] <quintus> VooDooNOFX: thanks for the tip. I'll get you all a link to both the relevant portion of the bash script and the python program.
[17:40] <kevlarman> fletom: i think boto more or less handles that
[17:40] == shackra [~shackra@186.32.192.115] has joined #python
[17:41] <LiquidSwordsman> bug_sniper, frostschutz here is the code I'm using to create the chunk array. http://bpaste.net/show/zNasd2l1F2iMM6xuJArM/ The goal is to given a pair of coordinates (corresponding to the initial array) figure out which chunk I'm looking at
[17:41] == m8 [~m@unaffiliated/m8] has quit [Quit: Sto andando via]
[17:41] == JotaK [~ChatZill@unaffiliated/jotak] has quit [Ping timeout: 264 seconds]
[17:41] == sboudrias [~sboudrias@2601:9:3480:11b9:e84b:23c7:a19c:d687] has joined #python
[17:41] == hoglahoo [~hoglahoo@unaffiliated/hoglahoo] has joined #python
[17:41] <fletom> kevlarman: Handles what exactly? The only part that involves AWS is downloading the small 1 MB chunks, so I don't think so.
[17:41] == bkuberek [~bkuberek@2600:c0e:3002:120:c066:9766:cdd6:94c] has quit [Ping timeout: 240 seconds]
[17:41] <kevlarman> fletom: acting as a lazy file-like object
[17:41] <jakesyl> YHG1S still getttin Value Error, new code: https://gist.github.com/jakesyl/75262b6dfae4410f0b09
[17:42] == onizo [~onizo@cpe-76-88-78-101.san.res.rr.com] has joined #python
[17:42] <kevlarman> fletom: although if your chunks are only 1mb, there's no real reason for you to bother being lazy
[17:42] == bus3rr0r [~bus3rr0r@unaffiliated/bus3rr0r] has joined #python
[17:42] <bug_sniper> LiquidSwordsman, don't you want your loop cap to be len/3?
[17:42] <kevlarman> you might as well process entire chunks
[17:42] <Yhg1s> jakesyl: then your toplevel directory doesn't contain an 'Applications' subdirectory.
[17:42] == seanz [~seanz@2605:a601:810:4d01:81cd:743d:5aa3:d580] has quit [Ping timeout: 240 seconds]
[17:42] == thelinuxkid [~thelinuxk@static-108-0-187-37.lsanca.fios.verizon.net] has quit [Quit: Leaving.]
[17:42] <quintus> VooDooNOFX & kevlarman: relevant portion of the bash script: https://github.com/qguv/agile/blob/df78ebc400b5a522350c678873306abbd10d7540/agile-all.sh#L21-L27
[17:42] <Yhg1s> jakesyl: perhaps you want to catch that exception and ignore it.
[17:42] <fletom> kevlarman: That'd only be for a single S3 object though. I'm talking about downloading dozens of objects, processing them in my code, combining them into several large files, and streaming it as a .zip.
[17:43] <Yhg1s> jakesyl: I doubt you want to make lines 33-40 conditional on the 'if' on line 30, though.
[17:43] <jakesyl> YHG1s then what does, and that's what i was doing before, in my previous paste
[17:43] <fletom> kevlarman: This isn't about downloading the chunks, that's easy.
[17:43] == ambro718 [~ambro@gentoo/contributor/ambro718] has quit [Ping timeout: 240 seconds]
[17:43] == Nizumzen [~Nizumzen@cpc1-reig5-2-0-cust251.6-3.cable.virginm.net] has joined #python
[17:43] <Yhg1s> jakesyl: you were unconditionally removing it earlier, and then *doing lines 33-40* in the except handler.
[17:43] <Yhg1s> jakesyl: that's probably not what you want either.
[17:43] == Gambit- [~Gambit-@unaffiliated/gambit-] has quit [Ping timeout: 256 seconds]
[17:44] <jakesyl> is there anyway to just add an exception into the for loop
[17:44] == dcrosta [~dcrosta@66.9.135.66] has quit [Quit: Quitting.]
[17:44] <kevlarman> fletom: then i guess just look at the source of stringio (not cstringio) it's trivial and easy to modify to do what you want
[17:44] == mlncn [~mlncn@18.111.14.36] has quit [Ping timeout: 240 seconds]
[17:44] <jakesyl> okay YHG1s do i have to set topdown to true
[17:44] <LiquidSwordsman> bug_sniper its called with size being equal to chunk_size (3 atm) so I can quickly adjust the size of chunks to find an optimal balance between draw speed and memory use, so if I made maps 160x160 and chunks 4x4 it would handle that
[17:44] == buck1 [~buck1@72-18-233-166.static-ip.telepacific.net] has joined #python
[17:45] == stangeland [~bdi@12.195.152.2] has quit [Ping timeout: 260 seconds]
[17:45] == robvdl [~robvdl@2404:130:0:1000:6984:244d:8550:155a] has joined #python
[17:45] == Balliad [~textual@52D95C9B.cm-11-1b.dynamic.ziggo.nl] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[17:45] == sboudrias [~sboudrias@2601:9:3480:11b9:e84b:23c7:a19c:d687] has quit [Ping timeout: 240 seconds]
[17:45] <kevlarman> quintus: yeah i'd implement that with os.path.walk i think
[17:45] <quintus> kevlarman: specifically, find (and friends; there's a lot of piping involved) is looking for the deepest directory matching "*/res/layouts" in a folder
[17:45] == mescalinum [~m@unaffiliated/mescalinum] has quit [Ping timeout: 272 seconds]
[17:45] <quintus> okay, and does os.path play nicely with pathlib?
[17:46] <quintus> or is there an equivalent for pathlib-style paths?
[17:46] == designbybeck [~designbyb@x172y125.angelo.edu] has joined #python
[17:46] == urh [~urh@flame.unix.si] has quit [Remote host closed the connection]