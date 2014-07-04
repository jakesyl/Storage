[21:14] <nedbat> yoLo_: has high aspirations
[21:14] <nedbat> oops
[21:14] <yoLo_> thank you nedbat
[21:14] <therealfakemoot> Yeah, aim for the stars dude
[21:14] <nedbat> yoLo_ has high aspirations
[21:14] == billcd [~billcd@c-68-56-27-185.hsd1.fl.comcast.net] has joined #python
[21:14] <therealfakemoot> You can do anything. You just might have to work really hard for a long time
[21:14] <jakesyl> hey nedbat it's you again!  how do i specify the root directory like ~ on unix
[21:14] <nedbat> yoLo_: np. in return, you stay focused on the little things now, ok?
[21:14] <kevlarman> Cowmoo: fun fact, indiana has 5 timezones that are mostly the same but for historical dates may differ
[21:14] <nedbat> jakesyl: the root is /
[21:14] <dash> nedbat: i didn't know it was ever started in the first place
[21:14] <spaceshiiiiiip> https://i.imgur.com/p1r71Qk.png linux and windows https://i.imgur.com/BIX4ViG.png nedbat: dash:
[21:15] <dash> yoLo_: there are several things that provide storage for fulltext search
[21:15] == ovejorock [~ovejorock@190.206.119.52] has joined #python
[21:15] <nedbat> dash: we spent a while yesterday on the search engine aspirations
[21:15] <dash> yoLo_: elasticsearch is what we use at work
[21:15] <dash> sqlite and postgres both have fulltext search extensions, but they're less focused on it
[21:16] == az4gh4l [~az4gh4l@78.24.93.79.rev.sfr.net] has quit [Remote host closed the connection]
[21:16] <yoLo_> sqlite is only for local search only
[21:16] <yoLo_> and i was thinking of using Whoosh...
[21:16] == maikowblue [~nobody@189.6.2.33] has joined #python
[21:16] <nedbat> yoLo_: please, do me a favor, don't talk about the search engine.  You aren't ready.
[21:16] <spaceshiiiiiip> nedbat: dash: http://pastebin.com/CZH9g7u8 is the code
[21:16] <infobob> http://paste.pound-python.org/show/guWeypvFjwt2a5j8JItw/ (repasted for spaceshiiiiiip)
[21:17] <nutzz> so it seems that I can't edit the value of the session in event handlers for websockets because of the extension that I'm using to implemet this feature, I can only view their value...
[21:17] == commandocoding [~commandoc@59.180.146.93] has joined #python
[21:17] <dash> yoLo_: local search? what other kind is there
[21:17] <yoLo_> nedbat, dash seems interested
[21:17] == Questions [~account@38.88.218.190] has quit [Quit: Lost terminal]
[21:17] == ic4ever [~GravityPh@c-24-127-65-5.hsd1.va.comcast.net] has joined #python
[21:17] <nedbat> yoLo_: that doesn't mean you have to talk about it.
[21:17] == nutzz [~chatzilla@84.117.60.106] has quit [Quit: ChatZilla 0.9.90.1 [Firefox 30.0/20140608211132]]
[21:17] == commandocoding [~commandoc@59.180.146.93] has left #python []
[21:18] == littlepython [7372321a@gateway/web/freenode/ip.115.114.50.26] has quit [Quit: Page closed]
[21:18] == malte__ [~mablae@dyndsl-095-033-221-225.ewe-ip-backbone.de] has joined #python
[21:19] <nedbat> spaceshiiiiiip: seems like linux and windows have different ideas about what SetLicense does.
[21:19] == worrelsik [~FirstLigh@dhcp-089-098-145-017.chello.nl] has quit [Quit: Leaving.]
[21:19] <dash> yoLo_: having reviewed the logs i agree with nedbat mostly
[21:19] <yoLo_> yea i know..
[21:19] <ic4ever> Anyone know how to have a tkinter button increment a number in a file? (noob here)
[21:20] <nedbat> spaceshiiiiiip: the SetDescription and SetLicense functions probably don't promise a particular style, and you've gotten the two different styles.
[21:20] <yoLo_> dash, are you constantly programming ?
[21:21] <spaceshiiiiiip> nedbat: alright. i just wanted to see if there was an issue or something
[21:21] <spaceshiiiiiip> thank you
[21:21] <ic4ever> also, should I just be using something other than tkinter for a simple ugly gui?
[21:21] <ic4ever> as a beginner
[21:22] == LeMike [~Thunderbi@dslb-178-009-074-111.pools.arcor-ip.net] has quit [Ping timeout: 252 seconds]
[21:22] <kevlarman> ic4ever: tkinter is fine
[21:22] <jakesyl> ic4ever: what os u deving for
[21:22] == mablae_ [~mablae@dyndsl-095-033-178-121.ewe-ip-backbone.de] has quit [Ping timeout: 272 seconds]
[21:22] <ic4ever> windows 7
[21:22] == bkuberek [~bkuberek@74.72.159.31] has joined #python
[21:22] <dash> yoLo_: no
[21:23] == jeffisabelle [~jeffisabe@88.227.135.164] has quit [Ping timeout: 248 seconds]
[21:23] <jakesyl> I would go c# front end
[21:23] <dash> yoLo_: mostly i waste time on irc
[21:23] <jakesyl> python back end
[21:23] <Avaris> ic4ever: forget about the tkinter part, do you know how to increment a number in a file?
[21:24] <jakesyl> with c# u can vb the whole thing connect to c functions that activate python files it doesn't take that long at all, I used to do it all the time
[21:24] <jakesyl> with js tho
[21:24] <yoLo_> why don't you build some revolutionary like the facebook guy or dropbox or twitter ?
[21:24] <yoLo_> something*
[21:24] <ic4ever> actually not really avaris, perhaps I should go figure that out and come back
[21:24] == zacdev [~zacdev@unaffiliated/zacdev] has quit [Ping timeout: 246 seconds]
[21:24] == Corey84 [~Corey84@unaffiliated/corey84] has joined #python
[21:24] <jakesyl> yoLo_ who u talkin to/
[21:24] <yoLo_> dash
[21:25] <jakesyl> too ?*, k
[21:25] <kevlarman> yoLo_: dash might be above average as far as programmers go, but he's not exactly unique
[21:26] <kevlarman> yoLo_: and programming isn't the hard part of what made all of those things successful
[21:26] <kevlarman> (it's just the expensive part)
[21:26] <ic4ever> thanks ya'll
[21:26] <nedbat> yoLo_: again, you seem to completely misunderstand the nature of programming and creation in general.
[21:26] <Avaris> ic4ever: yeah, tkinter part will be trivial after that
[21:26] <jakesyl> joined late what does dash wanna do
[21:26] == cdchapm2 [~cdchapm2@unaffiliated/cdchapm2] has left #python []
[21:26] <yoLo_> nedbat, with time.. i'll understand
[21:27] == bkuberek [~bkuberek@74.72.159.31] has quit [Ping timeout: 240 seconds]
[21:27] <kazagistar> the people who made the most money programming are not actually that amazing at programming quite often
[21:27] <yoLo_> yea... i noticed
[21:27] == trustyhank [~trustyhan@199.231.242.170] has quit [Quit: My iMac has gone to sleep. ZZZzzz…]
[21:27] <nedbat> yoLo_: time, and listening.
[21:27] <kevlarman> kazagistar: there are a few notable exceptions, carmack comes to mind
[21:28] <jakesyl> no the people who make the most money are your employers who came up with the idea to make their lives easier
[21:28] <jakesyl> pandora: shit my playlist is over, I wish something could help, oh ya let's start music genome project
[21:28] == joe100 [~joe100@unaffiliated/joe100] has joined #python
[21:28] <jakesyl> apple: I'm poor and can't buy a computer, well woz get the sodering iron
[21:29] == faure [~faure@155.143.104.92] has joined #python
[21:29] <jakesyl> facebook: I wanna bang chicks without leavin the apartment
[21:29] <kazagistar> kevlarman: true, of course, they are probably even somewhat positively correlated
[21:29] == kcj [~casey@unaffiliated/kcj] has joined #python
[21:29] == Corey84 [~Corey84@unaffiliated/corey84] has quit [Ping timeout: 264 seconds]
[21:30] <jakesyl> 2048: I'm bored
[21:30] <dash> yoLo_: none of those things were revolutionary
[21:30] <kevlarman> also, entry level programmers are getting 6 digits here, not exactly complaining
[21:30] == sunya7a [~pryde@unaffiliated/sunya7a] has joined #python
[21:30] == al1o [~al1o@180.249.175.9] has joined #python
[21:30] <VooDooNOFX> kevlarman: I assume in the south bay, silicon valley?
[21:30] == batisteo [~batisteo@91EC81E4.dsl.pool.telekom.hu] has quit [Ping timeout: 246 seconds]
[21:30] == al1o [~al1o@180.249.175.9] has quit [Max SendQ exceeded]
[21:30] <jakesyl> let's be honest best programmers are restricted by their own skill
[21:30] <yoLo_> VooDooNOFX, yeah!
[21:31] <kevlarman> VooDooNOFX: more or less
[21:31] <kazagistar> once you reach a certain level of money, the amount of happyness it buys has seriously diminishing returns, and programmers are almost always above that point
[21:31] <jakesyl> steve jobs (although he was a complete fake) could think different because he didn't know what an object was
[21:31] <VooDooNOFX> entry level is about 90k-110k here in Santa Monica, CA
[21:31] <kevlarman> VooDooNOFX: south bay tends to be a bit too far south for that
[21:31] == tedoc2000 [~tedoc2000@c-50-174-188-226.hsd1.ca.comcast.net] has joined #python
[21:31] == al1o [~al1o@180.249.175.9] has joined #python
[21:31] == al1o [~al1o@180.249.175.9] has quit [Max SendQ exceeded]
[21:31] <jakesyl> I challenge one person in this chatrooom to say they wouldn't dev a ton more for a billion dollars
[21:32] == Cowmoo [~Cowmoo@199-83-221-139.PUBLIC.monkeybrains.net] has quit [Ping timeout: 240 seconds]
[21:32] <kevlarman> jakesyl: i wouldn't do more work for a billion dollars
[21:32] <kevlarman> unless i was the one choosing the work
[21:32] <dash> jakesyl: i am probably already spending as much time programming as I can
[21:32] == al1o [~al1o@180.249.175.9] has joined #python
[21:32] == al1o [~al1o@180.249.175.9] has quit [Max SendQ exceeded]
[21:32] <jakesyl> if you think it's worth doing it should be open source
[21:32] == cdchapm2 [~cdchapm2@unaffiliated/cdchapm2] has joined #python
[21:32] <cdchapm2> hi all. HOw do I run my code in the background?
[21:32] <jakesyl> and dash up 22 hrs a day
[21:33] <kevlarman> but working for someone else? you can't really bribe me with more money when you're paying me this much
[21:33] <dash> jakesyl: everything i write is open source
[21:33] == OverNord [~brn@host-091-097-122-250.ewe-ip-backbone.de] has quit [Quit: OverNord]
[21:33] <kevlarman> cdchapm2: twisted
[21:33] <jakesyl> good for you dash
[21:33] <dash> cdchapm2: depends on what you mean
[21:33] == al1o [~al1o@180.249.175.9] has joined #python
[21:33] <jakesyl> ya my python is terrible, I'm learning i dev open source wordpress and linux
[21:33] <kazagistar> I don't think I have the choice to dev more. My brain does not really work that way, and money does not change that.
[21:33] <dash> cdchapm2: what do you want to do?
[21:33] == al1o [~al1o@180.249.175.9] has quit [Max SendQ exceeded]
[21:33] <cdchapm2> kevlarman: i had not considered this
[21:33] == porco [~porco@218.30.180.178] has joined #python
[21:33] <cdchapm2> dash: write a python daemon
[21:34] <cdchapm2> kevlarman: lol
[21:34] <dash> cdchapm2: what's it do
[21:34] == jontmorehouse [~jonmoreho@2605:e000:4202:dd00:4d04:b730:bbb7:802] has joined #python
[21:34] <dash> jakesyl: the problem is that i have to spend some of the time thinking
[21:34] <dash> and i can't think and program at the same time
[21:34] == al1o [~al1o@180.249.175.9] has joined #python
[21:34] <kevlarman> jakesyl: but seriously, if you pay me more money, that's a strong incentive for me to do less work at the higher rate so i earn the same amount
[21:34] <dash> naturally i try to keep it to a minimum
[21:34] <cdchapm2> dash: here is my beautiful script http://hastebin.com/girolutowo.py
[21:34] <jakesyl> wait you get paid per hour
[21:34] <infobob> http://paste.pound-python.org/show/sWbQr276dkMuBQJjO3ut/ (repasted for cdchapm2)
[21:34] == thelinuxkid [~thelinuxk@static-108-0-187-37.lsanca.fios.verizon.net] has joined #python
[21:35] == al1o [~al1o@180.249.175.9] has quit [Max SendQ exceeded]
[21:35] <dash> cdchapm2: oh yeah this
[21:35] <dash> cdchapm2: use twisted
[21:35] <cdchapm2> dash: it works now
[21:35] == blackdev1l [~Nick@host210-144-dynamic.58-82-r.retail.telecomitalia.it] has quit [Quit: Going offline, see ya! (www.adiirc.com)]
[21:35] <cdchapm2> it works perfectly 100%
[21:35] <cdchapm2> i used select
[21:35] <dash> cdchapm2: cool
[21:35] == innertracks [~Thunderbi@c-50-135-138-138.hsd1.wa.comcast.net] has quit [Quit: innertracks]
[21:35] <jakesyl> is normal pastebin/gist banned in here?
[21:35] <kevlarman> jakesyl: not currently, but i used to be, and getting a 1099 instead of a w-2 isn't hard if that's your thing
[21:35] == tedoc2000 [~tedoc2000@c-50-174-188-226.hsd1.ca.comcast.net] has quit [Ping timeout: 244 seconds]
[21:35] <nedbat> jakesyl: pastebins are encouraged
[21:35] == al1o [~al1o@180.249.175.9] has joined #python
[21:35] <dash> jakesyl: no we just don't like clicking on pastebin.com links
[21:35] <kevlarman> jakesyl: pastebin.com has ads and null routes certain isp's here, other than that pick your favorite
[21:35] == cdchapm2__ [~cdchapm2@unaffiliated/cdchapm2] has joined #python
[21:36] == al1o [~al1o@180.249.175.9] has quit [Max SendQ exceeded]
[21:36] == az4gh4l [~az4gh4l@78.24.93.79.rev.sfr.net] has joined #python
[21:36] == eeerik [~eeerik@145-118-118-99.fttx.bbned.nl] has quit [Read error: Connection reset by peer]
[21:36] <jakesyl> then gist, i'll be back in a lil bit
[21:36] == eeerik [~eeerik@145-118-118-99.fttx.bbned.nl] has joined #python
[21:36] <VooDooNOFX> cdchapm2: "Can't run headless with logging". You can with the logging module :)
[21:36] <kazagistar> plus, we have a nice standard for a not terrible looking pastebin
