# Issue 4761: [iwth patch, needs review] global cputime (inclusive some subprocesses like Singular)

Issue created by migration from https://trac.sagemath.org/ticket/4761

Original creator: malb

Original creation time: 2008-12-11 15:34:42

Assignee: malb

I always found this annoying:


```
sage: t = cputime()
sage: P = PolynomialRing(QQ,8,'x')
sage: I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis()
sage: print cputime(t)
0.217967
```


so here's my proposal for a fix:


```
sage: t = cputime_gobal()
sage: P = PolynomialRing(QQ,8,'x')
sage: I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis()
sage: print cputime_global(t)
5.647973
```


I am not sure if the design is particularly nice though.


---

Comment by was created at 2008-12-11 23:45:47

This needs to be rewritten since it makes the faulty assumption that there is at most one interface to singular/magma, etc., at a given moment, and also ignores many of the interfaces needlessly (?).  To emphasize the first point, if I do:

```
sage: s = Singular()
sage: t = Singular()
sage: s('2+2')
4
sage: t('2+2')
4
```

then none of the computations above will be seen by cputime_global(). 

Regarding the second point, here is a one liner that allows you to get a list of *all* interface objects:

```
sage: print [s() for s in sage.interfaces.quit.expect_objects if s()]
[Mathematica, Singular, Axiom, Gap, Genus2reduction, GP/PARI interpreter, Kash, Lisp Interpreter, Magma, Macaulay2, Maple, Maxima, Matlab, Mupad, Mwrank, Octave, Sage, LiE Interpreter, R Interpreter, Maxima, Maxima, R Interpreter]
```


If you start more, they get *registered* in the sage.interfaces.quit.expect_objects list. 

For example, this illustrates getting all currently running interface objects:

```
sage: gp('2+2')
4
sage: s = Singular()
sage: s('2+3')
5
sage: magma('5')
5
sage: [s() for s in sage.interfaces.quit.expect_objects if s() and s().is_running()]
[GP/PARI interpreter, Magma, Singular]
```


You could do this before and after the computation, and for newly started interface objects, the cputime for that one would be the total cputime (i.e., it defaults to 0). 
You could also just get all interface objects, even ones that aren't yet running, but that is NOT as useful, imho, since calling cputime() on them starts them up (which is terrible)...

Anyway, hopefully the above has enough "interface fu" that you can easily write the ultimate version of cputime.  And maybe it should just replace cputime?  I.e., 


```
sage: cputime()   # what you write
sage: cputime(subprocesses=False)  # the original cputime?
```


It probably depends on how much overhead there is...   I could easily imagine rewriting the cputime methods for each interface so that they are nearly instant *unless* the interface has actually done something -- i.e., put a cached value in the cputime() method for each interface that is cleared precisely when you send code to be evaluated.


---

Comment by malb created at 2008-12-12 00:27:15

Cool. I admit I should have searched a bit longer if there is a list of running interfaces already. Most `cputime()` implementations throw `NotImplementedError` but I assume we can just ignore those cpu times or fix that.


---

Comment by malb created at 2008-12-12 16:26:58

I updated the patch based on was' comments. Also, the new patch doesn't introduce a new function to the global namespace.


---

Comment by was created at 2008-12-12 17:57:55

REFEREE REPORT:
 * typo -- "be started an terminated at any given time.": The "an" should be "and". 

 * typo -- "somehwat random": should be "somewhat random". 

 * Design issues.  I think if t is output from cputime(subprocesses=True), then cputime(t) should automatically have subprocesses=True, since with it False, isn't it just giving nonsense?  Or is it really giving the Sage part?  If the later, ignore this comment, but please document this in the function.  (Yes, it's the latter.)

 * Maybe a sentence that explained that so far at least all we're timing is the pexpect interface subprocesses that have a working cputime method.  That any other subprocess (e.g., gfan) isn't timed.   Then people know exactly what they would have to do to make sure there expect interface gets included.

 * The __float__ method for GlobalCputime doesn't have the examples in an EXAMPLES block and they aren't indented properly.


---

Comment by SimonKing created at 2009-01-24 17:25:42

First of all, the patch applies cleanly.

I tested the example from the documentation, and I tested an example involving singular and gap. 

What I find really amazing: Assume that you did

```
sage: t=cputime(subprocesses=True)
sage: s=cputime(subprocesses=False)
```

and later you do

```
sage: cputime(t)
sage: cputime(s)
```


I expected that `cputime(t)` would assume `subprocesses=False`, since its previous usage (in the definition of s) had this option. But `cputime(t)` indeed recognizes that t was defined with `subprocesses=True`. This is a very nice feature.

However, something seems to be wrong.
I did the following:

```
sage: t=cputime(subprocesses=True)
sage: s=cputime(subprocesses=False)
sage: {... some lengthy computation...}
sage: cputime(t)
1.440028
sage: cputime(s)
0.45202800000000032
sage: cputime(s,subprocesses=True)
1.972029
sage: cputime()
2.2761420000000001
sage: cputime(subprocesses=False)
2.2801420000000001
sage: cputime(subprocesses=True)
3.800142
sage: quit
Exiting SAGE (CPU time 0m0.65s, Wall time 11m49.60s).
Exiting spawned Singular process.
Exiting spawned Gap process.
```


Hence, when leaving Sage, it is stated that the CPU time spent is 0.65s, whereas `cputime(subprocesses=False)` claims that it is more than 2 seconds. Therefore, I can not give a positive review yet.


---

Comment by SimonKing created at 2009-01-24 17:25:42

Changing keywords from "" to "global cputime subprocesses".


---

Comment by malb created at 2009-05-12 02:04:28

The behaviour described above is "normal" insofar as it is not caused by the patch, compare with the current implementation:


```
sage: cputime()
0.73999999999999999
sage: exit
Exiting SAGE (CPU time 0m0.05s, Wall time 0m5.60s).
```


This should be due to the fact that `cputime()` uses user + sys time while the stuff at exit only uses the CPU time.


---

Comment by malb created at 2009-05-12 02:06:23

Correction: the stuff at exit simply doesn't count the initialisation. Is that a positive review then?


---

Comment by mvngu created at 2009-06-08 03:40:24

Just a quick note: The docstring formatting should now follow the ReST format.


---

Attachment


---

Comment by malb created at 2009-06-08 10:50:13

Thanks Minh, I've updated the patch. Can someone comment on the open issue raised above, i.e. that I don't agree with Simon's `needs work`?


---

Comment by ncalexan created at 2009-06-19 23:07:07

I think the existing behaviour is fine.  The patch looks good and seems to work for me.  Positive review.


---

Comment by rlm created at 2009-06-24 09:49:37

Resolution: fixed
