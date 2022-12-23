# Issue 5789: create sagelite

Issue created by migration from https://trac.sagemath.org/ticket/5789

Original creator: was

Original creation time: 2009-04-15 01:07:39

Assignee: mabshoff




---

Comment by was created at 2009-04-15 06:19:43

NOTE: The patches don't apply cleanly.  The bundle works perfectly against sage-3.4.1.rc[1-2] and applies cleanly. 

The authors of this are Mike Hansen and William Stein.  

After applying the patch sage should work 100% as usual. However, if in devel/sage/ you type

  ./spkg-distlite

then the dist directory will contained

  dist/sagelite-3.4.1.tar.gz

You can take that sagelite-3.4.1.tar.gz and drop it into "any" Python (extract and do `python setup.py install`) that has twisted, pexpect, Ipython and maybe some other easy dependencies, and you should be able to do


```
>>> from sage.server.notebook.notebook_object import notebook
>>> notebook('test_dir')
```

and get the Sage notebook, completely independent of the rest of the Sage library!

If you switch the mode to python in the list at the top of the screen, you should be able to compute 2+2.

 -- William


---

Comment by was created at 2009-04-15 06:38:46

Here's a link to the sagelite-3.4.1.tar.gz that the above instructions would produce:

http://sage.math.washington.edu/home/wstein/patches/sagelite-3.4.1.tar.gz


---

Comment by mabshoff created at 2009-04-15 06:46:32

By the way: bundle_of_it_all.hg contains all changes since 3.4, so it might be nice to extract the relevant bits and post a unified patch.

Cheers,

Michael


---

Comment by certik created at 2009-04-15 08:14:24

I can confirm that the http://sage.math.washington.edu/home/wstein/patches/sagelite-3.4.1.tar.gz works! Here is a short howto:

http://code.google.com/p/spdproject/wiki/AdditionalPackages

the "from sage.all import notebook" doesn't work, but "from sage.server.notebook.notebook_object import notebook" and that's what is needed. I tested with sympy and SPD and all is fine. It was maybe small step for you, but a big step for me. :)

I am now going to review the actual patches and try to reproduce the tarball from the sage.


---

Comment by certik created at 2009-04-15 14:04:19

The bundle works fine for me and as far as I can tell, it's +1. However, I'd like if somebody with more familiarity with the code could also look at it, since the patch imho touches important things.

Some comments that I noticed: the following functions have doctests, but don't have any docstring, e.g. I was expecting some line about what the function does -- sometimes it's easy to infer from the example, sometimes it took me a while (e.g. the running_total):

```
+def prod(x, z=None):
+    """

+def running_total(L, start=None):
```


Anyway, this is minor.

I run the tests for a sever:

$ ./sage -t devel/sage/sage/server/

They all pass for me.


---

Comment by mhansen created at 2009-04-15 20:34:47

I've attach trac_5789.patch which rolls all of the previous patches into one and rebases them against what will be 3.4.1.rc3.  I also added to the docstrings of misc_compat.py


---

Comment by certik created at 2009-04-15 21:19:38

I apologize for the two changes above, I used a wrong field to put the comment in. I hope reverted my change correctly.

The patch is +1 from me.


---

Comment by certik created at 2009-04-15 21:22:33

Hopefully now the description is ok.


---

Comment by mabshoff created at 2009-04-15 21:33:23

I nuked the bundle since I see no point in keeping a huge 0.5MB bundle around when we now have the patch :)

Taking only trac_5789.patch I get:

```
byte-compiling /scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/structure/sobj.py to sobj.pyc
  File "/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-packages/sage/structure/sobj.py", line 202
    cdef bint make_pickle_jar = os.environ.has_key('SAGE_PICKLE_JAR')
            ^
SyntaxError: invalid syntax

running install_scripts
```

Cython vs. Python?

Cheers,

Michael


---

Attachment

I updated the patch to take care of this.


---

Comment by mabshoff created at 2009-04-15 21:51:13

Replying to [comment:12 mhansen]:
> I updated the patch to take care of this.

This patch causes one rather bizarre doctest failure:

```
sage -t -long "devel/sage/sage/rings/real_rqdf.pyx"         
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/rings/real_rqdf.pyx", line 587:
    sage: loads(s)
Expected:
    7.123456789000000000000000000000000000000000000000000000000000000
Got:
    doctest:1: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    7.123456789000000000000000000000000000000000000000000000000000000
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_24
```

Otherwise we do doctest fine.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 21:54:13

Another slight problem: spkg-distlite defines and hard codes

```
export SAGE_VERSION="3.4.1"
```

Is that desired? It seems like this is something we should define in sage-env.

Cheers,

Michael


---

Comment by was created at 2009-04-16 00:29:24

> `export SAGE_VERSION="3.4.1"`
> Is that desired?   

Nope, that's not good.  It should do something more clever. But fixing this is not IMHO a show stopper.


---

Comment by was created at 2009-04-16 00:30:07

One fix is to just do

```
if [ "$SAGE_VERSION" = "" ]; then
   echo "You must set the environment variable SAGE_VERSION."
   exit 1
```



---

Comment by mabshoff created at 2009-04-16 01:17:59

Replying to [comment:15 was]:

> Nope, that's not good.  It should do something more clever. But fixing this is not IMHO a show stopper.  

I agree that it isn't, but in that case we should address it via a followup ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-17 22:48:40

I am now in bug fix only mode for 3.4.1.rc4, so this ought to be the first patch in 3.4.2.alpha0 assuming the doctest failure gets fixed and the patch reviewed.

Cheers,

Michael


---

Comment by kcrisman created at 2009-06-22 20:46:13

This does not apply cleanly against 4.0.2; at the least one would have to make minor changes about where is_64_bit is imported a few places and rebase regarding the additional functionality e.g. unpickle_override in sage_object.pyx.


---

Comment by kcrisman created at 2009-11-04 15:46:30

Is this ticket now obsolete with the introduction of the sagenb package?  Just curious.


---

Comment by kcrisman created at 2010-01-06 16:44:41

To release manager: Since #485 was closed, this one should be as well.


---

Comment by was created at 2010-01-06 23:17:34

Resolution: wontfix


---

Comment by was created at 2010-01-06 23:17:34

Yes, this is obsolete.
