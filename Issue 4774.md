# Issue 4774: Upgrade matplotlib to 0.98.4

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-12 21:47:52

Assignee: tbd

CC:  ekirkman mhansen

Nice things include very nice arrow functionality, new legend functionality, and a fill_between keyword:

http://matplotlib.sourceforge.net/users/whats_new.html


---

Comment by mabshoff created at 2008-12-13 00:10:41

0.98.5 which is a bug fix release over 0.98.4 is out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 00:10:59

Changing component from algebra to packages.


---

Comment by mabshoff created at 2008-12-13 00:10:59

Changing assignee from tbd to mabshoff.


---

Comment by jason created at 2008-12-13 09:51:28


```
[03:47] <mabshoff> jason-: if you want to update matplotlib make sure to base it off the spkg in 3.2.2.a2.
[03:47] <jason-> okay
[03:47] <mabshoff> This one: http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/matplotlib-0.98.3.p4.spkg
```



---

Comment by mabshoff created at 2008-12-23 01:40:21

Latest upstream is 0.98.5.2.

Cheers,

Michael


---

Comment by jason created at 2009-01-24 06:06:16

A very preliminary package is up at http://sage.math.washington.edu/home/jason/matplotlib-svn6821.spkg , just in case someone wants to start using it (like Emily).

Lots of deprecation warnings and it probably also breaks stuff.  I'm fixing that now.  You probably should delete the directory $SAGE_ROOT/local/lib/python2.5/site-packages/matplotlib before installing to get rid of old cruft.


---

Comment by jason created at 2009-01-24 06:09:57

(ekirkman: I just posted a *very* preliminary spkg.)


---

Comment by jason created at 2009-01-26 16:08:36

This upgrade should fix #4465


---

Comment by jason created at 2009-01-26 22:47:53

apply in normal sage repository


---

Attachment

I've updated the spkg at http://sage.math.washington.edu/home/jason/matplotlib-svn6821.spkg

It should be ready to be reviewed now.


---

Comment by rlm created at 2009-02-05 22:54:31

Once I've deleted the old `matplotlibrc` files from everywhere, as proposed in

http://groups.google.com/group/sage-devel/browse_thread/thread/11704ed70dc0d6e3

I get failures related to `ft2font`:


```
sage: from matplotlib import ft2font

ImportError: dlopen(/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/ft2font.so, 2): Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/rlmill/sage-3.3.alpha5/local/lib//libpng12.0.dylib

```


Trying it again doesn't even give the error again: Sage just thrashes.


---

Comment by rlm created at 2009-02-05 23:57:36

Moved my `/opt/local` branch and rebuilt, everything worked this time around. Sorry!

Positive review for the spkg and patches. The thread above resolved the `matplotlibrc` issue. Full sail!


---

Comment by rlm created at 2009-02-06 00:26:11

OK, moving `/opt/local` out of the way wasn't enough:


```
sage: from matplotlib.pyplot import scatter

---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<SNIP>
/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/backends/backend_macosx.py in <module>()
     18 
     19 import matplotlib
---> 20 from matplotlib.backends import _macosx
     21 
     22 def show():

ImportError: dlopen(/Users/rlmill/sage-3.3.alpha5/local/lib/python2.5/site-packages/matplotlib/backends/_macosx.so, 2): Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/rlmill/sage-3.3.alpha5/local/lib//libpng12.0.dylib
```


So... wtf the linker is doing in `/System/Library/Frameworks` I can't say, but something is not right in Dodge.


---

Comment by mabshoff created at 2009-02-06 01:09:58

This spkg is twice as large as the previous:

```
-rw-r--r--`@` 1 michaelabshoff  staff  4845513 Feb  2 17:28 matplotlib-0.98.3.p5.spkg
-rw-r--r--  1 michaelabshoff  staff  8833439 Feb  5 16:52 matplotlib-svn6821.spkg
```

There was some discussion on the matplotlib list about the new tarballs containing more documentation than the old ones, so we should look into getting rid of some of the documentation.

This spkg is important to get graph related plotting improvements into Sage, so let's try for 3.3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 01:09:58

Changing priority from major to critical.


---

Comment by mabshoff created at 2009-02-06 01:21:23

This needs work: 

 * setupext.py.diff is not a unified diff, i.e. use -urN when diffing
 * some of the other diffs were created by diffing files in patches with files in src. The standard way in Sage to do this is to copy over foo from under source to foo.orig and then diff the changed foo against foo.orig in the same directory. Here also unified diff is required
 * the size issue need to be investigated, i.e. 4MB extra compressed for the spkg is a substantial increase in size
 * the name of the spkg should reflect the release branch it came from, i.e matplotlib-0.98.5.2-svnXXX

Aside from that:
 * We need to potentially make matplotlib not look for certain things on OSX like ghostview since that tends to pull in crap from Fink and/or MacPorts.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 01:39:27

I debugged this some more with rlm and the problem is the following:

```
OPTIONAL USETEX DEPENDENCIES
               dvipng: /System/Library/Frameworks/ApplicationServices.frame
                       work/Versions/A/Frameworks/ImageIO.framework/Version
                       s/A/ImageIO
          ghostscript: 8.62
                latex: 3.1415926
```

So killing dvipng support on OSX for now should solve the problem. His dvipng comes out of usr/texbin/dvipng.

And while looking at this problem I also come up with a workable fix for the libpng issue once and for all - see 

   http://groups.google.com/group/sage-devel/t/5c655c1e1a2dc0b8

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 02:14:26

Ok, the culprit is this extension: 

```
def build_macosx(ext_modules, packages):
    global BUILT_MACOSX
    if BUILT_MACOSX: return # only build it if you you haven't already
    module = Extension('matplotlib.backends._macosx',
                       ['src/_macosx.m'],
                       extra_link_args = ['-framework','Cocoa'],
                      )
    add_numpy_flags(module)
    ext_modules.append(module)
    BUILT_MACOSX = True
```

Since it links against a framework the only fix might be to fix the libpng.dylib issue on OSX once and for all.

Cheers,

Michael


---

Comment by jason created at 2009-02-13 05:18:19

The next version, 0.98.3, is going to be released Real Soon Now (there's already an RC out).  So I'm biding my time waiting for that before fixing the issues with the spkg.


---

Comment by jason created at 2009-02-13 05:18:40

uh, that release is 0.98.5.3.


---

Comment by jason created at 2009-02-13 16:16:48

Here are the directories that changed by more than 100Kb.  A negative number means the directory decreased by that many kb.  A positive number means it increased by that many kb:


```
('src/lib', -4280)
('src/lib/mpl_examples', -3108)
('src/lib/enthought', -1936)
('src/lib/enthought/traits', -1892)
('src/lib/mpl_examples/data', -1840)
('src/lib/enthought/traits/ui', -1012)
('src/lib/mpl_examples/pylab_examples', -728)
('src/lib/enthought/traits/ui/tk', -316)
('src/lib/enthought/traits/tests', -240)
('src/lib/mpl_examples/user_interfaces', -140)
('src/lib/enthought/traits/ui/tests', -124)
('src/lib/mpl_examples/api', -112)
```



```
('src/doc/api', 104)
('src/examples/tests/pngsuite', 108)
('src/unit', 116)
('src/examples/tests', 120)
('src/examples/user_interfaces', 144)
('src/examples/api', 144)
('src/lib/matplotlib/mpl-data', 480)
('src/lib/matplotlib/mpl-data/example', 528)
('src/lib/matplotlib', 764)
('src/examples/pylab_examples', 840)
('src/doc/_static', 1216)
('src/src', 1340)
('src/examples/data', 2152)
('src/doc/pyplots', 2424)
('src/examples', 3696)
('src/doc', 3828)
('src/', 4688)
```



---

Comment by jason created at 2009-02-13 16:18:31

so from the above, it looks like it was indeed the docs that increased by about 4mb (uncompressed)
.


---

Comment by jason created at 2009-02-13 17:30:06

An updated spkg which addresses all of mabshoff's comments is here: http://sage.math.washington.edu/home/jason/matplotlib-0.98.5.3rc0-svn6910.spkg

I also updated the spkg to the most recent svn, which is after the release candidate for 0.98.5.3.


---

Comment by jason created at 2009-02-13 17:30:22

The spkg installs cleanly for me (ubuntu 8.10).


---

Attachment


---

Comment by jason created at 2009-02-13 17:37:23

I updated the bin repository patch to delete a reference to matplotlib that I missed before (in sage-env).


---

Comment by mabshoff created at 2009-02-14 10:44:20

This patch is on top of Jason's latest spkg and resolved libpng12 linking issues on OSX


---

Attachment

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/matplotlib-0.98.5.3rc0-svn6910.p0.spkg

All spkg changes by Jason look good, indeed they are *very* clean. I will review the patches to the various repos and hopefully Jason will give my changes a review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 10:52:07

Note that even with libpng.dylib and libpng12.dylib on OSX we are definitely linking against libpng12.dylib.

Cheers,

Michael


---

Comment by jason created at 2009-02-14 10:53:42

Changing status from new to assigned.


---

Comment by jason created at 2009-02-14 10:53:42

Changing assignee from mabshoff to jason.


---

Comment by mabshoff created at 2009-02-14 11:13:37

Positive review on Jason's patches to the Sage library as well as the bin repo.

Cheers,

Michael


---

Comment by jason created at 2009-02-14 11:16:24

mabshoff's new spkg builds fine for me.


---

Comment by mabshoff created at 2009-02-14 11:26:30

Ok, there are some doctesting issues left with -long. Jason is looking into this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 11:46:41

On sage.math we are having problems with the tkagg backend. It used to happen only occasionally, but now it happens every time I doctest plot.py:

```
File "/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/plot/plot.py", line 172:
    sage: grid(True)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[60]>", line 1, in <module>
        grid(True)###line 172:
    sage: grid(True)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 2453, in grid
        ret =  gca().grid(*args, **kwargs)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 572, in gca
        ax =  gcf().gca(**kwargs)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 274, in gcf
        return figure()
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 252, in figure
        **kwargs)
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/site-packages/matplotlib/backends/backend_tkagg.py", line 90, in new_figure_manager
        window = Tk.Tk()
      File "/scratch/mabshoff/sage-3.3.rc1/local/lib/python2.5/lib-tk/Tkinter.py", line 1636, in __init__
        self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
    TclError: no display name and no $DISPLAY environment variable
```


We already disable tkagg on Itanium/Linux, so let's get rid of it globally.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 12:04:19

I have disabled tkagg globally and the problem above goes away. The spkg by the same names as the last one above is at


  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/matplotlib-0.98.5.3rc0-svn6910.p0.spkg

Cheers,

Michael


---

Comment by jason created at 2009-02-14 12:39:38

okay, new spkg up here: http://sage.math.washington.edu/home/jason/matplotlib-0.98.5.3rc0-svn6910.p1.spkg

This adds a fix (i.e., kludge) that lets matplotlib draw very tiny errors, which were giving us problems before.  I also cleaned up a few things from mabshoff's changes :).


---

Comment by mabshoff created at 2009-02-14 12:52:53

Jason's latest patch spkg fixes the problem, so an overall positive review via crossover between Jason's and my work.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 12:55:03

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 12:55:03

Merged

 * matplotlib-0.98.5.3rc0-svn6910.p1.spkg
 * trac_4774_arrow.patch (2.6 kB) 
 * trac_4774_BIN.patch 

in Sage 3.3.rc1.

Cheers,

Michael
