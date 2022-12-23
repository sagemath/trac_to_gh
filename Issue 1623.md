# Issue 1623: update gsl to 1.10

Issue created by migration from https://trac.sagemath.org/ticket/1623

Original creator: mabshoff

Original creation time: 2007-12-29 04:36:48

Assignee: was




---

Comment by mabshoff created at 2007-12-29 04:37:26

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-12-29 04:37:26

Changing status from new to assigned.


---

Comment by pdenapo created at 2007-12-31 22:33:50

Beware that in version 1.10 GNU gsl has chaged its license to
GPL version 3 (as it is stated in the linked mail), 
so that may raise a license issue


---

Comment by mabshoff created at 2007-12-31 22:43:49

All licensing issues regarding GPL V3 and Sage have been resolved by the relicensing of Singular 3-0-4 to "GPL V2 and V3".

Cheers,

Michael


---

Comment by pdenapo created at 2008-01-22 00:38:32

The other posible problematic package regarding licensing issues is Pari, that I believe is GPL-2


---

Comment by mabshoff created at 2008-01-22 00:48:35

Nope, pari is licensed under:

```
PARI/GP is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation. It is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY WHATSOEVER.
```

Since they do not mention a specific version it is any GPL license version, which include GPL V3. They do ship a copy of the GPL V2 in their sources tarball, but that doesn't imply GPL V2.

Cheers,

Michael


---

Comment by was created at 2008-01-22 00:49:45

PARI is *not* GPL-2.  It is "GPL versions >= 2".  They include the GPL V2 license file, but that file very explicitly says that anything licensed under it is GPL >= 2 unless there is an explicit statement to the contrary elsewhere in the distribution, which there isn't.


---

Comment by mabshoff created at 2008-01-25 22:03:28

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/gsl-1.10.spkg

It builds fine on OSX & Linux. Currently doctesting.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 22:55:45

I am seeing the following doctest failure:

```
sage -t  devel/sage-main/sage/rings/real_double.pyx
**********************************************************************
File "real_double.pyx", line 477:
    sage: a = -RDF(1)/RDF(0); a.str()
Expected:
    '-inf'
Got:
    'inf'
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 23:12:21

Another remark: The `spkg-check` target is broken, I am looking into that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 23:49:53

Ok, this boils down that at least on MacIntel OSX 10.5 the system's `isinf` returns always 1, i.e. all inf's are positive. The issue does not pop up on Linux at all and I have a fixed gsl.spkg that uses a workaround on OSX only.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 00:16:52

An updated spkg, that passes doctests now on OSX & Linux is at:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/gsl-1.10.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 00:19:12

Resolution: fixed


---

Comment by mabshoff created at 2008-01-26 00:19:26

Merged in Sage 2.10.1.alpha2
