# Issue 6416: Use Frobby for monomial ideals

archive/issues_006416.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  drkirkby\n\nKeywords: monomial ideal, Hilbert series, Alexander dual\n\nThis spkg and patch updates the Frobby library that is already an optional component of Sage, and gives it a Cython interface to a shared library instead of the pexpect interface in the current Frobby spkg. It also exposes more functionality. Functionality not currently in sage:\n\n- Multigraded Hilbert-Poincare series\n- Alexander dual of monomial ideals (already in the previous Frobby spkg)\n- Maximal standard monomials of monomial ideals\n- Irreducible decomposition of monomial ideals\n- Optimization of any linear function over the maximal standard monomials of a monomial ideal using branch-and-bound.\n\nThe patch applies cleanly to Sage 4.0.1, and the spkg is at\n\n  http://www.daimi.au.dk/~bjarke/frobby-0.8.0.spkg\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6416\n\n",
    "created_at": "2009-06-25T21:37:20Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.4",
    "title": "Use Frobby for monomial ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6416",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: @malb

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


Issue created by migration from https://trac.sagemath.org/ticket/6416





---

archive/issue_comments_051425.json:
```json
{
    "body": "Attachment [cython_frobby_library.patch](tarball://root/attachments/some-uuid/ticket6416/cython_frobby_library.patch) by broune created at 2009-06-25 21:38:38",
    "created_at": "2009-06-25T21:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51425",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Attachment [cython_frobby_library.patch](tarball://root/attachments/some-uuid/ticket6416/cython_frobby_library.patch) by broune created at 2009-06-25 21:38:38



---

archive/issue_events_015120.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/broune",
    "created_at": "2009-06-26T08:33:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15120"
}
```



---

archive/issue_comments_051426.json:
```json
{
    "body": "Am I right to assume that the Cython interface would require Frobby to become a standard SPKG? If so, this needs a vote on [sage-devel]. To ask for a vote write an e-mail to [sage-devel] which answers the following questions:\n* what is Frobby and what is it good for?\n* Is it the best (open-source) package for this job?\n* Is Frobby's license compatible with Sage's?\n* Do we have upstream support (trivial :)?\n* On which platforms was it tested (OSX 32-bit and 64-bit, Linux 32-bit and 64-bit, Solaris)?",
    "created_at": "2009-07-16T12:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51426",
    "user": "https://github.com/malb"
}
```

Am I right to assume that the Cython interface would require Frobby to become a standard SPKG? If so, this needs a vote on [sage-devel]. To ask for a vote write an e-mail to [sage-devel] which answers the following questions:
* what is Frobby and what is it good for?
* Is it the best (open-source) package for this job?
* Is Frobby's license compatible with Sage's?
* Do we have upstream support (trivial :)?
* On which platforms was it tested (OSX 32-bit and 64-bit, Linux 32-bit and 64-bit, Solaris)?



---

archive/issue_comments_051427.json:
```json
{
    "body": "The vote is at http://groups.google.com/group/sage-devel/browse_thread/thread/ad427ae37c733c48",
    "created_at": "2009-07-16T13:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51427",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

The vote is at http://groups.google.com/group/sage-devel/browse_thread/thread/ad427ae37c733c48



---

archive/issue_comments_051428.json:
```json
{
    "body": "Although I know about as much as my dog about Solaris, I gave it a try on t2.  After downloading the 0.8.0 spkg from trac I did:\n\n```\nsage -sh\nexport GMPLIB=/home/wstein/sparc/sage-3.4.1.rc4-mark-gcc-4.3.3/local\n$MAKE library MODE=shared ldflags=\"$LDFLAGS\" GMP_INC_DIR=\"$GMPLIB\"\n```\n\nand things compiled well for a while until I got:\n\n```\ng++   -Wall -ansi -pedantic -I /home/wstein/sparc/sage-3.4.1.rc4-mark-gcc-4.3.3/local/include -Wno-uninitialized -Wno-unused-parameter -O2 -fPIC -c src/test/TestSuite.cpp -o bin/shared/test/TestSuite.o\nsrc/test/TestSuite.cpp: In member function \u2018void TestSuite::sortTests()\u2019:\nsrc/test/TestSuite.cpp:43: error: \u2018sort\u2019 was not declared in this scope\nmake: *** [bin/shared/test/TestSuite.o] Error 1\n```\n\n-Marshall",
    "created_at": "2009-07-16T17:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

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

archive/issue_comments_051429.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-08-16T03:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51429",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_051430.json:
```json
{
    "body": "Changing assignee from tbd to @malb.",
    "created_at": "2009-08-16T03:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51430",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @malb.



---

archive/issue_comments_051431.json:
```json
{
    "body": "I am marking this as \"needs work\" because of the Solaris issue.  (Maybe David Kirkby can figure this one out.)",
    "created_at": "2009-08-16T09:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51431",
    "user": "https://github.com/aghitza"
}
```

I am marking this as "needs work" because of the Solaris issue.  (Maybe David Kirkby can figure this one out.)



---

archive/issue_comments_051432.json:
```json
{
    "body": "Given that #13007 updates Frobby to 0.9.0, this ticket probably needs at least a little TLC.  But in principle the vote still stands, assuming Frobby ever gets to *optional* status (currently experimental).",
    "created_at": "2012-06-05T14:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51432",
    "user": "https://github.com/kcrisman"
}
```

Given that #13007 updates Frobby to 0.9.0, this ticket probably needs at least a little TLC.  But in principle the vote still stands, assuming Frobby ever gets to *optional* status (currently experimental).



---

archive/issue_comments_051433.json:
```json
{
    "body": "Note also that in the vote it was perhaps recommended that Frobby should have a Cython interface that allows it to still be an optional spkg.  It adds perhaps 5 minutes to build time on my medium-age Mac, though it adds less than 1 MB of source.",
    "created_at": "2012-06-05T14:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51433",
    "user": "https://github.com/kcrisman"
}
```

Note also that in the vote it was perhaps recommended that Frobby should have a Cython interface that allows it to still be an optional spkg.  It adds perhaps 5 minutes to build time on my medium-age Mac, though it adds less than 1 MB of source.



---

archive/issue_events_015121.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15121"
}
```



---

archive/issue_events_015122.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15122"
}
```



---

archive/issue_events_015123.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15123"
}
```



---

archive/issue_events_015124.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15124"
}
```



---

archive/issue_events_015125.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15125"
}
```



---

archive/issue_events_015126.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15126"
}
```



---

archive/issue_events_015127.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15127"
}
```



---

archive/issue_events_015128.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15128"
}
```



---

archive/issue_events_015129.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2018-09-11T16:00:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15129"
}
```



---

archive/issue_events_015130.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2018-09-11T16:00:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15130"
}
```



---

archive/issue_comments_051434.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2018-09-11T16:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51434",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_051435.json:
```json
{
    "body": "This ticket is about an old-style spkg for frobby version 0.8.0. We now have frobby 0.9.0 in a new-style sage package. I know that in some examples in which Singular fails with an int overflow, frobby starts to use very much memory and takes a very long time. Moreover, it seems that the computation of multivariate Hilbert series has a bug: Frobby uses the base ring of the polynomial ring as the base ring of the Hilbert series (but Hilbert series are supposed to have integral coefficients). Moreover, if one uses integral coefficients, the monomials that are not standard monomials appear with coefficient TWO, but should of course have coefficient zero, in the expansion of the multivariate Hilbert series.\n\n```\n  sage: R.<x,y,z,w>=QQ[]\n  sage: I = R*[x^3,x^2*y,x*z]\n  sage: D = ~PowerSeriesRing(QQ,'x,y,z,w')((x-1)*(y-1)*(z-1)*(w-1))\n  sage: frobby.hilbert(I)\n  x^3*y*z + x^3*y + x^3*z + x^2*y*z + x^3 + x^2*y + x*z + 1\n  sage: (frobby.hilbert(I)*D)[:4]\n  1 + x + y + z + w + x^2 + x*y + 2*x*z + x*w + y^2 + y*z + y*w + z^2 +\n  z*w + w^2 + 2*x^3 + 2*x^2*y + 2*x^2*z + x^2*w + x*y^2 + 2*x*y*z +\n  x*y*w + 2*x*z^2 + 2*x*z*w + x*w^2 + y^3 + y^2*z + y^2*w + y*z^2 +\n  y*z*w + y*w^2 + z^3 + z^2*w + z*w^2 + w^3 + O(x, y, z, w)^12\n```\n\nSo, I think that frobby should not be the default backend for Hilbert series.\n\nHowever, it may still be a good idea to provide a Cython interface. So, question: Should the Cython-interface part of the patch be changed into a branch?",
    "created_at": "2018-09-11T16:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6416#issuecomment-51435",
    "user": "https://github.com/simon-king-jena"
}
```

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



---

archive/issue_events_015131.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2018-09-11T16:00:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15131"
}
```



---

archive/issue_events_015132.json:
```json
{
    "actor": "https://github.com/simon-king-jena",
    "created_at": "2018-09-11T16:00:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6416",
    "milestone": "sage-8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6416#event-15132"
}
```
