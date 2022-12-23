# Issue 8774: gap-4.4.12.p0 is full of *CRAP*

Issue created by migration from https://trac.sagemath.org/ticket/8774

Original creator: was

Original creation time: 2010-04-26 23:43:05

Assignee: tbd

CC:  wdj

While gap-4.4.12.p0 was unpacking, I noticed:

```
gap-4.4.12.p1/src/bin/
gap-4.4.12.p1/src/bin/gap.bat
gap-4.4.12.p1/src/bin/libW11.dll
gap-4.4.12.p1/src/bin/gap.pif
gap-4.4.12.p1/src/bin/gapicon.bmp
gap-4.4.12.p1/src/bin/cygncurses-8.dll
gap-4.4.12.p1/src/bin/regtool.exe
gap-4.4.12.p1/src/bin/gaprxvt.bat
gap-4.4.12.p1/src/bin/gap.dll
gap-4.4.12.p1/src/bin/gapw95.exe
gap-4.4.12.p1/src/bin/usemem.bat
gap-4.4.12.p1/src/bin/gapp.bat
gap-4.4.12.p1/src/bin/cygpanel-8.dll
gap-4.4.12.p1/src/bin/gapw95p.exe
gap-4.4.12.p1/src/bin/rxvt.exe
gap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/
gap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/gac
gap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/gap.dll
gap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/config.h
gap-4.4.12.p1/src/bin/gapp.pif
gap-4.4.12.p1/src/bin/cygwin1.dll
gap-4.4.12.p1/src/description4r4p7
gap-4.4.12.p1/src/grp/
...
```


NO!!!  We absolutely should not be shipping Windows frickin' binaries with Sage.    Ticket #8076 introduced all these.


---

Comment by was created at 2010-04-26 23:52:56


```
wstein@boxen:/tmp$ wget ftp://ftp.gap-system.org/pub/gap/gap44/tar.bz2/gap4r4p12.tar.bz2
--16:48:48--  ftp://ftp.gap-system.org/pub/gap/gap44/tar.bz2/gap4r4p12.tar.bz2
           => `gap4r4p12.tar.bz2'
Resolving ftp.gap-system.org... 138.251.192.244
Connecting to ftp.gap-system.org|138.251.192.244|:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD /pub/gap/gap44/tar.bz2 ... done.
==> PASV ... done.    ==> RETR gap4r4p12.tar.bz2 ... done.
Length: 47,715,810 (46M) (unauthoritative)

100%[=============================================================================>] 47,715,810   207.40K/s    ETA 00:00

16:52:19 (224.11 KB/s) - `gap4r4p12.tar.bz2' saved [47715810]

wstein@boxen:/tmp$ tar jxvf gap4r4p12.tar.bz2
gap4r4/
gap4r4/etc/
gap4r4/etc/GPL
gap4r4/etc/gap_indent.vim
gap4r4/etc/xrmtcmd.c
gap4r4/etc/README.vim-utils
gap4r4/etc/emacs/
gap4r4/etc/emacs/gap-mode.doc
gap4r4/etc/emacs/gap-mode.el
gap4r4/etc/emacs/comint.el
gap4r4/etc/emacs/gap-process.el
gap4r4/etc/debug.vim
gap4r4/etc/debugvim.txt
gap4r4/etc/gap.vim
gap4r4/description4r4p7
gap4r4/bin/
gap4r4/bin/libW11.dll
gap4r4/bin/gapp.pif
gap4r4/bin/regtool.exe
gap4r4/bin/gapp.bat
gap4r4/bin/gap.dll
gap4r4/bin/i686-pc-cygwin-gcc/
gap4r4/bin/i686-pc-cygwin-gcc/gap.dll
gap4r4/bin/i686-pc-cygwin-gcc/gac
gap4r4/bin/i686-pc-cygwin-gcc/config.h
gap4r4/bin/gapw95.exe
gap4r4/bin/gapicon.bmp
gap4r4/bin/gapw95p.exe
gap4r4/bin/usemem.bat
gap4r4/bin/cygpanel-8.dll
gap4r4/bin/cygncurses-8.dll
gap4r4/bin/rxvt.exe
gap4r4/bin/gap.pif
gap4r4/bin/cygwin1.dll
gap4r4/bin/gap.bat
gap4r4/bin/gaprxvt.bat
gap4r4/grp/
...
```



---

Comment by dimpase created at 2010-04-27 00:07:41

I'll make a new spkg later today.


---

Comment by dimpase created at 2010-04-27 00:07:41

Changing assignee from tbd to dimpase.


---

Comment by dimpase created at 2010-04-27 01:04:27

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-04-27 01:04:27

Replying to [comment:3 dimpase]:
> I'll make a new spkg later today.

new spkg is here: [http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg)

All I did is removing everything in src/bin/ and removing src/GAP\ 4\ PPC (apart from updating SPKG.txt etc)

Tested on Debian Linux x86_64 (just in case, as it shouldn't be anything problematic...)


---

Comment by dimpase created at 2010-04-28 06:09:51

should be very easy to review!


---

Comment by wjp created at 2010-04-28 15:23:50

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2010-04-28 15:23:50

The package isn't perfect yet, but these changes are definitely good. Positive review.

By the way, I'm creating a p3 for ticket #8773 at the moment, starting from this p2. It will fix some strict aliasing problems with gcc 4.5.0, and will also fix the pre-applied patch to saveload.c.


---

Comment by wjp created at 2010-04-28 16:01:45

(The p3 mentioned in my previous comment now needs review at #8773)


---

Comment by was created at 2010-04-28 18:58:01

Resolution: fixed
