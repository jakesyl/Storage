kill.d				uname
killall				uncompress
kinit				unexpand
klist				unifdef
kpasswd				unifdefall
kramdown			uniq
krb5-config			units
kswitch				unpack200
lam				unvis
last				unzip
lastcomm			unzipsfx
lastwords			update_dyld_shared_cache
latency				uptime
lc				users
ld				uucp
ldapadd				uudecode
ldapcompare			uuencode
ldapdelete			uuidgen
ldapexop			uulog
ldapmodify			uuname
ldapmodrdn			uupick
ldappasswd			uustat
ldapsearch			uuto
ldapurl				uux
ldapwhoami			vagrant
leaks				vbnc
leave				vbnc2
less				vboxwebsrv
lessecho			vi
lex				view
libnetcfg			vim
libnetcfg5.12			vimdiff
libnetcfg5.16			vimtutor
libtool				vis
lipo				vm_stat
listen				vmmap
lkbib				w
lldb				wait
llvm-g++			wall
llvm-gcc			wc
loads.d				wdutil
locale				weblatency.d
localedef			what
locate				whatis
lockfile			whereis
logger				which
login				who
logname				whoami
look				whois
lookbib				wish
lorder				wish8.4
lp				wish8.5
lpoptions			write
lppasswd			wsdl
lpq				wsdl2
lpr				wsgen
lprm				wsimport
lpstat				xar
lsappinfo			xargs
lsbom				xattr
lsm				xattr-2.5
lsvfs				xattr-2.6
lwp-download			xattr-2.7
lwp-download5.12		xbuild
lwp-download5.16		xcode-select
lwp-dump			xcodebuild
lwp-dump5.12			xcrun
lwp-dump5.16			xed
lwp-mirror			xgettext.pl
lwp-mirror5.12			xgettext5.12.pl
lwp-mirror5.16			xgettext5.16.pl
lwp-request			xip
lwp-request5.12			xjc
lwp-request5.16			xml2-config
m4				xml2man
macbinary			xmlcatalog
macerror			xmllint
macerror5.12			xpath
macerror5.16			xpath5.12
machine				xpath5.16
macpack				xsd
mail				xslt-config
mailq				xsltproc
mailstat			xsp
mailx				xsp2
make				xsp4
makecert			xsubpp
makeinfo			xsubpp5.12
malloc_history			xsubpp5.16
man				xxd
manpath				yacc
mautil				yes
mconfig				ypcat
mcs				ypmatch
mcxquery			ypwhich
mcxrefresh			zcat
mdassembler			zcmp
mddiagnose			zdiff
mdfind				zegrep
mdimport			zfgrep
mdimport32			zforce
mdls				zgrep
mdoc				zip
mdoc-assemble			zipcloak
mdoc-export-html		zipdetails
mdoc-export-msxdoc		zipdetails5.16
mdoc-update			zipgrep
mdoc-validate			zipinfo
mdutil				zipnote
mdvalidater			zipsplit
memcached			zless
memory_pressure			zmore
memtest				znew
mesg				zprint
mib2c
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  zip                         DEPRECATED. Zip individual packages.
  unzip                       DEPRECATED. Unzip individual packages.
  bundle                      DEPRECATED. Create pybundles.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output.
  --log-file <path>           Path to a verbose non-appending log, that only
                              logs failures. This log is active by default at
                              /Users/Jake_Sylvestre/.pip/pip.log.
  --log <path>                Path to a verbose appending log. This log is
                              inactive by default.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup.
  --cert <path>               Path to alternate CA bundle.
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ pip help

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  zip                         DEPRECATED. Zip individual packages.
  unzip                       DEPRECATED. Unzip individual packages.
  bundle                      DEPRECATED. Create pybundles.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output.
  --log-file <path>           Path to a verbose non-appending log, that only
                              logs failures. This log is active by default at
                              /Users/Jake_Sylvestre/.pip/pip.log.
  --log <path>                Path to a verbose appending log. This log is
                              inactive by default.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup.
  --cert <path>               Path to alternate CA bundle.
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ pip install paramiko
Requirement already satisfied (use --upgrade to upgrade): paramiko in /usr/local/lib/python2.7/site-packages
Cleaning up...
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import paramiko
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named paramiko
>>> exit()
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ python2.7
Python 2.7.5 (default, Mar  9 2014, 22:15:05)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import paramiko
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named paramiko
>>> exit()
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ sudo pip install pamariko
Password:
Downloading/unpacking pamariko
  Could not find any downloads that satisfy the requirement pamariko
Cleaning up...
No distributions at all found for pamariko
Storing debug log for failure in /Users/Jake_Sylvestre/.pip/pip.log
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ sudo pip install paramiko
Requirement already satisfied (use --upgrade to upgrade): paramiko in /usr/local/lib/python2.7/site-packages
Cleaning up...
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ sudo pip install paramiko --upgrade
Requirement already up-to-date: paramiko in /usr/local/lib/python2.7/site-packages
Cleaning up...
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import paramiko
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named paramiko
>>> exit()
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ pip install ecdsa
Requirement already satisfied (use --upgrade to upgrade): ecdsa in /usr/local/lib/python2.7/site-packages
Cleaning up...
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ecsda
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named ecsda
>>> import ecdsa
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named ecdsa
>>> python --version
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> exit()
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ python --version
Python 2.7.3
Jakes-MacBook-Pro-3:bin Jake_Sylvestre$ cd /Users/Jake_Sylvestre/Downloads/ecdsa-0.11
Jakes-MacBook-Pro-3:ecdsa-0.11 Jake_Sylvestre$ python setup.py build
running build
running build_py
creating build
creating build/lib
creating build/lib/ecdsa
copying ecdsa/__init__.py -> build/lib/ecdsa
copying ecdsa/_version.py -> build/lib/ecdsa
copying ecdsa/curves.py -> build/lib/ecdsa
copying ecdsa/der.py -> build/lib/ecdsa
copying ecdsa/ecdsa.py -> build/lib/ecdsa
copying ecdsa/ellipticcurve.py -> build/lib/ecdsa
copying ecdsa/keys.py -> build/lib/ecdsa
copying ecdsa/numbertheory.py -> build/lib/ecdsa
copying ecdsa/rfc6979.py -> build/lib/ecdsa
copying ecdsa/six.py -> build/lib/ecdsa
copying ecdsa/test_pyecdsa.py -> build/lib/ecdsa
copying ecdsa/util.py -> build/lib/ecdsa
Jakes-MacBook-Pro-3:ecdsa-0.11 Jake_Sylvestre$ python setup.py install
running install
running build
running build_py
running install_lib
creating /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/__init__.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/_version.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/curves.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/der.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/ecdsa.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/ellipticcurve.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/keys.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/numbertheory.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/rfc6979.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/six.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/test_pyecdsa.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
copying build/lib/ecdsa/util.py -> /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/__init__.py to __init__.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/_version.py to _version.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/curves.py to curves.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/der.py to der.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/ecdsa.py to ecdsa.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/ellipticcurve.py to ellipticcurve.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/keys.py to keys.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/numbertheory.py to numbertheory.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/rfc6979.py to rfc6979.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/six.py to six.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/test_pyecdsa.py to test_pyecdsa.pyc
byte-compiling /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa/util.py to util.pyc
running install_egg_info
Writing /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ecdsa-0.11-py2.7.egg-info
Jakes-MacBook-Pro-3:ecdsa-0.11 Jake_Sylvestre$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ecdsa
>>> exit()
Jakes-MacBook-Pro-3:ecdsa-0.11 Jake_Sylvestre$ cd /Users/Jake_Sylvestre/Downloads/paramiko-1.14.0
Jakes-MacBook-Pro-3:paramiko-1.14.0 Jake_Sylvestre$ python setup.py build
running build
running build_py
creating build
creating build/lib
creating build/lib/paramiko
copying paramiko/__init__.py -> build/lib/paramiko
copying paramiko/_winapi.py -> build/lib/paramiko
copying paramiko/agent.py -> build/lib/paramiko
copying paramiko/auth_handler.py -> build/lib/paramiko
copying paramiko/ber.py -> build/lib/paramiko
copying paramiko/buffered_pipe.py -> build/lib/paramiko
copying paramiko/channel.py -> build/lib/paramiko
copying paramiko/client.py -> build/lib/paramiko
copying paramiko/common.py -> build/lib/paramiko
copying paramiko/compress.py -> build/lib/paramiko
copying paramiko/config.py -> build/lib/paramiko
copying paramiko/dsskey.py -> build/lib/paramiko
copying paramiko/ecdsakey.py -> build/lib/paramiko
copying paramiko/file.py -> build/lib/paramiko
copying paramiko/hostkeys.py -> build/lib/paramiko
copying paramiko/kex_gex.py -> build/lib/paramiko
copying paramiko/kex_group1.py -> build/lib/paramiko
copying paramiko/message.py -> build/lib/paramiko
copying paramiko/packet.py -> build/lib/paramiko
copying paramiko/pipe.py -> build/lib/paramiko
copying paramiko/pkey.py -> build/lib/paramiko
copying paramiko/primes.py -> build/lib/paramiko
copying paramiko/proxy.py -> build/lib/paramiko
copying paramiko/py3compat.py -> build/lib/paramiko
copying paramiko/resource.py -> build/lib/paramiko
copying paramiko/rsakey.py -> build/lib/paramiko
copying paramiko/server.py -> build/lib/paramiko
copying paramiko/sftp.py -> build/lib/paramiko
copying paramiko/sftp_attr.py -> build/lib/paramiko
copying paramiko/sftp_client.py -> build/lib/paramiko
copying paramiko/sftp_file.py -> build/lib/paramiko
copying paramiko/sftp_handle.py -> build/lib/paramiko
copying paramiko/sftp_server.py -> build/lib/paramiko
copying paramiko/sftp_si.py -> build/lib/paramiko
copying paramiko/ssh_exception.py -> build/lib/paramiko
copying paramiko/transport.py -> build/lib/paramiko
copying paramiko/util.py -> build/lib/paramiko
copying paramiko/win_pageant.py -> build/lib/paramiko
Jakes-MacBook-Pro-3:paramiko-1.14.0 Jake_Sylvestre$ python setup.py install
running install
running bdist_egg
running egg_info
writing requirements to paramiko.egg-info/requires.txt
writing paramiko.egg-info/PKG-INFO
writing top-level names to paramiko.egg-info/top_level.txt
writing dependency_links to paramiko.egg-info/dependency_links.txt
reading manifest file 'paramiko.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'paramiko.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.6-intel/egg
running install_lib
running build_py
creating build/bdist.macosx-10.6-intel
creating build/bdist.macosx-10.6-intel/egg
creating build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/__init__.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/_winapi.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/agent.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/auth_handler.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/ber.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/buffered_pipe.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/channel.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/client.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/common.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/compress.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/config.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/dsskey.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/ecdsakey.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/file.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/hostkeys.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/kex_gex.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/kex_group1.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/message.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/packet.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/pipe.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/pkey.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/primes.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/proxy.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/py3compat.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/resource.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/rsakey.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/server.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp_attr.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp_client.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp_file.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp_handle.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp_server.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/sftp_si.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/ssh_exception.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/transport.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/util.py -> build/bdist.macosx-10.6-intel/egg/paramiko
copying build/lib/paramiko/win_pageant.py -> build/bdist.macosx-10.6-intel/egg/paramiko
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/__init__.py to __init__.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/_winapi.py to _winapi.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/agent.py to agent.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/auth_handler.py to auth_handler.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/ber.py to ber.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/buffered_pipe.py to buffered_pipe.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/channel.py to channel.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/client.py to client.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/common.py to common.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/compress.py to compress.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/config.py to config.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/dsskey.py to dsskey.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/ecdsakey.py to ecdsakey.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/file.py to file.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/hostkeys.py to hostkeys.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/kex_gex.py to kex_gex.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/kex_group1.py to kex_group1.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/message.py to message.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/packet.py to packet.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/pipe.py to pipe.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/pkey.py to pkey.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/primes.py to primes.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/proxy.py to proxy.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/py3compat.py to py3compat.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/resource.py to resource.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/rsakey.py to rsakey.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/server.py to server.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp.py to sftp.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp_attr.py to sftp_attr.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp_client.py to sftp_client.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp_file.py to sftp_file.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp_handle.py to sftp_handle.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp_server.py to sftp_server.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/sftp_si.py to sftp_si.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/ssh_exception.py to ssh_exception.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/transport.py to transport.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/util.py to util.pyc
byte-compiling build/bdist.macosx-10.6-intel/egg/paramiko/win_pageant.py to win_pageant.pyc
creating build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying paramiko.egg-info/PKG-INFO -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying paramiko.egg-info/SOURCES.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying paramiko.egg-info/dependency_links.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying paramiko.egg-info/requires.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying paramiko.egg-info/top_level.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/paramiko-1.14.0-py2.7.egg' and adding 'build/bdist.macosx-10.6-intel/egg' to it
removing 'build/bdist.macosx-10.6-intel/egg' (and everything under it)
Processing paramiko-1.14.0-py2.7.egg
creating /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/paramiko-1.14.0-py2.7.egg
Extracting paramiko-1.14.0-py2.7.egg to /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
Adding paramiko 1.14.0 to easy-install.pth file
error: /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/easy-install.pth: Permission denied
Jakes-MacBook-Pro-3:paramiko-1.14.0 Jake_Sylvestre$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import paramiko
>>> ^[[A^[[A^[[A^[[B^[[B^[[
  File "<stdin>", line 1
^
SyntaxError: invalid syntax
>>> exit()
Jakes-MacBook-Pro-3:paramiko-1.14.0 Jake_Sylvestre$ cd /Users/Jake_Sylvestre/Downloads/pysftp-0.2.8
Jakes-MacBook-Pro-3:pysftp-0.2.8 Jake_Sylvestre$ python setup.py build
running build
running build_py
creating build
creating build/lib
copying pysftp.py -> build/lib
Jakes-MacBook-Pro-3:pysftp-0.2.8 Jake_Sylvestre$ python setup.py install
running install
running bdist_egg
running egg_info
writing requirements to pysftp.egg-info/requires.txt
writing pysftp.egg-info/PKG-INFO
writing top-level names to pysftp.egg-info/top_level.txt
writing dependency_links to pysftp.egg-info/dependency_links.txt
reading manifest file 'pysftp.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
no previously-included directories found matching 'docs/_build'
writing manifest file 'pysftp.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.6-intel/egg
running install_lib
running build_py
creating build/bdist.macosx-10.6-intel
creating build/bdist.macosx-10.6-intel/egg
copying build/lib/pysftp.py -> build/bdist.macosx-10.6-intel/egg
byte-compiling build/bdist.macosx-10.6-intel/egg/pysftp.py to pysftp.pyc
creating build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying pysftp.egg-info/PKG-INFO -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying pysftp.egg-info/SOURCES.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying pysftp.egg-info/dependency_links.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying pysftp.egg-info/requires.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
copying pysftp.egg-info/top_level.txt -> build/bdist.macosx-10.6-intel/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/pysftp-0.2.8-py2.7.egg' and adding 'build/bdist.macosx-10.6-intel/egg' to it
removing 'build/bdist.macosx-10.6-intel/egg' (and everything under it)
Processing pysftp-0.2.8-py2.7.egg
creating /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pysftp-0.2.8-py2.7.egg
Extracting pysftp-0.2.8-py2.7.egg to /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
Adding pysftp 0.2.8 to easy-install.pth file
error: /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/easy-install.pth: Permission denied
Jakes-MacBook-Pro-3:pysftp-0.2.8 Jake_Sylvestre$ sudo python setup.py install
Password:
running install
running bdist_egg
running egg_info
writing requirements to pysftp.egg-info/requires.txt
writing pysftp.egg-info/PKG-INFO
writing top-level names to pysftp.egg-info/top_level.txt
writing dependency_links to pysftp.egg-info/dependency_links.txt
reading manifest file 'pysftp.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
no previously-included directories found matching 'docs/_build'
writing manifest file 'pysftp.egg-info/SOURCES.txt'
installing library code to build/bdist.macosx-10.9-intel/egg
running install_lib
running build_py
creating build/bdist.macosx-10.9-intel
creating build/bdist.macosx-10.9-intel/egg
copying build/lib/pysftp.py -> build/bdist.macosx-10.9-intel/egg
byte-compiling build/bdist.macosx-10.9-intel/egg/pysftp.py to pysftp.pyc
creating build/bdist.macosx-10.9-intel/egg/EGG-INFO
copying pysftp.egg-info/PKG-INFO -> build/bdist.macosx-10.9-intel/egg/EGG-INFO
copying pysftp.egg-info/SOURCES.txt -> build/bdist.macosx-10.9-intel/egg/EGG-INFO
copying pysftp.egg-info/dependency_links.txt -> build/bdist.macosx-10.9-intel/egg/EGG-INFO
copying pysftp.egg-info/requires.txt -> build/bdist.macosx-10.9-intel/egg/EGG-INFO
copying pysftp.egg-info/top_level.txt -> build/bdist.macosx-10.9-intel/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating 'dist/pysftp-0.2.8-py2.7.egg' and adding 'build/bdist.macosx-10.9-intel/egg' to it
removing 'build/bdist.macosx-10.9-intel/egg' (and everything under it)
Processing pysftp-0.2.8-py2.7.egg
Copying pysftp-0.2.8-py2.7.egg to /Library/Python/2.7/site-packages
Adding pysftp 0.2.8 to easy-install.pth file

Installed /Library/Python/2.7/site-packages/pysftp-0.2.8-py2.7.egg
Processing dependencies for pysftp==0.2.8
Searching for paramiko>=1.7.7
Reading http://pypi.python.org/simple/paramiko/
Best match: paramiko 1.14.0
Downloading https://pypi.python.org/packages/source/p/paramiko/paramiko-1.14.0.tar.gz#md5=e26324fd398af68ad506fe98853835c3
Processing paramiko-1.14.0.tar.gz
Running paramiko-1.14.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-FGbmOi/paramiko-1.14.0/egg-dist-tmp-I2ShCU
zip_safe flag not set; analyzing archive contents...
Adding paramiko 1.14.0 to easy-install.pth file

Installed /Library/Python/2.7/site-packages/paramiko-1.14.0-py2.7.egg
Searching for ecdsa
Reading http://pypi.python.org/simple/ecdsa/
Best match: ecdsa 0.11
Downloading https://pypi.python.org/packages/source/e/ecdsa/ecdsa-0.11.tar.gz#md5=8ef586fe4dbb156697d756900cb41d7c
Processing ecdsa-0.11.tar.gz
Running ecdsa-0.11/setup.py -q bdist_egg --dist-dir /tmp/easy_install-ubk_1g/ecdsa-0.11/egg-dist-tmp-0vy9Tf
zip_safe flag not set; analyzing archive contents...
Adding ecdsa 0.11 to easy-install.pth file

Installed /Library/Python/2.7/site-packages/ecdsa-0.11-py2.7.egg
Searching for pycrypto>=2.1,!=2.4
Reading http://pypi.python.org/simple/pycrypto/
Best match: pycrypto 2.6.1
Downloading https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz#md5=55a61a054aa66812daf5161a0d5d7eda
Processing pycrypto-2.6.1.tar.gz
Running pycrypto-2.6.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-UD9byj/pycrypto-2.6.1/egg-dist-tmp-MyNZjI
src/_fastmath.c:83:13: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                size = p->ob_size;
                     ~ ~~~^~~~~~~
src/_fastmath.c:86:10: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
                size = -p->ob_size;
                     ~ ^~~~~~~~~~~
src/_fastmath.c:113:49: warning: implicit conversion loses integer precision:
      'unsigned long' to 'int' [-Wshorten-64-to-32]
        int size = (mpz_sizeinbase (m, 2) + SHIFT - 1) / SHIFT;
            ~~~~   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
src/_fastmath.c:1310:12: warning: implicit conversion loses integer precision:
      'unsigned long' to 'unsigned int' [-Wshorten-64-to-32]
                offset = mpz_get_ui (mpz_offset);
                       ~ ^~~~~~~~~~~~~~~~~~~~~~~
/usr/local/include/gmp.h:840:20: note: expanded from macro 'mpz_get_ui'
#define mpz_get_ui __gmpz_get_ui
                   ^
src/_fastmath.c:1360:10: warning: implicit conversion loses integer precision:
      'unsigned long' to 'int' [-Wshorten-64-to-32]
                return return_val;
                ~~~~~~ ^~~~~~~~~~
src/_fastmath.c:1373:27: warning: implicit conversion loses integer precision:
      'unsigned long' to 'int' [-Wshorten-64-to-32]
                rounds = mpz_get_ui (n) - 2;
                       ~ ~~~~~~~~~~~~~~~^~~
src/_fastmath.c:1433:9: warning: implicit conversion loses integer precision:
      'unsigned long' to 'int' [-Wshorten-64-to-32]
        return return_val;
        ~~~~~~ ^~~~~~~~~~
src/_fastmath.c:1545:20: warning: comparison of unsigned expression < 0 is
      always false [-Wtautological-compare]
                        else if (result < 0)
                                 ~~~~~~ ^ ~
src/_fastmath.c:1621:20: warning: comparison of unsigned expression < 0 is
      always false [-Wtautological-compare]
                        else if (result < 0)
                                 ~~~~~~ ^ ~
9 warnings generated.
src/_fastmath.c:1545:20: warning: comparison of unsigned expression < 0 is
      always false [-Wtautological-compare]
                        else if (result < 0)
                                 ~~~~~~ ^ ~
src/_fastmath.c:1621:20: warning: comparison of unsigned expression < 0 is
      always false [-Wtautological-compare]
                        else if (result < 0)
                                 ~~~~~~ ^ ~
2 warnings generated.
ld: warning: ignoring file /usr/local/lib/libgmp.dylib, file was built for x86_64 which is not the architecture being linked (i386): /usr/local/lib/libgmp.dylib
In file included from src/MD2.c:147:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
src/MD2.c:44:19: warning: unused variable 'md2_oid' [-Wunused-const-variable]
static const char md2_oid[] = { 0x06, 0x08, 0x2a, 0x86, 0x48, 0x86, 0xf7...
                  ^
2 warnings generated.
src/MD2.c:44:19: warning: unused variable 'md2_oid' [-Wunused-const-variable]
static const char md2_oid[] = { 0x06, 0x08, 0x2a, 0x86, 0x48, 0x86, 0xf7...
                  ^
1 warning generated.
In file included from src/MD4.c:221:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
1 warning generated.
In file included from src/SHA256.c:72:
In file included from src/hash_SHA2_template.c:199:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
1 warning generated.
In file included from src/SHA224.c:73:
In file included from src/hash_SHA2_template.c:199:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
1 warning generated.
In file included from src/SHA384.c:80:
In file included from src/hash_SHA2_template.c:199:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
1 warning generated.
In file included from src/SHA512.c:80:
In file included from src/hash_SHA2_template.c:199:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
1 warning generated.
In file included from src/RIPEMD160.c:425:
src/hash_template.c:134:9: warning: implicit conversion loses integer precision:
      'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]
        size = PyBytes_Size(value);
             ~ ^~~~~~~~~~~~~~~~~~~
src/pycrypto_compat.h:39:22: note: expanded from macro 'PyBytes_Size'
#define PyBytes_Size PyString_Size
                     ^
src/RIPEMD160.c:197:20: warning: unused function 'byteswap_digest'
      [-Wunused-function]
static inline void byteswap_digest(uint32_t *p)
                   ^
2 warnings generated.
src/RIPEMD160.c:197:20: warning: unused function 'byteswap_digest'
      [-Wunused-function]
static inline void byteswap_digest(uint32_t *p)
                   ^
1 warning generated.
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1378:42: warning: implicit conversion loses integer
      precision: 'long' to 'ulong32' (aka 'unsigned int') [-Wshorten-64-to-32]
        *cook    = (*raw0 & 0x00fc0000L) << 6;
                 ~ ~~~~~~~~~~~~~~~~~~~~~~^~~~
src/libtom/tomcrypt_des.c:1382:42: warning: implicit conversion loses integer
      precision: 'long' to 'ulong32' (aka 'unsigned int') [-Wshorten-64-to-32]
        *cook    = (*raw0 & 0x0003f000L) << 12;
                 ~ ~~~~~~~~~~~~~~~~~~~~~~^~~~~
src/libtom/tomcrypt_des.c:1603:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], pt+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1604:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], pt+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1624:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], ct+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1625:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], ct+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1646:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], pt+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1647:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], pt+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1669:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], ct+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1670:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], ct+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
10 warnings generated.
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1378:42: warning: implicit conversion loses integer
      precision: 'long' to 'ulong32' (aka 'unsigned int') [-Wshorten-64-to-32]
        *cook    = (*raw0 & 0x00fc0000L) << 6;
                 ~ ~~~~~~~~~~~~~~~~~~~~~~^~~~
src/libtom/tomcrypt_des.c:1382:42: warning: implicit conversion loses integer
      precision: 'long' to 'ulong32' (aka 'unsigned int') [-Wshorten-64-to-32]
        *cook    = (*raw0 & 0x0003f000L) << 12;
                 ~ ~~~~~~~~~~~~~~~~~~~~~~^~~~~
src/libtom/tomcrypt_des.c:1603:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], pt+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1604:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], pt+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1624:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], ct+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1625:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], ct+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1646:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], pt+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1647:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], pt+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1669:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[0], ct+0);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
In file included from src/DES3.c:26:
In file included from src/DES.c:32:
src/libtom/tomcrypt_des.c:1670:5: warning: implicit conversion loses integer
      precision: 'unsigned long' to 'ulong32' (aka 'unsigned int')
      [-Wshorten-64-to-32]
    LOAD32H(work[1], ct+4);
    ^~~~~~~~~~~~~~~~~~~~~~
src/libtom/tomcrypt_macros.h:51:48: note: expanded from macro 'LOAD32H'
           ((unsigned long)((y)[2] & 255)<<8)  | \
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~
10 warnings generated.
src/strxor.c:31:19: warning: unused variable 'rcsid' [-Wunused-const-variable]
static const char rcsid[] = "$Id$";
                  ^
1 warning generated.
src/strxor.c:31:19: warning: unused variable 'rcsid' [-Wunused-const-variable]
static const char rcsid[] = "$Id$";
                  ^
1 warning generated.
src/_counter.c:99:74: warning: implicit conversion loses integer precision:
      'long' to 'uint32_t' (aka 'unsigned int') [-Wshorten-64-to-32]
  ...= PyBytes_GET_SIZE(prefix) + PyBytes_GET_SIZE(suffix) + self->nbytes;
     ~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
1 warning generated.
zip_safe flag not set; analyzing archive contents...
Adding pycrypto 2.6.1 to easy-install.pth file

Installed /Library/Python/2.7/site-packages/pycrypto-2.6.1-py2.7-macosx-10.9-intel.egg
Finished processing dependencies for pysftp==0.2.8
Jakes-MacBook-Pro-3:pysftp-0.2.8 Jake_Sylvestre$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pysftp
>>> exit()
Jakes-MacBook-Pro-3:pysftp-0.2.8 Jake_Sylvestre$