# Issue 842: SAGE's Singular build fails to factor simple polynomials

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-09 21:07:59

Assignee: malb

The following takes a very long time, possibly forever (I waited several minutes before giving up and killing it):

```
sage:  MR.<x,w,v,u> = QQ['x','w','v','u']
sage:  p = (4*v^4*u^2 - 16*v^2*u^4 + 16*u^6 - 4*v^4*u + 8*v^2*u^3 + v^4)
sage:  %time p.factor()
```


Similarly, if you run sage -singular, the equivalent code fails again:

```
> ring r = 0,(x,w,v,u),dp;
> factorize(4*v^4*u^2 - 16*v^2*u^4 + 16*u^6 - 4*v^4*u + 8*v^2*u^3 + v^4);
```


However, if I build my own copy of Singular from the source on the Singular website, or if I download and install the Debian binary package from the Singular website, then this second factorization completes instantly.


---

Comment by cwitty created at 2007-10-09 21:08:29

Changing component from packages to commutative algebra.


---

Comment by was created at 2007-10-09 21:50:15

I'm not sure what to make of this, but...

```
sage: MR.<x,w,v,u> = GF(20011)['x','w','v','u']
sage: p = (4*v^4*u^2 - 16*v^2*u^4 + 16*u^6 - 4*v^4*u + 8*v^2*u^3 + v^4)
sage: time h = p.factor ()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
```



```
14:47 < williamstein> cwitty -- I wonder if we could implement polynomial gcd and factoring
                      directly in sage based on
14:47 < williamstein> singular's excellent GF(p) factorization.
14:47 < williamstein> E.g., your example is trivial to factor instantly in sage mod p for any p.
14:48 < williamstein> It seems like Singular is really really good at mod-p factoring and gcd, and
14:48 < williamstein> seriously problematic at char 0 factoring (and maybe gcd?)
```



---

Comment by cwitty created at 2007-10-10 04:53:43

Changing priority from major to critical.


---

Comment by cwitty created at 2007-10-10 04:53:43

I'm attaching a patch to the Singular spkg that fixes this bug.  Basically, we didn't manage to tell Singular that it had NTL available, so there were several places where it used non-NTL code paths (that were evidently buggy) instead of the working NTL code paths.  This may also explain why the upstream Singular binaries are faster than the ones we build.

You will need to do "sage -ba" after installing the new Singular spkg.

Part of my patch reverts changeset 15:e085dde558b2 in the spkg repository; this is labeled "fixed build for OSX", so presumably my patch breaks the build for OSX.  I don't have access to an OSX machine (or time) to figure this out.


---

Comment by cwitty created at 2007-10-10 04:54:12

a patch for the Singular spkg


---

Attachment


---

Comment by cwitty created at 2007-10-10 07:08:20

Every bugfix should have a doctest, so I've provided 6720.patch.  This adds the example from this bug report as a doctest (so with the current broken Singular spkg, the doctest will hang approximately forever).


---

Comment by malb created at 2007-10-11 21:47:38

An updated spkg can be found at 
 http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-1-20071010.spkg

. This package fixes the linkage problem under OSX while passing `--with-NTL` to the configure script. However, now Singular's factorisation crashes under OSX. I'll open a new ticket for that and suggest this ticket to be closed.


---

Attachment

`multi_polynomial_ideal_singular_ntl_fixes.patch` fixes the doctest failures introduced by the switch to NTL.

To apply all patches:
 * install the new NTL spkg from http://sage.math.washington.edu/home/mabshoff/ntl-5.4.1.p6.spkg
 * install the new Singular spkg from http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-1-20071010.spkg
 * apply `6720.patch` attached above
 * apply `multi_polynomial_ideal_singular_ntl_fixes.patch`


---

Comment by was created at 2007-10-13 02:14:59

Resolution: fixed
