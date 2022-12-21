# Issue 9598: Make cvxopt be able to use GLPK

Issue created by migration from Trac.

Original creator: dunfield

Original creation time: 2010-07-26 00:25:33

Assignee: tbd

CC:  ncohen

The convex optimization Python module cvxopt and the linear programming library GLPK are both standard packages in Sage 4.5.  The module cvxopt includes a python interface to GLPK, but currently cvxopt is unaware of the presence of GLPK and does not compile or include that submodule: 


```
sage: from cvxopt import glpk
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
```





---

Comment by dunfield created at 2010-07-26 00:26:19

Changing assignee from tbd to dunfield.


---

Comment by dunfield created at 2010-07-26 03:02:55

To allow cvxopt to find and use glpk there are two things that need to be done to the cvxopt spkg.

1. Modify the two setup.py files in cvxopt-0.9.p8/patches to turn on support for GLPK.  

2. Modify "spkg/standard/deps" so that GLPK has to compile before cvxopt.   See Dave Kirkby's explanation of [this](http://groups.google.com/group/sage-devel/msg/866bb0112d4066eb?).  In particular, the cvxopt entry should look like this:


```
$(INST)/$(CVXOPT): $(BASE) $(INST)/$(FORTRAN) $(INST)/$(F2C) \ 
                    $(INST)/$(LAPACK) $(INST)/$(BLAS) $(INST)/$(NUMPY) \ 
                    $(INST)/$(ATLAS) $(INST)/$(CEPHES) $(INST)/$(GLPK) 
```


I have attached a mercurial patch for (1); as I couldn't figure out how the "deps" file is under version control, the above will have to do for (2).


---

Comment by dunfield created at 2010-07-26 03:02:55

Changing status from new to needs_review.


---

Attachment

patch


---

Comment by drkirkby created at 2010-07-26 09:24:20

I can help you out with the `spkg/standard/deps` file. I will attach one in a minute. I'll attach a new deps file, and a unified diff, which makes the changes more obvious. I will also correct the fact that SAGETEX is not shown to depend on BASE, when in fact all packages depend on BASE, with the exception of the four packages in BASE. 

But I don't see any evidence of doctests for this functionality. So it looks like there was extra functionality, but it will be totally untested. There needs to be some examples of use added to the documentation, which will get tested when the Sage testsuite is run. The results need to be verifiable too - in other words, not 


```
Expected: [4.1121212232455654, 4334.34]
```


just because you got `[4.1121212232455654, 4334.34]` on your computer. 

I would ask what platforms this has been tested on, as Sage does support Linux, OS X and Solaris, but it's not clear to me how this can be tested at all just now.


---

Comment by drkirkby created at 2010-07-26 09:24:20

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-07-26 10:40:26

Replying to [comment:4 drkirkby]:
> I can help you out with the `spkg/standard/deps` file. I will attach one in a minute.

I just need to verify if I have the correct original to base this on. I will attach it as soon as possible. But clearly this needs work in order that we can verify that the cvxopt is able to use glpk properly on all supported platforms.


---

Comment by ncohen created at 2010-07-26 15:05:02

Hello !! Shouldn't this tickt be coordinated with #6456 ?

Perhaps this modification could be included in the upgrade, which would avoid to update the spkg two times ! :-)

Nathann


---

Comment by dunfield created at 2010-07-26 15:13:30

Replying to [comment:6 ncohen]:
> Hello !! Shouldn't this tickt be coordinated with #6456 ?
> 
> Perhaps this modification could be included in the upgrade, which would avoid to update the spkg two times ! :-)
> 
> Nathann

Nathann,

Yes, that makes a lot of sense.


---

Comment by dunfield created at 2010-07-26 15:27:28

> But I don't see any evidence of doctests for this functionality. So it looks like there was extra functionality, but it will be totally untested. There needs to be some examples of use added to the documentation, which will get tested when the Sage testsuite is run. 

You can specify the which solver cvxopt uses via the "solvers" optional argument.   E.g. with the last example in [the current doctest](http://www.sagemath.org/doc/numerical_sage/cvxopt.html) one could follow this example with 

```
sage: sol2 = solvers.lp(c,G,h,solver='glpk')
GLPK Simplex Optimizer, v4.44
4 rows, 2 columns, 6 non-zeros
Preprocessing...
2 rows, 2 columns, 4 non-zeros
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  2.000e+00  ratio =  2.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 2
*     0: obj =   0.000000000e+00  infeas =  0.000e+00 (0)
*     2: obj =  -9.000000000e+00  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
}}
Near as I can tell, all that stuff is being printed by glpk directly; I'm not sure if it's platform sensitive or not.  

There is a more direct interface to glpk as well which one could test instead --- the function names differ between cvxopt 0.9 and cvxopt 1.1, though.  



> I would ask what platforms this has been tested on, as Sage does support Linux, OS X and Solaris, but it's not clear to me how this can be tested at all just now. 

OS X.


---

Comment by dimpase created at 2010-07-26 16:04:49

Replying to [comment:7 dunfield]:
> Replying to [comment:6 ncohen]:
> > Hello !! Shouldn't this tickt be coordinated with #6456 ?
> > 
> > Perhaps this modification could be included in the upgrade, which would avoid to update the spkg two times ! :-)
> > 
> > Nathann
> 
> Nathann,
> 
> Yes, that makes a lot of sense.  

I just incorporates this patch to my new cvxopt-1.1.2. (we really, really should move to 1.1.2 before doing anything to cvxopt!!!) please see

 http://boxen.math.washington.edu/home/dima/packages/cvxopt-1.1.2.p1.spkg

and the developments on #6456

Dima


---

Comment by dimpase created at 2010-07-26 16:04:49

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-07-26 17:20:27

Replying to [comment:8 dunfield]:
> Near as I can tell, all that stuff is being printed by glpk directly; I'm not sure if it's platform sensitive or not.  

How can it be ready for review if you are not sure if it's platform sensitive or not? 

> > I would ask what platforms this has been tested on, as Sage does support Linux, OS X and Solaris, but it's not clear to me how this can be tested at all just now. 
> 
> OS X.  

Since it's only been tested on OS X, I would suggest this is not ready for review. It has to be shown to work on 
 * Linux
 * Solaris
 * OS X. 

If someone has specific questions about building on Solaris, I will answer them if I can. But what I can't do is test everyones patches on Solaris. They will need to do that themselves. 

The page

http://www.sagemath.org/doc/numerical_sage/cvxopt.html 

has no reference to GLPK, or the use of other solvers. 

IMHO, it would be better to look at update cvxopt while you take the time to test this on multiple platforms and add some examples of how it is used. At the moment, it seems rather rushed to me. 

Dave


---

Comment by drkirkby created at 2010-07-26 17:20:27

Changing status from needs_review to needs_work.


---

Comment by dunfield created at 2010-07-26 18:13:47

Replying to [comment:10 drkirkby]:

> Replying to [comment:8 dunfield]: How can it be ready for review if you are not sure if it's platform sensitive or not?

Dave,

You're responding to my comment, but it was Dima who changed the status after he tested this patch in conjunction with #6456 (the upgrade to cvxopt 1.1.2).  Looking at Dima's current version of cvxopt 1.1.2, he simply changed the needed two lines in "setup.py" directly rather than apply the patch included here. 

The combination of #9598 and #6456 has so far been tested on OS X (me), Linux 32 (Dima), and also by shilly (OS not mentioned); see the comments in the #6456 thread.   I don't think it's been tested on Solaris, but I don't have access to any such machines and can't help with that.

Nathan


---

Comment by drkirkby created at 2010-07-26 19:18:11

Replying to [comment:11 dunfield]:

> Dave,
> 
> You're responding to my comment, but it was Dima who changed the status after he tested this patch in conjunction with #6456 (the upgrade to cvxopt 1.1.2).  Looking at Dima's current version of cvxopt 1.1.2, he simply changed the needed two lines in "setup.py" directly rather than apply the patch included here. 
> 
> The combination of #9598 and #6456 has so far been tested on OS X (me), Linux 32 (Dima), and also by shilly (OS not mentioned); see the comments in the #6456 thread.   I don't think it's been tested on Solaris, but I don't have access to any such machines and can't help with that.
> 
> Nathan

I've looked at this and can't see any documentation or doctests to accompany the change to cvxopt that will allow it to use glpk. As far as I can see, this just allows cvxopt to link to the glpk library - no proof that is working properly. There's nothing to tell a user of cvxopt that they can use the glpk solver. Whilst I appreciate you and the author know that this is so, the documentation does not reflect this. Once the documentation reflects this, it can be doctested and one determine if there are any problems with the cvxopt/glpk interaction after each release of Sage. It's not clear to me how that can be done with this patch. If I'm mistaken, please correct me. 

You do have access to a Solaris machine. In fact, you have a created a directory in /scratch on 't2'. 


```
kirkby`@`t2:[/scratch] $ ls /scratch
dima      dreyer    gray      juanjo2   mpatel    ncohen    rishi     sergey    wstein
drake     ghitza    jason     mhansen   mvngu     palmieri  scons     sking
```


So you *can* check it. If you need help, I will try to help you if you can tell me what you done, and what problems or error messages you got. 

Dave


---

Comment by dunfield created at 2010-07-26 19:42:48

> You do have access to a Solaris machine. In fact, you have a created a directory in /scratch on 't2'. 

Dave,

You're confusing me (Nathan Dunfield) with Nathann Cohen, whose scratch directory you're referring to.  You can tell us apart because Nathann has three 'n's in his first name ;-).  

As for a doctest, I think what schilly used in comment 42 of #6456 would work fine.  I've attached a patch for the documentation and also the file itself --- I'm not sure if DIma et al have also modified the docs.


---

Attachment

devel/sage/doc/en/numerical_sage/cvxopt.rst


---

Attachment

Replying to [comment:13 dunfield]:
> > You do have access to a Solaris machine. In fact, you have a created a directory in /scratch on 't2'. 
> 
> Dave,
> 
> You're confusing me (Nathan Dunfield) with Nathann Cohen, whose scratch directory you're referring to.  You can tell us apart because Nathann has three 'n's in his first name ;-).  
> 
> As for a doctest, I think what schilly used in comment 42 of #6456 would work fine.  I've attached a patch for the documentation and also the file itself --- I'm not sure if DIma et al have also modified the docs.  

Sorry Nathan, you are correct. I am confusing the two of you. It is especially easy as I know Nathann Cohen has been using GLPK - I helped him make the package which is in Sage. I even cc'ed him, as I know he has been working a lot with GLPK. So when there were replies from a Nathan

Do you have an account on sage.math? If so, you can have an account on the Solaris system t2.math and test there - let me know your username on sage.math. I can point you at some instructions on how to test on t2. Testing on the Solaris system sometimes gives slightly different results from other systems, as the floating point processors are not identical. (The CPUs are *totally* different to Intel or AMD CPUs - the code is not binary compatible, though it is at the source code level.)

It's not clear to me if there is a doc test or not on #6456, as it seems that #6456 is just showing the result of typing the commands at the command line. It is basically a ticket to upgrade cvxopt. 


Dave


---

Comment by dunfield created at 2010-07-26 20:43:28

Replying to [comment:14 drkirkby]:
> Do you have an account on sage.math?

No, I don't.  

Nathan


---

Comment by dunfield created at 2010-12-03 15:20:16

This has now been fixed as a small part of  #6456.


---

Comment by dunfield created at 2010-12-03 15:20:16

Resolution: fixed
