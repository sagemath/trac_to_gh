# Issue 4446: [with patch, needs work] New module complex_mpc using lib mpc for complex multiprecision arithmetic

Issue created by migration from Trac.

Original creator: thevenyp

Original creation time: 2008-11-05 18:04:29

Assignee: mabshoff

CC:  robertwb was mhansen mvngu schilly leif

Herewith and there ([http://www.loria.fr/~thevenyp/complex_mpc.patch](http://www.loria.fr/~thevenyp/complex_mpc.patch) 38K) is a patch with new classes using the MPC library for complex multi-precision arithmetic (see ticket #4308 for the associated spackage).

This is an adaptation of the module real_mpfr and of ComplexField and [ComplexNumber](ComplexNumber) classes. It adds a class MPComplexField with precision (common to both part) and rounding modes (specific to each part) and a class MPComplexNumber.

This first attempt implements only the complex arithmetic.

The test suite does fail due to coercion problems I can't solve.


---

Attachment


---

Attachment

replace the previous patch (rebase against 3.2)


---

Comment by AlexGhitza created at 2008-11-22 08:30:15

There seems to have been some bitrot due to recent changes in Sage.  I have uploaded a very slightly modified version of Philippe's patch, which applies cleanly against 3.2.  A number of doctests fail for various reasons.  I will try to look into this soon.


---

Attachment

coercion problems resolved, more functions


---

Comment by thevenyp created at 2008-12-04 18:04:58

The coercion problems have been solved, all doctests now succeed in new version. The whole set of mpc functions involving complex numbers is now in the interface.


---

Comment by AlexGhitza created at 2008-12-05 07:50:30

apply after complex_mpc.p0.patch


---

Attachment

Philippe,

Great work!  I'll do my best to review this for 3.2.2.  Right now I notice that the patch doesn't work in 3.2.1 because of #4580.  I'm attaching a tiny patch that fixes that (should be applied after complex_mpc.p0.patch.


---

Comment by AlexGhitza created at 2008-12-06 08:58:45

There are a few small issues that I ran into, but since this is going to be (for now) an optional part of Sage and nothing depends on it, I think we can fix these later (I'm keeping a list of them so they don't get lost).

However, there is a policy of 100% doctest for all new code.  The coverage is now:


```
[ghitza`@`artin sage]$ sage -coverage rings/complex_mpc.pyx
----------------------------------------------------------------------
rings/complex_mpc.pyx
SCORE rings/complex_mpc.pyx: 68% (46 of 67)

Missing documentation:
	 * _repr_ (self):
	 * _latex_(self):
	 * _an_element_(self):
	 * random_element(self, bound):
	 * __hash__(self):
	 * prec(self):
	 * _set(self, z, y=None, base=10):
	 * _repr_(self):
	 * _latex_(self):
	 * ModuleElement _add_(self, ModuleElement right):
	 * ModuleElement _sub_(self, ModuleElement right):
	 * RingElement _mul_(self, RingElement right):
	 * RingElement _div_(self, RingElement right):
	 * ModuleElement _neg_(self):
	 * __create__MPComplexField_version0 (prec, rnd):
	 * __create_MPComplexNumber_version0 (parent, s, base=10):


Missing doctests:
	 * _rnd(self):
	 * _rnd_re(self):
	 * _rnd_im(self):
	 * _real_field(self):
	 * _imag_field(self):


Possibly wrong (function name doesn't occur in doctests):
	 * _element_constructor_(self, z):
	 * _coerce_map_from_(self, S):
	 * bint is_exact(self) except -2: return False def is_finite(self):
	 * Element _call_(self, z):
	 * Element _call_(self, x):

----------------------------------------------------------------------
```


So the missing docstrings and doctests will have to be added before this patch can be merged.  I would happily do this but the earliest I can get to it is Thursday or so (and that's being optimistic).

To end on a positive note: this looks good.  It will take a bit more work, but if we can show that (a) the performance is improved, or doesn't suffer too much, and (b) the switch can be made seamlessly, then it will be easy to convince people that we should switch the core of our complex numbers functionality over to MPC.


---

Comment by AlexGhitza created at 2008-12-11 05:04:40

apply after complex_mpc.p0.patch and trac4446_fix.patch


---

Attachment

I added a patch trac4446_doctests.patch, which does a number of things:

 * adds doctests for all functions except three internal use only functions
 * changes _repr_ of complex numbers so that it agrees with the way complex numbers are currently printed in Sage
 * makes MPComplexField inherit from ParentWithGens, being generated over its real field by the square root of -1 (just as it is now); this required adding a few functions.  So now one can do


```
sage: from sage.rings.complex_mpc import MPComplexField
sage: MPC.<j> = MPComplexField()
sage: j^2
-1.00000000000000 + 0.000000000000000*I
```


Note that only the last three patches should be applied, in order: complex_mpc.p0.patch, trac4446_fix.patch, and trac4446_doctests.patch


---

Attachment


---

Comment by thevenyp created at 2008-12-18 12:57:44

One more patch trac4446_norm.patch with:

* Alex Ghitza listed in authors list and copyright notice

* complex_mpc uses a copy of mpfr rounding mode list instead of its private one

* the __abs__ and norm documentation has been improved.


---

Comment by was created at 2009-01-24 11:57:45

REFEREE REPORT:

1. How can this be optional? If the patch is applied then this is included:

```
 	625	    Extension('sage.rings.complex_mpc', 
 	626	              sources = ['sage/rings/complex_mpc.pyx'], 
 	627	              libraries = ['mpc', 'mpfr', 'gmp']), \ 
 	628	
```

So the only way I can see this going in like this is if it is standard.  Am I missing something (probably)?

2. Timings on Xeon 2.6Ghz (sage.math).   Multiplication is faster with mpc, but addition is significantly *slower*:

```
sage: K = MPComplexField(53)
sage: a = K(3.3902384)
sage: b = CC(3.3902384)

sage: timeit('a*a')
625 loops, best of 3: 376 ns per loop
sage: timeit('b*b')
625 loops, best of 3: 466 ns per loop

sage: timeit('a+a')
625 loops, best of 3: 368 ns per loop
sage: timeit('b+b')
625 loops, best of 3: 304 ns per loop

```


3. Powering doesn't work for mpc but it does for the current CC:

```
sage: a**a 
boom
```


4. Default rounding on coercion (or something?!) is different between MPC and CC:

```
sage: MPComplexField(100)(3.3902384)
3.3902383999999998742680418218 + 0.00000000000000000000000000000*I
sage: ComplexField(100)(3.3902384)
3.3902384000000000000000000000
```


5. With higher precision and nontrivial imaginary part, the timings are *all* in favor of the existing ComplexField already in Sage:

```
sage: K = MPComplexField(1000)
sage: a = K(3.3902384,9203483)
sage: b = ComplexField(1000)(3.3902384,9203483)
sage: a
3.39023839999999987426804182177875190973281860351562500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + 9.20348300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e6*I
sage: b
3.39023840000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + 9.20348300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e6*I
sage: timeit('a*a')
625 loops, best of 3: 2.27 µs per loop
sage: timeit('b*b')
625 loops, best of 3: 2.2 µs per loop
sage: timeit('a+a')
625 loops, best of 3: 515 ns per loop
sage: timeit('b+b')
625 loops, best of 3: 445 ns per loop
sage: timeit('a.sin()')
^P625 loops, best of 3: 221 µs per loop
sage: timeit('b.sin()')
625 loops, best of 3: 130 µs per loop
```


Thus until the above issues are addressed, I see no point in mpc going into sage.


---

Attachment


---

Attachment


---

Attachment


---

Comment by zimmerma created at 2009-08-26 12:35:55

Philippe Theveny, who had a 2-year contract with us, just left, thus he won't be able to continue working on this. In case somebody wants to pursue his work,
he has left the attached files. You need mpc-0.6 available at http://www.loria.fr/~thevenyp/mpc-0.6.spkg. According to Philippe, the performance was improved,
but still not as good as the current CC (but more reliable due to correct rounding).


---

Attachment


---

Comment by ylchapuy created at 2009-12-22 16:00:13

With the updated patch, and the corresponding spkg available at http://yann.laiglechapuy.net/spkg/mpc-0.8.1.p0.spkg
almost every methods for ComplexNumbers are defined for MPComplexNumbers to.

The performance is quite good:
with a precision of 500bits,


```
==========
add
ComplexField: a+b 40000 loops, best of 5: 700 ns per loop
MPComplexField: m+n 40000 loops, best of 5: 755 ns per loop
==========
add int
ComplexField: a+17 40000 loops, best of 5: 2.75 µs per loop
MPComplexField: m+17 40000 loops, best of 5: 2.43 µs per loop
==========
mul
ComplexField: a*b 40000 loops, best of 5: 2.66 µs per loop
MPComplexField: m*n 40000 loops, best of 5: 2.68 µs per loop
==========
div
ComplexField: a/b 40000 loops, best of 5: 5.76 µs per loop
MPComplexField: m/n 40000 loops, best of 5: 10.7 µs per loop
==========
real
ComplexField: a.real() 40000 loops, best of 5: 1.7 µs per loop
MPComplexField: m.real() 40000 loops, best of 5: 764 ns per loop
==========
conj
ComplexField: a.conjugate() 40000 loops, best of 5: 756 ns per loop
MPComplexField: m.conjugate() 40000 loops, best of 5: 633 ns per loop
==========
arg
ComplexField: a.argument() 2000 loops, best of 5: 104 µs per loop
MPComplexField: m.argument() 2000 loops, best of 5: 102 µs per loop
==========
cos
ComplexField: a.cos() 2000 loops, best of 5: 57.2 µs per loop
MPComplexField: m.cos() 2000 loops, best of 5: 86.4 µs per loop
==========
pow
ComplexField: a**b 2000 loops, best of 5: 240 µs per loop
MPComplexField: m**n 2000 loops, best of 5: 515 µs per loop
==========
pow int
ComplexField: a**12345 2000 loops, best of 5: 55.1 µs per loop
MPComplexField: m**12345 2000 loops, best of 5: 549 µs per loop
==========
log
ComplexField: a.log() 4000 loops, best of 5: 177 µs per loop
MPComplexField: m.log() 4000 loops, best of 5: 153 µs per loop
==========
exp
ComplexField: a.exp() 10000 loops, best of 5: 53.7 µs per loop
MPComplexField: m.exp() 10000 loops, best of 5: 57.5 µs per loop
```


The only big slow down is for `pow`.

It also allows to compute various trigonometric functions without convertion to pari.


---

Comment by ylchapuy created at 2009-12-22 16:01:25

Erratum: The only big slow down are for `pow` and `div`


---

Comment by ylchapuy created at 2010-01-09 12:53:21

apply after mpc-0.8.1.patch


---

Attachment

I put it as needs review to know what has eventually to be done.


---

Comment by ylchapuy created at 2010-02-08 11:33:58

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2010-02-08 11:51:38

Changing component from optional packages to basic arithmetic.


---

Comment by drkirkby created at 2010-02-21 23:56:05

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-02-21 23:56:05

Has this been checked on Solaris? There have been issues with complex maths recently on Solaris, which were solved, but this would need testing. 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by enge created at 2010-03-10 13:25:35

The poor performance of "pow int" is due to the fact that binary exponentiation is not currently implemented in mpc; "pow int" just calls "pow", and is present as a convenience function. Binary exponentiation is on the todo list.

Except for special cases, "pow" uses log and exp, so the timing should essentially be the sum for these two functions. Is it possible that you hit a corner case with your experiments, or are the timings consistent over several arguments?

Similarly, what are the arguments for division?

Concerning solaris, mpc itself builds without problems, see
   http://www.multiprecision.org/index.php?prog=mpc&page=platforms


---

Comment by zimmerma created at 2010-03-10 13:34:25

> Except for special cases, "pow" uses log and exp, so the timing should essentially be the sum for these two functions. Is it possible that you hit a corner case with your experiments, or are the timings consistent over several arguments?

then we should get about 210us for powint instead of 549us. Indeed, it would be good to know the
exact arguments, so that we can try to reproduce with vanilla MPC (maybe the problem is in the
interface between Sage and MPC).

For division, GMP 5 has a much faster division, which might benefit to MPC too. But again, we
could investigate more with a vanilla MPC, if we know the exact inputs used (with
exact_rational).


---

Attachment


---

Comment by ylchapuy created at 2010-03-10 14:51:53

First, I added a small patch to rebase this on sage 4.3.3.

One need to apply:

 * mpc-0.8.1.patch
 * bug_literal.patch
 * trac4446-rebase_sage4.3.3.patch

in this order; and of course install the spkg:

 * http://yann.laiglechapuy.net/spkg/mpc-0.8.1.p0.spkg

Then, here is an example with the exact input (I only put the last part concerning `pow`)

```
a.real().exact_rational()
-1558022726154386835635734102276225872461248356241845468520145243680772756232147166398716395960573602794592840676040928991781722240298082039889553874139/1636695303948070935006594848413799576108321023021532394741645684048066898202337277441635046162952078575443342063780035504608628272942696526664263794688
a.imag().exact_rational()
38743143824869548998159480051850490241205026500878413377278464034858416981434423320408166976481329585622042476431430168493334123089110626626927265425/102293456496754433437912178025862473506770063938845774671352855253004181137646079840102190385184504910965208878986252219038039267058918532916516487168
------------------------
a.log()
CC 5000 loops, best of 3: 170 µs per loop
MPC 5000 loops, best of 3: 143 µs per loop
------------------------
a.exp()
CC 5000 loops, best of 3: 45.6 µs per loop
MPC 5000 loops, best of 3: 49.1 µs per loop
------------------------
a**12345
CC 5000 loops, best of 3: 48.7 µs per loop
MPC 5000 loops, best of 3: 501 µs per loop
```



---

Comment by ylchapuy created at 2010-03-10 14:58:38

and for `div` (same value for `a`)

```
b.real().exact_rational()
-1335661139895223805455191750131391965080983427340135233479028132544481051566385358748782698880424407717119644643310969153530607585226701160632690491359/1636695303948070935006594848413799576108321023021532394741645684048066898202337277441635046162952078575443342063780035504608628272942696526664263794688
b.imag().exact_rational()
-191023642554886415830676606502854964270751830339806573746974716999454958912475563080101457087388705931975286670167330679505998875813037449880206143447/409173825987017733751648712103449894027080255755383098685411421012016724550584319360408761540738019643860835515945008876152157068235674131666065948672
------------------------
a/b
CC 100000 loops, best of 3: 4.84 µs per loop
MPC 100000 loops, best of 3: 9.57 µs per loop
```



---

Comment by zimmerma created at 2010-03-10 15:28:53

with the attached MPC program I get on a 2.83Ghz Core 2 under Fedora Core 2, with GMP 5.0.1 and
MPFR 2.4.2

```
tarte% ./sage
mpc_log took 74us per loop
mpc_exp took 24us per loop
mpc_pow(12345) took 260us per loop
mpc_div took 3.4us per loop
```

and within Sage with ComplexField I get (where I took the best of 3 %timeit runs):

```
sage: %timeit c=a.log()
625 loops, best of 3: 173 µs per loop
sage: %timeit c=a.exp()
625 loops, best of 3: 37.1 µs per loop
sage: %timeit c=a**12345
625 loops, best of 3: 26.6 µs per loop
sage: %timeit c=a/b
625 loops, best of 3: 2.71 µs per loop
```

thus we indeed need to work on powint, but the division is only 25% slower.

While doing this test I also noticed this strange thing with ComplexField:

```
sage: smallb = CC(b)
sage: %timeit c=a/b
625 loops, best of 3: 2.69 µs per loop
sage: %timeit c=a/smallb
625 loops, best of 3: 290 µs per loop
```

thus dividing by a 53-bit complex is 100 times slower than dividing by a 500-bit complex!
Should I open a separate ticket for that?

Did somebody check the 500-bit outputs of CC and MPC agree?


---

Attachment


---

Comment by zimmerma created at 2010-03-10 16:03:34

By studying what happens with the powint example, there was a failure in Ziv's strategy, thus we
did compute two approximations, one with precision 511 bits (which was not enough), and one with
a larger precision. By adding one more guard bit, the first approximation with 512 bits is enough
to get correct rounding, and we now get 131us per loop instead of 260us (in vanilla MPC). A further
gain could be obtained if we get rid of the mpc_log call to detect overflow or underflow: we would
then get 113us. But of course the definite solution will be to implement binary exponentiation.


---

Comment by zimmerma created at 2010-03-30 16:03:32

We have now implemented binary exponentiation in `mpc_pow_ui`. We now get on the same machine
as above with the svn version of MPC:

```
tarte% ./sage
mpc_log took 75us per loop
mpc_exp took 24us per loop
mpc_pow(12345) took 19us per loop
mpc_div took 3.5us per loop
```

thus now MPC powint should be comparable to CC powint. There is not yet a release of MPC with the
new code, but it suffices to modify the file `pow_ui.c`.


---

Comment by zimmerma created at 2010-03-30 16:05:56

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-03-30 16:05:56

I put it as "needs review" again to know if some more issues need to be fixed upstream.
Paul


---

Comment by ylchapuy created at 2010-03-31 12:26:11

Replying to [comment:23 zimmerma]:
> I put it as "needs review" again to know if some more issues need to be fixed upstream.
> Paul

If you send me the file `pow_ui.c` I can patch my spkg so that people can try it. Yann


---

Comment by zimmerma created at 2010-03-31 13:43:13

> If you send me the file pow_ui.c I can patch my spkg so that people can try it. Yann 

sorry, it is available from https://gforge.inria.fr/scm/viewvc.php/trunk/src/pow_ui.c?root=mpc
We might still improve it, thus if you update your spkg please indicate the revision of the file
you took.

Paul


---

Comment by jason created at 2010-05-15 07:18:40

Paul,

Now with MPC 0.8.2, mpz_pow_ui is fast, but mpz_pow_si is still slow.  As the MPC Sage code is written right now, calls are made to mpz_pow_si, mpz_pow_z, or mpz_pow, depending on the type of argument.  Each of these are still 5-6 slower than Sage's complex number type.

Do your great speedups for mpz_pow_ui make it easy to speed up mpz_pow_si, mpz_pow_z, or mpz_pow as well?


---

Comment by jason created at 2010-05-15 07:21:01

Replying to [comment:26 jason]:
> Paul,
> 
> Now with MPC 0.8.2, mpz_pow_ui is fast, but mpz_pow_si is still slow.  As the MPC Sage code is written right now, calls are made to mpz_pow_si, mpz_pow_z, or mpz_pow, depending on the type of argument.  Each of these are still 5-6 slower than Sage's complex number type.
> 


I mean: each of these calls (mpz_pow[_si|_z]) results in operations that are 5-6 times as long as Sage's complex type (~35 microseconds vs. ~200 microseconds).


---

Comment by jason created at 2010-05-15 10:20:30

Paul, I see in the MPC repository that you are already working on this.  Thanks!


---

Comment by zimmerma created at 2010-05-15 21:16:53

Replying to [comment:28 jason]:

Jason,

> Paul, I see in the MPC repository that you are already working on this.  Thanks!

yes we are working on this. Too bad that you didn't tell us before the 0.8.2 release. Are you
subscribed to the mpc-discuss list, where we ask feedback for release candidates?


---

Comment by jason created at 2010-05-15 21:35:08

Replying to [comment:29 zimmerma]:

> yes we are working on this. Too bad that you didn't tell us before the 0.8.2 release. Are you
> subscribed to the mpc-discuss list, where we ask feedback for release candidates?

I only just was able to squeeze some time out to look at this. I'm not subscribed to mpc-discuss; I'll subscribe now.


---

Comment by zimmerma created at 2010-06-18 09:33:10

Revision svn 790 from MPC implements a faster mpc_pow_si:

```
tarte% ./sage
mpc_log took 76us per loop
mpc_exp took 24us per loop
mpc_pow_ui(12345) took 19.2us per loop
mpc_pow_ui(4294967295) took 149.0us per loop
mpc_pow_si(12345) took 19.2us per loop
mpc_pow_si(-12345) took 22.6us per loop
mpc_pow_z(12345) took 19.2us per loop
mpc_pow(12345) took 133.4us per loop
mpc_div took 3.6us per loop
```

Yann, please can you prepare a new spkg so that Jason can review this ticket?

Paul


---

Comment by drkirkby created at 2010-06-18 10:27:43

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-06-18 10:27:43

In the spkg-install I see above:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O2 -g -m64 -fPIC"; export CFLAGS
   CXXLAGS="-O2 -g -m64 -fPIC"; export CXXFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
else
   CFLAGS="-O2 -g -fPIC"; export CFLAGS
fi
```


This will cause an issue that plagues a 64-bit port to OpenSolaris and Solaris 10. There is no reason to restrict the -m64 flag to be just OS X. It should be changed to:


```
if [ "x$SAGE64" = xyes ]; then
   echo "Building a 64-bit version of MPC"
   CFLAGS="-O2 -g -m64 -fPIC"; export CFLAGS
   CXXLAGS="-O2 -g -m64 -fPIC"; export CXXFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
else
   CFLAGS="-O2 -g -fPIC"; export CFLAGS
fi
```


Was there a good reason for unsetting 'RM' in the spkg-install, or was it just one copied from some other package, which happened to do that? 

Most packages use 

 * configure 
 * make 
 * make install

checking the error code of each of the 3 stages. This does 

 * configure 
 * make install

If 'make install' fails, there is no way to know if the build or installation failed. 

See

http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg

for some information on that. I note looking at the above link, there is no code which does anything when SAGE64 is set to "yes". That is in my mind an error in the documentation. Clearly that was written even before a 64-bit OS X port was attempted. 

Also, SPKG.txt is an empty file - again see that link above for how that should be created. 

Dave


---

Comment by ylchapuy created at 2010-06-18 21:22:52

new spkg here:

http://yann.laiglechapuy.net/spkg/mpc-0.8.2svn793.spkg


---

Comment by ylchapuy created at 2010-06-18 21:33:42

Changing status from needs_work to needs_review.


---

Attachment

after installing 'mpc-0.8.2svn793.spkg' ,
one needs to apply in order:
 * mpc-0.8.1.patch
 * bug_literal.patch
 * trac4446-rebase_sage4.3.3.patch
 * fix_declaration.patch

Tested with vanilla sage-4.4.3, Ubuntu 10.04, kernel 2.6.32-22-generic # 36-Ubuntu SMP Thu Jun 3 19:31:57 UTC 2010 x86_64 GNU/Linux, Intel(R) Core(TM) i5 CPU 650 `@` 3.20GHz.


```
sage -t  "devel/sage-main/sage/rings/complex_mpc.pyx"       
	 [1.8 s]
 
----------------------------------------------------------------------
All tests passed!
```


The script 'spkg-install' is a mix between the template from:

http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg

and the script from the mpfr spkg. In particular, I don't know what is the point of the EXTRA flags, but thought they might be useful.

You will also see in the file SPKG.txt:


```
## SPKG Maintainers

 * ???
```


I just can't be the maintainer, sorry...


---

Comment by drkirkby created at 2010-06-18 21:48:57

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-06-18 21:48:57

It builds, OK on both 

 * Solaris 10 03/2005 32-bit mode. 
 * OpenSolaris 06/2009 in 64-bit mode. 

But it fails tests on both machines. 

## Test failure on Solaris 10 03/2005
Configuration is 
 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/05 (This was the first release of Solaris 10)
 * Sage 4.4.4.alpha1
 * mpc-0.8.2svn793.spkg (md5 checksum 2060cdf173efa2943529745438b26f1e)
 * 32-bit build. 
 

```
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -MT read_data.lo -MD -MP -MF .deps/read_data.Tpo -c read_data.c  -fPIC -DPIC -o .libs/read_data.o
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -MT read_data.lo -MD -MP -MF .deps/read_data.Tpo -c read_data.c -o read_data.o >/dev/null 2>&1
mv -f .deps/read_data.Tpo .deps/read_data.Plo
/bin/bash ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I..  -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include   -O2 -MT comparisons.lo -MD -MP -MF .deps/comparisons.Tpo -c -o comparisons.lo comparisons.c
comparisons.o: No such file or directory
.libs/comparisons.o: No such file or directory
comparisons.lo: No such file or directory
comparisons.loT: No such file or directory
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -MT comparisons.lo -MD -MP -MF .deps/comparisons.Tpo -c comparisons.c  -fPIC -DPIC -o .libs/comparisons.o
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -MT comparisons.lo -MD -MP -MF .deps/comparisons.Tpo -c comparisons.c -o comparisons.o >/dev/null 2>&1
mv -f .deps/comparisons.Tpo .deps/comparisons.Plo
/bin/bash ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I..  -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include   -O2 -MT memory.lo -MD -MP -MF .deps/memory.Tpo -c -o memory.lo memory.c
memory.o: No such file or directory
.libs/memory.o: No such file or directory
memory.lo: No such file or directory
memory.loT: No such file or directory
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -MT memory.lo -MD -MP -MF .deps/memory.Tpo -c memory.c  -fPIC -DPIC -o .libs/memory.o
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -MT memory.lo -MD -MP -MF .deps/memory.Tpo -c memory.c -o memory.o >/dev/null 2>&1
mv -f .deps/memory.Tpo .deps/memory.Plo
/bin/bash ../libtool --tag=CC   --mode=link gcc  -O2  -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib  -o libmpc-tests.la  random.lo tgeneric.lo read_data.lo comparisons.lo memory.lo  -lmpfr -lgmp 
libtool: link: ar cru .libs/libmpc-tests.a .libs/random.o .libs/tgeneric.o .libs/read_data.o .libs/comparisons.o .libs/memory.o 
libtool: link: ranlib .libs/libmpc-tests.a
libmpc-tests.la: No such file or directory
libtool: link: ( cd ".libs" && rm "libmpc-tests.la" && ln -s "../libmpc-tests.la" "libmpc-tests.la" )
libmpc-tests.la: No such file or directory
make[2]: *** [libmpc-tests.la] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/mpc-0.8.2svn793/src/tests'
make[1]: *** [check-am] Error 2
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/mpc-0.8.2svn793/src/tests'
make: *** [check-recursive] Error 1
There was a problem during the mpc tests.
*************************************
Error testing package ** mpc-0.8.2svn793 **
*************************************
sage: An error occurred while testing mpc-0.8.2svn793
```

## Test Failure on OpenSolaris 06/2009
Configuration is 
 * Sun Ultra 27
 * Intel Xeon W3580 3.333 GHz, quad core, hyperthreaded (8 threads)
 * 12 GB RAM
 * OpenSolaris 06/2009 (This is the latest release of OpenSolaris, but has updated to snv_134).
 * Sage 4.4.4.alpha1
 * mpc-0.8.2svn793.spkg (md5 checksum 2060cdf173efa2943529745438b26f1e)
 * 64-bit build (SAGE64 was exported to "yes"). 


```
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -g -m64 -O2 -g -m64 -O2 -MT comparisons.lo -MD -MP -MF .deps/comparisons.Tpo -c comparisons.c  -fPIC -DPIC -o .libs/comparisons.o
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -g -m64 -O2 -g -m64 -O2 -MT comparisons.lo -MD -MP -MF .deps/comparisons.Tpo -c comparisons.c -o comparisons.o >/dev/null 2>&1
mv -f .deps/comparisons.Tpo .deps/comparisons.Plo
/bin/sh ../libtool --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I..  -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -g -m64   -O2 -g -m64   -O2 -MT memory.lo -MD -MP -MF .deps/memory.Tpo -c -o memory.lo memory.c
rm: memory.o: No such file or directory
rm: .libs/memory.o: No such file or directory
rm: memory.lo: No such file or directory
rm: memory.loT: No such file or directory
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -g -m64 -O2 -g -m64 -O2 -MT memory.lo -MD -MP -MF .deps/memory.Tpo -c memory.c  -fPIC -DPIC -o .libs/memory.o
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I.. -I../src -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -O2 -g -m64 -O2 -g -m64 -O2 -MT memory.lo -MD -MP -MF .deps/memory.Tpo -c memory.c -o memory.o >/dev/null 2>&1
mv -f .deps/memory.Tpo .deps/memory.Plo
/bin/sh ../libtool --tag=CC   --mode=link gcc  -O2 -g -m64   -O2  -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib  -o libmpc-tests.la  random.lo tgeneric.lo read_data.lo comparisons.lo memory.lo  -lmpfr -lgmp 
libtool: link: ar cru .libs/libmpc-tests.a .libs/random.o .libs/tgeneric.o .libs/read_data.o .libs/comparisons.o .libs/memory.o 
libtool: link: ranlib .libs/libmpc-tests.a
rm: libmpc-tests.la: No such file or directory
libtool: link: ( cd ".libs" && rm "libmpc-tests.la" && ln -s "../libmpc-tests.la" "libmpc-tests.la" )
rm: libmpc-tests.la: No such file or directory
make[2]: *** [libmpc-tests.la] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/mpc-0.8.2svn793/src/tests'
make[1]: *** [check-am] Error 2
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/mpc-0.8.2svn793/src/tests'
make: *** [check-recursive] Error 1
There was a problem during the mpc tests.
*************************************
Error testing package ** mpc-0.8.2svn793 **
*************************************
sage: An error occurred while testing mpc-0.8.2svn793
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /export/home/drkirkby/sage-4.4.4.alpha1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/mpc-0.8.2svn793 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/mpc-0.8.2svn793' && '/export/home/drkirkby/sage-4.4.4.alpha1/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.

real	0m12.719s
user	0m8.046s
sys	0m3.403s
```



---

Comment by ylchapuy created at 2010-06-18 22:34:04

ok, my fault, I didn't tried the spkg-check. (is the one in the mpfr spkg working???) It should be corrected with the brand new

 http://yann.laiglechapuy.net/spkg/mpc-0.8.3-dev-svn793.spkg

at least, it works for me... same proc, os, etc


```
===================
All 57 tests passed
===================
```



---

Comment by ylchapuy created at 2010-06-18 22:34:04

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-06-19 00:27:44

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-06-19 00:27:44

Replying to [comment:36 ylchapuy]:
> 
> 
> ok, my fault, I didn't tried the spkg-check. (is the one in the mpfr spkg working???) It should be corrected with the brand new
> 
>  http://yann.laiglechapuy.net/spkg/mpc-0.8.3-dev-svn793.spkg
> 
> at least, it works for me... same proc, os, etc
> {{{
> ===================
> All 57 tests passed
> ===================
> }}}
mpc-0.8.3-dev-svn793.spkg (md5 checksum 07e1b56fe1e551138b8862d5551d6948) passed all 57 tests on both machines I have tested on. 

    * Sun Blade 1000, UltraSPARC III+ processors, Solaris 10 03/2005 32-bit mode.
    * Sun Ultra 27, quad core Xeon processor, OpenSolaris 06/2009 in 64-bit mode. 

However, it seems a long way before this could get a positive review and be incorporated into Sage. 

 * William has made quite extensive comments - in particular the fact it could *not* be "optional" so would have to be a standard part of Sage. 
 * Nobody has agreed to maintain it. I believe there is a requirement for any standard package that someone agrees to maintain it for 2 years. 
 * For the package to become "standard" it needs a vote. 
 * I don't like the idea of using a SVN snapshot unless necessary. This is not based on a stable release of MPC, yet I believe it would have to become a standard part of Sage. That seems a bad idea in my opinion. 
 * It appears to have undergone very little testing. When I noticed the test suite had failed, you remarked you had not run the tests. When several months ago I asked if it had been tested on Solaris, nobody responded. 
 * Has it been tested on OS X? If so, what processors? 
 * Are you aware Sage is suppose to support all these platforms. What subset of these has MPC been tested on? 
  {{{
  PROCESSOR        OPERATING SYSTEM
  x86              32-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
                                   Fedora, openSUSE, Mandriva, Arch
  x86_64           64-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
                                   Fedora, openSUSE, Mandriva, Arch
  IA-64 Itanium 2  64-bit Linux -- Red Hat, SUSE
  x86              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
  PPC              Apple Mac OS X 10.4.x, 10.5.x, 10.6.x
  SPARC            Solaris 10
  }}}
 * Have the doc tests been run on different hardware? Would results be affected by different floating point processors, so that the doc tests might need to consider this. 

I would add, I have a lot of respect for Paul Zimmermann, so I would tend to trust code he is associated with. 

It just strikes me that this is going to need a lot more than one positive review to become part of Sage. I believe any competent reviewer will ask for more proof this would be a good addition to Sage. At the moment, whilst the fact Paul is associated with this code would tend to make me think it is well tested, as a package in Sage, there seems to be little evidence presented that this has undergone much testing. Given its based on a snapshot, makes me even more suspicious. 

A few others points. 
 * One of the attachments says it is released under the GPL, but does not state the version. I believe it should say "GPL version 2, or (at your option) any later version."
 * As for your question about the MPFR test suite, if you look at MPFR's spkg-install you will see that the test suite is run every time Sage is built. That is because the test suite tended to fail quite regularly with buggy compilers, or buggy operating systems, so it was wise to test it on every Sage build. 
 * What does the '793' in the .spkg mean? I assumed at first it was a revision, but now see that is unchanged, whilst the number in the package has changed from 0.8.2 to 0.8.3. 


Dave


---

Comment by zimmerma created at 2010-06-19 08:03:00

thank you David for your comments on this ticket. We (the MPC developers) have invested a lot of
time on this ticket (especially Philippe Theveny in 2008-2009, where at that time he was an
engineer paid by INRIA to work on MPFR and MPC), thus we would appreciate a lot if the Sage
developers could tell us right now in case they believe MPC will *never* become a standard package, so that we don't spend more time on this ticket.

As for the technical issues, I can answer a few ones:

- this package is based on svn version 793 just to speed up the `mpc_pow_si` computations.
  Note that if the Sage developers had requested this before, this could have been done for the
  last release (0.8.2). The changes wrt the 0.8.2 release are therefore minimal.

- about testing, you surely know that MPC is now a prerequisite to compile GCC 4.5
  (see http://gcc.gnu.org/install/prerequisites.html). You will find an extensive
  list of supported platforms on http://www.multiprecision.org/index.php?prog=mpc&page=platforms.

- about doctests, MPC is based on MPFR, which produces platform-independent results, thus the
  doctests do *not* depend on the platform, contrary to other numeric packages. This is one of
  the reasons MPC was chosen by GCC for constant folding.

- MPC is released under LGPL v2.1+.

Paul Zimmermann


---

Comment by ylchapuy created at 2010-06-19 09:40:12

Hi David,
Paul already gave you some answers, I will complete with my own point of view:
 * first just  to be clear,  I am not  related in any way  with the MPC  team. I
  started updating this spkg from the one made by Philippe Theveny because I do
  think it would be a good thing for the Sage project to have it;

 * regarding  the "optional"  problem; I  just extended  what Philippe  does.  I
  personally don't know how to  make an optional package with Cython interfaces
  to a C library, if you know how to do it please give me some pointers;

 * I know  it's the policy now to  have someone agreeing to  maintain spkg's for
  some time; but I just can't and live this to others;

 * as explained  by Paul, the  svn revision 793  respond to a request  from Sage
  developers.  The problem  with the  bad version  numbering (0.8.2  instead of
  0.8.3-dev) comes from me, sorry for this;

 * I have no access  to other platforms, **and** don't have more  time to spend (I
  know I could ask William for an account for Sage development);

 * the part  relying purely on MPC  should be platform oblivious;  of course the
  part  interacting   with  Sage  CC   stuff  can  still  have   some  rounding
  problems. None of this has been tested on different platforms (by me at least);

 * finally,  regarding the  license, the  file SPKG.txt  is clear  with  this. I
  didn't check the patches attached with this ticket.

As a  conclusion, I want to  say that I won't  have much more time  to spend on
this. If there is  a clear way not to transform those 20  months in a big waste
of time I would be please to make a last effort.

Yann

PS: the SPKG  changed once again. The problem with  the previous spkg-check was
just the usual  RM and libtool glitch.  My corrected script was doing  a lot of
work for nothing. The md5 sum is now af419b37f887082a2979ce3a9d0c194a .


---

Comment by jason created at 2010-06-19 12:19:18

Replying to [comment:39 ylchapuy]:

> As a  conclusion, I want to  say that I won't  have much more time  to spend on
> this. If there is  a clear way not to transform those 20  months in a big waste
> of time I would be please to make a last effort.


I can be the maintainer for the next two years.  I really think this ought to go into Sage (once objections are satisfied, of course).  I think I can help work on this in the next few weeks.

I really appreciate everyone's time in working on this, and David's extensive comments as well!


---

Comment by jason created at 2010-06-19 12:27:46

Replying to [comment:38 zimmerma]:
> thank you David for your comments on this ticket. We (the MPC developers) have invested a lot of
> time on this ticket (especially Philippe Theveny in 2008-2009, where at that time he was an
> engineer paid by INRIA to work on MPFR and MPC), thus we would appreciate a lot if the Sage
> developers could tell us right now in case they believe MPC will *never* become a standard package, so that we don't spend more time on this ticket.
> 

If I recall correctly, the vote on sage-devel was positive for inclusion, once some of the objections were resolved.  I definitely see it becoming a standard package in Sage (and am willing to be the maintainer to make it so!)

Jason


---

Comment by drkirkby created at 2010-06-19 12:30:45

I was just about to post a long message and see Jason beat me to it. 

Here is what I was going to write - some of it might be useful. 

Dave 
---------------------- 

Thank you Paul and Yann,

This clearly needs more than one person to agree to this, so I would think it right the ticket is discussed on the sage-devel mailing list. Before doing that, I just wanted to clarify if my understanding is correct. In particular, I'd like to know if the following comments seem a reasonable thing to post on sage-devel, asking if this should be a standard part of Sage. 

 * MPC is a C library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding of the result.
 * A trac ticket #4446 has been open for 20 months to add MPC to Sage, with 37 comments on it. 
 * Although personally I don't know much about how this overlaps with other components in Sage, a number of Sage developers have put a lot of effort into ticket #4446, so there must be interest in this. 
 * I personally believe the MPC library code should be of high quality as it is produced by a team of developers who in my personal opinion care about quality. 
 * The MPC library is LGPL v 2.1+
 * The license on one of the patches attached to the ticket #4446 is ambiguous, saying just "GPL", with nothing about version number(s), but I suspect that would be easy to resolve. 
 * Both Linux on x86 and Solaris 10 on SPARC are primary platforms for MPC, but OS X is a secondary platform. 
 * FreeBSD on x86 is a platform where a Sage port is in progress. FreeBSD is a primary platform for MPC, 
 * OpenSolaris on x64, is a platform where a Sage port is in progress. This is not listed as even a tertiary platform for MPC, though in practice MPC passed all 57 tests for me on OpenSolaris x64 using gcc 4.4.4. (This was using Sage 4.4.4.alpha1, which uses MPIR 1.2.2 and MPFR 2.4.2.) 
 * Solaris 10 on x86, is a platform where a Sage port is in progress. This is a tertiary platform for MPC, but with a report of all MPC library tests passing. 
 * The Sage package initially presented for review (mpc-0.8.2svn793.spkg) failed to even build the test suite on Solaris or OpenSolaris, but a revised edition of the Sage package passes all tests on Ubuntu 10.04 64-bit, Solaris 10 (SPARC) 32-bit and OpenSolaris (x64) 64-bit. The initial problem was a mistake in the packaging for Sage, rather than the MPC library. 
 * The package present for review is based on an SVN snapshot. Paul Zimmermann, an MPC developer, has said this minimal changes from the stable 0.82 release. Those changes were made to address a performance issue. 
 * The Sage package is not currently "optional", but would need to be "standard". (There may or may not be ways of making it "optional", but William's comments on the trac ticket tended to suggest it could not be.) 
 * The current package has not been tested much in Sage, and Yann who submitted the package does not have much more time to spend on it, so will not be asking William accounts to test on other platforms. 
 * Currently nobody has volunteered to maintain the package.   
 * A lot of work has been done on this ticket over a period of 20 months, so it would be a shame if that is wasted. 
 * The MPC developers would appreciate a lot if the Sage developers could tell them right now if they believe MPC will never become a standard package, so they don't spend more time on ticket #4446. 
 
Do you feel I've overlooked something, or that is inaccurate? If you believe that is OK, I will ask on sage-devel if this should become a standard part of Sage.


---

Comment by zimmerma created at 2010-06-19 13:26:50

Dave,

most of your comments are accurate. Upstream developers too have put a lot of effort (in addition to Sage developers). This collaboration has benefited to upstream, since several issues reported by the Sage developers were solved upstream. Note that the concept of primary, secondary or tertiary platform on the MPC development page is inherited from GCC (this classification is not done by the MPC developers). Also Jason volunteers to maintain the package (for at least 2 years).

Paul


---

Comment by drkirkby created at 2010-06-19 15:02:09

I've posted about this on the sage-devel list. 

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c8363227c72b6918

Hopefully that will be useful. 

I'm probably jumping ahead here, but before this could be included, an updated file spkg/standard/deps would need to be added. But I would not worry until there is more feedback from sage-devel. 

Dave


---

Attachment


---

Comment by zimmerma created at 2010-07-12 12:58:01

Dave, since you changed from needs review to needs info 3 weeks ago, did you get the answers
to all your questions? What is still blocking a review of this ticket?

Paul


---

Comment by drkirkby created at 2010-07-12 13:28:39

Replying to [comment:45 zimmerma]:
> Dave, since you changed from needs review to needs info 3 weeks ago, did you get the answers
> to all your questions? What is still blocking a review of this ticket?
> 
> Paul
Hi Paul, 

There is nothing I can do about this myself. I think you need to follow up on the thread I posted to sage-devel (see above). I asked about this and William responded with: 


''A while ago I tried out the proposed  MPC package for Sage, and it was
much slower than the multiprecision complex code that we already had
in Sage.  I wonder if these performance issues have been addressed?

 -- William''


I then responded with:

''It would appear the issue have been addressed. You would be in a better position
that me to determine if those issues are fully resolved. The last two entries in
the NEWS file are both related to performance.''

There really is little more I can do about this. I don't have the knowledge to evaluate the performance. You really need to convince William. 

BTW, what are the prequesites for this package? An updated spkg/install and updated spkg/standard/deps would be needed. You could usefully add them to the ticket. 


BTW, the author field is not filled in. 

Dave


---

Comment by zimmerma created at 2010-07-12 13:46:55

I have filled in the author field.

> BTW, what are the prequesites for this package?

MPC only depends on GMP and MPFR, which are standard Sage packages.

> You really need to convince William.

ok, then William please could you review this ticket? I change it to needs review since it seems
all requested information has been given.


---

Comment by zimmerma created at 2010-07-12 13:46:55

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-07-12 13:54:24

Replying to [comment:47 zimmerma]:
> I have filled in the author field.
> 
> > BTW, what are the prequesites for this package?
> 
> MPC only depends on GMP and MPFR, which are standard Sage packages.

But you still need to create an spkg/install and spkg/standard/deps for this to be a standard package. I would attach them to the ticket. 

> > You really need to convince William.
> 
> ok, then William please could you review this ticket? I change it to needs review since it seems
> all requested information has been given.


Dave


---

Comment by drkirkby created at 2010-08-02 14:13:58

Replying to [comment:48 drkirkby]:
> Replying to [comment:47 zimmerma]:
> > I have filled in the author field.
> > 
> > > BTW, what are the prequesites for this package?
> > 
> > MPC only depends on GMP and MPFR, which are standard Sage packages.
> 
> But you still need to create an spkg/install and spkg/standard/deps for this to be a standard package. I would attach them to the ticket. 

Paul,
did you do any more on this? There seems to be four things needed here

 * update spkg/install, to have something like 


```
MPC=`$newest mpc`
export MPC
```


 * update spkg/standard/deps to have something like


```
all: $(BASE) \
   $(INST)/$(ATLAS)
...
   $(INST)/$(MPC))
...
   $(INST)/$(ZODB)
```


 * Update spkg/standard/deps so it also has a line like this.  

```
$(INST)/$(MPC): $(BASE) $(INST)/$(MPIR) $(INST)/$(MPFR)
        $(INSTALL) "$(SAGE_SPKG) $(MPC) 2>&1" "tee -a $(SAGE_LOGS)/$(MPC).log"

```

 * Convince William that's this is necessary and not slower than what's in Sage, which was his objection before. I started a thread for you - see http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c8363227c72b6918 but you have not written anything on it. 

Dave


---

Comment by ylchapuy created at 2010-08-12 11:05:25

apply only this patch


---

Attachment

This ticket is already too long, but here is another rebased version:

 * I made a self contained patch rebased on sage 4.5.2. http://trac.sagemath.org/sage_trac/attachment/ticket/4446/trac4446-optional_mpc-sage4.5.2based.patch

 * An spkg is still available at http://yann.laiglechapuy.net/spkg/mpc-0.8.3-dev-svn793.spkg

 * this is intended to make `mpc` an *optional* spkg. The `complex_mpc` module won't be compiled if the spkg is not installed.


---

Comment by zimmerma created at 2010-08-24 18:56:59

Dave,

> Paul,
> did you do any more on this? There seems to be four things needed here [...]

>  * Convince William that's this is necessary and not slower than what's in Sage, which was his objection before. I started a thread for you - see http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c8363227c72b6918 but you have not written anything on it. 

this should be the very first thing to do, before we invest more time in this ticket. William, are you out there?

Paul


---

Comment by was created at 2010-08-24 19:04:24

I'm "out there".   Is it necessary and not slower than what is in Sage already?  I'm willing to take your (=Paul's) word for it, assuming you say you've done some benchmarks.   Also, rounding might be (vastly) better in mpc, which would be another point in its favor.


---

Comment by zimmerma created at 2010-09-26 12:10:48

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-09-26 12:10:48

Replying to [comment:52 was]:
> I'm "out there".   Is it necessary and not slower than what is in Sage already?  I'm willing to take your (=Paul's) word for it, assuming you say you've done some benchmarks.   Also, rounding might be (vastly) better in mpc, which would be another point in its favor. 

William, here are some results of benchmarks I've done on my Core 2 Duo laptop, with Sage 4.5.3,
with Yann latest patch and the associate spkg. Efficiency:

```
sage: K = MPComplexField(53)
sage: a = K(3.3902384+1.23456789*i)
sage: b = CC(3.3902384+1.23456789*i)
sage: timeit('a*a')
625 loops, best of 3: 1.03 µs per loop
sage: timeit('b*b')
625 loops, best of 3: 1.08 µs per loop # CC is slower
sage: timeit('a+a')
625 loops, best of 3: 566 ns per loop
sage: timeit('b+b')
625 loops, best of 3: 571 ns per loop # CC is slower

sage: K=MPComplexField(1000)
sage: a = K(3.3902384,9203483)
sage: b = ComplexField(1000)(3.3902384,9203483)
sage: timeit('a*a')
625 loops, best of 3: 3.26 µs per loop
sage: timeit('b*b')
625 loops, best of 3: 2.99 µs per loop # CC is slightly faster
sage: timeit('a+a')
625 loops, best of 3: 680 ns per loop
sage: timeit('b+b')
625 loops, best of 3: 694 ns per loop # CC is slower
sage: timeit('a.sin()')
625 loops, best of 3: 294 µs per loop
sage: timeit('b.sin()')
625 loops, best of 3: 343 µs per loop # CC is slower

sage: timeit('a+17')
625 loops, best of 3: 2.56 µs per loop
sage: timeit('b+17')
625 loops, best of 3: 3.02 µs per loop # CC is slower

sage: a2=a+17
sage: b2=b+17
sage: timeit('a/a2')
625 loops, best of 3: 30.3 µs per loop
sage: timeit('b/b2')
625 loops, best of 3: 14.6 µs per loop

sage: timeit('a.real()')
625 loops, best of 3: 854 ns per loop
sage: timeit('b.real()')
625 loops, best of 3: 5.13 µs per loop

sage: timeit('a.conjugate()')
625 loops, best of 3: 736 ns per loop
sage: timeit('b.conjugate()')
625 loops, best of 3: 750 ns per loop
sage: timeit('a.argument()')
625 loops, best of 3: 146 µs per loop
sage: timeit('b.argument()')
625 loops, best of 3: 155 µs per loop

sage: timeit('a**12345')
625 loops, best of 3: 126 µs per loop
sage: timeit('b**12345')
625 loops, best of 3: 176 µs per loop

sage: timeit('a.log()')
625 loops, best of 3: 315 µs per loop
sage: timeit('b.log()')
625 loops, best of 3: 400 µs per loop

sage: timeit('a.exp()')
625 loops, best of 3: 221 µs per loop
sage: timeit('b.exp()')
625 loops, best of 3: 211 µs per loop
```

For the accuracy, I've computed the maximal relative error on the real or imaginary part after
1000 random tries for several operations. My program also prints the inputs that give the
corresponding maximal error:

```
multiplication:
sage: foo(53) # 53 bits
MPC:  1.09250136812570e-16 (-0.199676992382071 - 0.194223361415138*I, 0.9413020\
06592817 + 0.645200777306369*I)
CC:   1.32263143752823e-14 (0.834168924383086 - 0.525629438090125*I, -0.4766533\
42074290 + 0.752454804563813*I)
sage: foo(100) # 100 bits
MPC:  7.83034842148009e-31 (-0.43034701147206399980669837638 - 0.81582963965013\
399110093432939*I, -0.83969050263610625199834532314 + 0.17390362688794167984134\
423048*I)
CC:   9.28509698731955e-29 (-0.36479911591428496460512307920 + 0.22548928494028\
018164534780632*I, -0.49018610148599010061638163259 - 0.30229330441199619133786\
980680*I)

division:
sage: foo(53)
MPC:  1.08485488717363e-16 (0.906903106647522 + 0.991328300040510*I, 0.26885465\
0418765 - 0.188551687646414*I)
CC:   4.27558190140949e-13 (-0.947451505768202 - 0.424071772860430*I, -0.499313\
865619141 - 0.223444662259920*I)
sage: foo(100)
MPC:  7.66357970552281e-31 (0.92755016191057837385980632404 - 0.004266231128213\
8322794515257916*I, 0.14072961243734751540073515895 - 0.21101836467335963334809\
014965*I)
CC:   1.06937889944401e-27 (-0.41008840630275384495897016614 + 0.43420284734725\
368743056683764*I, -0.61829368333881933443455346326 - 0.58354470182146315365872\
353144*I)

sqrt:
sage: foo(53)
MPC:  1.09880191814582e-16 (-0.621894659027438 - 0.0246731753089378*I, 0.823805\
504837539 - 0.981310087843700*I)
CC:   2.08688816342048e-16 (0.968316682679636 + 0.637686286592402*I, -0.2999297\
58140749 + 0.680399103485303*I)
sage: foo(100)
MPC:  7.83762497864303e-31 (0.87484855451536280543412317489 + 0.744936094843967\
94278935970162*I, -0.93716227305934196720704783450 - 0.765294741452728993051615\
69068*I)
CC:   1.59191232901277e-30 (0.22724304905610094307701469163 + 0.290884560229311\
05826353325335*I, -0.44728415428244253958062250934 + 0.959404399673905010209671\
68949*I)

exp:
sage: foo(53)
MPC:  1.08513702552684e-16 (0.801188951612012 - 0.440834327392402*I, -0.6487549\
15945509 - 0.558408459317570*I)
CC:   2.56306731927053e-16 (-0.534146492930164 - 0.126305922104917*I, -0.525552\
199671560 + 0.0746660767007601*I)
sage: foo(100)
MPC:  7.85000220770852e-31 (-0.25871533881495460870167038331 + 0.70802010475507\
807939080332669*I, 0.99833000148645085071979336755 + 0.103046934118108408058895\
43882*I)
CC:   2.02731881365962e-30 (0.033507794108965175610485564405 + 0.53119476356929\
639125934355035*I, 0.46545588987697950055582059300 + 0.896373882394705924442797\
08331*I)

log:
sage: foo(53)
MPC:  1.09778133774750e-16 (-0.391618732071762 + 0.824073966701766*I, 0.3486864\
59442427 - 0.191201122946134*I)
CC:   6.10819034602284e-14 (0.306684274970498 + 0.953229884394732*I, 0.69862405\
1151183 + 0.276699733597418*I)
sage: foo(100)
MPC:  7.78374256155462e-31 (0.50154056740914466911692379172 + 0.796641256036122\
24316946320184*I, -0.76918900642484651661867461393 - 0.286514343536794358035934\
91438*I)
CC:   6.82825438431515e-28 (-0.13721125119514449776575251187 + 0.99010163436560\
678238821778034*I, 0.92169332492985590698251634723 + 0.433132422276759879534575\
89642*I)

sin:
sage: foo(53)
MPC:  1.08720457020742e-16 (-0.369315245123802 + 0.854572675318644*I, 0.8169569\
42853907 - 0.383919250130617*I)
CC:   2.59601650874087e-16 (-0.546197856444743 - 0.534628610514192*I, 0.3036961\
63087668 - 0.231790426712382*I)
sage: foo(100)
MPC:  7.55871247471999e-31 (0.20947476591320905500539204843 - 0.626588978693616\
08926271268655*I, -0.55364821811403565597840750754 + 0.743341403117384889712851\
11372*I)
CC:   1.72458459418951e-30 (0.42758001678856166974028750611 - 0.923412131000390\
51795327859750*I, -0.99149234221470907346167026703 - 0.690427397584128136419461\
37603*I)

cos:
sage: foo(53)
MPC:  1.08584899379431e-16 (0.0646782540849349 - 0.111085748624151*I, 0.4701880\
86702821 + 0.252843262283133*I)
CC:   2.85959441825441e-16 (0.0850486257569383 - 0.330860565935531*I, 0.0564130\
612472886 + 0.0847664237260943*I)
sage: foo(100)
MPC:  7.78394156732906e-31 (0.93946166432029710121550615978 - 0.592139906105641\
30050851821134*I, 0.53601265027477876871715914306 - 0.1322166340317310632649551\
5769*I)
CC:   1.94260689254542e-30 (-0.55385187621901359297440670364 + 0.50415610417338\
788296133563973*I, -0.13371850315082336799522666801 - 0.96241946806142646000989\
112726*I)
```

I used the following programs:

```
def check(res,ref):
   if ref.real() == 0.0:
      if res.real() <> 0.0:
         err_real = +Infinity
      else:
         err_real = 0.0
   else:
      err_real = RR((res.real()-ref.real()).abs()/ref.real().abs())
   if ref.imag() == 0.0:
      if res.imag() <> 0.0:
         err_imag = +Infinity
      else:
         err_imag = 0.0
   else:
      err_imag = RR((res.imag()-ref.imag()).abs()/ref.imag().abs())
   return max(err_real,err_imag)

def foo(p):
   K=MPComplexField(p)
   L=ComplexField(p)
   K2=MPComplexField(p+20)
   L2=ComplexField(p+20)
   max_erra = 0
   max_errb = 0
   ina = 0
   inb = 0
   for i in range(10^3):
      b = L.random_element()
      br = b.real()
      bi = b.imag()
      a = K(b)
      c = L.random_element()
      cr = b.real()
      ci = b.imag()
      d = K(c)
      aa=cos(a) # change to a*d for multiplication
      bb=cos(b) # change to b*c for multiplication
      ref = cos(K2(a)) # change to K2(a)*K2(d) for multiplication
      erra = check(K2(aa),ref)
      errb = check(K2(bb),ref)
      if erra > max_erra:
         max_erra = erra
         ina = a, d
      if errb > max_errb:
         max_errb = errb
         inb = b, c
   print "MPC: ", max_erra, ina
   print "CC:  ", max_errb, inb
```

The conclusion is that MPC is in the majority of the cases faster than ComplexField (the only
exception being the division) and always more accurate, with a ratio of a factor up to 
3941 (i.e., about 12 bits) for the 53-bit division.

For MPC we observe that the maximal relative error is --- as guaranteed by MPC --- always less than 1/2 ulp (unit in last place) which corresponds to a relative error of 2**(-p), i.e., 1.12e-16 for p=53 and 7.89e-31 for p=100.

I thus give a positive review to Yann's patch.

Paul


---

Comment by mpatel created at 2010-09-29 10:27:00

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-29 10:27:00

Replying to [comment:50 ylchapuy]:
>  * I made a self contained patch rebased on sage 4.5.2. http://trac.sagemath.org/sage_trac/attachment/ticket/4446/trac4446-optional_mpc-sage4.5.2based.patch

>  * An spkg is still available at http://yann.laiglechapuy.net/spkg/mpc-0.8.3-dev-svn793.spkg

>  * this is intended to make `mpc` an *optional* spkg. The `complex_mpc` module won't be compiled if the spkg is not installed.


After applying the patch but not installing the optional package, I get

```
        sage -t -long  devel/sage/sage/rings/complex_mpc.pyx # 454 doctests failed
```

Should all of the tests in `complex_mpc.pyx` be tagged with `#optional - mpc` (see [this section of the developer guide](http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples))?  (I don't know if there's a easier way.)  Or am I mistaken?


---

Comment by mpatel created at 2010-09-29 10:31:04

Or one of

 * `# optional - mpc`
 * `# optional - Mpc`
 * `# optional - MPC`

etc.


---

Comment by ylchapuy created at 2010-09-29 10:45:47

Yes sorry, my mistake.

I won't be able to add this before next week, so if someone motivated beats me... (Paul?)


---

Attachment


---

Comment by ylchapuy created at 2010-09-29 11:57:58

I guess nobody has beaten me...
I had no time, but here it is. All doctests are now marked "# optional - Mpc'

I hope I choose the good version, it's the one used one the Mpc library web page.

Back to the stuff I have to do, I'm late now...

       Yann


---

Comment by ylchapuy created at 2010-09-29 11:57:58

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-09-29 12:50:53

with the last patch (to be applied after the previous one), I get before installing the optional
package:

```
tarte% ./sage -t -long  devel/sage/sage/rings/complex_mpc.pyx
sage -t -long "devel/sage/sage/rings/complex_mpc.pyx"       
         [2.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.1 seconds
```

and after installing it:

```
tarte% ./sage -t -long devel/sage/sage/rings/complex_mpc.pyx
sage -t -long "devel/sage/sage/rings/complex_mpc.pyx"       
         [1.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1.7 seconds
```

Paul


---

Comment by zimmerma created at 2010-09-29 12:50:53

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-29 23:35:16

Thanks!  With the package and patch installed, I get no errors with

```
./sage -t -long -only-optional=mpc "devel/sage/sage/rings/complex_mpc.pyx"
./sage -t -long -optional "devel/sage/sage/rings/complex_mpc.pyx"
```



---

Comment by mpatel created at 2010-09-29 23:43:08

Harald, Mike, or Minh, could one of you please add

 http://yann.laiglechapuy.net/spkg/mpc-0.8.3-dev-svn793.spkg

to the optional spkg repository?


---

Comment by mvngu created at 2010-09-30 00:45:49

Replying to [comment:60 mpatel]:
> Harald, Mike, or Minh, could one of you please add
> 
>  http://yann.laiglechapuy.net/spkg/mpc-0.8.3-dev-svn793.spkg
> 
> to the optional spkg repository?

Done. See the optional spkg repository at

http://www.sagemath.org/packages/optional/


---

Comment by mpatel created at 2010-09-30 00:48:14

Thanks, Minh.


---

Comment by mpatel created at 2010-09-30 00:48:14

Resolution: fixed
