# Issue 7576: improvements to the prove_BSD function

Issue created by migration from https://trac.sagemath.org/ticket/7576

Original creator: rlm

Original creation time: 2009-12-01 22:03:36

Assignee: cremona

This patch makes several improvements to the prove_BSD function:

- better handling of when the Heegner index is computed
- speeds up several cases and makes some other cases possible


---

Comment by rlm created at 2010-01-02 14:35:39

Changing status from new to needs_review.


---

Comment by was created at 2010-01-03 19:18:28

REFEREE REPORT:

1. For proper Sphinx the indention has to be consistent. Your docstring is wrong:

```
        INPUT:

            - ``verbosity`` - int, how much information about the proof to print.

                - 0 - print nothing
                - 1 - print sketch of proof
                - 2 - print information about remaining primes

            - ``simon`` - bool (default False), whether to use two_descent or
              simon_two_descent at p=2.

            -  ``proof`` - bool or None (default: None, see
              proof.elliptic_curve or sage.structure.proof). If False, this
              function just immediately returns the empty list.

            - ``secs_hi`` - how many seconds to try to compute the Heegner index
              before switching over to trying to compute the Heegner index bound.
              (Rank 0 only!)
```


E.g., the proof one should be:

```
            - ``proof`` - bool or None (default: None, see
              proof.elliptic_curve or sage.structure.proof). If False, this
              function just immediately returns the empty list.
```


I find it useful to try making a simple function with the given docstring in the notebook, then evaluate and introspect that, to see what Sphinx does.


2. ```secs_hi`` - how many seconds to try to compute the Heegner index` -- change "how many seconds" to "maximum number of seconds", which is more precise. 

3. Add something to the verbose output when secs_hi interrupts a calculation.  

4. Once you have 3, add an example that illustrates it.   

5. Unfortunately, evidently hitting control-c doesn't work for some reason:

```
for E in cremona_optimal_curves([1..1000]):
     if E.rank() == 0:
         print E.label(), E.prove_BSD(secs_hi=0.1, verbosity=1)

....
<try hitting control-c -- ignored. :-(>
....
}}}         
This might be related to how you setup the alarm.  It's hard to tell.

6. The multiple uses of D here seems potentially confusing:
{{{
        5993	                for D in self.heegner_discriminants_list(100): 
 	5994	                    heegner_primes, D = self.heegner_index_bound(D, verbose=False) 
 	5995	                    if isinstance(heegner_primes, list): 
 	5996	                        break 
}}}

Also, the above hard-coded 100 makes me a little nervous.  What happens if we go through the whole list of 100 and don't find one that works?  (Highly unlikely in practice, of course.) Then we think the last one we looked at does work.  Not good.  

7. What is the point of this line?:
{{{
6157	                print '    ord_p(#Sha) >= 0' 
}}}
It's trivial that `ord_p(#Sha)>=0`, since `#Sha` is an integer, and `ord_p(n)>=0` for any integer n. 

8. In the docstring you should give precise references for the results you're using later.  E.g., instead of just "by Jetchev", you could explain that this means "by Theorem xyz" in his Compositio paper xxx.  "by Mazur" you mean theorem blah of blah, etc.   This could just go in the docstring, not the actual output (your choice).


---

Comment by was created at 2010-01-03 19:18:28

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-01-04 17:01:47

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-04 17:01:47

I think I've addressed all your comments, including handling the alarm better.


---

Comment by was created at 2010-01-12 22:13:55

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-01-12 22:13:55

New report:

  1. The alarm doesn't work perfectly.  On boxen.math with this patch applied to a clean sage-4.3, this fails on the command line (and when doctesting):

```
            sage: E = EllipticCurve('198b')
            sage: E.prove_BSD(verbosity=1, secs_hi=1)
```


Otherwise, everse looks good.


---

Comment by rlm created at 2010-01-12 22:23:27

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-12 22:28:55

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 05:08:55

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 05:08:55

For 438e1 and 960d1, we get:

```
RuntimeError                              Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc
in prove_BSD(self, verbosity, simon, proof, secs_hi)
  6372                 print 'p = 2: true by 2-descent'
  6373         else:
-> 6374             raise RuntimeError("ord2(#Sha) was computed to be
%d, but ord2(#Sha_an) is %d for this curve (%s)! This may be a
counterexample to BSD, but is more likely a
bug."%(sha_ord_2,sha_an.ord(2),self))
  6375
  6376         # reduce set of remaining primes to a finite set

RuntimeError: ord2(#Sha) was computed to be 1, but ord2(#Sha_an) is 0
for this curve (Elliptic Curve defined by y^2 + x*y + y = x^3 - 130*x
- 556 over Rational Field)! This may be a counterexample to BSD, but
is more likely a bug.
```



---

Comment by was created at 2010-01-13 14:39:15

Copying from Facebook again:

```
Jamie Weigandt
I read that Robert has implemented a fast 2-isogeny descent. Can this compute the honest 2-Selmer group of a given elliptic curve?

I thought these bugs might be arising from the fact that mwrank does not always do this.

With 438e, it erroneously computes the rank bound to be 1, while it should be 0.

With 960d the optimal curve has sha of order 4 while sha is trivial for an isogenous 
curve, so mwrank returns a rank bound of 0.
```



---

Comment by cremona created at 2010-01-13 15:33:20

For the record, it is hardly correct to say that a rank bound of 1 is wrong when the rank is zero!  But I know from communication from Weigandt that what the verbose output of mwrank claims to be the "2-Selmer rank" is not always that.

I should send rlm the example he sent me.


---

Comment by was created at 2010-01-13 23:42:58

Needs work:


```
sage: for E in cremona_optimal_curves([1001..2000]):
    print E.cremona_label(); print E.prove_BSD(verbosity=1, secs_hi=1)

...

1014g1
p = 2: Unverified since it is difficult to access the rank bound for Sha[2] computed by MWrank
Interrupting Mwrank...
Timeout stopped Heegner index computation...
Proceeding to use heegner_index_bound instead.
True for p not in {2, 5} by Kolyvagin.
Kolyvagin's bound for p = 5 applies by Stein et al.
ALERT: p = 5 left in Kolyvagin bound
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/virtual/scratch/wstein/build/sage-4.3.1.alpha2/<ipython console> in <module>()

/virtual/scratch/wstein/build/sage-4.3.1.alpha2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in prove_BSD(self, verbosity, simon, proof, secs_hi)
   6603             if verbosity > 0:
   6604                 print 'ALERT: p = %d left in Kolyvagin bound'%p
-> 6605                 print '    0 <= ord_p(#Sha) <= %d'%ord_p_bound
   6606                 print '    ord_p(#Sha_an) =', sha_an.ord(p)
   6607         for p in primes_to_remove:

UnboundLocalError: local variable 'ord_p_bound' referenced before assignment
```



---

Comment by rlm created at 2010-01-14 00:46:05

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-14 00:46:05

I wasn't able to include a doctest for `EllipticCurve('1014g1').prove_BSD(verbosity=1, secs_hi=1)` because it gives a very strange pexpect bug when run from a doctest, even though it runs perfectly fine from the command line.


---

Attachment


---

Comment by rlm created at 2010-01-19 04:33:18

I tried the following conductor "swaths" and the only error I ran into was caused by the issue at #7575 (I also interrupted a few since they were taking forever):

- range(350,450)

- range(800, 840)


---

Comment by rlm created at 2010-01-19 04:43:42

Just tried `range(1200, 1220)`, with similar results (although #7575 did not rear its head).


---

Comment by was created at 2010-01-19 05:53:16

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 05:58:52

Resolution: fixed
