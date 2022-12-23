# Issue 4680: [with diff, needs new spkg] matplotlib configuration finds system-wide files on OSX

Issue created by migration from https://trac.sagemath.org/ticket/4680

Original creator: craigcitro

Original creation time: 2008-12-02 23:59:37

Assignee: mabshoff

The matplotlib install on OSX can find the system-wide files, leading to problems like this:


```
sage: from matplotlib import _png
ImportError: dlopen(/sage/local/lib/python/site-packages/matplotlib/_png.so, 2): Library not loaded: /usr/X11/lib/libpng12.0.dylib
      Referenced from: /sage/local/lib/python/site-packages/matplotlib/_png.so
      Reason: Incompatible library version: _png.so requires version 27.0.0 or later, but libpng12.0.dylib provides version 23.0.0
```


The matplotlib config tries to look all over for libpng, but we only want it to find the sage specific one. The attached diff of `setupext.py` in `matplotlib-0.98.3.p3/patches/` tells it not to.


---

Attachment

looks good to me...


---

Comment by mabshoff created at 2008-12-11 16:31:29

I am building an updated spkg with the fix now. Sorry that this slipped off my radar.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-12 16:32:46

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/matplotlib-0.98.3.p4.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-12 16:33:01

Merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-12 16:33:01

Resolution: fixed
