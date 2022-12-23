# Issue 7012: clean up sage/numerical/mip.pyx

Issue created by migration from https://trac.sagemath.org/ticket/7012

Original creator: mvngu

Original creation time: 2009-09-25 08:04:10

Assignee: jkantor

CC:  ncohen mhansen

As the subject says. This is a follow up to #6869 to address mhansen's suggestions:

```


After going through this patch, I think it would be best to revert it before 4.1.2 is released. There is still a lot of things that need to be done to get it cleaned up. Some of the things,

1. Almost all of the docstrings are incorrectly formatted.

1. This module should _definitely_ not be a Cython module as it does not gain any benefit from Cython. It just makes Sage slower to compile and things harder to debug.

1. Some of the naming conventions do not match Sage's conventions. (isbinary vs. is_binary). Also, names like the more explicit MixedIntegerProgram? are preferred over the shortened MIP.

1. The optional spkgs should not install modules into the sage.* namespace (sage.numerical.mipGlpk). This is not the right way to do things and will eventually break. I think it also makes sense to use (and contribute to) something like ctypes-glpk to allow greater functionality and not reinvent the wheel.

I have some code that addresses some of these things that I'll put up shortly.
```



---

Comment by ncohen created at 2009-09-26 14:50:13

Hello !!!

Could I have more information about some points :

1. Almost all of the docstrings are incorrectly formatted.

Could you tell me in which way ? I am still learning how to write these, and may have learnt a few things since this patch but I would like to know what you have in mind.

1. This module should _definitely_ not be a Cython module as it does not gain any benefit from Cython. It just makes Sage slower to compile and things harder to debug.

- I understand that there may be very few reasons left ( now ) for keeping this as a Cython module. Here is the reason why I built it this way : initially, I thought the GLPK package would be merged immediately merged to standard Sage, and the function sending the LP problem to the solver GLPK ( necessarily written in Cython as it uses C functions ) was at this time contained in the file numerical.mip. I did not know how to change this when I learnt GLPK was to be optional for a while, and this is the reason why I just moved the function solveGLPK to the optional package. This, though, is way less handy when I need to improve functions like solveGLPK or solveCBC, as I always need to update the whole package.. I intended to move function solveGLPK to the file numerical.MIP as soon as GLPK is accepted as a standard spkg.

1. Some of the naming conventions do not match Sage's conventions. (isbinary vs. is_binary). Also, names like the more explicit MixedIntegerProgram? are preferred over the shortened MIP.

- I quite agree

1. The optional spkgs should not install modules into the sage.* namespace (sage.numerical.mipGlpk). This is not the right way to do things and will eventually break. I think it also makes sense to use (and contribute to) something like ctypes-glpk to allow greater functionality and not reinvent the wheel.

I wrote to many people to get informations about how best these things should be done. I am not happy either with the way it is now... What would you advise ? I know nothing of ctypes-glpk ! I just visited its front page and I can only see that it makes C functions available under python, which Cython can already do.


On top of all this, I have a "personal" request.... I intend to write a lot of things that will be added to the MIP class ( soon to be MixedIntegerProgram ), but I initially wrote this class just to write new Graph-related functions. I have still a lot of patches waiting to be reviewed/accepted ( #6764 #6763 #6680 #6679 #6765 #6962 ), all using this class. Each time a modification is brought to the main class MIP, I have to rewrite patches for all of these tickets to make them coherent with the "current" state of the MIP Class. Could this ticket wait for these patches to be merged ? It would be easier, later, to change MIP to MixedIntegerProgram, isbinary to is_binary, and many other problems/bugs I already noticed in an unique patch to correct them all at once.... :-)

Thank you a lot for your interest, though :-)

Nathann


---

Comment by mvngu created at 2009-09-26 22:48:07

Replying to [comment:1 ncohen]:
> Hello !!!
> 
> Could I have more information about some points :
> 
> 1. Almost all of the docstrings are incorrectly formatted.
> 
> Could you tell me in which way ? I am still learning how to write these, and may have learnt a few things since this patch but I would like to know what you have in mind.

The Developers' Guide has a section on [docstring](http://www.sagemath.org/doc/developer/conventions.html#documentation-strings). You should follow the conventions listed in that section.





> 1. This module should _definitely_ not be a Cython module as it does not gain any benefit from Cython. It just makes Sage slower to compile and things harder to debug.
> 
> - I understand that there may be very few reasons left ( now ) for keeping this as a Cython module. Here is the reason why I built it this way : initially, I thought the GLPK package would be merged immediately merged to standard Sage, and the function sending the LP problem to the solver GLPK ( necessarily written in Cython as it uses C functions ) was at this time contained in the file numerical.mip. I did not know how to change this when I learnt GLPK was to be optional for a while, and this is the reason why I just moved the function solveGLPK to the optional package. This, though, is way less handy when I need to improve functions like solveGLPK or solveCBC, as I always need to update the whole package.. I intended to move function solveGLPK to the file numerical.MIP as soon as GLPK is accepted as a standard spkg.
In light of the recent discussion about making a package standard, a package that is to be a standard spkg must satisfy at minimum the following requirements:

 1. Build as 32-bit with GCC on SPARC
 1. Build as 64-bit with GCC on SPARC
 1. Build as 32-bit with Sun's compiler on SPARC
 1. Build as 64-bit with Sun's compiler on SPARC
 1. Build as 32-bit with GCC on x86
 1. Build as 64-bit with GCC on x86_64
 1. Build as 32-bit with Sun's compiler on x86
 1. Build as 64-bit with Sun's compiler on x86_64

Note that satisfying the first four would likely satisfy the remaining criteria. It much less work to have GLPK and CBC be optional packages and hence improve on the MIP module. As far as I can tell, both of these packages are already optional spkg's and they satisfy the minimum of being optional packages, namely they build on supported Linux distributions and Mac OS X 10.5. I have not tried building and using them on OS X 10.6 yet. But if you have an account on bsd.math which runs OS X 10.6 now, you could test on that machine. See [here](http://groups.google.com/group/sage-devel/browse_thread/thread/15c461b1355a8460/d9660e265ad982d8) and [here](http://groups.google.com/group/sage-devel/browse_thread/thread/b54a6b4317add033/bf7224be375df49f) for the discussions about making a package standard.





> 1. The optional spkgs should not install modules into the sage.* namespace (sage.numerical.mipGlpk). This is not the right way to do things and will eventually break. I think it also makes sense to use (and contribute to) something like ctypes-glpk to allow greater functionality and not reinvent the wheel.
> 
> I wrote to many people to get informations about how best these things should be done. I am not happy either with the way it is now... What would you advise ? I know nothing of ctypes-glpk ! I just visited its front page and I can only see that it makes C functions available under python, which Cython can already do.
I have little experience with Cython and much less with maintaining an optional package. Since I'm busy with release management in the next week or so, I won't have time to investigate this issue. After finishing the 4.1.2 release, I won't be able to work on anything but my thesis project.





> On top of all this, I have a "personal" request.... I intend to write a lot of things that will be added to the MIP class ( soon to be MixedIntegerProgram ), but I initially wrote this class just to write new Graph-related functions. I have still a lot of patches waiting to be reviewed/accepted ( #6764 #6763 #6680 #6679 #6765 #6962 ), all using this class. Each time a modification is brought to the main class MIP, I have to rewrite patches for all of these tickets to make them coherent with the "current" state of the MIP Class. Could this ticket wait for these patches to be merged ? It would be easier, later, to change MIP to MixedIntegerProgram, isbinary to is_binary, and many other problems/bugs I already noticed in an unique patch to correct them all at once.... :-)
I think a good way about this is to look through how Simon King produced his optional p_group_cohomology package. You should ask Simon about his experiences with writing a self-contained package.




I do intend to clean up the MIP class before releasing Sage 4.1.2. Any help is appreciated.


---

Comment by ncohen created at 2009-09-28 07:57:09

Ok... I will be trying to send some coherent patch in the next few days, so it would be better if I am the only one working on this so our modification do not overlap. I changed some methods like setmin to set_min to let them be more Sage-like, and this involves modifying once more the packages CBC and GLPK ( which will have to be reviewed again... )

I may bring several other modifications too, while I'm at it. How close is next release ?

Nathann


---

Comment by mvngu created at 2009-09-28 08:00:57

Replying to [comment:3 ncohen]:
> Ok... I will be trying to send some coherent patch in the next few days, so it would be better if I am the only one working on this so our modification do not overlap. 

Thanks letting me know. I'll leave it to you to clean up MIP. Inform me when it's ready and I'll take a look.





> I changed some methods like setmin to set_min to let them be more Sage-like, and this involves modifying once more the packages CBC and GLPK ( which will have to be reviewed again... )

Inform me when it's ready and I'll take a look.





> I may bring several other modifications too, while I'm at it. How close is next release ?

The upcoming rc0 is in about 3 days or so.


---

Comment by ncohen created at 2009-09-28 09:34:59

Changing type from enhancement to defect.


---

Comment by ncohen created at 2009-09-28 09:34:59

What this patch does :
    * renames function getmin to get_min, isinteger to is_integer, etc ....
    * renames class MIP to MixedIntegerLinearProgram
    * function 
    * Typos
    * stupid bugfix 1 : setinteger was setting variables as binary in some cases ...
    * stupid bugfix 2 : setinteger(x) did not set x[2] as integer if x[2] had not been mentionned before setinteger() 
    * Some ":" replaced by "::", some '' by ``


---

Attachment


---

Comment by ncohen created at 2009-09-28 09:36:32

I forgot to mention this new patch can only be used through GLPK at #7049 as many methods had to be renamed and brek compatibility with old spkg.


---

Comment by mhansen created at 2009-09-28 09:51:58

Nathann, can you sign into #sage-devel on IRC?


---

Comment by mvngu created at 2009-10-01 11:29:22

rebased against Sage 4.1.2.rc0


---

Attachment

Applying the patch `trac_7012.patch` results in a hunk failure:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7012/trac_7012.patch && hg qpush
adding trac_7012.patch to series file
applying trac_7012.patch
patching file sage/numerical/knapsack.py
Hunk #1 FAILED at 640
1 out of 1 hunks FAILED -- saving rejects to file sage/numerical/knapsack.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_7012.patch
```

The hunk in question is:

```
[mvngu@sage sage-main]$ cat sage/numerical/knapsack.py.rej
--- knapsack.py
+++ knapsack.py
@@ -641,16 +641,16 @@
     if reals:
         seq=[(x,1) for x in seq]
 
-    from sage.numerical.mip import MIP
-    p=MIP(sense=1)
-    present=p.newvar()
-    p.setobj(sum([present[i]*seq[i][1] for i in range(len(seq))]))
-    p.addconstraint(sum([present[i]*seq[i][0] for i in range(len(seq))]),max=max)
+    from sage.numerical.mip import MixedIntegerLinearProgram
+    p=MixedIntegerLinearProgram(sense=1)
+    present=p.new_variable()
+    p.set_objective(sum([present[i]*seq[i][1] for i in range(len(seq))]))
+    p.add_constraint(sum([present[i]*seq[i][0] for i in range(len(seq))]),max=max)
 
     if binary:
-        p.setbinary(present)
+        p.set_binary(present)
     else:
-        p.setinteger(present)
+        p.set_integer(present)
 
     if value_only:
         return p.solve(objective_only=True)
```

I have rebased the patch against Sage 4.1.2.rc0; see `trac_7012-rebased.patch`.


---

Attachment

reviewer patch; apply on top of previous patch


---

Comment by mvngu created at 2009-10-01 17:43:24

I have uploaded a reviewer patch that makes the following changes (see `trac_7012-reviewer.patch`):

 1. Consistent use of double quotation marks in `sage/numerical/mip.pyx`.
 1. Doesn't use trailing white spaces.
 1. Limit the line width to about 75 characters. Don't go over 75 or so characters per line if you don't need to.
 1. Some typo fixes.
 1. Add `sage/numerical/mip.pyx` to the reference manual.
 1. Use 4-space indentation.
 1. Proper ReST formatting so the module appears nicely when rendered.
 1. Use `ValueError` instead of `Exception`. `ValueError` is more explicit, whereas `Exception` would catch anything.
 1. Use `maximization` with boolean values, instead of `sense` with either 1 or -1. This was suggested by Mike Hansen on IRC. So I would credit Mike and myself as reviewers for this ticket.

Now my patch needs some reviewing by anyone other than me.


---

Comment by ncohen created at 2009-10-01 18:55:02

Minh you're really amazing !! Thank you for your work ! :-)


---

Comment by ncohen created at 2009-10-02 16:32:14

I tested it with #7049 :
    * I updated #7049 because the change from variable sense to variable maximization had to be mentionned there
    * There was a wrong docstring report because GLPK sometines returns 1.684643648434 * 10^(-16) instead of 0 ( as CBC does )
      I added a "random" near the "optional" as GLPK and CBC do not agree on this.
    * sense->minimization needed changing in knapsack too

The docstrings are perfect !!!

Here is a new flattened patch with those two modifications included


---

Comment by mvngu created at 2009-10-04 15:14:30

flattened patch; include rebased patch and reviewer patch


---

Attachment


---

Comment by ncohen created at 2009-10-14 23:52:24

This ticket depends on #7049


---

Comment by mvngu created at 2009-10-21 22:36:22

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-10-21 22:36:22

I applied patches against Sage 4.2.alpha0 in the following order:

 1. `trac_7012-flattened.patch`
 1. `trac_7012-details.patch`
 
These two patches touch modules under `sage/numerical`. All doctests under this directory pass with the two patches. Doctesting the whole Sage library results in the following failure:

```
[mvngu@sage sage-4.2.alpha0-sage.math]$ sage -t -long devel/sage-main/sage/modules/vector_real_double_dense.pyx
sage -t -long "devel/sage-main/sage/modules/vector_real_double_dense.pyx"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.1 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-main/sage/modules/vector_real_double_dense.pyx"
Total time for all tests: 3.1 seconds
```

This is a known failure and has been reported before at ticket #6825. I then installed the optional GLPK package at #7049. All doctests passed when doctesting the whole Sage library. If the above two patches are merged, then the updated GLPK package at #7049 should also be merged in the optional spkg repository.


---

Comment by mhansen created at 2009-10-23 09:05:24

Resolution: fixed
