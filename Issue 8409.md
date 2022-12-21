# Issue 8409: Fix build and doctest issues for Solaris 10 (SPARC)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-01 16:12:56

Assignee: drkirkby

CC:  mvngu

As of Sage 4.3.3, Sage will not build on Solaris 10 (SPARC). This lists all the items which I'm aware are needed to allow Sage to build, and pass all doctests. 

 == Hardware used for testing ==

Since 't2' is rather slow, a somewhat ancient and low-spec Sun Blade 1000 was used for these tests. 

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Patches needed to build Sage 4.4.3 on Solaris 10 (SPARC) ==

Sage will not build without *all* of the following patches. 

 * #7867 A patch for Python, which solves an issue from #6583.
 * #8191 Addition of iconv, which was needed following an update to R. 
 * #8285 Update R's spkg-install to work on Solaris.
 * #8363 Remove a useless check for mpir in cddlib which breaks Solaris build. 
 * #8371 Patch to allow pyprocessing to build on Solaris - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely, so #8371 may be unnecessary). 

 == Patches needed for Sage to pass all the doctests ==

 * #8374 Numerical noise in sage/symbolic/constants_c.pyx
 * #8375 Numerical noise in sage/symbolic/pynac.pyx
 * #8391 Change 'top' to 'prstat' on Solaris, othewise lots of doctests time out.
 * #8408 Update sqlite to the latest version (otherwise #8397, #8398, #8399, #8400 and #8401 all fail).

 == Other changes ==

It was necessary to increase SAGE_TIMEOUT. The longest test is taking 460 s on the Blade 1000. Despite the relative age and cost of the T5240 (t2) and my Blade 1000 (redstart), the T5240 is designed for a very different task to what it is used for, so some of the doctests will take longer on 't2'. I would suggest a minimum timeout of 2000 s would be necessary to be sure of no failures due to the lack of speed in 't2'. 

Dave


---

Comment by drkirkby created at 2010-03-03 02:03:01

As reported at #8416 this doctest pass after I rebuilt the Sage library completely. So I believe all doctests should now pass on Solaris 10 - including the long ones. 

We will have to wait and see.


---

Comment by jhpalmieri created at 2010-04-23 05:16:10

As of 4.4.alpha1 or alpha2, there are several long doctests which still fail on t2:

```
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py # 2 doctests failed
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py # File not found
        sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # File not found
        sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py # File not found
        sage -t  -long devel/sage/sage/categories/coxeter_groups.py # File not found
```

All but the first are timeouts; I'll increase SAGE_TIMEOUT_LONG and see what happens.  I don't know what causes the first; I'll open a ticket: #8749.

As it stands, I'm not sure what we can do about this ticket, so I'm pushing it to Sage 5.0.


---

Comment by jhpalmieri created at 2010-04-23 14:19:41

With longer SAGE_TIMEOUT_LONG, tests pass:

```
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py
         [2238.6 s]
sage -t  -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
         [3010.0 s]
sage -t  -long devel/sage/sage/modular/ssmod/ssmod.py
         [2336.2 s]
sage -t  -long devel/sage/sage/categories/coxeter_groups.py
         [3101.2 s]
```

except for the ones tracked at #8749 and #8750.


---

Comment by jhpalmieri created at 2010-04-27 14:24:07

Once #8749 is fixed, can we close this?


---

Comment by was created at 2010-06-03 04:08:16

Note a 4.4.3 blocker.


---

Comment by drkirkby created at 2010-06-05 19:32:37

As of sage 4.4.4, #9127 is the only outstanding doctest issue and that would appear to be related to the low speed of the machines used to perform a test - it creates a timeout. 

Once that is fixed, this ticket can be closed.


---

Comment by drkirkby created at 2010-07-12 22:55:49

This can now be closed. All issues have been resolved, and Sage certainly does build on Solaris 10 (SPARC) while passing all doc tests. 

There are still issues on OpenSolaris, and when building in 64-bits, but all the 32-bit issues have been resolved. I added "in 32-bit mode" to the title, so its clear not all issues have been resolved. 

#9026 tracks some of the other Solaris/OpenSolaris related issues. #9281 lists the passes and failures for SAGE_CHECK to work on OpenSolaris x64. 

Dave


---

Comment by drkirkby created at 2010-07-12 22:55:49

Resolution: fixed
