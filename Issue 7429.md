# Issue 7429: pari is misbuilt on OS X using xcode 3.2.1, making sage be mostly broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-11 17:38:54

Assignee: drkirkby

After building sage on OS X 10.6.2 with Xcode 3.2.1 (all latest versions right now, and using #7426), PARI doesn't work, which causes massive failures all over the place:


```
PARI/GP is free software, covered by the GNU General Public License, and comes WITHOUT
ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 8000000, primelimit = 500000
? polcoeff(1/eta(x)^2, 8, x)
dyld: lazy symbol binding failed: Symbol not found: ___gmpn_mul_1
  Referenced from: /Users/was/build/sage-4.2.1.alpha0/local/lib//libpari-gmp.dylib
  Expected in: flat namespace

dyld: Symbol not found: ___gmpn_mul_1
  Referenced from: /Users/was/build/sage-4.2.1.alpha0/local/lib//libpari-gmp.dylib
  Expected in: flat namespace

sage: 
```





---

Comment by was created at 2009-11-11 18:56:24

Resolution: invalid


---

Comment by was created at 2009-11-11 18:56:24

NOTE: I just forced a rebuild of PARI on my box and the above problem vanished.  I think I fixed #7426 but did not force a rebuild of PARI after applying that fix.  So fortunately this problem is invalid :-)
