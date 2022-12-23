# Issue 6958: [with patch, not ready] prove_BSD function for elliptic curves over QQ

Issue created by migration from https://trac.sagemath.org/ticket/6958

Original creator: rlm

Original creation time: 2009-09-19 03:13:09

Assignee: davidloeffler

CC:  was

Comments welcome!


---

Attachment


---

Comment by was created at 2009-09-19 22:32:04

Given the nature of this function, i.e., it should never raise an exception with the default inputs, I think it should run successfully for all curves of conductor up to 100 (say) before getting into Sage.  It fails already on 11a2.


```
for E in cremona_curves([1..100]+[389]):
    print E.cremona_label(), E.prove_BSD(verbosity=2)
```



```
11a1 p = 2: true by 2-descent
True for p not in {2, 5} by Kolyvagin.
True for p=5 by Mazur
[]
11a2 p = 2: true by 2-descent
True for p not in {2, 5} by Kolyvagin.
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/Users/wstein/.sage/temp/flat.local/1342/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in prove_BSD(self, verbosity, simon, proof)
   5270         # Kato's bound
   5271         if rank == 0 and not E.has_cm():
-> 5272             assert E.optimal_curve() == E
   5273             L_over_Omega = E.lseries().L_ratio()
   5274             kato_primes = Sha.bound_kato()

AssertionError: 
```


Also, I think the fix for the above is to just switch to the optimal curve.  

OK, done by changing the code that raises the error to:

```
            # We can replace E by the corresponding optimal curve without changing truth
            # of BSD at p.
            E = E.optimal_curve()
```


A quicker test once we always first switch to the optimal curve is to do:

```
for E in cremona_optimal_curves([1..100]):
    print E.cremona_label()
    try:
        E.prove_BSD(verbosity=2)
    except Exception, msg:
        print "** problem !!", msg
```


This test passes right now up to 91, then this hangs forever (=15 minutes):

```
90c1
p = 2: true by 2-descent
True for p not in {2, 3} by Kolyvagin.
...
```


With set_verbose(2) we see that:

```
True for p not in {2, 3} by Kolyvagin.
verbose 1 (6244: heegner.py, heegner_index) computing heegner point height...
verbose 1 (6244: heegner.py, heegner_index) Height of heegner point = 41.383? (time = 0.195229)
verbose 1 (6244: heegner.py, heegner_index) Heegner height bound = 41.384
verbose 1 (6244: heegner.py, heegner_index) CPS bound = 8.48553581472
verbose 1 (6244: heegner.py, heegner_index) Search would have to be up to height = 18.832
verbose 1 (6244: heegner.py, heegner_index) doing point search
...
```

so doing the index bound as a future patch is the way to go.


---

Attachment

For the second patch, proof=False and proof=True are reversed for the doctest on 389a.


---

Comment by rlm created at 2009-09-19 22:59:14

OK, William agrees to my fixes and I to his. Positive review!


---

Comment by mvngu created at 2009-09-24 15:26:10

The patch `trac_6958-typos_followup.patch` results in a hunk failure:

```
[mvngu@mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6958/trac_6958-typos_followup.patch && hg qpush
adding trac_6958-typos_followup.patch to series file
applying trac_6958-typos_followup.patch
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 FAILED at 5688
1 out of 5 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6958-typos_followup.patch
```



---

Attachment


---

Comment by mhansen created at 2009-10-05 07:04:54

I've attached a new version of `trac_6958-typos_followup.patch` which removes the failing hunk since the doctest that it changed had been removed.


---

Comment by davidloeffler created at 2009-10-09 09:11:17

Remove assignee davidloeffler.


---

Comment by mhansen created at 2009-10-15 16:13:41

Resolution: fixed
