# Issue 9659: EK.regulator_of_points() doctest error in ell_number_field.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-01 10:17:05

Assignee: mvngu

CC:  cremona ddrake leif

Reported by Leif Leonhardy on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/a932af7b005283b4#a932af7b005283b4):

```
On 32-bit Ubuntu 9.04 (P4 Prescott 3.2GHz, gcc 4.3.3, native code) 
[...]
   sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
   ***************************************************************
   File "/home/leif/sage-4.5.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_number_field.py", line 444:
       sage: EK.regulator_of_points([P,T])
   Expected:
       -1.23259516440783e-32
   Got:
       -4.93038065763132e-32
   ***************************************************************
   1 items had failures:
      1 of  42 in __main__.example_5
   ***Test Failed*** 1 failures.
   For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_ell_number_field.py
            [171.9 s] 
```


See [this thread](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8315/trac_8315-doc_sidebar.patch) for a discussion.


---

Comment by leif created at 2010-08-01 17:37:07

If someone provides a patch, I can test it, but not much more at the moment.

So this might change to a 4.5.3 blocker. (I wouldn't mind, especially since I haven't yet done anything to track this issue down further.)


---

Comment by mpatel created at 2010-08-01 22:57:55

I've inquired about this problem at [comment:ticket:9343:159 #9343].


---

Comment by cremona created at 2010-08-02 01:15:39

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-02 01:15:39

The correct mathematical result is an exact 0,  obtained as a 2x2 determinant of the form [a,0; 0,0]:

```
sage: EK.height_pairing_matrix([P,T])
[     1.41516132073186 -1.11022302462516e-16]
[-1.11022302462516e-16     0.000000000000000]
```

I think the best way to get a machine-independent test here is to have

```
sage: EK.regulator_of_points([P,T]).abs() < 1e30
True
```

instead of putting the spurious small value into the doctest.

The patch does this (as well as leaving the original test with a #random tag).


---

Comment by mpatel created at 2010-08-02 01:30:11

Just to be sure:  Should that be `1e30`, in order to be ultra-safe, or its reciprocal?


---

Comment by leif created at 2010-08-02 01:32:06

Hmmm, really `< 1e30`?

Also, I'd add a backref to this ticket.


---

Comment by cremona created at 2010-08-02 01:46:07

Replying to [comment:6 leif]:
> Hmmm, really `< 1e30`?
> 
> Also, I'd add a backref to this ticket.
>
 
If you have a better suggestion, just do it.  Any specific numerical result will change with the new pari anyway.

The height of a torsion point is already exactly 0.  We could add more special cases for the regulator of two points P,Q that if either P or Q or P-Q were torsion then the regulator is 0, but as the necessary condition is that some linear combination n*P+m*Q=0 no such code would catch all these special cases.


---

Comment by leif created at 2010-08-02 02:20:21

This is again a really weird one. The affected machine has just finished `ptestlong` on rc0: "*All* tests passed!" (This time the exclamation mark is appropriate, if it is intended to express surprise.)

The only thing I've changed w.r.t. the alpha0 and alpha1 builds is that I've added `-O2` to `CFLAGS` and `CXXFLAGS` (for the first time btw, not expecting this would make a difference regarding this doctest, since most parts are compiled with `-O2` or `-O3` by default).

In fact, `./sage -t -long` on `ell_number_field.py` now takes only about 159 seconds instead of the previous 172-173 seconds. (The whole `ptestlong` though took almost exactly four hours as usual.)

I don't know what we should do with this ticket now. Merge anyway (with corrected upper bound)?


P.S.: I just meant 1<sup>-30</sup> instead of 1<sup>30</sup> (as Mitesh noted, too).


---

Comment by cremona created at 2010-08-02 02:32:16

applies to 4.5.2.alpha0


---

Attachment

OK, my mistake -- I have updated the patch so it now says 1e-30.

The optimization change will effect this a lot.   The optimization flag on a pari build was downgraded a while back for a silly reason; and upped again on the ticket upgrading pari.  This will effect all the number field code.


---

Comment by leif created at 2010-08-02 02:43:51

Strange though this seems to only have a "visible" effect (i.e., numerical noise in a doctest) on that specific processor.


---

Comment by leif created at 2010-08-02 02:48:45

(I actually touched that file on both Pentiums and compared the compile commands previously - there was no difference; of course not knowing this doctest uses external code.)


---

Comment by drkirkby created at 2010-08-02 10:30:47

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-08-02 10:30:47

Replying to [comment:9 cremona]:
> OK, my mistake -- I have updated the patch so it now says 1e-30.

That looks reasonable to me. 

> The optimization change will effect this a lot.   The optimization flag on a pari build was downgraded a while back for a silly reason; and upped again on the ticket upgrading pari.  This will effect all the number field code.
  
As a matter of interest, [I asked on gcc-help about the use of -O1 and -O3](http://gcc.gnu.org/ml/gcc-help/2010-07/msg00190.html). To quote from someone who I believe is a gcc developer

''The -O3 optoin should be safe for correct code.  An important difference between -O2/-O3 and -O1 is that -O2 and -O3 enable strict aliasing and strict overflow.  Those options provide better optimization for correct code, but are far more likely to cause unexpected code generation for incorrect code.  See the -fstrict-aliasing and -fstrict-overflow
options.'' 

''The main difference between -O3 and -O2 is that -O3 enables more
speculative optimizations.  These should not miscompile your code, but
they may cause your program to run more slowly.''

It's not to me whether -O2 or -O3 is the better choice. You might find -O2 is actually faster than -O3!

IMHO, we really do need set of benchmark results. 

But the patch looks quite reasonable to me. The [IEEE 754 standard](http://en.wikipedia.org/wiki/IEEE_754-2008) does not guarantee that different systems implementing IEEE 754 maths will give the same result. Nor is there anything to say that any two different processors from Intel will give the same result. 

Since the correct result should be 0.0, a test that expected a number like -1.23259516440783e-32  was clearly flawed. 

Positive review. 

Dave


---

Comment by mpatel created at 2010-08-02 21:41:34

Just to check and for the record:  Leif, does Dr. Cremona's patch fix the failure with your alpha0 (or alpha1) build and, if you have one available, a similarly built rc0?


---

Comment by mpatel created at 2010-08-04 02:17:26

I'm merging the patch into my working copy of 4.5.2.rc1.


---

Comment by mpatel created at 2010-08-04 02:18:04

Resolution: fixed
