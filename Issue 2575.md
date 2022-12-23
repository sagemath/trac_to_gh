# Issue 2575: GAP doesn't compile with CC='ccache gcc'

archive/issues_002575.json:
```json
{
    "body": "Assignee: mabshoff\n\ni'm using ccache to speed up compilation. this works very well for other packages, but the configure script of GAP seems to be have an error.\n\nenvironment variables:\n\n```\nCC=ccache gcc\nCXX=ccache g++\n```\n\n\nGAP message:\n\n```\nHost system\nuname -a:\nLinux edoras 2.6.15-51-686 #1 SMP PREEMPT Tue Feb 12 16:59:15 UTC 2008 i686 GNU/Linux\n****************************************************\n****************************************************\nGCC Version\ngcc -v\nEs werden eingebaute Spezifikationen verwendet.\nZiel: i486-linux-gnu\nKonfiguriert mit: ../src/configure -v --enable-languages=c,c++,java,f95,objc,ada,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.0 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-java-awt=gtk-default --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-4.0-1.4.2.0/jre --enable-mpfr --disable-werror --with-tune=pentium4 --enable-checking=release i486-linux-gnu\nThread-Modell: posix\ngcc-Version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)\n****************************************************\nchecking build system type... i686-pc-linux-gnu\nchecking host system type... i686-pc-linux-gnu\nchecking target system type... i686-pc-linux-gnu\nchecking for gcc... ccache gcc\nchecking for C compiler default output file name... a.out\nchecking whether the C compiler works... yes\nchecking whether we are cross compiling... no\nchecking for suffix of executables...\nchecking for suffix of object files... o\nchecking whether we are using the GNU C compiler... yes\nchecking whether ccache gcc accepts -g... yes\nchecking for ccache gcc option to accept ANSI C... none needed\nchecking whether make sets $(MAKE)... yes\nconfigure: creating ./config.status\nconfig.status: creating Makefile\nconfig.status: creating sysinfo.gap\nconfig.status: creating bin/gap.sh\nBuilding and installing gap-4.4.10\nmake[1]: Betrete Verzeichnis '/local/scratch/schilly/sage/spkg/build/gap-4.4.10.p2/src'\nif test ! -d bin;  then mkdir bin;  fi\nif test ! -d bin/i686-pc-linux-gnu-ccache;  then mkdir bin/i686-pc-linux-gnu-ccache;  fi\ncp cnf/configure.out bin/i686-pc-linux-gnu-ccache/configure\n( cd bin/i686-pc-linux-gnu-ccache ; CC='ccache gcc' ./configure --target=i686-pc-linux-gnu --prefix=/local/scratch/schilly/sage/local PREFIX=/local/scratch/schilly/sage/local CC=ccache gcc CXX=ccache g++ )\nconfigure: WARNING: you should use --build, --host, --target\nconfigure: WARNING: you should use --build, --host, --target\nconfigure: WARNING: invalid host type: g++  \nchecking for gcc-gcc... ccache\nchecking for C compiler default output file name... configure: error: C compiler cannot create executables\nSee `config.log' for more details.\nmake[1]: *** [bin/i686-pc-linux-gnu-ccache/Makefile] Fehler 77\nError building gap.\n```\n\n\nmy guess:\n\nconfigure script, line 2293: `BASECC=`basename ${CC}``\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2575\n\n",
    "created_at": "2008-03-17T18:26:01Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "GAP doesn't compile with CC='ccache gcc'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2575",
    "user": "schilly"
}
```
Assignee: mabshoff

i'm using ccache to speed up compilation. this works very well for other packages, but the configure script of GAP seems to be have an error.

environment variables:

```
CC=ccache gcc
CXX=ccache g++
```


GAP message:

```
Host system
uname -a:
Linux edoras 2.6.15-51-686 #1 SMP PREEMPT Tue Feb 12 16:59:15 UTC 2008 i686 GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Es werden eingebaute Spezifikationen verwendet.
Ziel: i486-linux-gnu
Konfiguriert mit: ../src/configure -v --enable-languages=c,c++,java,f95,objc,ada,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.0 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-java-awt=gtk-default --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-4.0-1.4.2.0/jre --enable-mpfr --disable-werror --with-tune=pentium4 --enable-checking=release i486-linux-gnu
Thread-Modell: posix
gcc-Version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)
****************************************************
checking build system type... i686-pc-linux-gnu
checking host system type... i686-pc-linux-gnu
checking target system type... i686-pc-linux-gnu
checking for gcc... ccache gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache gcc accepts -g... yes
checking for ccache gcc option to accept ANSI C... none needed
checking whether make sets $(MAKE)... yes
configure: creating ./config.status
config.status: creating Makefile
config.status: creating sysinfo.gap
config.status: creating bin/gap.sh
Building and installing gap-4.4.10
make[1]: Betrete Verzeichnis '/local/scratch/schilly/sage/spkg/build/gap-4.4.10.p2/src'
if test ! -d bin;  then mkdir bin;  fi
if test ! -d bin/i686-pc-linux-gnu-ccache;  then mkdir bin/i686-pc-linux-gnu-ccache;  fi
cp cnf/configure.out bin/i686-pc-linux-gnu-ccache/configure
( cd bin/i686-pc-linux-gnu-ccache ; CC='ccache gcc' ./configure --target=i686-pc-linux-gnu --prefix=/local/scratch/schilly/sage/local PREFIX=/local/scratch/schilly/sage/local CC=ccache gcc CXX=ccache g++ )
configure: WARNING: you should use --build, --host, --target
configure: WARNING: you should use --build, --host, --target
configure: WARNING: invalid host type: g++  
checking for gcc-gcc... ccache
checking for C compiler default output file name... configure: error: C compiler cannot create executables
See `config.log' for more details.
make[1]: *** [bin/i686-pc-linux-gnu-ccache/Makefile] Fehler 77
Error building gap.
```


my guess:

configure script, line 2293: `BASECC=`basename ${CC}``


Issue created by migration from https://trac.sagemath.org/ticket/2575





---

archive/issue_comments_017590.json:
```json
{
    "body": "Attachment\n\nconfig.log produced by the configure process, for debugging, see BASECC variable",
    "created_at": "2008-03-17T18:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17590",
    "user": "schilly"
}
```

Attachment

config.log produced by the configure process, for debugging, see BASECC variable



---

archive/issue_comments_017591.json:
```json
{
    "body": "just fo the record, problem still exists in 3.0 - this time the build process doesn't halt but continues (no info about failed gap).\n\nafter ./sage startup it raises a runtime exception complaining about broken gap.",
    "created_at": "2008-04-22T14:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17591",
    "user": "schilly"
}
```

just fo the record, problem still exists in 3.0 - this time the build process doesn't halt but continues (no info about failed gap).

after ./sage startup it raises a runtime exception complaining about broken gap.



---

archive/issue_comments_017592.json:
```json
{
    "body": "This has now popped up in other places. For now the short term solution is to unset CC in spkg-install. More long term we need to fix the autoconf issue and/or report this bug upstream.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T19:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17592",
    "user": "mabshoff"
}
```

This has now popped up in other places. For now the short term solution is to unset CC in spkg-install. More long term we need to fix the autoconf issue and/or report this bug upstream.

Cheers,

Michael



---

archive/issue_comments_017593.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-15T19:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17593",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017594.json:
```json
{
    "body": "There is an updated spkg which should fix the issue at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/rc0/gap-4.4.10.p8.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-06-16T18:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17594",
    "user": "mabshoff"
}
```

There is an updated spkg which should fix the issue at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/rc0/gap-4.4.10.p8.spkg

Cheers,

Michael



---

archive/issue_comments_017595.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-16T18:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17595",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_017596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T18:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17596",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017597.json:
```json
{
    "body": "it doesn't work with 4.4.10 in sage 3.1.2/src\n\n\n```\nchecking for inttypes.h... yes\nchecking for stdint.h... yes\nchecking for unistd.h... yes\nchecking whether byte ordering is bigendian... no\nchecking for void *... yes\nchecking size of void *... 4\nchecking for nm... nm\nchecking whether symbols begin with an underscore... no\nchecking build system type... Invalid configuration `g++': machine `g++' not recognized\nconfigure: error: /bin/bash ../../src/../cnf/config.sub g++ failed\nmake[1]: *** [bin/i686-pc-linux-gnu-gcc/Makefile] Error 1\nmake[1]: Leaving directory `/opt/sage/sage-src/spkg/build/gap-4.4.10.p9/src'\nError building gap.\n```\n\n\n\n```\nCXX=ccache g++\nCC=ccache gcc\n```\n\n\nunsetting those variables and the configure script works.",
    "created_at": "2008-09-20T19:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17597",
    "user": "schilly"
}
```

it doesn't work with 4.4.10 in sage 3.1.2/src


```
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking whether byte ordering is bigendian... no
checking for void *... yes
checking size of void *... 4
checking for nm... nm
checking whether symbols begin with an underscore... no
checking build system type... Invalid configuration `g++': machine `g++' not recognized
configure: error: /bin/bash ../../src/../cnf/config.sub g++ failed
make[1]: *** [bin/i686-pc-linux-gnu-gcc/Makefile] Error 1
make[1]: Leaving directory `/opt/sage/sage-src/spkg/build/gap-4.4.10.p9/src'
Error building gap.
```



```
CXX=ccache g++
CC=ccache gcc
```


unsetting those variables and the configure script works.



---

archive/issue_comments_017598.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-09-20T19:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17598",
    "user": "schilly"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_017599.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-20T19:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17599",
    "user": "schilly"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_017600.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-20T20:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17600",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017601.json:
```json
{
    "body": "We do not reopen tickets that have been fixed. This is not a regression, but the problem is that you set CXX in addition to CC. Unsetting CXX in the spkg-install will fix your problem, but for that open another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T20:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17601",
    "user": "mabshoff"
}
```

We do not reopen tickets that have been fixed. This is not a regression, but the problem is that you set CXX in addition to CC. Unsetting CXX in the spkg-install will fix your problem, but for that open another ticket.

Cheers,

Michael



---

archive/issue_comments_017602.json:
```json
{
    "body": "Harald, \n\nI now see that your original bug report also raises the issue with CXX, but since we hit this bug on another machine with CC and not CXX set we ended up fixing only the CXX case. You should still open a new ticket and not open old tickets for issues like that since it will muddy HISTORY.txt, i.e. fixing #2575 twice will only confuse people looking for specific tickets. Also resolving those tickets is messy since the comments on this ticket are already long. So a clean new ticket will solve all those problems.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T20:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17602",
    "user": "mabshoff"
}
```

Harald, 

I now see that your original bug report also raises the issue with CXX, but since we hit this bug on another machine with CC and not CXX set we ended up fixing only the CXX case. You should still open a new ticket and not open old tickets for issues like that since it will muddy HISTORY.txt, i.e. fixing #2575 twice will only confuse people looking for specific tickets. Also resolving those tickets is messy since the comments on this ticket are already long. So a clean new ticket will solve all those problems.

Cheers,

Michael



---

archive/issue_comments_017603.json:
```json
{
    "body": "Perhaps striping 'ccache' out with 'sed' might have been a better solution.",
    "created_at": "2010-01-08T19:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17603",
    "user": "drkirkby"
}
```

Perhaps striping 'ccache' out with 'sed' might have been a better solution.



---

archive/issue_comments_017604.json:
```json
{
    "body": "this ticket is already closed & fixed since it works. Is there a new compile problem? (If yes -> new ticket)\n\nfor me ccache works!\n\nAnd stripping stuff out is probably not so cool, since it disables ccache ;)",
    "created_at": "2010-01-08T19:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17604",
    "user": "schilly"
}
```

this ticket is already closed & fixed since it works. Is there a new compile problem? (If yes -> new ticket)

for me ccache works!

And stripping stuff out is probably not so cool, since it disables ccache ;)



---

archive/issue_comments_017605.json:
```json
{
    "body": "Replying to [comment:11 schilly]:\n> And stripping stuff out is probably not so cool, since it disables ccache ;)\n\nUnsetting `CC` and `CXX` (as is currently done) also disables it. ;-)\n\nIf GAP still fails to configure / build when `CC` or `CXX` contain multiple words, we should probably unset `CC` and `CXX` **just in that case**, since currently even `CC=gcc-4.6.3` etc. are broken, and if the \"default\" gcc doesn't understand the flags intended for `$CC`, the build fails for no real reason.",
    "created_at": "2012-03-22T14:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17605",
    "user": "leif"
}
```

Replying to [comment:11 schilly]:
> And stripping stuff out is probably not so cool, since it disables ccache ;)

Unsetting `CC` and `CXX` (as is currently done) also disables it. ;-)

If GAP still fails to configure / build when `CC` or `CXX` contain multiple words, we should probably unset `CC` and `CXX` **just in that case**, since currently even `CC=gcc-4.6.3` etc. are broken, and if the "default" gcc doesn't understand the flags intended for `$CC`, the build fails for no real reason.



---

archive/issue_comments_017606.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> If GAP still fails to configure / build when `CC` or `CXX` contain multiple words, we should probably unset `CC` and `CXX` **just in that case** [...]\n\nFor the record: My GAP 4.4.12.p7 spkg for #7041 will just do that.",
    "created_at": "2012-03-22T17:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2575#issuecomment-17606",
    "user": "leif"
}
```

Replying to [comment:12 leif]:
> If GAP still fails to configure / build when `CC` or `CXX` contain multiple words, we should probably unset `CC` and `CXX` **just in that case** [...]

For the record: My GAP 4.4.12.p7 spkg for #7041 will just do that.
