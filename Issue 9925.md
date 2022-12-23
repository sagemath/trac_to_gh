# Issue 9925: Doctest error in sage/schemes/generic/toric_divisor.py on OS X

Issue created by migration from https://trac.sagemath.org/ticket/9926

Original creator: mpatel

Original creation time: 2010-09-17 00:46:23

Assignee: mvngu

CC:  novoselt vbraun mhampton

I get this reproducible doctest error with a trial 4.6.alpha1 (32-bit build) on bsd.math (OS X 10.6):

```python
sage -t -long "devel/sage/sage/schemes/generic/toric_divisor.py"
**********************************************************************
File "/Users/mpatel/tmp/bb/slave/bsd_scratch/build/sage-4.6.alpha1/devel/sage/sage/schemes/generic/toric_divisor.py", line 1522:
    sage: supp.Vrepresentation()
Expected:
    [A vertex at (-1, 1), A vertex at (0, 2), A vertex at (0, -1), A vertex at (3, -1)]
Got:
    [A vertex at (-1, 1), A vertex at (0, 2), A vertex at (3, -1), A vertex at (0, -1)]
```



---

Comment by mpatel created at 2010-09-17 00:47:01

If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000.


---

Comment by mpatel created at 2010-09-17 00:49:30

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.


---

Comment by novoselt created at 2010-09-17 04:21:48

Volker, what's the correct way to sort vertices? And what does their order in `Vrepresentation` depend on?


---

Comment by vbraun created at 2010-09-17 11:24:24

The output order should be deterministic: `_sheaf_cohomology_support()` does nothing that could randomize the order of `chamber_vertices` and `Polyhedron` takes the ordering of the vertices to be whatever `cddlib` returns. I don't have access to an OSX machine nor an account on bsd.math, so someone else will have to debug this.


---

Comment by novoselt created at 2010-09-17 14:54:54

Marshall, is there any chance you can settle this, since I don't understand the guts of Polyhedron? Does cddlib have any specific ordering of vertices? (IMHO, taking convex hull should delete extra points and otherwise leave the order the same.) Even if cddlib does not care about any particular order I find it strange that it can depend on architecture...

Of course, an easy fix to this is to put "#random output" comment in the doctest, but it does not feel satisfactory in this case.


---

Comment by mhampton created at 2010-09-17 15:24:48

I'll try to check this out but I don't have much time today, it might take me a few.


---

Comment by jhpalmieri created at 2010-09-20 05:29:31

This is not as pleasant, but what about something like:

```
sage: all([v in supp.vertices() for v in [[-1, 1], [0, 2], [3, -1], [0, -1]]])
True
```



---

Comment by mhampton created at 2010-09-20 13:22:09

That would work, although as an example it seems harder to understand.  I think I would prefer:


```
sage: vertices = supp.vertices()
sage: vertices.sort()
sage: vertices
[[-1, 1], [0, -1], [0, 2], [3, -1]]
```


at least as a temporary workaround.  It would be nice if the Polyhedron class produced a specific output, but that will require some significant additions that I won't have time for before this release.


---

Comment by vbraun created at 2010-09-20 16:11:47

I think the problem is that `cddlib` uses `rand()` to sometimes make random initial choices while searching for generating sets. Although `cddlib` fixes the seed, there is no guarantee that different platforms implement `rand()` in the same way.

To make sure this is indeed the problem, can you run

```
sage: Polyhedron(vertices=[(0, 1), (1, 1), (0, 1), (-1, 1), (0, 2), (0, -1), (0, 0), (0, 0), (3, -1), (0, 2), (0, -1), (1, -1), (0, 0)], verbose=True)
V-representation
begin
 13 3 rational
 1 0 1
 1 1 1
 1 0 1
 1 -1 1
 1 0 2
 1 0 -1
 1 0 0
 1 0 0
 1 3 -1
 1 0 2
 1 0 -1
 1 1 -1
 1 0 0
end

V-representation
begin
 4 3 rational
 1 -1 1
 1 0 2
 1 0 -1
 1 3 -1
end

H-representation
begin
 4 3 rational
 2 1 -1
 1 2 1
 1 0 1
 2 -1 -1
end
A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices.
```

on the OSX machine and paste the output? I can then rip out the `rand()` from the `cddlib.spkg`...


---

Comment by mhampton created at 2010-09-20 19:57:25

Changing assignee from mvngu to mhampton.


---

Comment by mhampton created at 2010-09-20 19:57:25

I'm confused by "rip out the rand() from the cddlib.spkg" - are you going to patch the source code?

Anyway on OS X 10.6 I get:


```
V-representation
begin
 13 3 rational
 1 0 1
 1 1 1
 1 0 1
 1 -1 1
 1 0 2
 1 0 -1
 1 0 0
 1 0 0
 1 3 -1
 1 0 2
 1 0 -1
 1 1 -1
 1 0 0
end


V-representation
begin
 4 3 rational
 1 -1 1
 1 0 2
 1 3 -1
 1 0 -1
end

H-representation
begin
 4 3 rational
 2 1 -1
 1 2 1
 1 0 1
 2 -1 -1
end

Vertex graph
begin
  4    4
 1 2 : 2 4 
 2 2 : 1 3 
 3 2 : 2 4 
 4 2 : 1 3 
end

Facet graph
begin
  4    4
 1 2 : 2 4 
 2 2 : 1 3 
 3 2 : 2 4 
 4 
```



---

Comment by mhampton created at 2010-09-20 19:57:51

Changing assignee from mhampton to mvngu.


---

Comment by vbraun created at 2010-09-20 20:14:56

Yes, thats what I'm planning to do: patch the `cddlib` source code to use a portable random number generator. I already have an updated spkg for #9798, so I'll patch this issue at the same time if you don't object.


---

Comment by dimpase created at 2010-09-21 04:43:00

same failure on PPC MacOSX 10.5, just in case...
Dima


---

Comment by vbraun created at 2010-09-21 13:51:45

Changing status from new to needs_info.


---

Comment by vbraun created at 2010-09-21 13:51:45

Updated spkg is at #9798, please test on your OSX machines. Note: also needs patch to the sage library which you can find on the same ticket.


---

Comment by dimpase created at 2010-09-21 15:02:08

Changing status from needs_info to needs_work.


---

Comment by dimpase created at 2010-09-21 15:02:08

Replying to [comment:14 vbraun]:
> Updated spkg is at #9798, please test on your OSX machines. Note: also needs patch to the sage library which you can find on the same ticket.
> 

I just did, please see the other ticket...
Dima


---

Comment by jason created at 2010-10-11 17:51:56

Replying to [comment:12 vbraun]:
> Yes, thats what I'm planning to do: patch the `cddlib` source code to use a portable random number generator. I already have an updated spkg for #9798, so I'll patch this issue at the same time if you don't object.
> 

I'm curious; are you planning on using Sage's framework for interfacing to random number generators?  See sage/devel/sage/sage/misc/randstate.pyx, and examples for setting the random seed in gap, pari, the libc generator, etc., or see http://sagemath.org/doc/reference/sage/misc/randstate.html#generating-random-numbers-in-library-code


---

Comment by vbraun created at 2010-10-11 19:42:25

My plan is described in #10039. So I'm not interested in adding more to cddlib than what we absolutely have to.


---

Comment by mpatel created at 2010-10-17 03:13:39

Update: I also get the problem in the description with a _64-bit_ build of 4.6.alpha3 on bsd.math (OS X 10.6).


---

Comment by vbraun created at 2010-10-18 10:33:46

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-10-18 10:33:46

I've fixed the bug in #9798. That ticket will fix the issue in this ticket, too.


---

Comment by dimpase created at 2010-10-18 14:52:20

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-10-18 14:52:20

Replying to [comment:19 vbraun]:
> I've fixed the bug in #9798. That ticket will fix the issue in this ticket, too.

tested on Debian x64 and on MacOSX 10.5 PPC. Positive!


---

Comment by mpatel created at 2010-10-21 08:39:25

Resolution: fixed
