# Issue 551: consider changing python to UCS4

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-01 16:40:14

Assignee: was


```
William,

I noticed that the Python that comes with SAGE-2.8.3
still has UCS2.

Are you still considering changing to UCS4?

Jaap



On 8/14/07, Jaap Spies <j.spies`@`hccnet.nl> wrote:
> See also
>
> > http://mail.python.org/pipermail/distutils-sig/2006-July/006579.html
>
> for a discussion of Python and UCS2 vs. UCS4
>
> Ubuntu and Fedora distribute Python compiled with UCS4.
> Maybe the Python version of SAGE should comply with the distribution,
> so for example libboost_python can be used.

I would definitely consider making this change, at least as long as nobody
sees any major problems with it in the next few days.   One problem is
that doing "sage -upgrade" will require rebuilding every Python-related thing
i SAGE, which will be a bit painful.

Anyway, comments?
gmane.comp.mathematics.sage.devel
 -- William
```



---

Comment by was created at 2007-09-23 18:59:24

Making this change is very hard.  It means that Sage has to be almost completely recompiled from scratch -- at least, everything that involves Python extensions must be rebuilt.  It would thus be difficult for automatic upgrades. 

A test for which mode a Python is compiled with is the following:


```
if len(u'\U00010800') == 1: 
   print "UCS4"
else:
   print "USC2"
```


Probably the best solution in the long run is to test for a system-wide Python, and then figure out what its UCS number is, then make Sage's agree with it.  That would be far better than just always using 4 and leaving the distros that use 2 in the dust.


---

Comment by mabshoff created at 2008-01-03 14:54:13

Even though it requires a rebuild of most python modules the 2.10 release would be a good point in time to do it.

#1663 certainly seems like a good reason to do so.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 12:56:18

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-01-11 12:56:18

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-11 12:56:18

As long as we compile our own copy of python we can force ucs4, especially as long as we ship our own binaries with out own python. Once we get into distributions we need to consider what William commented about above using the local distributions default. 

An spkg which forces ucs4 is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha2/python-2.5.1.p11.spkg

Caution: you need to rebuild all python extensions to test this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 17:06:16

When building python with ucs4 upon completion of the install all python site-packages are recompiled, i.e. numpy, scipy, sympy and so on. But upon startup of Sage the following thing happens:

```
<type 'exceptions.ImportError'>: /tmp/Work-mabshoff/release-cycle/sage-2.10.alpha2/local/lib/python2.5/site-packages/sage/misc/misc_c.so: undefined symbol: PyUnicodeUCS2_DecodeUTF8
```

Rebuilding Sage lib fixes the issue, but then we need to rebuild:

 * zodb3-3.7.0.spkg
 * numpy-20080104-1.0.4.p1

in order to make Sage start, but I expect that we need to rebuild a couple more spkgs to make the doctests actually pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 17:55:23

Other spkgs that need to be rebuild for `testall` to pass:

 * matplotlib-0.91.1.p1
 * r-2.6.1.p7

So, overall, it isn't too bad.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-11 18:37:55

Make sure to rebuild matplotlib *after* numpy since matplotlib does depend on numpy.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-12 18:50:04

Resolution: fixed


---

Comment by mabshoff created at 2008-01-12 18:50:04

Merged in Sage 2.10.alpha2.

After feeback from various people the ucs4 switchover doesn't cause any problems as far as I can tell. So I am closing this.

Cheers,

Michael
