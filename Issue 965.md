# Issue 965: incorporate drew sutherland's smalljac into Sage

Issue created by migration from https://trac.sagemath.org/ticket/965

Original creator: was

Original creation time: 2007-10-21 20:34:08

Assignee: was

CC:  jen

The code is attached to this ticket and is GPL'd now. 

Actually, the code is here:
   http://sage.math.washington.edu/tmp/smalljac.tar.bz2


---

Comment by was created at 2007-10-21 20:35:44


```
Hi William,

I have modified the smalljac program so that it can work with 64-bit field
coefficients to enable larger computations. This is slightly slower than
the 32-bit version, but only by 10 or 20 percent. The code is available on
sage.math in /home/drew/smalljac and is licensed under GPL (version 2 or
later).

In the example below, each row lists deltas between the first 5 moments of
the actual distribution of a1 for p up to the specified bound, and the
theoretical values, which are: 1 0 2 0 5. This can be easily modified to
support whatever statistics you want - the file to be changed is
smalljac_stats.c. Tom Booth should know what he needs to do this.

Roughly speaking, on my 8 node (16 core) cluster the timings are

   p <= 10^6   <2 secs
   p <= 10^7    4 secs
   p <= 10^8   20 secs
   p <= 10^9  3-4 mins
   p <= 10^10  45 mins

The transcript below goes up to 2^36, which took about 7 hours.
Of course, YMMV.

Drew

Rank 14, torsion group Z/2Z  Fermigier 1997

drew@penguin1:~/dev/net$ ./smalljacclient 1 2e36
[0,1,0,-1692310759026568999140789578145,839379398840982294584587970773038145228669599]
zeta 11 0 penguins.cfg Skipping 2 primes below 4 20 bad primes in remaining
interval: 7 23 43 61 79 103 157 167 179 191 199 227 229 257 271 307 487 619
1283 3739 listening on port 50100 16 servers loaded from penguins.cfg 2^10:
+0.701748 +0.224807 +1.511885 +0.802241 +4.033526 0.0 secs 2^11: +0.460192
+0.097375 +0.913882 +0.315814 +2.311088 0.0 secs 2^12: +0.351208 +0.130256
+0.683686 +0.388719 +1.720796 0.0 secs 2^13: +0.259257 +0.091129 +0.506374
+0.263650 +1.250202 0.0 secs 2^14: +0.186329 +0.080927 +0.358597 +0.228978
+0.866592 0.1 secs 2^15: +0.146251 +0.051710 +0.289137 +0.140110 +0.705587
0.1 secs 2^16: +0.097092 +0.037386 +0.204797 +0.107219 +0.527321 0.2 secs
2^17: +0.079035 +0.022411 +0.156440 +0.066359 +0.398332 0.4 secs 2^18:
+0.059734 +0.009358 +0.131100 +0.026234 +0.348324 0.7 secs 2^19: +0.040360
+0.003497 +0.090564 +0.009052 +0.241141 1.5 secs 2^20: +0.028682 +0.000948
+0.059805 +0.005800 +0.150596 1.8 secs 2^21: +0.020557 +0.001069 +0.041813
+0.004954 +0.105266 3.5 secs 2^22: +0.014209 +0.000278 +0.029935 +0.001816
+0.075829 3.7 secs 2^23: +0.011182 +0.000005 +0.025632 +0.000250 +0.067925
3.8 secs 2^24: +0.007879 -0.000072 +0.017972 -0.000091 +0.048165 4.5 secs
2^25: +0.005137 -0.001018 +0.011046 -0.003078 +0.028931 7.3 secs 2^26:
+0.003562 -0.000810 +0.007789 -0.002474 +0.020682 13.1 secs 2^27: +0.002519
-0.000491 +0.005048 -0.001666 +0.012677 25.1 secs 2^28: +0.001929 -0.000541
+0.004039 -0.001785 +0.010231 50.6 secs 2^29: +0.001291 -0.000470 +0.002732
-0.001611 +0.007064 105.6 secs 2^30: +0.000959 -0.000286 +0.002165
-0.001041 +0.005812 221.1 secs 2^31: +0.000558 -0.000208 +0.001346
-0.000688 +0.003678 468.1 secs 2^32: +0.000487 -0.000121 +0.001128
-0.000383 +0.003115 1002.5 secs 2^33: +0.000323 -0.000052 +0.000772
-0.000099 +0.002138 2374.6 secs 2^34: +0.000223 -0.000057 +0.000528
-0.000163 +0.001533 5342.0 secs 2^35: +0.000153 -0.000046 +0.000337
-0.000138 +0.000963 11790.2 secs 2^36: +0.000086 +0.000009 +0.000194
+0.000006 +0.000561 25897.0 secs

Final Moment Values
a1:    +0.0001    +1.0000    +0.0002    +2.0000    +0.0006    +5.0000

Count = 2874398493 Errors = 0 Skipped = 2 Bad = 20 Total for interval
[1,68719476736) = 2874398515 2874398493 curves 0.144 msecs/curve 646
gops/curve 4488398 gops/cpu-sec CPU time: 414038.970 secs, Wall time:
25897.014 secs
```



---

Comment by was created at 2007-11-16 21:13:09

From Drew:


```

A single-threaded smalljac module based on the design previously discussed
is now available on sage.math.washington.edu:/drew/newsmalljac. For genus 1
curves, it should be in a reasonably stable state and ready for general
use. I am still working on integrating genus 2 and 3.

I have added support for the primes we all love to hate (2 and 3), and I
have increased the allowed range up to 2^63. Obviously one is unlikely to
use the interval [1,2^63], but you might want to look at specific values or
small subintervals well up into this range. I have included a demo program
which simply sums all the a_p values for a specified curve and range that
may be useful as a model and for testing.

This assumes the parameter SMALLJAC_FF_64BITS is set to 1 in smalljac.h,
which it is by default. Setting it to 0 will lower the limit to 2^31 but
speed things up by 5-10%. As it is, the demo program runs about 4-6 times
faster than sum(EllipticCurve([...]).aplist(...)) in SAGE.

I have also modified the program to not attempt to factor scary
discriminants, so it now can handle curves with arbitrarily large
conductors, including Elkies rank 28 curve (its actually quite interesting
to look at the partial sums of the a_p values for this curve with the demo
program - they seem noticeably biased toward increasingly negative values).

I made one change to the interface, adding a function for parsing and
initializing the curve into a dynamically allocated data structure which is
then passed into smalljac_Lpolys(). This is significantly more efficient if
the same curve is used repeatedly (e.g. if you want to jump around using
different intervals). If desired, these could of course be wrapped up into
a single call, but it seemed to make more sense to break them out.

The new interface is:

smalljac_Qcurve_t smalljac_Qcurve_init (char *str, int *err);

long smalljac_Lpolys (smalljac_Qcurve_t c,
                     unsigned long start,
                     unsigned long end,
                     unsigned long flags,
                     int (*callback)(smalljac_Qcurve_t c,
                                     unsigned long p,
                                     int good,
                                     long a[],
                                     int n,
                                     void *arg),
                    void *arg);

void smalljac_Qcurve_clear (smalljac_Qcurve_t c);

The smalljac_Qcurve_t datatype is simply a (void*). See smalljac.h for more
details. The new function smalljac_Lpoly() doesn't use the smalljac_Qcurve
data type, it takes a string specification.

I have also made an effort to clean up the code a bit, removing a fair
amount of cruft, and adding some comments.

The file readme.txt contains a list of all the modules and other relevant
information. Please let me know how it works!

Drew
```


ALSO


```
In addition to the demo program, I also included a utility called lpoly
which calls the function smalljac_Lpoly() to compute the L-polynomial of a
curve over a single specified finite field. In deference to Kiran :), it
supports non-prime fields (the curve must be defined over Q, but I plan to
add support for curves defined over F_q). The function smalljac_Lpoly()
does not use the new smalljac_Qcurve datatype, but just takes a string
specification for the curve.

Drew


```



---

Comment by boothby created at 2007-11-21 08:54:14

a preliminary package


---

Attachment


---

Attachment

Here's a patch and a new (very preliminary!) spkg.  It builds for me on sage.math but won't work most other places, since Drew's code assumes a 64-bit `unsigned long`.


---

Comment by ncalexan created at 2009-07-09 03:20:38

Changing keywords from "" to "drew sutherland smalljac point counting hyperelliptic curve genus 2 jacobian".


---

Attachment


---

Comment by kedlaya created at 2016-03-21 16:00:21

Given that Drew is no longer supporting smalljac on 32-bit architectures, is this still feasible? Maybe only as an optional spkg?


---

Comment by was created at 2016-03-21 16:21:36

Drew never supported smalljac on 32-bits -- as the docs of his package say "life is too short for 32-bits".

The right way to do this is to support only 64-bit and have an error message on 32-bit.  We might have to add something to the doctest framework to support such differences in behavior, e.g., # optional - 64-bit.

Incidentally, I also wrote a smalljac wrapper as part of psage, which is probably way more sophisticated.  It recompiles smalljac multiple times, one for each genus...


---

Comment by was created at 2016-03-21 16:22:20

As to the value of this, I think in psage smalljac is no longer built, which a student of Koblitz -- Travis Scholl -- was complaining to me about just two weeks ago.


---

Comment by kedlaya created at 2016-04-05 18:20:15

Replying to [comment:11 was]:
> Drew never supported smalljac on 32-bits -- as the docs of his package say "life is too short for 32-bits".
> 
> The right way to do this is to support only 64-bit and have an error message on 32-bit.  We might have to add something to the doctest framework to support such differences in behavior, e.g., # optional - 64-bit.
> 
How is this handled in the build framework?

> Incidentally, I also wrote a smalljac wrapper as part of psage, which is probably way more sophisticated.  It recompiles smalljac multiple times, one for each genus...
> 

I'd say that's overkill for present purposes.

Also, to clarify the workflow here, I'm assuming that this will ticket be closed once there exists _some_ way to call smalljac within Sage, however user-unfriendly (i.e., get it to build and write a minimal wrapper). Making it useful, by adding appropriate class methods to elliptic and hyperelliptic curves, should be a separate ticket.


---

Comment by was created at 2016-04-05 18:24:23

> How is this handled in the build framework?

I would make a completely separate python package, maybe called pysmalljac, which builds smalljac and makes it usable from Python.  It would be on github and pypi.  That's how most Sage development should be done.  What a monster I've created by following the Magma way of doing things instead of the standard open source best practices...

> I'd say that's overkill for present purposes.

When you build it you choose the one genus for which you build it.  Is it overkill to have it work for more than just genus one??


---

Comment by kedlaya created at 2016-04-05 18:32:17

Replying to [comment:14 was]:
> > How is this handled in the build framework?
> 
> I would make a completely separate python package, maybe called pysmalljac, which builds smalljac and makes it usable from Python.  It would be on github and pypi.  That's how most Sage development should be done.  What a monster I've created by following the Magma way of doing things instead of the standard open source best practices...
> 
+1

> > I'd say that's overkill for present purposes.
> 
> When you build it you choose the one genus for which you build it.  Is it overkill to have it work for more than just genus one??

Fair enough, one also wants genera two and three. I'm not sure smalljac is recommended for use for genus >= 4.


---

Comment by kedlaya created at 2016-04-06 00:38:35

Replying to [comment:15 kedlaya]:
> Replying to [comment:14 was]:
> > > How is this handled in the build framework?
> > 
> > I would make a completely separate python package, maybe called pysmalljac, which builds smalljac and makes it usable from Python.  It would be on github and pypi.  That's how most Sage development should be done.  What a monster I've created by following the Magma way of doing things instead of the standard open source best practices...
> > 
> +1
> 
> > > I'd say that's overkill for present purposes.
> > 
> > When you build it you choose the one genus for which you build it.  Is it overkill to have it work for more than just genus one??
> 
> Fair enough, one also wants genera two and three. I'm not sure smalljac is recommended for use for genus >= 4.

In fact, Drew reminds me that smalljac currently doesn't even support genus 3; however, this should be added in the near future (i.e., sometime this year).

Kiran


---

Comment by kedlaya created at 2016-04-09 21:47:54

Drew reminds me that this is addressed on ticket #13376, so maybe further discussion should happen there.
