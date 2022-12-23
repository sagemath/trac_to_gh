# Issue 5301: In sage-3.3.rc2, doing sage -t -long "devel/sage/sage/plot/plot.py" causing a matplotlib GUI window to popup

Issue created by migration from https://trac.sagemath.org/ticket/5301

Original creator: was

Original creation time: 2009-02-18 06:57:29

Assignee: was

CC:  ghtdak jason

This happens on OS X with a local GUI. Moreover, I get this doctest failure, which is perhaps related:

```
	 [2.5 s]
sage -t -long "devel/sage/sage/plot/plot.py"                
**********************************************************************
File "/Users/wstein/build/build/sage-3.3.rc2/devel/sage/sage/plot/plot.py", line 173:
    sage: savefig('sage.png')
Exception raised:
    Traceback (most recent call last):
      File "/Users/wstein/build/build/sage-3.3.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wstein/build/build/sage-3.3.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wstein/build/build/sage-3.3.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[61]>", line 1, in <module>
        savefig('sage.png')###line 173:
    sage: savefig('sage.png')
      File "/Users/wstein/build/build/sage-3.3.rc2/local/lib/python2.5/site-packages/matplotlib/pyplot.py", line 346, in savefig
        return fig.savefig(*args, **kwargs)
      File "/Users/wstein/build/build/sage-3.3.rc2/local/lib/python2.5/site-packages/matplotlib/figure.py", line 1001, in savefig
        self.canvas.print_figure(*args, **kwargs)
      File "/Users/wstein/build/build/sage-3.3.rc2/local/lib/python2.5/site-packages/matplotlib/backends/backend_macosx.py", line 268, in print_figure
        self.write_bitmap(filename, width, height)
    ValueError: Unknown file type
**********************************************************************
1 items had failures:
```



---

Comment by mabshoff created at 2009-02-20 10:51:54

This problem is caused by this code snipped:

```
    sage: from pylab import *
    sage: t = arange(0.0, 2.0, 0.01)
    sage: s = sin(2*pi*t)
    sage: P = plot(t, s, linewidth=1.0)
    sage: xl = xlabel('time (s)')
    sage: yl = ylabel('voltage (mV)')
    sage: t = title('About as simple as it gets, folks')
    sage: grid(True)
    sage: savefig('sage.png')
```


Glenn has reported the same issue on a Linux box. This might be a genuine bug in MPL. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 11:02:30

Oops, forgot to add Jason to the CC :)

Cheers,

Michael


---

Comment by was created at 2009-02-20 14:54:20

I think there are two separate problems:

(1) 

```
    sage: from pylab import *
    sage: t = arange(0.0, 2.0, 0.01)
    sage: s = sin(2*pi*t)
    sage: P = plot(t, s, linewidth=1.0)
[a popup appears]
```


(2) then do the following one line after the above:

```
sage: savefig('sage.png')
BOOM
ValueError: Unknown file type
```


Other remarks:

   * This bug occurs exactly the same in the notebook, so is a major show stopper.
 
   * There is probably a way to get around it, since of course our own matplotlib-based plotting works fine without popping up GUI's and writing to files. 


I'm guessing the the best fix is to patch setup.py to avoid building any GUI backends for now, until we can figure out how to patch pylab itself to not use the GUI backends.  I mean, given that one has built any GUI backend, the above behavior (sans the savefig issue) definitely seems like appropriate behavior for matplotlib.


---

Comment by was created at 2009-02-20 15:28:43

Further remarks:

 * I built the new matplotlib into sage-3.3.alpha5, which has the previous libpng spkg and both the popup and rendering of png problems vanished.   So the real bug is probably in libpng/matplotlib interaction.

 * I build without the OS X gui backend and the problem vanishes for OS X.

A quick fix for sage-3.3.rc3 would be to disable the OS X GUI.  This can be done with a one line change to setup.py (just put an if False in the part of setup.py that involves that macos X gui), or something involving setup.cfg or something more complicated to setup.py.


---

Comment by was created at 2009-02-20 15:33:50

I will post an spkg that fixes this in a second.  Take it or leave it.  At least it will make it possible to release sage-3.3  It only disables GUI's by default on OS X, and creates an environment variable to control this in general.  If somebody wants to somehow redo this use setup.cfg, be my guest.


---

Comment by was created at 2009-02-20 15:34:38

The spkg is here:

http://sage.math.washington.edu/home/was/patches/matplotlib-0.98.5.3rc0-svn6910.p2.spkg


---

Comment by mabshoff created at 2009-02-20 16:08:34

Positive review. I checked in one diff as unified diff, but other than that no changes.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 16:09:02

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 16:09:02

Merged the spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/matplotlib-0.98.5.3rc0-svn6910.p2.spkg

in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 17:28:32

For the record: I did turn off GUI support per default since it causes trouble on X less boxen, i.e. sage.math. This might very well be a bug in the new MPL, so someone should check with them why the inport of tcl or pygtk is not caught and dealt with appropriately. I talked all this over with William and he agreed with me that this is the right fix for 3.3, but that the issue should be revisited. The spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/matplotlib-0.98.5.3rc0-svn6910.p3.spkg

was merged in 3.3.rc3 and replaced the one mentioned above.

Cheers,

Michael


---

Comment by jason created at 2009-02-27 15:39:38

Instructions for reenabling the gui backends are:

set the environment variable SAGE_MATPLOTLIB_GUI to anything besides 'no'

Reinstall the spkg: ` sage -f matplotlib-0.98.5.3rc0-svn6910.p3`
