pathquestion.md

[16:51] == jakesyl [442d5d98@gateway/web/freenode/ip.68.45.93.152] has joined #python
[16:51] -ChanServ- [#python] Welcome to #python, puny fleshlings. Please see our website, http://pound-python.org/ , for information about the channel and Python.
[16:51] == pedantic [~pedantic@unaffiliated/pedantic] has joined #python
[16:51] <kofna> therealfakemoot: I'm worried I'll develop bad habits
[16:51] == bars0 [~Name@87.106.107.151] has joined #python
[16:51] <therealfakemoot> kofna: You will
[16:51] <therealfakemoot> Loads and loads of them
[16:51] <jakesyl> Happy 4th! does anyone know how I can access last modification of the files and not their paths, similiar to this: os.path.getatime(path)
[16:51] <therealfakemoot> and eventually you'll break them
[16:51] == kaiserpathos [~kaiserpat@cpe-76-184-228-101.tx.res.rr.com] has joined #python
[16:51] <therealfakemoot> jakesyl: I'm not sure what you mean by "not their paths"
[16:51] <scruz> if you don’t want to learn bad habits, don’t learn to program ;)
[16:52] == tedoc2000 [~tedoc2000@173-11-87-145-SFBA.hfc.comcastbusiness.net] has joined #python
[16:52] <bob2> jakesyl, ?
[16:52] == eka__ [~eka@190.117.224.180] has quit [Quit: My computer has gone to sleep. ZZZzzz…]
[16:52] <jakesyl> Christopher Poole: What I mean is not the folder's access date but the files themselves
[16:52] <bob2> what on earth are you talking about
[16:52] <therealfakemoot> jakesyl: so pass a file path instead of a directory path
[16:52] <bob2> the only sensible way to get at the file is by its' path
[16:52] <jakesyl> and get the last access time for that file path
[16:53] <nanonyme> Note atime is not modification time
[16:53] <nanonyme> It's access time
[16:53] <jakesyl> okay example: I want to get a file in /tmp so how do i get the last access time for tmp/file instead of for last access to tmp
[16:53] <bob2> lordy
[16:53] <therealfakemoot> jakesyl: by passing `"/tmp/file"` to getatime
[16:53] == kireevco [~kireevco@cpe-76-175-91-121.socal.res.rr.com] has quit [Quit: Leaving.]
[16:53] <jakesyl> and yes nanonyme
[16:53] == DTVD [~DTVD@230.115.100.220.dy.bbexcite.jp] has quit [Ping timeout: 264 seconds]
[16:53] <bob2> getatime("/tmp/whatever")
[16:53] <jakesyl> is get a time the method name?
[16:54] <jakesyl> no, haha whats the method name
[16:54] <bob2> ?
[16:54] <jakesyl> okay nvm i got it thanks bob2 and chris poole
[16:54] <KirkMcDonald> os.path.getatime()
[16:54] <bob2> https://docs.python.org/2/library/os.path.html#os.path.getatime
[16:54] == Cache_Money [~Cache_Mon@c-67-182-135-234.hsd1.wa.comcast.net] has quit [Quit: Cache_Money]
[16:54] == djural [~djural@212095007022.public.telering.at] has quit [Quit: WeeChat 1.0-dev]
[16:54] <jakesyl> and to verify this is for access and not modification?
[16:54] <bob2> there is no one called chris poole here
[16:55] <bob2> stop being so weird
[16:55] <jakesyl> chris poole is moots name
[16:55] == Praise [~Fat@unaffiliated/praise] has joined #python
[16:55] <bob2> it may be for access, if the filesystem supports that
[16:55] <jakesyl> get it moot from 4chan=chris poole
[16:55] == Jordan_U [~jordan@c-50-173-14-225.hsd1.ca.comcast.net] has quit [Remote host closed the connection]
[16:55] <bob2> yes i know who it is
[16:55] <nanonyme> atime means when it was last read
[16:55] <nanonyme> (well, or written)
[16:55] <simpson> jakesyl: moot's nick on Freenode is `moot`; therealfakemoot is not moot.
[16:55] == Balliad [~textual@52D95C9B.cm-11-1b.dynamic.ziggo.nl] has quit [Quit: My MacBook Pro has gone to sleep. ZZZzzz…]
[16:55] == eka [~eka@190.117.224.180] has joined #python
[16:55] <nanonyme> mtime is likely what you actually want if you care about modification
[16:55] <jakesyl> simpson it's a joke
[16:55] <bob2> or some random time in the past, depending on filesystem type and mount options