# Issue 694: SAGE's multivariate gcd sucks over QQ and/or ZZ

Issue created by migration from https://trac.sagemath.org/ticket/694

Original creator: was

Original creation time: 2007-09-19 20:23:41

Assignee: somebody

CC:  =


```

I think those timings are way out of date, since Singular 3 seems
to be *very* fast at mod p multivariate GCD computation, even
though it sucks over QQ.   Check out this paper:

          http://www.cecm.sfu.ca/CAG/papers/brown.ps

It on exactly the problem of GCD over QQ (or equiv ZZ),
and section 2 has a complete description of a gcd algorithm 
that reduces gcd over ZZ to doing gcd's mod p.

Who wants to be a hero -- like Jon Bober and number of partitions -- 
and implement this for Sage, so that multivariate GCD's aren't 
embarrassingly slow in Sage anymore?   This slowness *has* 
been something reported to me on several occasions during 
the last 2 years. 

William
```



---

Attachment

this file has the singular input of a multivariate polynomial gcd that takes *minutes* in SAGE over QQ, but mod p the same takes 0.08 seconds.


---

Comment by was created at 2007-09-19 22:19:06

This paper describes the algorithm used in Singular:
   http://portal.acm.org/citation.cfm?doid=800192.805698

Jack Schmidt claims the paper I mention above is a dead end for this problem:

```
Careful to check the papers.  The Moses, et al. paper for singular
shows that Brown's method is ineffective for your problem, and it is
reasonably likely that this modified Brown method of Kaltofen et al.
is also ineffective.  The Kaltofen, et al. paper avoids the question
of exponential runtime by restricting to bivariate dense polynomials.
The Wang paper describes one major improvement in a reasonable common
corner case for singular's algorithm.  One presumes singular can be
asked to describe what it is doing during its EZ-GCD calculation, and
you can check if you are in this corner case.   Wang's EEZ-GCD may be
the better solution, and one should be able to implement a prototype
of this quickly in the singular language.  At any rate, it may be
better to look for improvements to EZ-GCD than for the modular gcd.
```


EZ-GCD is also a modular/p-adic algorithm, so it should benefit from various
fast mod-p gcd.


---

Comment by was created at 2007-09-19 22:19:23

Changing assignee from somebody to jbmohler.


---

Comment by was created at 2007-09-26 16:35:45

This is basically fixed (as soon as we upgrade to the newer singular).  
From the Singular team:


```
"hannes@mathematik.uni-kl.de" 	
to me, joel, sage-devel, singular-team
	
show details
	 8:40 am (49 minutes ago) 
Dear sage-devel readers,

following the discussion on sage-devel last week we implemented a
modular approach to compute the multivariate gcd over QQ in
Singular.
We still need to develop the heuristic when to prefer
EZGCD or the modular method: currently,
the modular method is prefered - this is not too bad:
the posted examples goes from several minutes to 1 sec running time.

These changes are inlcuded in
ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-0-3/Singular-3-0-3-1.tar.gz

Hans

PS: the timings at
http://magma.maths.usyd.edu.au/users/allan/gcdcomp.html
(originally from http://home.bway.net/lewis/fermat/gcdcomp)
are questionable as they refer also to computations in characteristic 43051
in Singular 2.0.4, which it did not support.

```



---

Attachment


---

Comment by malb created at 2007-10-01 23:22:40

Attached is a patch (6546) which makes use of the new SINGULAR spkg found at 

http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-1-20070929.spkg

which provides a multimodular GCD.


---

Comment by malb created at 2007-10-01 23:22:40

Changing assignee from jbmohler to malb.


---

Comment by malb created at 2007-10-01 23:22:40

Changing status from new to assigned.


---

Comment by was created at 2007-10-04 03:24:24

Resolution: fixed
