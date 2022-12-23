# Issue 2567: remove limitation on computing digits of pi using mpfr

Issue created by migration from https://trac.sagemath.org/ticket/2567

Original creator: was

Original creation time: 2008-03-17 07:03:24

Assignee: somebody

CC:  zimmerma fbissey


```
> >  CODE:
>
> >  s = pi.str(3000000*log(10,2))
> >  o = open('/Users/ericahls/Desktop/file.txt','w')
> >  o.write(str(s))
> >  o.close()
>
> >  --- Trying to get out to the farthest decimal point of PI I can.
>
> >  Error message:
>
> >  Traceback (most recent call last):    o.write(str(s))
> >   File "/Applications/sage/local/lib/python2.5/site-packages/sage/
> >  functions/functions.py", line 140, in str
> >     raise ValueError, "Number of bits must be at most 2^23."
> >  ValueError: Number of bits must be at most 2^23.
>
> >  ----If i Put 2000000 instead 0f 3000000 the equation works.  much over
> >  2 million the equation breaks dwon.
>
> I think that 2^23 is a bound in mpfr, and Sage uses mpfr to
> compute digits of pi.  I don't know if one can compute more than
> about 2^23 digits using mpfr.
>
> William


Yes we can. The issue was that MPFR used the stack instead of the heap
for certain operations [even when told not to use alloca] and would
smash it therefore with large number of digits. That has been fixed in
MPFR 2.3.1 (which we include) and all we need to do is to raise or
remove the limit in our code and do some testing. Care to open a
ticket?

 -- Mabshoff
```



---

Comment by AlexGhitza created at 2008-12-28 15:50:30

As far as I can tell, there is still a limit, namely the maximum precision MPFR_PREC_MAX, which is 2^24 on my 32-bit machine.  

I guess this means that we can relax the current 2^23 limit a little bit.  However, the MPFR manual says: "Warning! MPFR needs to increase the precision internally, in order to provide accurate results (and in particular, correct rounding). Do not attempt to set the precision to any value near MPFR_PREC_MAX, otherwise MPFR will abort due to an assertion failure."


---

Comment by fredrik.johansson created at 2009-02-05 21:47:03

You could use the pi function in mpmath; as far as I know, it is limited only by available memory. I just verified that computing 100 million digits works on a 32-bit system. The last time someone compared, it was also about three times faster than MPFR (but probably less memory efficient).

Or you could perhaps use this code which is even faster: http://gmplib.org/pi-with-gmp.html


---

Comment by mabshoff created at 2009-02-05 21:59:18

The problem is not so much the computation of Pi itself, but that we limit the maximum amount of precision on can ask for when using MPFR. It seems the limit is good for 32 bits, but for 64 bits MPFR is also basically limited by memory only.

The solution to this ticket might be to import MPFR_PREC_MAX from mpfr.h or wherever it is defined and then the problem will magically go away.

Cheers,

Michael


---

Comment by zimmerma created at 2009-02-06 06:51:59

> The solution to this ticket might be to import MPFR_PREC_MAX from mpfr.h

right. It is defined there as 2<sup>31</sup>-1 on a 32-bit machine and 2<sup>63</sup>-1 on a 64-bit machine.


---

Comment by zimmerma created at 2009-02-06 07:47:55

> You could use the pi function in mpmath; as far as I know, it is limited only by available memory. I just verified that computing 100 million digits works on a 32-bit system. The last time someone compared, it was also about three times faster than MPFR (but probably less memory efficient).

I am curious. Can you give real timings? Here is what I get on sage.math:

```
zimmerma@sage:~/mpfr-2.4.0/tests$ pwd
/home/zimmerma/mpfr-2.4.0/tests
zimmerma@sage:~/mpfr-2.4.0/tests$ time ./tconst_pi 332192809 0 0

real    42m21.420s
user    41m55.500s
sys     0m25.910s
```

This is without using the new FFT code we designed with Gaudry and Kruppa, which should give a
twofold speedup. Anyway if mpmath can compute 100 million digits in less than 15 minutes, I am
really impressed!


---

Comment by fredrik.johansson created at 2009-02-06 09:55:16

In mpmath on an Athlon 3700+ 2.21 GHz, 1 GB RAM,

10**6 digits took 5.96 seconds (4.77 calc, 1.19 convert)

10**7 digits took 109.45 seconds (82.16 calc, 27.28 convert)

10**8 digits took 2184.68 seconds (1634.65 calc, 550.02 convert)

I can't compare with MPFR on the same computer at the moment, due to network problems. (With an old version of sage, 3.0.2, %time str(pi.n(10**6*log(10.,2))) takes 43.06 s, but I don't trust that number).

This is the result reported by Ondrej a few months ago:

```
E.g. in sympy+gmpy:

In [3]: time a = pi.evalf(10**6)
CPU times: user 5.13 s, sys: 0.04 s, total: 5.17 s
Wall time: 5.19 s

Sage 3.1.1:

sage: time a = pi.n(digits=10**6)
CPU times: user 14.06 s, sys: 0.06 s, total: 14.12 s
Wall time: 14.34 s 
```


> This is without using the new FFT code we designed with Gaudry and Kruppa, which should give a twofold speedup. Anyway if mpmath can compute 100 million digits in less than 15 minutes, I am really impressed!

Mpmath relies directly on multiplication of GMP mpz's. If it is faster than MPFR, that is entirely due to using a better formula. Before using the Chudnovsky series, mpmath used AGM which has better theoretical complexity but was 3x slower up to at least 1M digits.


---

Comment by mabshoff created at 2009-02-06 10:13:18

This discussion is very interesting, but it should not happen in trac, but on some mailing list since there people actually tend to see it. Trac's audience is rather limited and the comment section isn't meant for discussions :)

I have changed the ticket to reflect Paul's pointer about pulling in MPFR_PREC_MAX from mpfr.h

Cheers,

Michael


---

Comment by zimmerma created at 2009-02-06 10:18:49

> Mpmath relies directly on multiplication of GMP mpz's. If it is faster than MPFR, that is entirely due to using a better formula. Before using the Chudnovsky series, mpmath used AGM which has better theoretical complexity but was 3x slower up to at least 1M digits.

yes in a previous version MPFR did use the Chudnovsky series, but it only gives a fixed number of terms per iteration, whereas the current AGM-based code doubles the accuracy at each iteration, thus is asymptotically better. Also when the division in GMP is really O(M(n)) the current MPFR code should be much faster. However we should use the Chudnovsky series for small precision and the AGM for large precision.


---

Comment by zimmerma created at 2010-02-27 21:58:43

I guess this ticket is now obsolete.


---

Comment by mhansen created at 2010-03-04 04:44:50

I've attached a patch which removes our hard coded value.


---

Comment by mhansen created at 2010-03-04 04:44:50

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-03-05 19:20:24

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-03-05 19:20:24

> I've attached a patch which removes our hard coded value. 

Mike, I guess this has to be rebased due to #8157. Or #8157 should be undone since your patch is
better (in particular on 64-bit machines we should be able to compute with more that 2<sup>31</sup> bits).

Paul


---

Comment by mhansen created at 2010-03-05 20:01:58

Oops, I knew that I had seen that ticket in the title a few days ago, but wasn't able to find it again :-)  I'll rebase this one.

The warning in the comment seems not to apply now.


---

Comment by zimmerma created at 2010-03-05 20:24:14

Mike,

> The warning in the comment seems not to apply now. 

which warning do you mean?


---

Comment by mhansen created at 2010-03-05 20:27:11

Sorry, I knew after posting that I should have been more specific.  There's a comment in the source code that said that things totally break if we use the value from mpfr.h.


---

Comment by mhansen created at 2010-07-11 00:04:36

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-07-11 00:04:36

I've rebased this and posted a new patch.  This needs to be tested on a 32-bit machine.


---

Comment by zimmerma created at 2010-07-11 16:35:06

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-07-11 16:35:06

while trying to review that ticket, I get with the input in the description:

```
sage: s = pi.str(3000000*log(10,2))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/localdisk/tmp/sage-4.4.4/<ipython console> in <module>()

/localdisk/tmp/sage-4.4.4/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)()

/localdisk/tmp/sage-4.4.4/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)()

/localdisk/tmp/sage-4.4.4/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2602)()

AttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'str'
```

Is that normal?

Paul


---

Comment by mhansen created at 2010-07-11 17:47:48

Did you mean


```
sage: s = pi.n(digits=3000000*log(10,2))
```

?

Expression objects don't have a `str` method.


---

Comment by zimmerma created at 2010-07-11 18:13:52

Replying to [comment:17 mhansen]:
> Did you mean
> 
> {{{
> sage: s = pi.n(digits=3000000*log(10,2))
> }}}
> ?

no, I just copy-pasted the example in the description above.

Paul


---

Comment by mhansen created at 2010-07-18 03:42:27

I'm not sure what pi was defined to be in that example, and I was unable to find it in the logs.  I could try tracking down an old Sage install to possibly find out.


---

Comment by zimmerma created at 2010-07-18 08:03:35

Replying to [comment:19 mhansen]:
> I'm not sure what pi was defined to be in that example, and I was unable to find it in the logs.  I could try tracking down an old Sage install to possibly find out.

maybe William remembers, since he reported that ticket.

Paul


---

Comment by mhansen created at 2011-12-17 19:43:33

I think this can / should still go in.


---

Comment by mhansen created at 2011-12-17 19:43:33

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2011-12-18 15:39:11

Mike, why do you import sys at line 186? Also, please could you add a short test on 64-bit
computers? For example:

```
sage: R = RealField(2^31)
sage: RR(R(2.0)) == RR(2.0)
True
```

Paul


---

Comment by zimmerma created at 2011-12-18 15:39:11

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2011-12-18 15:52:57

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2011-12-18 15:52:57

I put up a new patch addressing your changes.


---

Comment by zimmerma created at 2011-12-18 19:13:01

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2011-12-18 19:13:01

Mike, there is a test that fails:

```
[zimmerma@coing sage]$ sage -t  devel/sage-2567/sage/misc/explain_pickle.py
sage -t  "devel/sage-2567/sage/misc/explain_pickle.py"      
**********************************************************************
File "/usr/local/sage-4.7.2/sage/devel/sage-2567/sage/misc/explain_pickle.py", line 210:
    sage: explain_pickle(dumps(RR(pi)), in_current_sage=True)
Expected:
    from sage.rings.real_mpfr import __create__RealNumber_version0
    from sage.rings.real_mpfr import __create__RealField_version0
    __create__RealNumber_version0(__create__RealField_version0(53r, False, 'RNDN'), '3.4gvml245kc0@0', 32r)
Got:
    from sage.rings.real_mpfr import __create__RealNumber_version0
    from sage.rings.real_mpfr import __create__RealField_version0
    __create__RealNumber_version0(__create__RealField_version0(long(53), False, 'RNDN'), '3.4gvml245kc0@0', 32r)
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_1
```

Please could you have a look?

Paul


---

Comment by mhansen created at 2011-12-19 10:05:04

I put up a patch fixing that doctest.


---

Comment by mhansen created at 2011-12-19 10:05:04

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2011-12-19 18:11:19

all tests pass on a 64-bit computer. However I still have to check on a 32-bit computer.

Paul


---

Comment by zimmerma created at 2011-12-20 08:47:53

one item fails on a 32-bit machine (with Sage 4.7.2):

```
sage -t  "devel/sage/sage/rings/real_mpfr.pyx"              
**********************************************************************
File "/localdisk/tmp/sage-4.7.2/devel/sage/sage/rings/real_mpfr.pyx", line 196:
    sage: R = RealField(2^31); R
Expected:
    Traceback (most recent call last):                     
    ...                                                    
    OverflowError: ... too large to convert to int         
Got:
    Traceback (most recent call last):
      File "/localdisk/tmp/sage-4.7.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/localdisk/tmp/sage-4.7.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/localdisk/tmp/sage-4.7.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        R = RealField(Integer(2)**Integer(31)); R###line 196:
    sage: R = RealField(2^31); R
      File "real_mpfr.pyx", line 280, in sage.rings.real_mpfr.RealField (sage/rings/real_mpfr.c:3802)
      File "real_mpfr.pyx", line 299, in sage.rings.real_mpfr.RealField_class.__init__ (sage/rings/real_mpfr.c:4025)
    ValueError: prec (=2147483648) must be >= 2 and <= 2147483647.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /users/caramel/zimmerma/.sage//tmp/real_mpfr_5754.py
         [14.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/real_mpfr.pyx"
```

Paul


---

Comment by zimmerma created at 2011-12-20 08:47:53

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2011-12-24 12:15:04

Mike, please can you fix the error message on 32-bit?

Paul


---

Attachment


---

Comment by mhansen created at 2012-03-28 20:56:33

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2012-03-28 20:56:33

I fixed the error message.


---

Comment by davidloeffler created at 2012-03-29 17:39:09

The patch does not apply to 5.0.beta11 -- see patchbot logs. (I guess the cause is #11666.)


---

Comment by davidloeffler created at 2012-03-29 17:39:16

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2012-08-01 06:39:52

Paul, does MPFR_PREC_MAX now reflect the `2^31 - 257` limit in 3.1.0?  For 64-bit, it seems to be set at `2^63`.


---

Comment by zimmerma created at 2012-08-01 07:22:25

in 3.1.x MPFR_PREC_MAX is 2<sup>63</sup>-1 on 64-bit computers. In the development version of MPFR it is set to 2<sup>31</sup>-257 in 32-bit and 2<sup>63</sup>-257 in 64-bit mode.

Paul


---

Comment by zimmerma created at 2013-01-07 08:43:50

any progress on this ticket?

Paul


---

Comment by chapoton created at 2020-12-26 18:03:30

New commits:


---

Comment by chapoton created at 2020-12-26 18:03:30

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2020-12-26 20:37:32

Well, I made a branch and this seems to work. Anybody interested ?


---

Comment by fbissey created at 2020-12-27 20:22:28

Well, it looks good to me. I cannot see clear objections in the earlier ticket comments so let's see what happens when we include it for real.

The author field may need updating though.


---

Comment by chapoton created at 2020-12-27 20:44:43

voilà, voilà.


---

Comment by fbissey created at 2020-12-27 20:46:53

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2020-12-27 20:46:53

Comme une lettre à la poste :)


---

Comment by vbraun created at 2020-12-28 23:34:29

Resolution: fixed
