# Issue 5301: In sage-3.3.rc2, doing sage -t -long "devel/sage/sage/plot/plot.py" causing a matplotlib GUI window to popup

archive/issues_005301.json:
```json
{
    "body": "Assignee: was\n\nCC:  ghtdak jason\n\nThis happens on OS X with a local GUI. Moreover, I get this doctest failure, which is perhaps related:\n\n```\n\t [2.5 s]\nsage -t -long \"devel/sage/sage/plot/plot.py\"                \n**********************************************************************\nFile \"/Users/wstein/build/build/sage-3.3.rc2/devel/sage/sage/plot/plot.py\", line 173:\n    sage: savefig('sage.png')\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/wstein/build/build/sage-3.3.rc2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/wstein/build/build/sage-3.3.rc2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/wstein/build/build/sage-3.3.rc2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[61]>\", line 1, in <module>\n        savefig('sage.png')###line 173:\n    sage: savefig('sage.png')\n      File \"/Users/wstein/build/build/sage-3.3.rc2/local/lib/python2.5/site-packages/matplotlib/pyplot.py\", line 346, in savefig\n        return fig.savefig(*args, **kwargs)\n      File \"/Users/wstein/build/build/sage-3.3.rc2/local/lib/python2.5/site-packages/matplotlib/figure.py\", line 1001, in savefig\n        self.canvas.print_figure(*args, **kwargs)\n      File \"/Users/wstein/build/build/sage-3.3.rc2/local/lib/python2.5/site-packages/matplotlib/backends/backend_macosx.py\", line 268, in print_figure\n        self.write_bitmap(filename, width, height)\n    ValueError: Unknown file type\n**********************************************************************\n1 items had failures:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5301\n\n",
    "created_at": "2009-02-18T06:57:29Z",
    "labels": [
        "graphics",
        "blocker",
        "bug"
    ],
    "title": "In sage-3.3.rc2, doing sage -t -long \"devel/sage/sage/plot/plot.py\" causing a matplotlib GUI window to popup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5301",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/5301





---

archive/issue_comments_040777.json:
```json
{
    "body": "This problem is caused by this code snipped:\n\n```\n    sage: from pylab import *\n    sage: t = arange(0.0, 2.0, 0.01)\n    sage: s = sin(2*pi*t)\n    sage: P = plot(t, s, linewidth=1.0)\n    sage: xl = xlabel('time (s)')\n    sage: yl = ylabel('voltage (mV)')\n    sage: t = title('About as simple as it gets, folks')\n    sage: grid(True)\n    sage: savefig('sage.png')\n```\n\n\nGlenn has reported the same issue on a Linux box. This might be a genuine bug in MPL. \n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T10:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40777",
    "user": "mabshoff"
}
```

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

archive/issue_comments_040778.json:
```json
{
    "body": "Oops, forgot to add Jason to the CC :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T11:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40778",
    "user": "mabshoff"
}
```

Oops, forgot to add Jason to the CC :)

Cheers,

Michael



---

archive/issue_comments_040779.json:
```json
{
    "body": "I think there are two separate problems:\n\n(1) \n\n```\n    sage: from pylab import *\n    sage: t = arange(0.0, 2.0, 0.01)\n    sage: s = sin(2*pi*t)\n    sage: P = plot(t, s, linewidth=1.0)\n[a popup appears]\n```\n\n\n(2) then do the following one line after the above:\n\n```\nsage: savefig('sage.png')\nBOOM\nValueError: Unknown file type\n```\n\n\nOther remarks:\n\n* This bug occurs exactly the same in the notebook, so is a major show stopper.\n \n* There is probably a way to get around it, since of course our own matplotlib-based plotting works fine without popping up GUI's and writing to files. \n\n\nI'm guessing the the best fix is to patch setup.py to avoid building any GUI backends for now, until we can figure out how to patch pylab itself to not use the GUI backends.  I mean, given that one has built any GUI backend, the above behavior (sans the savefig issue) definitely seems like appropriate behavior for matplotlib.",
    "created_at": "2009-02-20T14:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40779",
    "user": "was"
}
```

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

archive/issue_comments_040780.json:
```json
{
    "body": "Further remarks:\n\n* I built the new matplotlib into sage-3.3.alpha5, which has the previous libpng spkg and both the popup and rendering of png problems vanished.   So the real bug is probably in libpng/matplotlib interaction.\n\n* I build without the OS X gui backend and the problem vanishes for OS X.\n\nA quick fix for sage-3.3.rc3 would be to disable the OS X GUI.  This can be done with a one line change to setup.py (just put an if False in the part of setup.py that involves that macos X gui), or something involving setup.cfg or something more complicated to setup.py.",
    "created_at": "2009-02-20T15:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40780",
    "user": "was"
}
```

Further remarks:

* I built the new matplotlib into sage-3.3.alpha5, which has the previous libpng spkg and both the popup and rendering of png problems vanished.   So the real bug is probably in libpng/matplotlib interaction.

* I build without the OS X gui backend and the problem vanishes for OS X.

A quick fix for sage-3.3.rc3 would be to disable the OS X GUI.  This can be done with a one line change to setup.py (just put an if False in the part of setup.py that involves that macos X gui), or something involving setup.cfg or something more complicated to setup.py.



---

archive/issue_comments_040781.json:
```json
{
    "body": "I will post an spkg that fixes this in a second.  Take it or leave it.  At least it will make it possible to release sage-3.3  It only disables GUI's by default on OS X, and creates an environment variable to control this in general.  If somebody wants to somehow redo this use setup.cfg, be my guest.",
    "created_at": "2009-02-20T15:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40781",
    "user": "was"
}
```

I will post an spkg that fixes this in a second.  Take it or leave it.  At least it will make it possible to release sage-3.3  It only disables GUI's by default on OS X, and creates an environment variable to control this in general.  If somebody wants to somehow redo this use setup.cfg, be my guest.



---

archive/issue_comments_040782.json:
```json
{
    "body": "The spkg is here:\n\nhttp://sage.math.washington.edu/home/was/patches/matplotlib-0.98.5.3rc0-svn6910.p2.spkg",
    "created_at": "2009-02-20T15:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40782",
    "user": "was"
}
```

The spkg is here:

http://sage.math.washington.edu/home/was/patches/matplotlib-0.98.5.3rc0-svn6910.p2.spkg



---

archive/issue_comments_040783.json:
```json
{
    "body": "Positive review. I checked in one diff as unified diff, but other than that no changes.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T16:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40783",
    "user": "mabshoff"
}
```

Positive review. I checked in one diff as unified diff, but other than that no changes.

Cheers,

Michael



---

archive/issue_comments_040784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T16:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40784",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040785.json:
```json
{
    "body": "Merged the spkg at\n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/matplotlib-0.98.5.3rc0-svn6910.p2.spkg\n\nin Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T16:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40785",
    "user": "mabshoff"
}
```

Merged the spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/matplotlib-0.98.5.3rc0-svn6910.p2.spkg

in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_040786.json:
```json
{
    "body": "For the record: I did turn off GUI support per default since it causes trouble on X less boxen, i.e. sage.math. This might very well be a bug in the new MPL, so someone should check with them why the inport of tcl or pygtk is not caught and dealt with appropriately. I talked all this over with William and he agreed with me that this is the right fix for 3.3, but that the issue should be revisited. The spkg at \n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/matplotlib-0.98.5.3rc0-svn6910.p3.spkg\n\nwas merged in 3.3.rc3 and replaced the one mentioned above.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T17:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40786",
    "user": "mabshoff"
}
```

For the record: I did turn off GUI support per default since it causes trouble on X less boxen, i.e. sage.math. This might very well be a bug in the new MPL, so someone should check with them why the inport of tcl or pygtk is not caught and dealt with appropriately. I talked all this over with William and he agreed with me that this is the right fix for 3.3, but that the issue should be revisited. The spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/matplotlib-0.98.5.3rc0-svn6910.p3.spkg

was merged in 3.3.rc3 and replaced the one mentioned above.

Cheers,

Michael



---

archive/issue_comments_040787.json:
```json
{
    "body": "Instructions for reenabling the gui backends are:\n\nset the environment variable SAGE_MATPLOTLIB_GUI to anything besides 'no'\n\nReinstall the spkg: ` sage -f matplotlib-0.98.5.3rc0-svn6910.p3`",
    "created_at": "2009-02-27T15:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5301#issuecomment-40787",
    "user": "jason"
}
```

Instructions for reenabling the gui backends are:

set the environment variable SAGE_MATPLOTLIB_GUI to anything besides 'no'

Reinstall the spkg: ` sage -f matplotlib-0.98.5.3rc0-svn6910.p3`
