# Issue 1998: animate -- completley broken in sage-2.10.*

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 05:07:18

Assignee: was


```
was`@`sage:~/build/sage-2.10.1.rc3$ ./sage -t -optional devel/sage-main/sage/plot/animate.py
sage -t -optional devel/sage-main/sage/plot/animate.py      **********************************************************************
File "animate.py", line 47:
    sage: a.show()          # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[3]>", line 1, in <module>
        a.show()          # optional###line 47:
    sage: a.show()          # optional
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/animate.py", line 283, in show
        self.gif(delay = delay, iterations = iterations)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/animate.py", line 271, in gif
        d = self.png()
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/animate.py", line 212, in png
        xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, **self.__kwds)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1388, in save
        g._render_on_subplot(subplot)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1915, in _render_on_subplot
        p = patches.lines.Line2D(self.xdata, self.ydata, **options)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/matplotlib/lines.py", line 279, in __init__
        self.update(kwargs)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/matplotlib/artist.py", line 394, in update
        raise AttributeError('Unknown property %s'%k)
    AttributeError: Unknown property xmin
**********************************************************************
File "animate.py", line 48:
    sage: a[:5].show()      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[4]>", line 1, in <module>
        a[:Integer(5)].show()      # optional###line 48:
    sage: a[:5].show()      # optional
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/animate.py", line 283, in show
        self.gif(delay = delay, iterations = iterations)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/animate.py", line 271, in gif
        d = self.png()
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/animate.py", line 212, in png
        xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, **self.__kwds)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1388, in save
        g._render_on_subplot(subplot)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1915, in _render_on_subplot
        p = patches.lines.Line2D(self.xdata, self.ydata, **options)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/matplotlib/lines.py", line 279, in __init__
        self.update(kwargs)
      File "/home/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/matplotlib/artist.py", line 394, in update
        raise AttributeError('Unknown property %s'%k)
    AttributeError: Unknown property xmin
**********************************************************************

etc.
```


We missed this because it is "optional", because of the reliance on the convert command. 


---

Comment by moretti created at 2008-01-31 05:28:42

Crap. I will take a look at it and try to post a fix tonight.


---

Comment by moretti created at 2008-02-08 21:51:14

There were two problems here. One was that plot() no longer took xmin and xmax keywords. The other is that animate() calls the plot command with the xmin, xmax style syntax. I will post a patch that fixes both.


---

Attachment

See changesets 8313 - 8317 of the attached bundle.


---

Comment by mabshoff created at 2008-02-14 18:49:39

The second commit in the bundle is the patch from #2097, which has already been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-10 07:51:45

Bobby, please extract the change sets that are relevant to this ticket and post it as a patch so it can be reviewed and merged.

Cheers,

Michael


---

Comment by mhansen created at 2008-04-08 04:46:21

Is this still an issue:


```
mhansen`@`sage:~/sage-3.0.alpha2-sage.math-only-x86_64-Linux/devel/sage$ sage -t -optional sage/plot/animate.py
sage -t -optional devel/sage-main/sage/plot/animate.py      
         [26.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 26.7 seconds
```



---

Comment by mabshoff created at 2008-04-08 09:34:18

I am not sure, but there is a bundle with nine changesets attached to this ticket. But only some of them are relevant and I would really like 

 * to know if this is still a problem (I think it isn't any more)
 * have the bundle split up into proper patches related only to the various tickets

Bobby? Are you listening?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-08 12:00:58

Resolution: fixed


---

Comment by mabshoff created at 2008-04-08 12:00:58

This is fixed:

```
[13:22] <mabshoff> wstein: can you comment on #1998 ?
[13:25] <wstein> #1998 can be closed since the --optional doctests now pass on that file.
[13:25] <mabshoff> ok. good
```


Cheers,

Michael
