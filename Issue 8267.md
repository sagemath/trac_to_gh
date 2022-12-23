# Issue 8267: cygwin: ratpoints is broken again

Issue created by migration from https://trac.sagemath.org/ticket/8267

Original creator: was

Original creation time: 2010-02-15 00:09:00

Assignee: tbd

I just tried building the ratpoints package on Cygwin, and 

```
gcc main.c -o ratpoints -I/home/wstein/build/sage-4.3.3.alpha0/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -DUSE_SSE -L/home/wstein/build/sage-4.3.3.alpha0/local/lib -lgmp -lm -L. -lratpoints                                     
main.c:1: warning: -fPIC ignored for target (all code is position independent)                                             
./libratpoints.a(find_points.o):find_points.c:(.text+0x170): undefined reference to `__imp____gmpz_mul_si' 
BOOM!
```


Thus the fixed that got in from #7015 has been broken before it ever really got to live :-(. 

So this ticket is to implement that fix again. 


---

Comment by was created at 2010-02-15 00:22:00

Changing status from new to needs_review.


---

Comment by was created at 2010-02-15 00:22:00

Please review this:

   http://sage.math.washington.edu/home/wstein/ports/cygwin/ratpoints-2.1.3.p1.spkg


---

Comment by mvngu created at 2010-02-15 05:51:12

Here are a few changes to William's spkg:

 * I renamed it to `ratpoints-2.1.3.p0`, which is the patch level that comes after `ratpoints-2.1.3`.
 * Turned on the executable bits of `spkg-install`.
 * Separate the changelog for `ratpoints-2.1.3.p0` and `ratpoints-2.1.3`. The changelog now reads:
 {{{
### ratpoints-2.1.3.p0 (William Stein, 14 Feb 2010)
 * Include change to spkg-install so that build works on Cygwin,
   a fix that was in (trac #7015), and somehow got list.  See
   trac #8267.

### ratpoints-2.1.3 (William Stein, 14 Feb 2010)
 * Evidently somebody updated ratpoints to 2.1.3 and didn't
   update the SPKG.txt.  Oops.
 }}}

An updated spkg with the above changes is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/ratpoint/ratpoints-2.1.3.p0.spkg


---

Comment by mvngu created at 2010-02-16 05:06:44

The package [ratpoints-2.1.3.p0.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/ratpoint/ratpoints-2.1.3.p0.spkg) includes some cosmetic changes on top of William's spkg. Building ratpoints-2.1.3.p0.spkg went OK on Cygwin (winxp1 on boxen.math).


---

Comment by mvngu created at 2010-02-16 05:06:44

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-16 05:08:08

Resolution: fixed


---

Comment by mvngu created at 2010-02-16 05:08:08

Merged in the standard spkg repository.
