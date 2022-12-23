# Issue 6416: [with spkg and patch, needs review] Frobby for monomial ideals

Issue created by migration from https://trac.sagemath.org/ticket/6416

Original creator: broune

Original creation time: 2009-06-25 21:37:20

Assignee: tbd

CC:  drkirkby

Keywords: monomial ideal, Hilbert series, Alexander dual

This spkg and patch updates the Frobby library that is already an optional component of Sage, and gives it a Cython interface to a shared library instead of the pexpect interface in the current Frobby spkg. It also exposes more functionality. Functionality not currently in sage:

 - Multigraded Hilbert-Poincare series
 - Alexander dual of monomial ideals (already in the previous Frobby spkg)
 - Maximal standard monomials of monomial ideals
 - Irreducible decomposition of monomial ideals
 - Optimization of any linear function over the maximal standard monomials of a monomial ideal using branch-and-bound.

The patch applies cleanly to Sage 4.0.1, and the spkg is at

  http://www.daimi.au.dk/~bjarke/frobby-0.8.0.spkg



---

Attachment


---

Comment by malb created at 2009-07-16 12:35:58

Am I right to assume that the Cython interface would require Frobby to become a standard SPKG? If so, this needs a vote on [sage-devel]. To ask for a vote write an e-mail to [sage-devel] which answers the following questions:
 * what is Frobby and what is it good for?
 * Is it the best (open-source) package for this job?
 * Is Frobby's license compatible with Sage's?
 * Do we have upstream support (trivial :)?
 * On which platforms was it tested (OSX 32-bit and 64-bit, Linux 32-bit and 64-bit, Solaris)?


---

Comment by broune created at 2009-07-16 13:25:45

The vote is at http://groups.google.com/group/sage-devel/browse_thread/thread/ad427ae37c733c48


---

Comment by mhampton created at 2009-07-16 17:23:36

Although I know about as much as my dog about Solaris, I gave it a try on t2.  After downloading the 0.8.0 spkg from trac I did:


```
sage -sh
export GMPLIB=/home/wstein/sparc/sage-3.4.1.rc4-mark-gcc-4.3.3/local
$MAKE library MODE=shared ldflags="$LDFLAGS" GMP_INC_DIR="$GMPLIB"
```


and things compiled well for a while until I got:

```
g++   -Wall -ansi -pedantic -I /home/wstein/sparc/sage-3.4.1.rc4-mark-gcc-4.3.3/local/include -Wno-uninitialized -Wno-unused-parameter -O2 -fPIC -c src/test/TestSuite.cpp -o bin/shared/test/TestSuite.o
src/test/TestSuite.cpp: In member function ‘void TestSuite::sortTests()’:
src/test/TestSuite.cpp:43: error: ‘sort’ was not declared in this scope
make: *** [bin/shared/test/TestSuite.o] Error 1
```


-Marshall


---

Comment by AlexGhitza created at 2009-08-16 03:50:21

Changing component from algebra to commutative algebra.


---

Comment by AlexGhitza created at 2009-08-16 03:50:21

Changing assignee from tbd to malb.


---

Comment by AlexGhitza created at 2009-08-16 09:39:50

I am marking this as "needs work" because of the Solaris issue.  (Maybe David Kirkby can figure this one out.)


---

Comment by kcrisman created at 2012-06-05 14:08:55

Given that #13007 updates Frobby to 0.9.0, this ticket probably needs at least a little TLC.  But in principle the vote still stands, assuming Frobby ever gets to _optional_ status (currently experimental).


---

Comment by kcrisman created at 2012-06-05 14:10:38

Note also that in the vote it was perhaps recommended that Frobby should have a Cython interface that allows it to still be an optional spkg.  It adds perhaps 5 minutes to build time on my medium-age Mac, though it adds less than 1 MB of source.


---

Comment by SimonKing created at 2018-09-11 16:00:10

Changing status from needs_work to needs_info.


---

Comment by SimonKing created at 2018-09-11 16:00:10

This ticket is about an old-style spkg for frobby version 0.8.0. We now have frobby 0.9.0 in a new-style sage package. I know that in some examples in which Singular fails with an int overflow, frobby starts to use very much memory and takes a very long time. Moreover, it seems that the computation of multivariate Hilbert series has a bug: Frobby uses the base ring of the polynomial ring as the base ring of the Hilbert series (but Hilbert series are supposed to have integral coefficients). Moreover, if one uses integral coefficients, the monomials that are not standard monomials appear with coefficient TWO, but should of course have coefficient zero, in the expansion of the multivariate Hilbert series.

```
  sage: R.<x,y,z,w>=QQ[]
  sage: I = R*[x^3,x^2*y,x*z]
  sage: D = ~PowerSeriesRing(QQ,'x,y,z,w')((x-1)*(y-1)*(z-1)*(w-1))
  sage: frobby.hilbert(I)
  x^3*y*z + x^3*y + x^3*z + x^2*y*z + x^3 + x^2*y + x*z + 1
  sage: (frobby.hilbert(I)*D)[:4]
  1 + x + y + z + w + x^2 + x*y + 2*x*z + x*w + y^2 + y*z + y*w + z^2 +
  z*w + w^2 + 2*x^3 + 2*x^2*y + 2*x^2*z + x^2*w + x*y^2 + 2*x*y*z +
  x*y*w + 2*x*z^2 + 2*x*z*w + x*w^2 + y^3 + y^2*z + y^2*w + y*z^2 +
  y*z*w + y*w^2 + z^3 + z^2*w + z*w^2 + w^3 + O(x, y, z, w)^12
```


So, I think that frobby should not be the default backend for Hilbert series.

However, it may still be a good idea to provide a Cython interface. So, question: Should the Cython-interface part of the patch be changed into a branch?
