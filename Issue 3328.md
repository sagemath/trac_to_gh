# Issue 3328: minor fix rpy

Issue created by migration from https://trac.sagemath.org/ticket/3328

Original creator: fbissey

Original creation time: 2008-05-29 09:38:16

Assignee: mabshoff

A problem was reported to me a month or two ago and I was hit by it
when I built sage-3.0.2 from scratch (rather than by sage -upgrade).
rpy didn't build because RHOME was not defined. This may be required 
because I have not only sage version of R but also a system provided
version. After adding a line in rpy spkg-install pointing RHOME to 
SAGE_LOCAL/lib/R it did build without problem.
However a test failed:
sage -t  devel/sage/sage/stats/test.py                      **********************************************************************
File "/home/francois/Work/SAGE/tmp/test.py", line 5:
    sage: import rpy
Exception raised:
    Traceback (most recent call last):
      File "/home/francois/Work/SAGE/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[1]>", line 1, in <module>
        import rpy###line 5:
    sage: import rpy
      File "/home/francois/Work/SAGE/local/lib/python2.5/site-packages/rpy.py", line 58, in <module>
        RVERSION = rpy_tools.get_R_VERSION(RHOME)
      File "/home/francois/Work/SAGE/local/lib/python2.5/site-packages/rpy_tools.py", line 99, in get_R_VERSION
        " `%s'.\n" % rexec )
    RuntimeError: Couldn't execute the R interpreter `/usr/lib/R/bin/R'.

================
As one can see sage's rpy was trying to use the system provided R rather
than sage's own. An extra line in sage-env  took care of that.
2 small patch attached to cover this corner case. Note that the patches
won't make any difference to people not affected by this issue.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-05-29 11:52:38

Hi Francois,

thanks for the patches, we already had a ticket for this issue at #3011, so I am closing that as a duplicate. Please make sure in the future that you add "[with patch, needs review]" line to the Summary field and also assign a default milestone so your patch isn't slipping through the cracks. I will review this patch shortly, but it looks good as is :)

Cheers,

Michaek


---

Comment by mabshoff created at 2008-05-29 14:18:59

Ok, both patches look good. A couple remarks:

 * please post proper mercurial patches. I committed the patches in your name, but it would make applying future patches easier
 * be precise, i.e. spkg-install is for the rpy.spkg - it tool me some time to figure that out. 

An updated r.spkg containing all your fixes [and some more things by me like updated SPKG.txt] is available at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha1/r-2.6.1.p17.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 14:42:27

Merged in Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-05-29 14:42:27

Resolution: fixed
