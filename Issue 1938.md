# Issue 1938: Fast (double) function evaluation for plotting, etc.

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-01-26 12:11:19

Assignee: somebody

When one wishes to plot a 3d surface, one ends up evaluating one or more algebraic expressions several hundreds of times. This is especially slow if maxima is involved via the calculus package. Up until now the solution has been to plot lambda expressions, but this is neither intuitive, Sage-like, nor efficient (compared to operating on raw c doubles).

We need a way to get a quick-to-evaluate version of a symbolic expression (polynomial, ...) I would imagine this would be useful for optimization problems and simulations as well. 


---

Comment by robertwb created at 2008-01-26 12:11:44

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-26 12:11:44

Changing assignee from somebody to robertwb.


---

Attachment

The attached bundle builds on and includes #1828 and #1862.


---

Comment by mabshoff created at 2008-01-26 14:03:33

Hi Robert, 

the patch looks very nice, but I am seeing a massive number of merge conflict against 2.10.1.rc0. Could you take 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/sage-2.10.1.rc0.tar

and rebase the patch? There have been a lot of tricky merges in the plotting code in 2.10.1.x, so it isn't really a surprise that there are problems :(

Cheers,

Michael


---

Comment by robertwb created at 2008-01-26 19:54:12

Sure, I'll re-base it. 

Is there a repo I could -upgrade from rather than re-building the whole thing from source?


---

Comment by mabshoff created at 2008-01-26 22:46:56

Replying to [comment:4 robertwb]:
> Sure, I'll re-base it. 
> 
> Is there a repo I could -upgrade from rather than re-building the whole thing from source? 

Nope, but it has been suggested a couple time to create a devel repo somewhere on sagemath.org to offer such a way to testbuild. I also saw that R failed to build for you on OSX 10.4 - I am building rc0 now on a 10.4 box to fix the issue.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-26 23:20:04

Here's some timings:


```
sage: f(x,y,z) = sin(z)/(1+x^2+y^2)
sage: lambda_f = lambda x,y,z: math.sin(z)/(1+x^2+y^2)
sage: fast_f = f._fast_float_('x','y','z')

sage: sage: A = range(50000)
sage: sage: time for _ in A: r = f(1.0r, 2.0r, 3.0r)
CPU times: user 12.47 s, sys: 0.08 s, total: 12.54 s
Wall time: 12.73

sage: sage: time for _ in A: r = lambda_f(1.0r, 2.0r, 3.0r)
CPU times: user 1.32 s, sys: 0.01 s, total: 1.33 s
Wall time: 1.37

sage: sage: time for _ in A: r = fast_f(1.0r, 2.0r, 3.0r)
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04
```



---

Attachment


---

Comment by robertwb created at 2008-01-27 11:00:29

The bundle just attached is merged with the plotting code of 2.10.1.rc0. Since William Stein was the other one who worked in this area, he should probably take a look at this as well to make sure I didn't regress anything.


---

Comment by was created at 2008-01-27 16:44:07

Wow, this is amazing compared to before!!!!!!!!!!!!!!!!!  Wow!  This is an awesome patch full of beautiful code.   It will have a major impact on how the calculus code is used in the future, and make things like numerical integration, ode's, etc. way way way faster. 

refereeing:

 * The the file morphism.pyx there are a bunch of print statements that shouldn't be there.  They must have been for debugging purposes:

```
    cdef Element _call_c_impl(self, Element x):
        print type(self), self
        print <long>self._call_c
        print <long>Morphism._call_c
        print <long>FormalCoercionMorphism._call_c
        raise NotImplementedError

```


  * More doctests are needed, e.g., L3096 of calculus.py, has two functions without doctests:

```
    def fast_float_function(self, vars):
        return self._fast_float_(vars)

    def _fast_float_(self, *vars):
        try:
```


  * Is ext/ really the right place for fast_eval.pyx?  Maybe.  I'm just not sure...

  * I wish there were a few sentences at the top of fast_eval.pyx about what it does. 

  * There's still a lot in fast_eval.pyx that needs doctests; it's coverage score is only 14%:

```
teragon:ext was$ sage -coverage fast_eval.pyx
----------------------------------------------------------------------
fast_eval.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE fast_eval.pyx: 14% (6 of 41)
```


   * This code in fast_eval.pyx is clearly TOTALLY WRONG and would give an infinite loop if it were actually tested: 

```
+    def sec(self):
+        return ~self.sec()   
```


   

Otherwise it looks good to me.   Fix the above then this patch should get marked with "positive review"


---

Comment by robertwb created at 2008-01-29 10:03:59

OK, I have fixed all the above issues, and added lots more documentation. As for placing it in sage/ext, I'm not sure but I can't think of another place that would be better. 

The most recently attached bundle contains everything.


---

Attachment

There are still doctest failures in fast_eval.pyx.  Otherwise this patch is good.
I've posted a .patch that fixes most of those failures, plus a bunch of roughness in the paragraphs at the top.  But there are three failing doctests left.  Please fix and then this patch will be ready to go.

 -- William


---

Comment by robertwb created at 2008-01-29 18:49:30

Do not apply the above patch last patch--everything passes on my computer including the lines 


```
sage: list(h)
['push 1.5', 'load 0', 'add', 'call sin(1)']
```


instead of 



```
sage: list(h)
['push 1.5', 'load 0', 'add', 'call 1 0x942acc20']
```


It looks like you didn't do a sage -b after applying merging the changes.


---

Comment by was created at 2008-01-30 03:02:12

do apply this


---

Attachment

You're right -- I didn't "sage -br" after the merge.  I redid the last patch, with a few fixes to typos and the writing in the paragraph, but without changing any doctests.


---

Comment by was created at 2008-01-30 03:14:19

This is now good to go, I think.  Very nice.


---

Comment by robertwb created at 2008-01-30 03:37:49

Yes, the documentation fixes are from the new patch should be applied. Thanks.


---

Comment by mabshoff created at 2008-01-30 09:21:21

Resolution: fixed


---

Comment by mabshoff created at 2008-01-30 09:21:21

Merged 1938-fast-float-fixes.hg and trac-1938-fix_some_docstrings.patch in Sage 2.10.1.rc3
