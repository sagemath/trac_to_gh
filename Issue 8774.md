# Issue 8774: gap-4.4.12.p0 is full of *CRAP*

archive/issues_008774.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wdj\n\nWhile gap-4.4.12.p0 was unpacking, I noticed:\n\n```\ngap-4.4.12.p1/src/bin/\ngap-4.4.12.p1/src/bin/gap.bat\ngap-4.4.12.p1/src/bin/libW11.dll\ngap-4.4.12.p1/src/bin/gap.pif\ngap-4.4.12.p1/src/bin/gapicon.bmp\ngap-4.4.12.p1/src/bin/cygncurses-8.dll\ngap-4.4.12.p1/src/bin/regtool.exe\ngap-4.4.12.p1/src/bin/gaprxvt.bat\ngap-4.4.12.p1/src/bin/gap.dll\ngap-4.4.12.p1/src/bin/gapw95.exe\ngap-4.4.12.p1/src/bin/usemem.bat\ngap-4.4.12.p1/src/bin/gapp.bat\ngap-4.4.12.p1/src/bin/cygpanel-8.dll\ngap-4.4.12.p1/src/bin/gapw95p.exe\ngap-4.4.12.p1/src/bin/rxvt.exe\ngap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/\ngap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/gac\ngap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/gap.dll\ngap-4.4.12.p1/src/bin/i686-pc-cygwin-gcc/config.h\ngap-4.4.12.p1/src/bin/gapp.pif\ngap-4.4.12.p1/src/bin/cygwin1.dll\ngap-4.4.12.p1/src/description4r4p7\ngap-4.4.12.p1/src/grp/\n...\n```\n\n\nNO!!!  We absolutely should not be shipping Windows frickin' binaries with Sage.    Ticket #8076 introduced all these.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8774\n\n",
    "created_at": "2010-04-26T23:43:05Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "gap-4.4.12.p0 is full of *CRAP*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8774",
    "user": "was"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8774





---

archive/issue_comments_080315.json:
```json
{
    "body": "\n```\nwstein@boxen:/tmp$ wget ftp://ftp.gap-system.org/pub/gap/gap44/tar.bz2/gap4r4p12.tar.bz2\n--16:48:48--  ftp://ftp.gap-system.org/pub/gap/gap44/tar.bz2/gap4r4p12.tar.bz2\n           => `gap4r4p12.tar.bz2'\nResolving ftp.gap-system.org... 138.251.192.244\nConnecting to ftp.gap-system.org|138.251.192.244|:21... connected.\nLogging in as anonymous ... Logged in!\n==> SYST ... done.    ==> PWD ... done.\n==> TYPE I ... done.  ==> CWD /pub/gap/gap44/tar.bz2 ... done.\n==> PASV ... done.    ==> RETR gap4r4p12.tar.bz2 ... done.\nLength: 47,715,810 (46M) (unauthoritative)\n\n100%[=============================================================================>] 47,715,810   207.40K/s    ETA 00:00\n\n16:52:19 (224.11 KB/s) - `gap4r4p12.tar.bz2' saved [47715810]\n\nwstein@boxen:/tmp$ tar jxvf gap4r4p12.tar.bz2\ngap4r4/\ngap4r4/etc/\ngap4r4/etc/GPL\ngap4r4/etc/gap_indent.vim\ngap4r4/etc/xrmtcmd.c\ngap4r4/etc/README.vim-utils\ngap4r4/etc/emacs/\ngap4r4/etc/emacs/gap-mode.doc\ngap4r4/etc/emacs/gap-mode.el\ngap4r4/etc/emacs/comint.el\ngap4r4/etc/emacs/gap-process.el\ngap4r4/etc/debug.vim\ngap4r4/etc/debugvim.txt\ngap4r4/etc/gap.vim\ngap4r4/description4r4p7\ngap4r4/bin/\ngap4r4/bin/libW11.dll\ngap4r4/bin/gapp.pif\ngap4r4/bin/regtool.exe\ngap4r4/bin/gapp.bat\ngap4r4/bin/gap.dll\ngap4r4/bin/i686-pc-cygwin-gcc/\ngap4r4/bin/i686-pc-cygwin-gcc/gap.dll\ngap4r4/bin/i686-pc-cygwin-gcc/gac\ngap4r4/bin/i686-pc-cygwin-gcc/config.h\ngap4r4/bin/gapw95.exe\ngap4r4/bin/gapicon.bmp\ngap4r4/bin/gapw95p.exe\ngap4r4/bin/usemem.bat\ngap4r4/bin/cygpanel-8.dll\ngap4r4/bin/cygncurses-8.dll\ngap4r4/bin/rxvt.exe\ngap4r4/bin/gap.pif\ngap4r4/bin/cygwin1.dll\ngap4r4/bin/gap.bat\ngap4r4/bin/gaprxvt.bat\ngap4r4/grp/\n...\n```\n",
    "created_at": "2010-04-26T23:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80315",
    "user": "was"
}
```


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

archive/issue_comments_080316.json:
```json
{
    "body": "I'll make a new spkg later today.",
    "created_at": "2010-04-27T00:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80316",
    "user": "dimpase"
}
```

I'll make a new spkg later today.



---

archive/issue_comments_080317.json:
```json
{
    "body": "Changing assignee from tbd to dimpase.",
    "created_at": "2010-04-27T00:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80317",
    "user": "dimpase"
}
```

Changing assignee from tbd to dimpase.



---

archive/issue_comments_080318.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-27T01:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80318",
    "user": "dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080319.json:
```json
{
    "body": "Replying to [comment:3 dimpase]:\n> I'll make a new spkg later today.\n\nnew spkg is here: [http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg)\n\nAll I did is removing everything in src/bin/ and removing src/GAP\\ 4\\ PPC (apart from updating SPKG.txt etc)\n\nTested on Debian Linux x86_64 (just in case, as it shouldn't be anything problematic...)",
    "created_at": "2010-04-27T01:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80319",
    "user": "dimpase"
}
```

Replying to [comment:3 dimpase]:
> I'll make a new spkg later today.

new spkg is here: [http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg)

All I did is removing everything in src/bin/ and removing src/GAP\ 4\ PPC (apart from updating SPKG.txt etc)

Tested on Debian Linux x86_64 (just in case, as it shouldn't be anything problematic...)



---

archive/issue_comments_080320.json:
```json
{
    "body": "should be very easy to review!",
    "created_at": "2010-04-28T06:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80320",
    "user": "dimpase"
}
```

should be very easy to review!



---

archive/issue_comments_080321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T15:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80321",
    "user": "wjp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080322.json:
```json
{
    "body": "The package isn't perfect yet, but these changes are definitely good. Positive review.\n\nBy the way, I'm creating a p3 for ticket #8773 at the moment, starting from this p2. It will fix some strict aliasing problems with gcc 4.5.0, and will also fix the pre-applied patch to saveload.c.",
    "created_at": "2010-04-28T15:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80322",
    "user": "wjp"
}
```

The package isn't perfect yet, but these changes are definitely good. Positive review.

By the way, I'm creating a p3 for ticket #8773 at the moment, starting from this p2. It will fix some strict aliasing problems with gcc 4.5.0, and will also fix the pre-applied patch to saveload.c.



---

archive/issue_comments_080323.json:
```json
{
    "body": "(The p3 mentioned in my previous comment now needs review at #8773)",
    "created_at": "2010-04-28T16:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80323",
    "user": "wjp"
}
```

(The p3 mentioned in my previous comment now needs review at #8773)



---

archive/issue_comments_080324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T18:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8774#issuecomment-80324",
    "user": "was"
}
```

Resolution: fixed
