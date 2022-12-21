# Issue 7022: os x -- 10.6 -- generated the matplotlib font cache crashes sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-27 01:34:49

Assignee: was

This is a huge problem and total blocker:

```
flat:.matplotlib wstein$ mv fontList.cache fontList.cache.XXX
flat:.matplotlib wstein$ cd
flat:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: parallel
sage: import pylab
/Users/wstein/sage/build/64bit/sage/local/bin/sage-sage: line 199: 58213 Abort trap              sage-ipython "$`@`" -i
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
flat:.matplotlib wstein$ mv fontList.cache.XXX fontList.cache
flat:.matplotlib wstein$ cd ..
flat:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: parallel
sage: import pylab
sage: 
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
Ideas for solution: 

  (1) track down exactly where the problem happens in the matplotlib/freetype(?) code and fix it.

  (2) Just ship the font cache with Sage until this gets resolved upstream.


---

Comment by was created at 2009-09-27 03:43:50

The spkg is here:

    http://wstein.org/home/wstein/patches/matplotlib-0.99.1.p1.spkg

This supersedes what is at #6994.

The attached package *only* patches Matplotlib on OS X 10.6 by changing one line to use


---

Comment by was created at 2009-09-27 04:11:32

Doctesting reveals that just using FONTCONFIG is not enough, e.g., any saving to pdf still breaks. 

Here is the problem narrowed down more:

```
sage: import ft2font; ft2font.FT2Font('/Library/Fonts/NISC18030.ttf')
/Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/local/bin/sage-sage: line 199: 65960 Abort trap              sage-ipython "$`@`" -i
```


ft2font.so is a C extension in matplotlib.


---

Comment by was created at 2009-09-27 04:17:29

above it should be

```
sage: import matplotlib.ft2font; ft2font.FT2Font('/Library/Fonts/NISC18030.ttf')
/Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/local/bin/sage-sage: line 199: 65960 Abort trap    
```



---

Comment by was created at 2009-09-27 04:18:00

How about

```
import matplotlib.ft2font; matplotlib.ft2font.FT2Font('/Library/Fonts/NISC18030.ttf')
```



---

Comment by was created at 2009-09-27 06:33:51

I found yet another issue (X11 must be in the PATH), but this spkg fixes that issue too:

  http://wstein.org/home/wstein/patches/matplotlib-0.99.1.p1.spkg


---

Comment by was created at 2009-09-28 03:52:08

OK, even this doesn't fix the problem on all machines.  E.g., on bsd.math.washington.edu it does not fix the problem.


---

Comment by was created at 2009-09-28 04:21:00

Comment -- upgrading freetype doesn't fix the problems at all.  Also, upgrading freetype is itself broken, and the only workaround that I found that worked was to alias "rm" to be "rm -f" -- then freetype built and installed fine.


---

Comment by was created at 2009-09-30 04:22:03

See http://groups.google.com/group/sage-devel/browse_thread/thread/2c538915abc99946


---

Comment by was created at 2009-09-30 04:49:55

This spkg fixes the problems on all my test systems:

   http://sage.math.washington.edu/home/wstein/patches/matplotlib-0.99.1.p2.spkg

All it does is take the plane vanilla matplotlib-0.99.1.spkg spkg and add a little script that simply rebuilds f2font.so again using *exactly* the same command lines used by distutils to build that extension.  That's it.  For some reason -- probably involving environment variables (?) -- this fixes the problem.  I consider this a temporary 1-sage release solution until the matplotlib developers (or me) come up with a real fix.


---

Comment by was created at 2009-09-30 04:50:51

By the way, here is a simple test that things are working:

```
sage: import pylab
sage: plot(sin).save('a.pdf')
```



---

Comment by mhansen created at 2009-09-30 05:31:19

Looks good to me.  Everything worked for me on bsd.


---

Comment by mvngu created at 2009-09-30 12:05:42

Merged `matplotlib-0.99.1.p2.spkg` in the standard packages repository.


---

Comment by mvngu created at 2009-09-30 12:05:42

Resolution: fixed


---

Comment by jhpalmieri created at 2009-12-21 17:54:31

I'm still getting a crash with lines like these:

```
sage: import pylab
sage: plot(sin).save('a.pdf')
```

I made a related comment at #7095 because I didn't know about this ticket.  Also, as opposed to this ticket, #7095 is still open, so further discussion should continue there (or on a new ticket?).


---

Comment by jhpalmieri created at 2010-01-06 04:27:49

The matplotlib problem may be in its spkg file: it says

```
if [ $UNAME = "Darwin" -a `uname -r` = "10.0.0" ]; then
    echo "Running a horrible hack to force ft2font.so to build in a way that doen't crash."
    echo "This is of course temporary.  See http://trac.sagemath.org/sage_trac/ticket/7022"
    ../patches/osx10.6hack
fi
```

But with my computer, "uname -r" returns "10.2.0", not "10.0.0".  How do you modify a shell script like this to make it work for a range of version numbers?  (We don't just want "10.0.0" or "10.2.0", I'm guessing.)
