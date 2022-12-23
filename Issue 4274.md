# Issue 4274: assertion failure in rank for elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/4274

Original creator: zimmerma

Original creation time: 2008-10-13 14:45:31

Assignee: was

CC:  cremona peter@cryptojedi.org

This was reported to me by Peter Schwabe:

```
sage: EllipticCurve([1,0,0,0,37455]).rank(proof=False)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/usr/local/sage-3.1.2/sage/devel/sage-main/sage/schemes/elliptic_curves/<ipython console> in <module>()

/tmp/sage-3.1.2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in rank(self, use_database, verbose, only_use_mwrank, algorithm, proof)
   1274                 proof = True #since we actually provably found the rank
   1275             i = X.find('Rank = ')
-> 1276             assert i != -1
   1277             j = i + X[i:].find('\n')
   1278             self.__rank[proof] = Integer(X[i+7:j])

AssertionError: 
```

Without proof=False, we get:

```
sage: EllipticCurve([1,0,0,0,37455]).rank()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/usr/local/sage-3.1.2/sage/devel/sage-main/sage/schemes/elliptic_curves/<ipython console> in <module>()

/tmp/sage-3.1.2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in rank(self, use_database, verbose, only_use_mwrank, algorithm, proof)
   1268             if not 'The rank and full Mordell-Weil basis have been determined unconditionally' in X:
   1269                 if proof:
-> 1270                     raise RuntimeError, '%s\nRank not provably correct.'%X
   1271                 else:
   1272                     misc.verbose("Warning -- rank not provably correct", level=1)
```



---

Comment by cremona created at 2008-10-13 17:04:10

Comment:  What's wrong here is the logic in parsing mwrank's output for a curve (and there are many) where the lower and upper bounds for the rank as computed by mwrank are not equal.  Here the lower bound is 0 and the upper bound is 2.  This is the *correct* mwrank output for a curve whose rank is 0 and whose Tate-Shafarevich group has 2-rank equal to 2.

The correct behaviour for Sage in this case is:  if proof==True, raise a run-time error (since mwrank by itself is incapable of find the rank for such a curve);  if proof==False, return a rank of 0 silently, showing a warning if the appropriate misc.verbose flag is set.

I think that this is what the Sage code is trying to do, but it is not doing it correctly at present.

OK, so that's an informed diagnosis but but not yet a cure!


---

Attachment


---

Comment by cremona created at 2009-01-22 20:47:22

Review:  

Patch applies fine to 3.3.alpha0.  Tests in elliptic_curves/ell_rational_field.py pass (but not with -long, see below).

I think this is ok.  It handles the case where the lower and upper bounds of the rank, as output by mwrank,  are not equal. 

At first I was not sure that it handled properly the case where the bounds are equal (so the rank is known for sure) but the saturation step is incomplete, but it's ok:

```
sage: EllipticCurve( [0,0,1,-49,132]).conductor()
26171
sage: EllipticCurve( [0,0,1,-49,132]).rank(proof=True)
3
sage: EllipticCurve( [0,0,1,-49,132]).gens(proof=False)
[(-6 : 14 : 1), (4 : -1 : 1), (5 : -4 : 1)]
sage: EllipticCurve( [0,0,1,-49,132]).gens(proof=True)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
Generators not provably computed.
```

[If testing the above example, do so on a Sage without the large database, else the gens will be known from there.]

This is exactly right. 

Testing with -long gives one failure but I don't see why it is a failure.  The test which fails is NOT a "long" one!  So is this a bug in the doctesting framewirk (due to the verbose output perhaps?)?


```
sage -t -long "devel/sage-4274/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/home/john/sage-3.3.alpha0/devel/sage-4274/sage/schemes/elliptic_curves/ell_rational_field.py", line 1291:
    sage: EllipticCurve([1,0,0,0,37455]).rank(proof=True)
Expected:
    Traceback (most recent call last):
    ...
    Rank not provably correct.
Got:
    Traceback (most recent call last):
      File "/home/john/sage-3.3.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-3.3.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-3.3.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_31[15]>", line 1, in <module>
        EllipticCurve([Integer(1),Integer(0),Integer(0),Integer(0),Integer(37455)]).rank(proof=True)###line 1291:
    sage: EllipticCurve([1,0,0,0,37455]).rank(proof=True)
      File "/home/john/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1342, in rank
        raise RuntimeError, '%s\nRank not provably correct.'%X
    RuntimeError: Curve [1,0,0,0,37455] :	Basic pair: I=1, J=-64722242
    disc=-4188968609506560
    2-adic index bound = 2
    By Lemma 5.1(b), 2-adic index = 1
    2-adic index = 1
    One (I,J) pair
    *** BSD give two (I,J) pairs
    Looking for quartics with I = 1, J = -64722242
    Looking for Type 3 quartics:
    Trying positive a from 1 up to 115 (square a first...)
    Trying positive a from 1 up to 115 (...then non-square a)
    (15,20,1,396,132)	--nontrivial...locally soluble...no rational point found (limit 10) --new (B) #1
    (33,30,199,198,-55)	--nontrivial...locally soluble...no rational point found (limit 10) --new (B) #2
    (33,66,-395,500,-144)	--nontrivial...--equivalent to (B) #1
    (83,-52,139,106,-36)	--nontrivial...--equivalent to (B) #1
    Trying negative a from -1 down to -77
    (-9,17,244,297,411)	--nontrivial...--equivalent to (B) #1
    (-15,10,331,646,501)	--nontrivial...locally soluble...no rational point found (limit 10) --new (B) #3
    (-67,-71,220,305,141)	--nontrivial...--equivalent to (B) #1
    Finished looking for Type 3 quartics.
    Mordell rank contribution from B=im(eps) = 0
    Selmer  rank contribution from B=im(eps) = 2
    Sha     rank contribution from B=im(eps) = 2
    Mordell rank contribution from A=ker(eps) = 0
    Selmer  rank contribution from A=ker(eps) = 0
    Sha     rank contribution from A=ker(eps) = 0
    <BLANKLINE>
    Summary of results (all should be powers of 2):
    <BLANKLINE>
    n0 = #E(Q)[2]    = 1
    n1 = #E(Q)/2E(Q) >= 1
    n2 = #S^(2)(E/Q) = 4
    #III(E/Q)[2]     <= 4
    <BLANKLINE>
    0 <= rank <= selmer-rank = 2
    <BLANKLINE>
    0 <= rank <= selmer-rank = 2
    Searching for points (bound = 8)...done:
      found points of rank 0
      and regulator 1
    Processing points found during 2-descent...done:
      now regulator = 1
    Saturating (bound = 100)...done:
      points were already saturated.
    <BLANKLINE>
    <BLANKLINE>
    Regulator = 1
    <BLANKLINE>
    The rank has not been completely determined, 
    only a lower bound of 0 and an upper bound of 2.
    <BLANKLINE>
     (0.868055 seconds)
    Rank not provably correct.
**********************************************************************
1 items had failures:
   1 of  16 in __main__.example_31
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/john/sage-3.3.alpha0/tmp/.doctest_ell_rational_field.py
	 [286.8 s]
exit code: 1024
```



---

Comment by GeorgSWeber created at 2009-01-23 20:35:05

Perhaps the "magic three dots" used in the verbose output at several places are problematic?

I agree that from first sight, this seems to be a framework problem, not one of the code to be doctested.


---

Comment by cremona created at 2009-01-23 20:59:15

Replying to [comment:5 GeorgSWeber]:
> Perhaps the "magic three dots" used in the verbose output at several places are problematic?
> 

That sounds plausible -- but why would it only be a problem when the -long flag is set?

> I agree that from first sight, this seems to be a framework problem, not one of the code to be doctested.


---

Comment by mabshoff created at 2009-02-15 14:33:47

Replying to [comment:6 cremona]:
> Replying to [comment:5 GeorgSWeber]:
> > Perhaps the "magic three dots" used in the verbose output at several places are problematic?
> > 
> 
> That sounds plausible -- but why would it only be a problem when the -long flag is set?

It fails for me without long, but this is truly bizarre. I have looked at the patch, but cannot find anything obviously wrong with it. 

> > I agree that from first sight, this seems to be a framework problem, not one of the code to be doctested.

Cheers,

Michael


---

Attachment

Apply after previous


---

Comment by cremona created at 2009-02-15 15:13:24

I have sorted this.  the problem was that the RuntimeError output string included the whole of the mwrank output, but the doctesting machinery soes not seem to be able to strip bits out of that string, only normal output.  So I changed it so that (in the case in question), first the mwrank output string is output, then the RuntimeError is raised with a short message.

At the same time i trimmed the long mwrank output so that only the short extract from near the end is output.  People who want to see the whole lot can always call mwrank() on the curve.

Additional patch does this, and fixes the problem -- minor review only required, I think!


---

Comment by mabshoff created at 2009-02-15 15:42:40

Replying to [comment:8 cremona]:
> 
> Additional patch does this, and fixes the problem -- minor review only required, I think!

Nice catch, I am doctesting it to make 100% there are no new issues. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 15:46:05

Resolution: fixed


---

Comment by mabshoff created at 2009-02-15 15:46:05

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by cremona created at 2009-02-15 15:59:21

Replying to [comment:10 mabshoff]:
> Merged both patches in Sage 3.3.rc1.

Excellent, thanks.

John
