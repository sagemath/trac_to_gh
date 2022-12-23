# Issue 7592: Flow method using LP

Issue created by migration from https://trac.sagemath.org/ticket/7592

Original creator: ncohen

Original creation time: 2009-12-03 14:34:56

Assignee: rlm

As the title says, this patch implements the flow function for Graphs ( weighted or not, directed or not )


---

Comment by ncohen created at 2009-12-03 15:18:33

Changing status from new to needs_review.


---

Comment by wdj created at 2009-12-08 19:52:57

This does not apply to 4.3.a1 on an imac running 10.6.1:


```
jeeves:sage-4.3.alpha1 wdj$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
WARNING: There is one major unsolved bug in some versions of
Sage on OS X 10.6 that causes an 'Abort trap' crash when
doing certain symbolic computations.
See http://trac.sagemath.org/sage_trac/ticket/7095/.
Loading Sage library. Current Mercurial branch is: 7592-flow
sage: hg_sage.apply("/Users/wdj/sagefiles/trac_7592.patch")
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg status
/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg import   "/Users/wdj/sagefiles/trac_7592.patch"
applying /Users/wdj/sagefiles/trac_7592.patch
patching file sage/graphs/graph.py
Hunk #2 FAILED at 3019
1 out of 2 hunks FAILED -- saving rejects to file sage/graphs/graph.py.rej
abort: patch failed to apply
sage: 
```



---

Comment by wdj created at 2009-12-08 19:54:46

Replying to [comment:3 wdj]:
> This does not apply to 4.3.a1 on an imac running 10.6.1:
> 

...


I should add though that this version of sage has the latest networkx package installed.
Would that screw things up?


---

Comment by ncohen created at 2009-12-08 20:52:28

It could have, but in this case it was mainly my fault. I have no idea why, but the patch did not even apply on my version, perhaps they were not based on alpha... Here is a new version based on alpha, with my excuses :-)


---

Comment by ncohen created at 2009-12-08 21:11:54

There was a small mistake in the 

```
if vertex_bound:            
        CORRECTED LINE
```

Some variable had no assigned value.... And the patch I just updated takes this into account :-)


---

Comment by rlm created at 2009-12-15 17:04:19

You need more examples in the doctest section. Some of the options return something different than what the docs say, such as:

```
sage: g.flow(1,2, value_only=False)
[3.0, Pappus Graph: Graph on 18 vertices]
```



---

Comment by rlm created at 2009-12-15 17:04:19

Changing status from needs_review to needs_work.


---

Attachment

I corrected the documentation as I finally thought returning a graph would be much more useful :-)

I also added a more interesting example of what one can do with flows :-)

Nathann


---

Comment by ncohen created at 2009-12-16 00:44:53

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-16 02:52:48

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 21:09:33

Resolution: fixed
