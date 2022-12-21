# Issue 4860: upgrade networkx to 0.99 upstream release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-23 21:23:00

Assignee: rlm

CC:  jason

See http://networkx.lanl.gov/reference/news.html

It seems that this could still come in handy since we will need it for Python 2.6 support for example. 

Cheers,

Michael


---

Comment by rlm created at 2008-12-23 21:53:58

Proposed upgrade package found here:

http://8tb.us/home/rlmill/networkx-0.99.spkg

Passed long tests in `sage.graphs`, haven't yet tested elsewhere. Someone should check this out, because the pkg doubled in size (although this is 0.36 --> 0.99)


---

Comment by mabshoff created at 2008-12-23 22:58:10

From http://groups.google.com/group/networkx-discuss/browse_thread/thread/28e898e144a5e282

Looks like we need to wait for Scipy 0.7:

```
> > Thanks Cyril.  It looks like networkx-0.99 currently depends on 
> > python-scipy >= 0.7.0 (just out in beta).  I'll see if I can make it 
> > work correctly with 0.6.0. 
> Note that it's not really required on my end, I thought I would report 
> it in case that could be useful. I can live (and the package in 
> experimental too) with a failure in the test suite. Don't bother too 
> much. ;-) 


I took a look and it looks like the SciPy sparse matrix handling 
has changed quite a bit between 0.6.0 and 0.7.0.  So I'll leave 
it as is and require 0.7.0 for that (small,optional) part of networkx. 
Aric 
```


Cheers,

Michael


---

Comment by rlm created at 2008-12-23 23:07:27

AFAIK nothing we do in Sage depends on that (small,optional) part of networkx that requires up-to-date scipy.


---

Comment by mvngu created at 2009-01-28 23:43:21

Changing keywords from "" to "networkx-0.99".


---

Comment by mvngu created at 2009-01-28 23:43:21

On i686 Debian 5.0 Lenny (testing) with kernel 2.6.24-1-686, and Sage 3.2.3, I downloaded the package at 



[http://8tb.us/home/rlmill/networkx-0.99.spkg](http://8tb.us/home/rlmill/networkx-0.99.spkg)



to my machine and installed it with

```
sage -i networkx-0.99.spkg
```

and ran tests with

```
sage -t -long /path/to/SAGE_ROOT/devel/sage-main/sage/graphs
```

All tests passed.


---

Comment by mabshoff created at 2009-01-29 06:27:15

I have fixed various issues in SPKG.txt and spkg-install and put the updates spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/networkx-0.99.p0.spkg

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 06:31:02

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 06:31:02

Resolution: fixed
