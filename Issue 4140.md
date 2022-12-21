# Issue 4140: "Naughty" libraries that get called in by sage

Issue created by migration from Trac.

Original creator: dphilp

Original creation time: 2008-09-17 23:13:47

Assignee: mabshoff

Keywords: naughty libraries

When fink is in the path, sage-check-libraries.py reveals that the following libraries get called in to vanilla sage:

```
sage-3.1.2/local/lib/python2.5/lib-dynload/_bsddb.so links to non-whitelisted file /sw/lib/libdb-4.4.dylib
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtcl8.4.dylib
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtk8.4.dylib
```


Also, clisp didn't biuld, with 

```
dyld: Symbol not found: __cg_jpeg_resync_to_restart
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /sw/lib/libJPEG.dylib
```


and if it had built, maybe more bad linkages would have shown up.  

At the moment, this ticket is quite open ended, and probably needs to be split into little specific tickets.  Would appreciate any vision on exactly what would go in those tickets.

If have attached the whitelist built on my system.  (I edited it to remove libraries in /sw.)  It is likely to be incomplete because sage didn't finish building.  It is also likely to have some improper files (/usr/local stuff) that got installed e.g. by GIMP.


---

Attachment

Hi David,

it should be one issue per ticket, so I edited this ticket to be limited to the clisp issue. 

The problem with R should be another ticket and fixed:

```
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtcl8.4.dylib
sage-3.1.2/local/lib/R/library/tcltk/libs/tcltk.so links to non-whitelisted file /sw/lib/libtk8.4.dylib
```

The db extension with Python

```
sage-3.1.2/local/lib/python2.5/lib-dynload/_bsddb.so links to non-whitelisted file /sw/lib/libdb-4.4.dylib
```

is something we will likely not fix since it should not cause any trouble.

You alsp don't need to add your email address to the CC field since that should happen automatically for any ticket you are involved with. If not check "settings" in the upper right corner. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-18 00:25:34

Changing status from new to assigned.


---

Comment by dphilp created at 2008-09-18 00:37:45

Michael:

Got the CC thing, thanks.

I didn't think we cared about clisp?  Anyway, it's up to you.

I will add another ticket for R.

D


---

Comment by dphilp created at 2008-09-18 04:24:56

Similar problem with MacPorts:

```
dyld: Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/dphilp/s312/sage-3.1.2/local/lib//libPng.dylib
```

oddly enough it says nothing about /opt.  The preceding line is:

```
dvipdf clisp.dvi clisp.pdf
```

and so I assume it's Ports' dvipdf that is calling the ImageIO framework.


---

Comment by mabshoff created at 2009-02-16 04:31:23

Resolution: fixed


---

Comment by mabshoff created at 2009-02-16 04:31:23

This has been fixed via #5217.

Cheers,

Michael
