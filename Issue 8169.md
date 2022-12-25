# Issue 8169: include TOPCOM

archive/issues_008169.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  mhampton @novoselt\n\nTOPCOM is a C++ program for triangulating polyhedra. More generally, it can find a single triangulation as well as enumerate all triangulations of a \"point configuration\", that is, the convex hull of points in euclidean space such that all vertices of simplices of the triangulation are in the given (finite) list of points.\n\nOne problem with the upstream distribution is that it statically links many helper programs, yielding almost 200mb of binaries. Therefore, I suggest the following:\n\n- dynamically link TOPCOM via libtools to reduce size\n- Write a sage<->TOPCOM interface at sage.geometry.triangulation.py\n\nAs an initial submission, my libtoolized TOPCOM spkg is here:\n\nhttp://www.stp.dias.ie/~vbraun/TOPCOM-0.16.2.spkg\n\nand a first draft of triangulation.py is attached. The basic usage is\n\n\n```\nsage: points = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]]);\nsage: points\nA point configuration in QQ^2 consisting of 5 points.\nsage: triang = points.triangulate()   # find one triangulation       \nsage: triang\nA triangulation in QQ^2 consisting of 4 simplices.\nsage: triang.plot(axes=False)                                        \n```\n\n\nAfter we confirm that the libtoolized TOPCOM builds on all sage platforms, I'll contact upstream for eventual inclusion of the autotools sources.\n\nNote: see #8115 for a modified cddlib (required by TOPCOM) that provides a non-static cddlib library.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8169\n\n",
    "created_at": "2010-02-03T12:11:31Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "include TOPCOM",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8169",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  mhampton @novoselt

TOPCOM is a C++ program for triangulating polyhedra. More generally, it can find a single triangulation as well as enumerate all triangulations of a "point configuration", that is, the convex hull of points in euclidean space such that all vertices of simplices of the triangulation are in the given (finite) list of points.

One problem with the upstream distribution is that it statically links many helper programs, yielding almost 200mb of binaries. Therefore, I suggest the following:

- dynamically link TOPCOM via libtools to reduce size
- Write a sage<->TOPCOM interface at sage.geometry.triangulation.py

As an initial submission, my libtoolized TOPCOM spkg is here:

http://www.stp.dias.ie/~vbraun/TOPCOM-0.16.2.spkg

and a first draft of triangulation.py is attached. The basic usage is


```
sage: points = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]]);
sage: points
A point configuration in QQ^2 consisting of 5 points.
sage: triang = points.triangulate()   # find one triangulation       
sage: triang
A triangulation in QQ^2 consisting of 4 simplices.
sage: triang.plot(axes=False)                                        
```


After we confirm that the libtoolized TOPCOM builds on all sage platforms, I'll contact upstream for eventual inclusion of the autotools sources.

Note: see #8115 for a modified cddlib (required by TOPCOM) that provides a non-static cddlib library.

Issue created by migration from https://trac.sagemath.org/ticket/8169





---

archive/issue_comments_071760.json:
```json
{
    "body": "This looks great.  I looked into TOPCOM briefly but because of its size and some build issues I gave up thinking about it.  I don't have time to review this week, but I will try to take a look at it soon.\n\n-Marshall",
    "created_at": "2010-02-03T13:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This looks great.  I looked into TOPCOM briefly but because of its size and some build issues I gave up thinking about it.  I don't have time to review this week, but I will try to take a look at it soon.

-Marshall



---

archive/issue_comments_071761.json:
```json
{
    "body": "Thanks to a contribution by Josh Whitney we can now compute volumes and the secondary polytope.\n\nStill todo: the TOPCOM spkg crashes when checking for coherency/regularity of a triangulation, investigating...",
    "created_at": "2010-06-05T12:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71761",
    "user": "https://github.com/vbraun"
}
```

Thanks to a contribution by Josh Whitney we can now compute volumes and the secondary polytope.

Still todo: the TOPCOM spkg crashes when checking for coherency/regularity of a triangulation, investigating...



---

archive/issue_comments_071762.json:
```json
{
    "body": "updated version",
    "created_at": "2010-06-05T12:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71762",
    "user": "https://github.com/vbraun"
}
```

updated version



---

archive/issue_comments_071763.json:
```json
{
    "body": "Attachment [triangulation.2.py](tarball://root/attachments/some-uuid/ticket8169/triangulation.2.py) by @vbraun created at 2010-06-05 20:04:42\n\nI fixed the segfaulting regularity check, it works for me now. Updated spkg is here:\n[http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p1.spkg](http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p1.spkg)\n\nAlso, doctests now all pass in the updated triangulation.py",
    "created_at": "2010-06-05T20:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71763",
    "user": "https://github.com/vbraun"
}
```

Attachment [triangulation.2.py](tarball://root/attachments/some-uuid/ticket8169/triangulation.2.py) by @vbraun created at 2010-06-05 20:04:42

I fixed the segfaulting regularity check, it works for me now. Updated spkg is here:
[http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p1.spkg](http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p1.spkg)

Also, doctests now all pass in the updated triangulation.py



---

archive/issue_comments_071764.json:
```json
{
    "body": "updated version",
    "created_at": "2010-06-05T20:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71764",
    "user": "https://github.com/vbraun"
}
```

updated version



---

archive/issue_comments_071765.json:
```json
{
    "body": "Attachment [triangulation.4.py](tarball://root/attachments/some-uuid/ticket8169/triangulation.4.py) by @vbraun created at 2010-08-09 19:38:14\n\nUpdated patch for timeout issue",
    "created_at": "2010-08-09T19:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71765",
    "user": "https://github.com/vbraun"
}
```

Attachment [triangulation.4.py](tarball://root/attachments/some-uuid/ticket8169/triangulation.4.py) by @vbraun created at 2010-08-09 19:38:14

Updated patch for timeout issue



---

archive/issue_comments_071766.json:
```json
{
    "body": "The previous version would raise `pexpect.TIMEOUT` after 30 seconds of computation. The new version will unconditionally wait for the computation to end. \n\nWhoever is interested in using it can now either apply `trac_8169_triangulate_using_TOPCOM.patch` or manually load the `triangulation.py` code as before.",
    "created_at": "2010-08-09T19:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71766",
    "user": "https://github.com/vbraun"
}
```

The previous version would raise `pexpect.TIMEOUT` after 30 seconds of computation. The new version will unconditionally wait for the computation to end. 

Whoever is interested in using it can now either apply `trac_8169_triangulate_using_TOPCOM.patch` or manually load the `triangulation.py` code as before.



---

archive/issue_comments_071767.json:
```json
{
    "body": "I get the following error when trying to install the spkg on a mac (10.5.8):\n\n```\nconfig.status: executing libtool commands\nCDPATH=\"${ZSH_VERSION+.}:\" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing --run aclocal-1.11 -I m4\n/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing: line 52: aclocal-1.11: command not found\nWARNING: `aclocal-1.11' is missing on your system.  You should only need it if\n         you modified `acinclude.m4' or `configure.ac'.  You might want\n         to install the `Automake' and `Perl' packages.  Grab them from\n         any GNU archive site.\n cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing --run automake-1.11 --gnu\n/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing: line 52: automake-1.11: command not found\nWARNING: `automake-1.11' is missing on your system.  You should only need it if\n         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.\n         You might want to install the `Automake' and `Perl' packages.\n         Grab them from any GNU archive site.\nCDPATH=\"${ZSH_VERSION+.}:\" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing --run autoconf\naclocal.m4:20: warning: this file was generated for autoconf 2.63.\nYou have another version of autoconf.  It may work, but is not guaranteed to.\nIf you have problems, you may need to regenerate the build system entirely.\nTo do so, use the procedure documented by the package, typically `autoreconf'.\n/usr/bin/gm4:aclocal.m4:953: cannot open `m4/ltoptions.m4': No such file or directory\nautom4te: /usr/bin/gm4 failed with exit status: 1\nmake: *** [configure] Error 1\nError building TOPCOM.\n```\n",
    "created_at": "2010-08-14T15:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71767",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I get the following error when trying to install the spkg on a mac (10.5.8):

```
config.status: executing libtool commands
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing --run aclocal-1.11 -I m4
/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing: line 52: aclocal-1.11: command not found
WARNING: `aclocal-1.11' is missing on your system.  You should only need it if
         you modified `acinclude.m4' or `configure.ac'.  You might want
         to install the `Automake' and `Perl' packages.  Grab them from
         any GNU archive site.
 cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing --run automake-1.11 --gnu
/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing: line 52: automake-1.11: command not found
WARNING: `automake-1.11' is missing on your system.  You should only need it if
         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.
         You might want to install the `Automake' and `Perl' packages.
         Grab them from any GNU archive site.
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2.p1/src/missing --run autoconf
aclocal.m4:20: warning: this file was generated for autoconf 2.63.
You have another version of autoconf.  It may work, but is not guaranteed to.
If you have problems, you may need to regenerate the build system entirely.
To do so, use the procedure documented by the package, typically `autoreconf'.
/usr/bin/gm4:aclocal.m4:953: cannot open `m4/ltoptions.m4': No such file or directory
autom4te: /usr/bin/gm4 failed with exit status: 1
make: *** [configure] Error 1
Error building TOPCOM.
```




---

archive/issue_comments_071768.json:
```json
{
    "body": "The `patches/autogenerated/m4` directory had symlinks to `/usr` instead of copies, this probably caused the build failure on OSX. I guess all previous users had `automake-1.11` already... I've updated the spkg, can you try the updated spkg at http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p2.spkg",
    "created_at": "2010-08-14T15:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71768",
    "user": "https://github.com/vbraun"
}
```

The `patches/autogenerated/m4` directory had symlinks to `/usr` instead of copies, this probably caused the build failure on OSX. I guess all previous users had `automake-1.11` already... I've updated the spkg, can you try the updated spkg at http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p2.spkg



---

archive/issue_comments_071769.json:
```json
{
    "body": "Great! That fixed it.  Patch applies fine too (to sage-4.5.2).\n\nI get the following coverage issues, which I would be happy to work on if you don't mind:\n\n\n```\nSCORE devel/sage-p1/sage/geometry//triangulation.py: 66% (14 of 21)\n\nMissing documentation:\n\t * __len__(self):\n\t * _TOPCOM_points(self):\n\t * liststring(container, conversion=str):\n\n\nMissing doctests:\n\t * __iter__(self):\n\t * __getitem__(self, i):\n\t * __init__(self, points, projective=False):\n\t * _repr_(self):\n\n\nPossibly wrong (function name doesn't occur in doctests):\n\t * _render_2d(triangulation, **kwds):\n\t * _render_3d(triangulation, **kwds):\n\t * _repr_(self):\n```\n",
    "created_at": "2010-08-14T16:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Great! That fixed it.  Patch applies fine too (to sage-4.5.2).

I get the following coverage issues, which I would be happy to work on if you don't mind:


```
SCORE devel/sage-p1/sage/geometry//triangulation.py: 66% (14 of 21)

Missing documentation:
	 * __len__(self):
	 * _TOPCOM_points(self):
	 * liststring(container, conversion=str):


Missing doctests:
	 * __iter__(self):
	 * __getitem__(self, i):
	 * __init__(self, points, projective=False):
	 * _repr_(self):


Possibly wrong (function name doesn't occur in doctests):
	 * _render_2d(triangulation, **kwds):
	 * _render_3d(triangulation, **kwds):
	 * _repr_(self):
```




---

archive/issue_comments_071770.json:
```json
{
    "body": "Feel free to make changes! I'm right now working on other tickets.",
    "created_at": "2010-08-14T16:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71770",
    "user": "https://github.com/vbraun"
}
```

Feel free to make changes! I'm right now working on other tickets.



---

archive/issue_comments_071771.json:
```json
{
    "body": "I'm getting lots of doctest failures; I think most of them are because points2placingtriang doesn't work:\n\n\n```\n(sage subshell) thorn:bin mh$ ./points2placingtriang\nBus error\n```\n\n\nI didn't see any errors relating to this during compilation; not sure what is going on.",
    "created_at": "2010-08-14T18:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I'm getting lots of doctest failures; I think most of them are because points2placingtriang doesn't work:


```
(sage subshell) thorn:bin mh$ ./points2placingtriang
Bus error
```


I didn't see any errors relating to this during compilation; not sure what is going on.



---

archive/issue_comments_071772.json:
```json
{
    "body": "A few comments. \n* There appears to be no code for 64-bit builds on systems which don't default to 64-bit, but want it. Take a look at spkg-install of the latest GSL library for an example how to do it. \n* There's no spkg-check file. It is possible to add one? I note you delete the examples, but often those can be used in tests of the package. \n* You appear to copy over configure.ac, but no configure script. Is that intentional? Whilst I agree configure.ac is the preferred usage over configure.in, I'm not sure its actually worth patching that. I think the patch will cause more confusion. If you have actually patched the file, then sure, call it configure.ac. But in that case the configure script will need to be updated too. \n* Since we don't ship GMP, I think the dependencies should list MPIR rather than GMP, or at least have a note like \"MPIR (used in Sage instead of GMP)\"",
    "created_at": "2010-08-14T23:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71772",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

A few comments. 
* There appears to be no code for 64-bit builds on systems which don't default to 64-bit, but want it. Take a look at spkg-install of the latest GSL library for an example how to do it. 
* There's no spkg-check file. It is possible to add one? I note you delete the examples, but often those can be used in tests of the package. 
* You appear to copy over configure.ac, but no configure script. Is that intentional? Whilst I agree configure.ac is the preferred usage over configure.in, I'm not sure its actually worth patching that. I think the patch will cause more confusion. If you have actually patched the file, then sure, call it configure.ac. But in that case the configure script will need to be updated too. 
* Since we don't ship GMP, I think the dependencies should list MPIR rather than GMP, or at least have a note like "MPIR (used in Sage instead of GMP)"



---

archive/issue_comments_071773.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-08-14T23:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71773",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_071774.json:
```json
{
    "body": "I'll try to add the 64-bit stuff and a spkg-check. The examples are huge (the upstream distribution is 22M gzipped), but we probably should keep some for the check. \n\nSince the intention is to eventually move the changes upstream I would prefer to move the deprecated `configure.in` to `configure.ac`. We do copy `patches/autogenerated/configure` over the configure script.\n\nAs for the bus error, I don't have a OSX machine to test on. But running points2placingtriangs in gdb and producing a stack trace would probably help.",
    "created_at": "2010-08-14T23:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71774",
    "user": "https://github.com/vbraun"
}
```

I'll try to add the 64-bit stuff and a spkg-check. The examples are huge (the upstream distribution is 22M gzipped), but we probably should keep some for the check. 

Since the intention is to eventually move the changes upstream I would prefer to move the deprecated `configure.in` to `configure.ac`. We do copy `patches/autogenerated/configure` over the configure script.

As for the bus error, I don't have a OSX machine to test on. But running points2placingtriangs in gdb and producing a stack trace would probably help.



---

archive/issue_comments_071775.json:
```json
{
    "body": "Replying to [comment:11 vbraun]:\n> I'll try to add the 64-bit stuff and a spkg-check. The examples are huge (the upstream distribution is 22M gzipped), but we probably should keep some for the check. \n\nI think we should keep them **all** for the check myself if they can be used in a check. The problem with the doc tests is that they test so little really in most cases. \n\n> Since the intention is to eventually move the changes upstream I would prefer to move the deprecated `configure.in` to `configure.ac`. We do copy `patches/autogenerated/configure` over the configure script.\n\nI must have missed that. \n \n> As for the bus error, I don't have a OSX machine to test on. But running points2placingtriangs in gdb and producing a stack trace would probably help.\n\nWilliam will give you access to bsd.math I expect. That runs OS X.",
    "created_at": "2010-08-14T23:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71775",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:11 vbraun]:
> I'll try to add the 64-bit stuff and a spkg-check. The examples are huge (the upstream distribution is 22M gzipped), but we probably should keep some for the check. 

I think we should keep them **all** for the check myself if they can be used in a check. The problem with the doc tests is that they test so little really in most cases. 

> Since the intention is to eventually move the changes upstream I would prefer to move the deprecated `configure.in` to `configure.ac`. We do copy `patches/autogenerated/configure` over the configure script.

I must have missed that. 
 
> As for the bus error, I don't have a OSX machine to test on. But running points2placingtriangs in gdb and producing a stack trace would probably help.

William will give you access to bsd.math I expect. That runs OS X.



---

archive/issue_comments_071776.json:
```json
{
    "body": "Changing component from algebra to geometry.",
    "created_at": "2010-09-02T10:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71776",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to geometry.



---

archive/issue_comments_071777.json:
```json
{
    "body": "I do not plan to review this ticket since it involves a package, but I'll allow myself some critical remarks anyway ;-)\n\n1. Module level description is probably not what it was supposed to be (\"all vertices of points\" does not quite make sense).\n2. It would be nice to explain what's the point of using projective coordinates even when the input is affine.\n3. I think it is counter-intuitive that iterating over a point configuration deals with projective coordinates and over its points - affine ones. If the default input is affine, I think that default iterating also should be over affine version with `points(projective=True)` returning projective coordinates.\n4. I personally don't like getting generators as output of methods like `points` and people less familiar with Python find it quite confusing. So I think it would be better to return a tuple (or a list, if it is not cached) and obtain a generator either using something like `point_generator()` method or by passing an optional argument like `points(generator=True)`. I understand that generators are more efficient, but when efficiency is an issue users should be willing to work a little harder to get them, while for interactive work and new users tuples and lists are more convenient.\n5. I like the interface to restricting type of triangulations, but it would be nice for each restricting function to have a precise definition of the corresponding triangulation type.\n\nP.S. My previous attempts to install and use TOPCOM didn't succeed, but with Volker's package installation was completely painless. So I hope that it will make its way into Sage in the near future!",
    "created_at": "2010-09-10T03:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71777",
    "user": "https://github.com/novoselt"
}
```

I do not plan to review this ticket since it involves a package, but I'll allow myself some critical remarks anyway ;-)

1. Module level description is probably not what it was supposed to be ("all vertices of points" does not quite make sense).
2. It would be nice to explain what's the point of using projective coordinates even when the input is affine.
3. I think it is counter-intuitive that iterating over a point configuration deals with projective coordinates and over its points - affine ones. If the default input is affine, I think that default iterating also should be over affine version with `points(projective=True)` returning projective coordinates.
4. I personally don't like getting generators as output of methods like `points` and people less familiar with Python find it quite confusing. So I think it would be better to return a tuple (or a list, if it is not cached) and obtain a generator either using something like `point_generator()` method or by passing an optional argument like `points(generator=True)`. I understand that generators are more efficient, but when efficiency is an issue users should be willing to work a little harder to get them, while for interactive work and new users tuples and lists are more convenient.
5. I like the interface to restricting type of triangulations, but it would be nice for each restricting function to have a precise definition of the corresponding triangulation type.

P.S. My previous attempts to install and use TOPCOM didn't succeed, but with Volker's package installation was completely painless. So I hope that it will make its way into Sage in the near future!



---

archive/issue_comments_071778.json:
```json
{
    "body": "4. I think thats fine with points, but triangulations should default to a generator. Almost always there will be a lot of them and we should train the user to not create an unpacked list of them all :-)\n\nOther TODO's:\n\n6. If the point configuration is not full-dimensional TOPCOM will refuse to work. We should keep an internal auxiliary copy of the point configuration on the spanned hyperplane.\n\n7. Implement the basic edge traversal algorithm on the secondary polytope without resorting to TOPCOM, hence making TOPCOM optional :-) This would really help in getting the triangulation code into Sage, I think.",
    "created_at": "2010-09-10T11:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71778",
    "user": "https://github.com/vbraun"
}
```

4. I think thats fine with points, but triangulations should default to a generator. Almost always there will be a lot of them and we should train the user to not create an unpacked list of them all :-)

Other TODO's:

6. If the point configuration is not full-dimensional TOPCOM will refuse to work. We should keep an internal auxiliary copy of the point configuration on the spanned hyperplane.

7. Implement the basic edge traversal algorithm on the secondary polytope without resorting to TOPCOM, hence making TOPCOM optional :-) This would really help in getting the triangulation code into Sage, I think.



---

archive/issue_comments_071779.json:
```json
{
    "body": "4. Good point, let triangulations be implemented as a generator. Looking at a list of triangulations is not enlightening anyway (in their default repr-output, that is).\n\n   7. In what sense it will make TOPCOM optional? If you already have both the point configuration and its secondary polytope?",
    "created_at": "2010-09-10T14:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71779",
    "user": "https://github.com/novoselt"
}
```

4. Good point, let triangulations be implemented as a generator. Looking at a list of triangulations is not enlightening anyway (in their default repr-output, that is).

   7. In what sense it will make TOPCOM optional? If you already have both the point configuration and its secondary polytope?



---

archive/issue_comments_071780.json:
```json
{
    "body": "I will post a patch improving the coverage sometime today (US Central time).\n\nI am wondering what the point of the function \"liststring\" is in the _TOPCOM_points method.  Seems like overkill to make this function given the very limited way its used.  \n\nI still haven't fixed the build on OS X; on the TOPCOM page it says \"The current version compiles successfully under Darwin gcc-4.0 and gcc-4.2 if you choose the -m32 or -m64 architecture manually for all libraries.\" - which maybe means that we need to add such flags somewhere.  I am not good with build issues though.",
    "created_at": "2010-09-11T14:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I will post a patch improving the coverage sometime today (US Central time).

I am wondering what the point of the function "liststring" is in the _TOPCOM_points method.  Seems like overkill to make this function given the very limited way its used.  

I still haven't fixed the build on OS X; on the TOPCOM page it says "The current version compiles successfully under Darwin gcc-4.0 and gcc-4.2 if you choose the -m32 or -m64 architecture manually for all libraries." - which maybe means that we need to add such flags somewhere.  I am not good with build issues though.



---

archive/issue_comments_071781.json:
```json
{
    "body": "I think this is a bug in the secondary polytope code, maybe from the optional argument reduce_dimension not being set correctly in the LatticePolytope call.\n\n\n```\nc = polytopes.n_cube(3)\np = PointConfiguration(c.vertices())\np.secondary_polytope()\n```\n\n\n...this results in:\n\n\n```\nRuntimeError: Error executing \"poly.x -fv\" for a polytope sequence!\nOutput:\npoly.x: Vertex.c:613: Finish_Find_Equations: Assertion `_V->nv<64' failed.\nAborted\n```\n\n\nA similar command with an octahedron instead of a cube works fine.",
    "created_at": "2010-09-11T19:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I think this is a bug in the secondary polytope code, maybe from the optional argument reduce_dimension not being set correctly in the LatticePolytope call.


```
c = polytopes.n_cube(3)
p = PointConfiguration(c.vertices())
p.secondary_polytope()
```


...this results in:


```
RuntimeError: Error executing "poly.x -fv" for a polytope sequence!
Output:
poly.x: Vertex.c:613: Finish_Find_Equations: Assertion `_V->nv<64' failed.
Aborted
```


A similar command with an octahedron instead of a cube works fine.



---

archive/issue_comments_071782.json:
```json
{
    "body": "Oops, I don't think my initial guess about the above problem was correct, since the octahedron secondary polytope is also in a larger ambient dimension.  Would it be OK to switch the secondary polytope to a Polyhedron instead of a lattice polytope?",
    "created_at": "2010-09-11T19:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Oops, I don't think my initial guess about the above problem was correct, since the octahedron secondary polytope is also in a larger ambient dimension.  Would it be OK to switch the secondary polytope to a Polyhedron instead of a lattice polytope?



---

archive/issue_comments_071783.json:
```json
{
    "body": "Yes, the secondary polytope needs to be returned as a Polyhedron to avoid the dimension and #of point restrictions of PALP.",
    "created_at": "2010-09-11T21:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71783",
    "user": "https://github.com/vbraun"
}
```

Yes, the secondary polytope needs to be returned as a Polyhedron to avoid the dimension and #of point restrictions of PALP.



---

archive/issue_comments_071784.json:
```json
{
    "body": "I was checking some things from the TOPCOM examples, and this seems odd:\n\n```\nsage: q = [[0,0,0,0,0,1],[1,1,1,1,1,1],[2,4,8,16,32,1],[3,9,27,81,243,1],[4,16,64,256,1024,1],[5,25,125,625,3125,1],[6,36,216,1296,7776,1],[7,49,343,2401,16807,1],[8,64,512,4096,32768,1],[9,81,729,6561,59049,1],[10,100,1000,10000,100000,1]]\nsage: p = PointConfiguration(q)\nsage: t = p.triangulations_list()\nsage: len(t)\n0\n```\n\n\nThis is a 5-dimensional point configuration with 11 points.  Shouldn't it have some triangulations?",
    "created_at": "2010-09-11T22:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I was checking some things from the TOPCOM examples, and this seems odd:

```
sage: q = [[0,0,0,0,0,1],[1,1,1,1,1,1],[2,4,8,16,32,1],[3,9,27,81,243,1],[4,16,64,256,1024,1],[5,25,125,625,3125,1],[6,36,216,1296,7776,1],[7,49,343,2401,16807,1],[8,64,512,4096,32768,1],[9,81,729,6561,59049,1],[10,100,1000,10000,100000,1]]
sage: p = PointConfiguration(q)
sage: t = p.triangulations_list()
sage: len(t)
0
```


This is a 5-dimensional point configuration with 11 points.  Shouldn't it have some triangulations?



---

archive/issue_comments_071785.json:
```json
{
    "body": "Here's a simpler example with similar problems.\n\n\n```\nsage: p = [[0,0,0,1],[0,3,0,1],[3,0,0,1],[0,0,1,1],[0,3,1,1],[3,0,1,1],[1,1,2,1]]\nsage: pc = PointConfiguration(p)\nsage: t = pc.triangulations_list()\nsage: len(t)\n0\n```\n\n\nAnd this blows up:\n\n\n```\nsage: pc.restrict_to_nonregular_triangulations()\nsage: t = pc.triangulations_list()\n```\n\n\nIs this the same problem that is noted by the line:\n# TOPCOM bug: points2alltriangs --nonregular does not work\n?",
    "created_at": "2010-09-11T22:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Here's a simpler example with similar problems.


```
sage: p = [[0,0,0,1],[0,3,0,1],[3,0,0,1],[0,0,1,1],[0,3,1,1],[3,0,1,1],[1,1,2,1]]
sage: pc = PointConfiguration(p)
sage: t = pc.triangulations_list()
sage: len(t)
0
```


And this blows up:


```
sage: pc.restrict_to_nonregular_triangulations()
sage: t = pc.triangulations_list()
```


Is this the same problem that is noted by the line:
# TOPCOM bug: points2alltriangs --nonregular does not work
?



---

archive/issue_comments_071786.json:
```json
{
    "body": "OK, I have to work on some other things now.  I didn't finish adding doctests to some of the restrict_to_* functions since I am a little stymied by failures.  My current version is:\n[http://sage.math.washington.edu/home/mhampton/triangulation_mh1.py](http://sage.math.washington.edu/home/mhampton/triangulation_mh1.py)",
    "created_at": "2010-09-11T23:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71786",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, I have to work on some other things now.  I didn't finish adding doctests to some of the restrict_to_* functions since I am a little stymied by failures.  My current version is:
[http://sage.math.washington.edu/home/mhampton/triangulation_mh1.py](http://sage.math.washington.edu/home/mhampton/triangulation_mh1.py)



---

archive/issue_comments_071787.json:
```json
{
    "body": "As a general PSA: please use the `pc.triangulate(verbose=True)` option when reporting bugs. \n\n* Your problem is point number 6. above. \n* Indeed, `points2alltriangs --nonregular` segfaults (as indicated by my comments in the source). There is a workaround already in place. But thats not the reason why it blows up in your example.\n\nI'll work on it later today.",
    "created_at": "2010-09-12T00:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71787",
    "user": "https://github.com/vbraun"
}
```

As a general PSA: please use the `pc.triangulate(verbose=True)` option when reporting bugs. 

* Your problem is point number 6. above. 
* Indeed, `points2alltriangs --nonregular` segfaults (as indicated by my comments in the source). There is a workaround already in place. But thats not the reason why it blows up in your example.

I'll work on it later today.



---

archive/issue_comments_071788.json:
```json
{
    "body": "Attachment [trac_8169_triangulate_using_TOPCOM.patch](tarball://root/attachments/some-uuid/ticket8169/trac_8169_triangulate_using_TOPCOM.patch) by @vbraun created at 2010-09-12 20:30:47\n\nUpdated patch",
    "created_at": "2010-09-12T20:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71788",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_8169_triangulate_using_TOPCOM.patch](tarball://root/attachments/some-uuid/ticket8169/trac_8169_triangulate_using_TOPCOM.patch) by @vbraun created at 2010-09-12 20:30:47

Updated patch



---

archive/issue_comments_071789.json:
```json
{
    "body": "Updated version",
    "created_at": "2010-09-12T20:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71789",
    "user": "https://github.com/vbraun"
}
```

Updated version



---

archive/issue_comments_071790.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-09-12T20:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71790",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_071791.json:
```json
{
    "body": "Attachment [triangulation.py](tarball://root/attachments/some-uuid/ticket8169/triangulation.py) by @vbraun created at 2010-09-12 20:41:48\n\nI've dealt with 3. and 4. in comment 15, and 6. in comment 16. Now generally tuples instead of lists are returned, and a new `class Point` is added which has methods for affine, projective, or reduced (with linearities removed) coordinates. This should also fix Marshall's problems.\n\nNow `PointConfiguration`/`Triangulation` have a Parent/Element relationship. In particular, the `PointConfiguration` is unique and immutable. The `restrict_to_...` interface for restricting the admissible triangulations has been slightly changed, and now returns a **new** `PointConfiguration`. I think that also fits better with the general Sage philosophy.",
    "created_at": "2010-09-12T20:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71791",
    "user": "https://github.com/vbraun"
}
```

Attachment [triangulation.py](tarball://root/attachments/some-uuid/ticket8169/triangulation.py) by @vbraun created at 2010-09-12 20:41:48

I've dealt with 3. and 4. in comment 15, and 6. in comment 16. Now generally tuples instead of lists are returned, and a new `class Point` is added which has methods for affine, projective, or reduced (with linearities removed) coordinates. This should also fix Marshall's problems.

Now `PointConfiguration`/`Triangulation` have a Parent/Element relationship. In particular, the `PointConfiguration` is unique and immutable. The `restrict_to_...` interface for restricting the admissible triangulations has been slightly changed, and now returns a **new** `PointConfiguration`. I think that also fits better with the general Sage philosophy.



---

archive/issue_comments_071792.json:
```json
{
    "body": "I've split off a self-contained triangulation module into #9918. This ticket will focus on getting the TOPCOM spkg build on all platforms. In particular, OSX seems to be broken at the moment. \n\nI still don't have access to an OSX machine, but will get this sorted out eventually...",
    "created_at": "2010-09-16T11:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71792",
    "user": "https://github.com/vbraun"
}
```

I've split off a self-contained triangulation module into #9918. This ticket will focus on getting the TOPCOM spkg build on all platforms. In particular, OSX seems to be broken at the moment. 

I still don't have access to an OSX machine, but will get this sorted out eventually...



---

archive/issue_comments_071793.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-26T16:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71793",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071794.json:
```json
{
    "body": "Ok, I got a Mac OS X machine (10.6.4, 64 bit) and TOPCOM compiles and runs fine, including the regular/nonregular checks. In particular, I don't get the \"bus error\". I also don't get the segfault with the nonregularity check any more. Marshall, can you try again? \n\nAll I did was refresh the automake files, maybe there was a bug in the older autotools that got fixed? I did upgrade from Fedora 12 -> Fedora 13 in the meantime.\n\nIn any case, doctests pass on OS X and Fedora 13 x86_64",
    "created_at": "2010-09-26T16:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71794",
    "user": "https://github.com/vbraun"
}
```

Ok, I got a Mac OS X machine (10.6.4, 64 bit) and TOPCOM compiles and runs fine, including the regular/nonregular checks. In particular, I don't get the "bus error". I also don't get the segfault with the nonregularity check any more. Marshall, can you try again? 

All I did was refresh the automake files, maybe there was a bug in the older autotools that got fixed? I did upgrade from Fedora 12 -> Fedora 13 in the meantime.

In any case, doctests pass on OS X and Fedora 13 x86_64



---

archive/issue_comments_071795.json:
```json
{
    "body": "Trying on OS X 10.5, against sage-4.6.alpha1, and using your http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p2.spkg, I get:\n\n\n```\nCDPATH=\"${ZSH_VERSION+.}:\" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing --run aclocal-1.11 -I m4\n/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing: line 46: aclocal-1.11: command not found\nWARNING: `aclocal-1.11' is missing on your system.  You should only need it if\n         you modified `acinclude.m4' or `configure.ac'.  You might want\n         to install the `Automake' and `Perl' packages.  Grab them from\n         any GNU archive site.\n cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing --run automake-1.11 --gnu\n/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing: line 46: automake-1.11: command not found\nWARNING: `automake-1.11' is missing on your system.  You should only need it if\n         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.\n         You might want to install the `Automake' and `Perl' packages.\n         Grab them from any GNU archive site.\nCDPATH=\"${ZSH_VERSION+.}:\" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing --run autoconf\naclocal.m4:20: warning: this file was generated for autoconf 2.63.\nYou have another version of autoconf.  It may work, but is not guaranteed to.\nIf you have problems, you may need to regenerate the build system entirely.\nTo do so, use the procedure documented by the package, typically `autoreconf'.\n/usr/bin/gm4:aclocal.m4:953: cannot open `m4/ltoptions.m4': No such file or directory\nautom4te: /usr/bin/gm4 failed with exit status: 1\nmake: *** [configure] Error 1\nError building TOPCOM.\n```\n",
    "created_at": "2010-09-26T16:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71795",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Trying on OS X 10.5, against sage-4.6.alpha1, and using your http://www.stp.dias.ie/~vbraun/Sage/spkg/TOPCOM-0.16.2.p2.spkg, I get:


```
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing --run aclocal-1.11 -I m4
/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing: line 46: aclocal-1.11: command not found
WARNING: `aclocal-1.11' is missing on your system.  You should only need it if
         you modified `acinclude.m4' or `configure.ac'.  You might want
         to install the `Automake' and `Perl' packages.  Grab them from
         any GNU archive site.
 cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing --run automake-1.11 --gnu
/Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing: line 46: automake-1.11: command not found
WARNING: `automake-1.11' is missing on your system.  You should only need it if
         you modified `Makefile.am', `acinclude.m4' or `configure.ac'.
         You might want to install the `Automake' and `Perl' packages.
         Grab them from any GNU archive site.
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/sh /Users/mh/sagestuff/sage-4-x/spkg/build/TOPCOM-0.16.2/src/missing --run autoconf
aclocal.m4:20: warning: this file was generated for autoconf 2.63.
You have another version of autoconf.  It may work, but is not guaranteed to.
If you have problems, you may need to regenerate the build system entirely.
To do so, use the procedure documented by the package, typically `autoreconf'.
/usr/bin/gm4:aclocal.m4:953: cannot open `m4/ltoptions.m4': No such file or directory
autom4te: /usr/bin/gm4 failed with exit status: 1
make: *** [configure] Error 1
Error building TOPCOM.
```




---

archive/issue_comments_071796.json:
```json
{
    "body": "Changing assignee from @aghitza to mhampton.",
    "created_at": "2010-09-26T16:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71796",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from @aghitza to mhampton.



---

archive/issue_comments_071797.json:
```json
{
    "body": "Changing assignee from mhampton to @vbraun.",
    "created_at": "2010-09-26T16:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mhampton to @vbraun.



---

archive/issue_comments_071798.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-26T18:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71798",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_071799.json:
```json
{
    "body": "The warnings are ok except for the \"cannot open m4/ltoptions.m4\"; This looks like you have the old version where I had not correctly packaged the m4/ directory. The current TOPCOM spkg should be 766185 bytes long. Can you double check that?",
    "created_at": "2010-09-26T18:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71799",
    "user": "https://github.com/vbraun"
}
```

The warnings are ok except for the "cannot open m4/ltoptions.m4"; This looks like you have the old version where I had not correctly packaged the m4/ directory. The current TOPCOM spkg should be 766185 bytes long. Can you double check that?



---

archive/issue_comments_071800.json:
```json
{
    "body": "OK, sorry about that.  I had some older versions lying around and mistakenly installed one of those.  The new one seems to build fine, but after installing 9918 it doesn't seem to work.  The first doctest failure looks like this:\n\n\n```\nsage -t  \"devel/sage-t2/sage/geometry/triangulation/base.pyx\"\n**********************************************************************\nFile \"/Users/mh/sagestuff/sage-4-x/devel/sage-t2/sage/geometry/triangulation/base.pyx\", line 259:\n    sage: p = PointConfiguration([[0, 1], [0, 0], [1, 0]])   # indirect doctest\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/mh/sagestuff/sage-4-x/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_12[2]>\", line 1, in <module>\n        p = PointConfiguration([[Integer(0), Integer(1)], [Integer(0), Integer(0)], [Integer(1), Integer(0)]])   # indirect doctest###line 259:\n    sage: p = PointConfiguration([[0, 1], [0, 0], [1, 0]])   # indirect doctest\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/misc/classcall_metaclass.py\", line 258, in __call__\n        return cls.__classcall__(cls, *args, **options)\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py\", line 759, in __classcall__\n        .__classcall__(cls, points, connected, fine, regular, star)\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/misc/cachefunc.py\", line 115, in __call__\n        w = self.f(*args, **kwds)\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/structure/unique_representation.py\", line 449, in __classcall__\n        instance = type.__call__(cls, *args, **options)\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py\", line 793, in __init__\n        self.set_engine()\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py\", line 821, in set_engine\n        self._use_TOPCOM = (engine=='TOPCOM') or (engine=='auto' and PointConfiguration._have_TOPCOM())\n      File \"/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py\", line 730, in _have_TOPCOM\n        except ExceptionPexpect:\n    NameError: global name 'ExceptionPexpect' is not defined\n**********************************************************************\n```\n",
    "created_at": "2010-09-26T18:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71800",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, sorry about that.  I had some older versions lying around and mistakenly installed one of those.  The new one seems to build fine, but after installing 9918 it doesn't seem to work.  The first doctest failure looks like this:


```
sage -t  "devel/sage-t2/sage/geometry/triangulation/base.pyx"
**********************************************************************
File "/Users/mh/sagestuff/sage-4-x/devel/sage-t2/sage/geometry/triangulation/base.pyx", line 259:
    sage: p = PointConfiguration([[0, 1], [0, 0], [1, 0]])   # indirect doctest
Exception raised:
    Traceback (most recent call last):
      File "/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4-x/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mh/sagestuff/sage-4-x/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[2]>", line 1, in <module>
        p = PointConfiguration([[Integer(0), Integer(1)], [Integer(0), Integer(0)], [Integer(1), Integer(0)]])   # indirect doctest###line 259:
    sage: p = PointConfiguration([[0, 1], [0, 0], [1, 0]])   # indirect doctest
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/misc/classcall_metaclass.py", line 258, in __call__
        return cls.__classcall__(cls, *args, **options)
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py", line 759, in __classcall__
        .__classcall__(cls, points, connected, fine, regular, star)
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/misc/cachefunc.py", line 115, in __call__
        w = self.f(*args, **kwds)
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/structure/unique_representation.py", line 449, in __classcall__
        instance = type.__call__(cls, *args, **options)
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py", line 793, in __init__
        self.set_engine()
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py", line 821, in set_engine
        self._use_TOPCOM = (engine=='TOPCOM') or (engine=='auto' and PointConfiguration._have_TOPCOM())
      File "/Users/mh/sagestuff/sage-4-x/local/lib/python/site-packages/sage/geometry/triangulation/point_configuration.py", line 730, in _have_TOPCOM
        except ExceptionPexpect:
    NameError: global name 'ExceptionPexpect' is not defined
**********************************************************************
```




---

archive/issue_comments_071801.json:
```json
{
    "body": "I tried installing the patch for this ticket but it seems to conflict with the one at 9918.  Are these out of sync now?  Sorry for my confusion.",
    "created_at": "2010-09-26T19:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71801",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I tried installing the patch for this ticket but it seems to conflict with the one at 9918.  Are these out of sync now?  Sorry for my confusion.



---

archive/issue_comments_071802.json:
```json
{
    "body": "I tried directly running points2facets from $SAGE_LOCAL/bin and got this:\n\n```\nsage-4-x: local/bin/points2facets \ndyld: Library not loaded: /Users/mh/sagestuff/sage-4.6.alpha0/local/lib/libgmpxx.3.dylib\n  Referenced from: /Users/mh/sagestuff/sage-4-x/local/bin/points2facets\n  Reason: image not found\nTrace/BPT trap\n```\n\n\nI had renamed my sage folder from \"sage-4.6.alpha0\" to \"sage-4-x\" after upgrading to 4.6.alpha1, and apparently that is causing some problems.  So I'll try this again with a cleaner 4.6.alpha1 but that will take me a while.",
    "created_at": "2010-09-26T19:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71802",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I tried directly running points2facets from $SAGE_LOCAL/bin and got this:

```
sage-4-x: local/bin/points2facets 
dyld: Library not loaded: /Users/mh/sagestuff/sage-4.6.alpha0/local/lib/libgmpxx.3.dylib
  Referenced from: /Users/mh/sagestuff/sage-4-x/local/bin/points2facets
  Reason: image not found
Trace/BPT trap
```


I had renamed my sage folder from "sage-4.6.alpha0" to "sage-4-x" after upgrading to 4.6.alpha1, and apparently that is causing some problems.  So I'll try this again with a cleaner 4.6.alpha1 but that will take me a while.



---

archive/issue_comments_071803.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-26T19:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71803",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071804.json:
```json
{
    "body": "Thanks for testing!\n\nThe precise version of the sage<->TOPCOM interface in #9918 should not matter. Of course you need *some* version, or there is no interface.\n\nIn case anyone else wants to give it a try: Since TOPCOM compiled correctly it should work.",
    "created_at": "2010-09-26T19:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71804",
    "user": "https://github.com/vbraun"
}
```

Thanks for testing!

The precise version of the sage<->TOPCOM interface in #9918 should not matter. Of course you need *some* version, or there is no interface.

In case anyone else wants to give it a try: Since TOPCOM compiled correctly it should work.



---

archive/issue_comments_071805.json:
```json
{
    "body": "To be more precise in my question:  should I ignore the patch http://trac.sagemath.org/sage_trac/attachment/ticket/8169/trac_8169_triangulate_using_TOPCOM.patch if I install the patch from #9918?",
    "created_at": "2010-09-26T19:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

To be more precise in my question:  should I ignore the patch http://trac.sagemath.org/sage_trac/attachment/ticket/8169/trac_8169_triangulate_using_TOPCOM.patch if I install the patch from #9918?



---

archive/issue_comments_071806.json:
```json
{
    "body": "Either patch should work should work for testing the TOPCOM spkg. You can't install both of them as they definitely conflict. If you have a choice, I would recommend using the newer one at #9918.",
    "created_at": "2010-09-26T20:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71806",
    "user": "https://github.com/vbraun"
}
```

Either patch should work should work for testing the TOPCOM spkg. You can't install both of them as they definitely conflict. If you have a choice, I would recommend using the newer one at #9918.



---

archive/issue_comments_071807.json:
```json
{
    "body": "I started with sage-4.6.alpha1 compiled from source on OS X 10.5.  After cloning I installed the TOPCOM package and the patch from 9918.  Everything seemed to compile OK with TOPCOM.\n\nIf I try to run one of the TOPCOM programs in $SAGE_ROOT/local/bin, I get a \"bus error\".  If I do \"sage -sh\" and try again, it seems to work.  But if I test geometry/triangulation/base.pyx or triangulation/point_configuration.py, everything fails.  So I think there is some sort of linking issue here.",
    "created_at": "2010-09-27T12:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71807",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I started with sage-4.6.alpha1 compiled from source on OS X 10.5.  After cloning I installed the TOPCOM package and the patch from 9918.  Everything seemed to compile OK with TOPCOM.

If I try to run one of the TOPCOM programs in $SAGE_ROOT/local/bin, I get a "bus error".  If I do "sage -sh" and try again, it seems to work.  But if I test geometry/triangulation/base.pyx or triangulation/point_configuration.py, everything fails.  So I think there is some sort of linking issue here.



---

archive/issue_comments_071808.json:
```json
{
    "body": "That sounds strange; can you post the output of `otool -L points2alltriangs` before running `sage -sh` (when you get the bus error) and `gcc --version`?",
    "created_at": "2010-09-27T13:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71808",
    "user": "https://github.com/vbraun"
}
```

That sounds strange; can you post the output of `otool -L points2alltriangs` before running `sage -sh` (when you get the bus error) and `gcc --version`?



---

archive/issue_comments_071809.json:
```json
{
    "body": "OK, here it is:\n\n\n```\nbin: otool -L points2alltriangs\npoints2alltriangs:\n\t/Users/mh/sagestuff/sage-4-x/local/lib/libcddgmp.0.dylib (compatibility version 1.0.0, current version 1.0.0)\n\t/Users/mh/sagestuff/sage-4-x/local/lib/libgmpxx.3.dylib (compatibility version 5.0.0, current version 5.6.0)\n\t/Users/mh/sagestuff/sage-4-x/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.6.0)\n\t/Users/mh/sagestuff/sage-4-x/local/lib/libTOPCOM.0.dylib (compatibility version 1.0.0, current version 1.0.0)\n\t/Users/mh/sagestuff/sage-4-x/local/lib/libCHECKREG.0.dylib (compatibility version 1.0.0, current version 1.0.0)\n\t/usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)\n\t/usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)\n\t/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.1.5)\n```\n\n\n\n```\nbin: gcc --version\ni686-apple-darwin9-gcc-4.0.1 (GCC) 4.0.1 (Apple Inc. build 5465)\nCopyright (C) 2005 Free Software Foundation, Inc.\nThis is free software; see the source for copying conditions.  There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n```\n",
    "created_at": "2010-09-28T00:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, here it is:


```
bin: otool -L points2alltriangs
points2alltriangs:
	/Users/mh/sagestuff/sage-4-x/local/lib/libcddgmp.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/Users/mh/sagestuff/sage-4-x/local/lib/libgmpxx.3.dylib (compatibility version 5.0.0, current version 5.6.0)
	/Users/mh/sagestuff/sage-4-x/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.6.0)
	/Users/mh/sagestuff/sage-4-x/local/lib/libTOPCOM.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/Users/mh/sagestuff/sage-4-x/local/lib/libCHECKREG.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)
	/usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.1.5)
```



```
bin: gcc --version
i686-apple-darwin9-gcc-4.0.1 (GCC) 4.0.1 (Apple Inc. build 5465)
Copyright (C) 2005 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```




---

archive/issue_comments_071810.json:
```json
{
    "body": "Sounds like it should work? Is this on `bsd.math`? Trying to debug this via trac is painfull... Maybe you can post a stack backtrace from gdb?",
    "created_at": "2010-09-28T10:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71810",
    "user": "https://github.com/vbraun"
}
```

Sounds like it should work? Is this on `bsd.math`? Trying to debug this via trac is painfull... Maybe you can post a stack backtrace from gdb?



---

archive/issue_comments_071811.json:
```json
{
    "body": "This works for me now on OS X 10.5.  Works for OS X 10.6 and linux, so I think this is OK for an optional spkg.",
    "created_at": "2011-01-13T02:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This works for me now on OS X 10.5.  Works for OS X 10.6 and linux, so I think this is OK for an optional spkg.



---

archive/issue_comments_071812.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T02:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71812",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071813.json:
```json
{
    "body": "Changing component from geometry to optional packages.",
    "created_at": "2011-01-27T14:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71813",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from geometry to optional packages.



---

archive/issue_events_008373.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-02-06T09:58:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8169#event-8373"
}
```



---

archive/issue_comments_071814.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-06T09:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8169#issuecomment-71814",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
