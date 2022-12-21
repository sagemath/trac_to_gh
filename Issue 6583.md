# Issue 6583: Implement two descent over QQ natively in Sage using ratpoints

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-07-21 19:26:23

Assignee: davidloeffler

CC:  cremona was




---

Comment by rlm created at 2009-07-21 19:44:45

Although the patch above isn't finished, I do consider it polished for what it does. The next steps are:

1. plug into NTL for factoring over FF_p[X] for large p.

2. incorporate the optimization based on linear algebra in QQ*/(QQ*)^2.

3. do second descents in the case that the exact rank is not found.

4. General two-descent -- I have a rudimentary version of this in a notebook worksheet, which will eventually wind up here.

Although not in a completely finished state, comments are still welcome!


---

Comment by rlm created at 2009-09-17 20:34:15

Changing type from defect to enhancement.


---

Comment by rlm created at 2009-09-17 23:42:21

For my purposes (working within Cremona's big table, N<130000), the dimensions of the subspaces of Q*/(Q*)^2 I am considering are 

0: 242 cases
1: 15019 cases
2: 93479 cases
3: 141373 cases
4: 59005 cases
5: 7339 cases
6: 187 cases

Based on this, I do not consider it a priority to do #2. The others are also not necessary for my purposes, so I'm doing some serious triage and getting this into a mergable state now. These other enhancements can come later.


---

Comment by rlm created at 2009-09-18 01:18:43

Changing status from new to assigned.


---

Comment by rlm created at 2009-09-18 01:18:43

Changing assignee from davidloeffler to rlm.


---

Attachment


---

Attachment


---

Comment by was created at 2009-09-22 14:43:20

Applying the patch and doing "sage -t" yields some failures, probably because you assume the large cremona database is installed, but it isn't:

```
wstein`@`sage:~/build/sage-4.1.2.alpha1$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx
sage -t  "devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx"
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1093:
    sage: E = EllipticCurve('59450i')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[12]>", line 1, in <module>
        E = EllipticCurve('59450i')###line 1093:
    sage: E = EllipticCurve('59450i')
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/schemes/elliptic_curves/constructor.py", line 216, in EllipticCurve
        return ell_rational_field.EllipticCurve_rational_field(x)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 191, in __init__
        X = sage.databases.cremona.CremonaDatabase()[label]
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/databases/cremona.py", line 383, in __getitem__
        return self.elliptic_curve(N)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python/site-packages/sage/databases/cremona.py", line 570, in elliptic_curve
        raise RuntimeError, message
    RuntimeError: There is no elliptic curve with label 59450i in the default database; try installing the optional package database_cremona_ellcurve-20071019 which contains all curves of conductor up to 130000
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1095:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    3
Got:
    2
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 56:
    sage: from sage.schemes.elliptic_curves.descent import test_valuation as tv
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        from sage.schemes.elliptic_curves.descent import test_valuation as tv###line 56:
    sage: from sage.schemes.elliptic_curves.descent import test_valuation as tv
    ImportError: No module named descent
**********************************************************************
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 57: 
    sage: for i in [1..20]:
       print '%10s'%factor(i), tv(i,Integer(2)), tv(i,Integer(3)), tv(i,Integer(5))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 2, in <module>
        print '%10s'%factor(i), tv(i,Integer(2)), tv(i,Integer(3)), tv(i,Integer(5))
    NameError: name 'tv' is not defined
**********************************************************************
2 items had failures:
   2 of  24 in __main__.example_18
   2 of   4 in __main__.example_2
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.1.2.alpha1/tmp/.doctest_descent_two_isogeny.py
         [3.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx"
Total time for all tests: 3.4 seconds
wstein`@`sage:~/build/sage-4.1.2.alpha1$ 
```



---

Comment by rlm created at 2009-10-30 03:01:22

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by wuthrich created at 2009-11-04 13:30:19

Ok. I tested the patches and they all go through. Also the -coverage gives 6 out of 6 despite the fact that many functions in descent_two_isogeny.pyx lack a good documentation and especially examples are missing often. I guess this is because cdefs are not tested. (I admit I never reviewed a cython file.)

Currently the main function gives back four integers, like mwrank does. They are useful to compute an upper bound on the rank of the Mordell-Weil group and should (in the future) be called from `rank()` and also from `sha()`.

Personnally I would like more, namely I would like to have a phi-Selmer group. Ideally we should give back a abelian group associated to the elliptic curve, or even better to the isogeny. But isogenies are not there yet, though 2-isogenies should be. The Selmer groups would contain more information than just these four integers and I believe this extra-information is already computed in this algorithm.

Right now the functions are not callable without an extra import and so they do not pollute the name-space and we are still flexible in how to do this later; like `.selmer_group()` etc. That is very good. Yet it does not really look like a finished patch.

It is work in progress (and it is very good work in the right direction), but I am incapable of saying whether this sort of work should already be included in sage or not. So before giving a positive review to this patch, I would like to ask the author's and other's opinion on this. Maybe I could also ask for more examples, especially in the header of the file, despite the fact that it is not included in the documentation right now.

Chris.


---

Comment by cremona created at 2009-11-04 13:52:58

A couple of follow-up points to Chris, from an independent observer:  first, can we have some motivation, such as examples where this works better than calling mwrank?  There will certainly be curves for which the performance is worse (where mwrank would use a second descent).  I suspect that any enhanced perofrmance comes from the use of the more recent version of ratpoints than mwrank uses.

Secondly, the isogeny patch I am finishing up will allow 2-isogenies (and more) to be easily constructed (which they almost can already).  A very interesting project would be to take any (cyclic) isogeny between elliptic curves, defined over QQ, and return an appropriate Selmer group.


---

Comment by rlm created at 2009-12-01 18:56:54

Here's an example where mwrank does not do a second descent, where the runtime is approximately 90 times faster:


```
sage: E = EllipticCurve('676a1')
sage: from sage.schemes.elliptic_curves.descent_two_isogeny import two_descent_by_two_isogeny
sage: timeit('two_descent_by_two_isogeny(E)')
125 loops, best of 3: 2.83 ms per loop
sage: A = E.mwrank_curve()
sage: timeit('A.two_descent(verbose=False)')
5 loops, best of 3: 252 ms per loop
```


I ran the following to compare times in general:


```
sage: for E in cremona_optimal_curves(range(200)):
...    if E.torsion_order()%2 == 0:
...        t = walltime()
...        E.mwrank_curve().two_descent(verbose=False, second_descent=False)
...        t = walltime(t)
...        s = walltime()
...        _ = two_descent_by_two_isogeny(E)
...        s = walltime(s)
```


mwrank is always slower by a factor of at least 5, almost always slower by a factor of at least 20, and frequently slower by factors of up to 150.


---

Comment by rlm created at 2009-12-01 19:00:34

Maybe this is a more accurate comparison:

```
sage: L = []
sage: for E in cremona_optimal_curves(range(200)):
    if E.torsion_order()%2 == 0:
        A = E.mwrank_curve(); t = walltime()
        A.two_descent(verbose=False, second_descent=False)
        t = walltime(t)
        s = walltime()
        _ = two_descent_by_two_isogeny(E)
        s = walltime(s)
        if s > t: print E.label()
        else:
            L.append(t/s)
....:             
sage: sum(L)/len(L)
28.023321958157503
```


Thus the average speedup is 28x.


---

Comment by rlm created at 2009-12-01 19:02:11

For the curious, standard deviation:

```
sage: sqrt(sum([(l - 28.0233)^2 for l in L])/len(L))
10.6330410085500
```



---

Comment by cremona created at 2009-12-01 20:08:14

Robert -- I am quite prepared to believe that your code is fast, but all these tests on the curves of conductor up to 200 are not exactly typical!  I seem to remember that there is one curve in that range which mwrank used to take longer on than all the others put together, for example.


---

Comment by rlm created at 2009-12-01 21:34:59

I was just trying to address your question whether there were examples where this was better than mwrank. Your second comment, "any enhanced performance comes from the use of the more recent version of ratpoints" is very false: if I remove the use of ratpoints altogether, the speedup factors increase!

```
sage: L = []
sage: for E in cremona_optimal_curves(range(200)):
    if E.torsion_order()%2 == 0:
        A = E.mwrank_curve()
        t = walltime()
        A.two_descent(verbose=False, selmer_only=True, second_descent=False)
        t = walltime(t)
        s = walltime()
        _ = two_descent_by_two_isogeny(E, selmer_only=True)
        s = walltime(s)
        if s > t: print E.label()
        else:
            L.append(t/s)
....:             
sage: sum(L)/len(L)
147.24136054804828
```


Thus I argue that this code is definitely worth including, especially since this exact code was the main motivation for including ratpoints in Sage in the first place. I don't know what "typical" means regarding the conductor bound, especially since I'm primarily interested in curves with small conductor. I spent a long time optimizing this code, and I'd rather not see that work getting lost to the four winds.

(John-- Maybe I'm just missing your point?)


---

Comment by cremona created at 2009-12-02 15:43:53

Sorry, I did not mean to sound so critical.  Of course this should be included.  I have not had time to look at it in detail (though I feel that people expect me to, and give an expert opinion).  I think it would be good to have native 2-descent code in Sage (another extremely useful project would be to rewrite Simon's gp program over number fields in Sage), not least because the current interface is not very good (hard to use non-standard parameter settings, for example) and uses the ancient ratpoints, all because I have not had the time to improve those things.

Experience tells me that if you put in code which was designed for curves with small conductor then you will very soon find that people try to run the same code on huge examples.  This is precisely what happened to me -- the first version of what later became mwrank was written solely for the purpose of computing the ranks of the curves in my book, i.e. N<1000.  So the new code must be tested on large examples too.


---

Comment by rlm created at 2009-12-02 20:10:12

I've tried the same benchmarks on curves in the conductor range 129800 to 130000. There the average speedup is 117x. Once I have the Stein-Watkins database downloaded, I can try running some examples from there.

I'd like to attempt to summarize the referee comments so far:

- more documentation
- more examples
- output the Selmer group explicitly
- eventually we need to implement second descents


---

Comment by was created at 2009-12-09 00:44:39

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 00:44:39

REPORT:

1. I can't apply the patch to 4.3.alpha1:

```
patching file sage/libs/flint/zmod_poly.pxd
Hunk #2 FAILED at 249
1 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly.pxd.rej
abort: patch failed to apply
```


The rebase is trivial, and I've posted it.

---

2. The main concern in Chris's report is just that this code doesn't yet do enough.  However, rlm isn't just writing this as some one-off thing for a little project.  He's doing his Ph.D. thesis mostly on descent (and its applications), and this is what he'll be working on fulltime, probably for the next year (for his thesis, then his postdoc).  So I think getting this in now makes *perfect* sense, instead of waiting until we get a big patch bomb later. 

3. All those cdef'd methods with no doctests and minimal documentation isn't good, just as Chris says.  You could open another ticket and fix that, since it will make it way easier for others to work on (and use in surprising ways!) this code if those functions are documented and tested.  For each cdef'd method, just make a corresponding def'd method called "test_..." that calls the cdef'd method, then put the tests there.   You already do just that in *some* cases, e.g., `def test_els(a,b,c,d,e):`. 

4. Docstrings like this would be more readable if they used latex:

```
Given an elliptic curve E with a two-isogeny phi : E --> E' and dual isogeny 
 	799	    phi', runs a two-isogeny descent on E, returning n1, n2, n1' and n2'. Here 
 	800	    n1 is the number of quartic covers found with a rational point, and n2 is 
 	801	    the number which are ELS. 
```


5. All tests pass with this code applied to sage-4.3.alpha1.

In summary:

I've applied the patches, skimmed them, and run the test suite.  Positive review.


---

Attachment


---

Comment by cremona created at 2009-12-09 16:23:09

I am very happy to endorse this decision.  When I looked at this some time ago I think I found some extra functionality with the ratpoints package which should be, but is not yet, exposed, and started to work on that, but got diverted into other things.  Never mind:  we can always build on this and extra things if and when we want to.  Good, job, Robert!


---

Comment by mhansen created at 2010-01-04 04:02:54

Resolution: fixed


---

Comment by drkirkby created at 2010-01-07 07:28:51

Could you please take a look at #7867 which is a ticket indicating a problem building Sage on 't2' which could possibly be related to this.


---

Comment by drkirkby created at 2010-02-22 14:14:51

For the record, this is definitely the code which has broken the Solaris build. 

Minh has proven this: 

http://groups.google.com/group/sage-devel/msg/bb1da5365b7f1c90


Dave
