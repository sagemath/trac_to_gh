# Issue 1396: Ideal.groebner_basis should accept keyword arguments for strategy parameters

archive/issues_001396.json:
```json
{
    "body": "Assignee: malb\n\ne.g. Singular supports `redTail` and such. We should provide a somewhat unified interface for those (probably modelled after whatever Singular provides).\n\nIssue created by migration from https://trac.sagemath.org/ticket/1396\n\n",
    "created_at": "2007-12-04T15:39:11Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Ideal.groebner_basis should accept keyword arguments for strategy parameters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1396",
    "user": "malb"
}
```
Assignee: malb

e.g. Singular supports `redTail` and such. We should provide a somewhat unified interface for those (probably modelled after whatever Singular provides).

Issue created by migration from https://trac.sagemath.org/ticket/1396





---

archive/issue_comments_008973.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8973",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008974.json:
```json
{
    "body": "Changing assignee from malb to john_perry.",
    "created_at": "2009-01-23T02:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8974",
    "user": "malb"
}
```

Changing assignee from malb to john_perry.



---

archive/issue_comments_008975.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-23T02:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8975",
    "user": "malb"
}
```

Changing status from assigned to new.



---

archive/issue_comments_008976.json:
```json
{
    "body": "Replying to [ticket:1396 malb]:\n> e.g. Singular supports `redTail` and such. We should provide a somewhat unified interface for those (probably modelled after whatever Singular provides).\n\nI have a version of this going now, with the behavior similar to what the ticket requests. However, would it be more desirable to allow the user's options to persist through several operations, using an interface such as (say)\n\n* `I.set_singular_option(\"lazy\"); I.groebner_basis()`\n\nrather than add arguments only to the Groebner basis command, such as\n\n* `I.groebner_basis(lazy=True)`",
    "created_at": "2009-01-23T09:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8976",
    "user": "john_perry"
}
```

Replying to [ticket:1396 malb]:
> e.g. Singular supports `redTail` and such. We should provide a somewhat unified interface for those (probably modelled after whatever Singular provides).

I have a version of this going now, with the behavior similar to what the ticket requests. However, would it be more desirable to allow the user's options to persist through several operations, using an interface such as (say)

* `I.set_singular_option("lazy"); I.groebner_basis()`

rather than add arguments only to the Groebner basis command, such as

* `I.groebner_basis(lazy=True)`



---

archive/issue_comments_008977.json:
```json
{
    "body": "Replying to [comment:3 john_perry]:\n> I.set_singular_option(\"lazy\"); I.groebner_basis()\n\nThat stuff somewhat works already:\n\n\n```\nsage: singular.option('lazy')\nsage: singular.option()\n//options: lazy redefine loadLib usage prompt\n```\n\n\nThe point of this ticket is that the user can be ignorant of the fact that (s)he is running Singular in the background and can specify options for a particular GB computation.",
    "created_at": "2009-01-23T09:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8977",
    "user": "malb"
}
```

Replying to [comment:3 john_perry]:
> I.set_singular_option("lazy"); I.groebner_basis()

That stuff somewhat works already:


```
sage: singular.option('lazy')
sage: singular.option()
//options: lazy redefine loadLib usage prompt
```


The point of this ticket is that the user can be ignorant of the fact that (s)he is running Singular in the background and can specify options for a particular GB computation.



---

archive/issue_comments_008978.json:
```json
{
    "body": "[with patch, needs work] Adds options to groebner_basis for lazy, redTail, redSB, and notSugar -- currently implemented for Singular only",
    "created_at": "2009-01-24T02:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8978",
    "user": "john_perry"
}
```

[with patch, needs work] Adds options to groebner_basis for lazy, redTail, redSB, and notSugar -- currently implemented for Singular only



---

archive/issue_comments_008979.json:
```json
{
    "body": "Attachment [singular_options.patch](tarball://root/attachments/some-uuid/ticket1396/singular_options.patch) by john_perry created at 2009-01-24 03:00:59",
    "created_at": "2009-01-24T03:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8979",
    "user": "john_perry"
}
```

Attachment [singular_options.patch](tarball://root/attachments/some-uuid/ticket1396/singular_options.patch) by john_perry created at 2009-01-24 03:00:59



---

archive/issue_comments_008980.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T03:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8980",
    "user": "john_perry"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008981.json:
```json
{
    "body": "Changing assignee from john_perry to malb.",
    "created_at": "2009-01-24T03:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8981",
    "user": "john_perry"
}
```

Changing assignee from john_perry to malb.



---

archive/issue_comments_008982.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-24T03:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8982",
    "user": "john_perry"
}
```

Changing status from assigned to new.



---

archive/issue_comments_008983.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-15T20:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8983",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_008984.json:
```json
{
    "body": "Changing keywords from \"\" to \"libSingular options\".",
    "created_at": "2010-07-15T20:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8984",
    "user": "SimonKing"
}
```

Changing keywords from "" to "libSingular options".



---

archive/issue_comments_008985.json:
```json
{
    "body": "This patch extends Martin's work on libSingular options. Now, the options `degBound` and `multBound` can be used. A decorator, applied to all relevant methods, ensures that standard options are used unless explicitly requested by setting named arguments -- even if outside the methods other options are set.\n\nThe options can be named in Python style (deg_bound) or in Singular style (`degBound`), at the user's choice.\n\nExamples:\n\n1. Degree bound\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: I = R*[x^3+y^2,x^2*y+1]\nsage: from sage.libs.singular.option import opt\n# Use prot and deg_bound\nsage: I.groebner_basis(prot=True, deg_bound=2)\nstd in (0),(x,y),(dp(2),C)\n[4294967295:2]3ss\n(S:1)-\nproduct criterion:0 chain criterion:0\n[x^3 + y^2, x^2*y + 1]\n\n# Set prot and degBound outside the method\nsage: opt['prot'] = True\n# Singular style name\nsage: opt['degBound'] = 2\n# ... but inside the method, standard options are used:\nsage: I.groebner_basis()\n[x^3 + y^2, x^2*y + 1, y^3 - x]\nsage: opt['prot']\nTrue\n# Python style name\nsage: opt['deg_bound']\n2\n\n# similarly in Singular, rather than libSingular\nsage: I.groebner_basis(algorithm='singular',deg_bound=2)\n[x^3 + y^2, x^2*y + 1]\nsage: singular.eval('degBound=2')\n'degBound=2;'\nsage: I.groebner_basis(algorithm='singular')\n[x^3 + y^2, x^2*y + 1, y^3 - x]\nsage: singular.eval('degBound')\n'2'\n```\n\n\n2. Multiplicity bound\n\n\n```\nsage: Rlocal.<x,y,z> = PolynomialRing(QQ, order='ds')\nsage: J = [x^7+y^7+z^6,x^6+y^8+z^7,x^7+y^5+z^8, x^2*y^3+y^2*z^3+x^3*z^2,x^3*y^2+y^3*z^2+x^2*z^3]*Rlocal\n# prot:\nsage: J.groebner_basis(prot=True)\nstd in basering\n[1048575:2]5(4)s(3)s6s7s8s(4)s(5)sH(13)9(3)sH(12)8(4)s(5).s.s9....sH(11)8.10\n(S:10)-----------\nproduct criterion:9 chain criterion:30\n[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]\n# bounding the multiplicity\nsage: J.groebner_basis(prot=True,mult_bound=100)\nstd in basering\n[1048575:2]5(4)s(3)s6s7s8s(4)s(5)sH(13)\n(S:5)------\nproduct criterion:7 chain criterion:7\n[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]\n\n# Set the multBound in Singular\nsage: singular.eval('multBound=100')\n'multBound=100;'\n# ... nevertheless, the default multBound=0 is used:\nsage: J.groebner_basis(algorithm='singular')\n[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]\nsage: singular.eval('multBound')\n'100'\n# ... unless requested otherwise\nsage: J.groebner_basis(algorithm='singular',mult_bound=100)\n[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]\n```\n\n\nI just verified that `sage -testall` passes. So, ready for review!\n\nOne remark: It turned out to be impossible to doctest `libSingular's` protocol output. I inserted examples with protocol in the documentation, for illustration, but don't test these. Of course, deg_bound and mult_bound is doctested.",
    "created_at": "2010-07-15T20:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8985",
    "user": "SimonKing"
}
```

This patch extends Martin's work on libSingular options. Now, the options `degBound` and `multBound` can be used. A decorator, applied to all relevant methods, ensures that standard options are used unless explicitly requested by setting named arguments -- even if outside the methods other options are set.

The options can be named in Python style (deg_bound) or in Singular style (`degBound`), at the user's choice.

Examples:

1. Degree bound


```
sage: R.<x,y> = QQ[]
sage: I = R*[x^3+y^2,x^2*y+1]
sage: from sage.libs.singular.option import opt
# Use prot and deg_bound
sage: I.groebner_basis(prot=True, deg_bound=2)
std in (0),(x,y),(dp(2),C)
[4294967295:2]3ss
(S:1)-
product criterion:0 chain criterion:0
[x^3 + y^2, x^2*y + 1]

# Set prot and degBound outside the method
sage: opt['prot'] = True
# Singular style name
sage: opt['degBound'] = 2
# ... but inside the method, standard options are used:
sage: I.groebner_basis()
[x^3 + y^2, x^2*y + 1, y^3 - x]
sage: opt['prot']
True
# Python style name
sage: opt['deg_bound']
2

# similarly in Singular, rather than libSingular
sage: I.groebner_basis(algorithm='singular',deg_bound=2)
[x^3 + y^2, x^2*y + 1]
sage: singular.eval('degBound=2')
'degBound=2;'
sage: I.groebner_basis(algorithm='singular')
[x^3 + y^2, x^2*y + 1, y^3 - x]
sage: singular.eval('degBound')
'2'
```


2. Multiplicity bound


```
sage: Rlocal.<x,y,z> = PolynomialRing(QQ, order='ds')
sage: J = [x^7+y^7+z^6,x^6+y^8+z^7,x^7+y^5+z^8, x^2*y^3+y^2*z^3+x^3*z^2,x^3*y^2+y^3*z^2+x^2*z^3]*Rlocal
# prot:
sage: J.groebner_basis(prot=True)
std in basering
[1048575:2]5(4)s(3)s6s7s8s(4)s(5)sH(13)9(3)sH(12)8(4)s(5).s.s9....sH(11)8.10
(S:10)-----------
product criterion:9 chain criterion:30
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]
# bounding the multiplicity
sage: J.groebner_basis(prot=True,mult_bound=100)
std in basering
[1048575:2]5(4)s(3)s6s7s8s(4)s(5)sH(13)
(S:5)------
product criterion:7 chain criterion:7
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]

# Set the multBound in Singular
sage: singular.eval('multBound=100')
'multBound=100;'
# ... nevertheless, the default multBound=0 is used:
sage: J.groebner_basis(algorithm='singular')
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]
sage: singular.eval('multBound')
'100'
# ... unless requested otherwise
sage: J.groebner_basis(algorithm='singular',mult_bound=100)
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]
```


I just verified that `sage -testall` passes. So, ready for review!

One remark: It turned out to be impossible to doctest `libSingular's` protocol output. I inserted examples with protocol in the documentation, for illustration, but don't test these. Of course, deg_bound and mult_bound is doctested.



---

archive/issue_comments_008986.json:
```json
{
    "body": "Attachment [trac1396-singular_options.patch](tarball://root/attachments/some-uuid/ticket1396/trac1396-singular_options.patch) by malb created at 2010-07-15 21:25:24\n\nReplaces the first patch. Full support for all Singular options in both Singular and libSingular",
    "created_at": "2010-07-15T21:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8986",
    "user": "malb"
}
```

Attachment [trac1396-singular_options.patch](tarball://root/attachments/some-uuid/ticket1396/trac1396-singular_options.patch) by malb created at 2010-07-15 21:25:24

Replaces the first patch. Full support for all Singular options in both Singular and libSingular



---

archive/issue_comments_008987.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T21:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8987",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_008988.json:
```json
{
    "body": "The patch looks good, is well documented, applies cleanly, doctests pass. My referee patch adds one whitespace character thus I feel I can give it a positive review.",
    "created_at": "2010-07-15T21:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8988",
    "user": "malb"
}
```

The patch looks good, is well documented, applies cleanly, doctests pass. My referee patch adds one whitespace character thus I feel I can give it a positive review.



---

archive/issue_comments_008989.json:
```json
{
    "body": "Applying [attachment:trac1396-singular_options.patch] to a long queue of other patches I've put together for 4.5.2.alpha0, I get\n\n```\n$ hg qpush\napplying trac1396-singular_options.patch\npatching file sage/libs/singular/singular-cdefs.pxi\nHunk #2 FAILED at 993\n1 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac1396-singular_options.patch\n```\n\nEarlier tickets in the queue include #6922 and #9499.  Since `sage/libs/singular/singular-cdefs.pxi.rej` contains just\n\n```diff\n--- singular-cdefs.pxi\n+++ singular-cdefs.pxi\n@@ -995,8 +994,6 @@\n     poly *prCopyR_NoSort(poly *p, ring *r, ring *dest_r)\n     poly *prCopyR(poly *p, ring *r, ring *dest_r)\n \n-\n-\n     cdef int LANG_TOP\n \n cdef extern from \"stairc.h\":\n```\n\nI'll ignore the rejects, refresh the patch, and attach the refreshed patch here.  Please let me know if this is a problem.",
    "created_at": "2010-07-21T01:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8989",
    "user": "mpatel"
}
```

Applying [attachment:trac1396-singular_options.patch] to a long queue of other patches I've put together for 4.5.2.alpha0, I get

```
$ hg qpush
applying trac1396-singular_options.patch
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #2 FAILED at 993
1 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac1396-singular_options.patch
```

Earlier tickets in the queue include #6922 and #9499.  Since `sage/libs/singular/singular-cdefs.pxi.rej` contains just

```diff
--- singular-cdefs.pxi
+++ singular-cdefs.pxi
@@ -995,8 +994,6 @@
     poly *prCopyR_NoSort(poly *p, ring *r, ring *dest_r)
     poly *prCopyR(poly *p, ring *r, ring *dest_r)
 
-
-
     cdef int LANG_TOP
 
 cdef extern from "stairc.h":
```

I'll ignore the rejects, refresh the patch, and attach the refreshed patch here.  Please let me know if this is a problem.



---

archive/issue_comments_008990.json:
```json
{
    "body": "Attachment [trac1396-singular_options.2.patch](tarball://root/attachments/some-uuid/ticket1396/trac1396-singular_options.2.patch) by mpatel created at 2010-07-21 01:19:31\n\nRebased for 4.5.2.alpha0 queue.  See comment 9.  Replaces all previous patches.",
    "created_at": "2010-07-21T01:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8990",
    "user": "mpatel"
}
```

Attachment [trac1396-singular_options.2.patch](tarball://root/attachments/some-uuid/ticket1396/trac1396-singular_options.2.patch) by mpatel created at 2010-07-21 01:19:31

Rebased for 4.5.2.alpha0 queue.  See comment 9.  Replaces all previous patches.



---

archive/issue_comments_008991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8991",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_008992.json:
```json
{
    "body": "This ticket *might* be the source of an \"Unhandled SIGSEGV\" on t2.  Please see #9583, a blocker for Sage 4.5.2.",
    "created_at": "2010-07-24T00:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8992",
    "user": "mpatel"
}
```

This ticket *might* be the source of an "Unhandled SIGSEGV" on t2.  Please see #9583, a blocker for Sage 4.5.2.



---

archive/issue_comments_008993.json:
```json
{
    "body": "Perhaps I didn't rebase the patch properly?",
    "created_at": "2010-07-24T00:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8993",
    "user": "mpatel"
}
```

Perhaps I didn't rebase the patch properly?



---

archive/issue_comments_008994.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> This ticket *might* be the source of an \"Unhandled SIGSEGV\" on t2.  Please see #9583, a blocker for Sage 4.5.2.\n\nBacking out the patch does allow Sage to start on t2.math, so for 4.5.2, I'm going to yank this patch, and open another ticket; this patch can go back in, along with the necessary spkg, in the next release. Sorry.\n\nWe don't have an \"unmerged in:\" field, but this patch is getting \"unmerged\" in 4.5.2.alpha1.",
    "created_at": "2010-07-26T07:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8994",
    "user": "ddrake"
}
```

Replying to [comment:11 mpatel]:
> This ticket *might* be the source of an "Unhandled SIGSEGV" on t2.  Please see #9583, a blocker for Sage 4.5.2.

Backing out the patch does allow Sage to start on t2.math, so for 4.5.2, I'm going to yank this patch, and open another ticket; this patch can go back in, along with the necessary spkg, in the next release. Sorry.

We don't have an "unmerged in:" field, but this patch is getting "unmerged" in 4.5.2.alpha1.



---

archive/issue_comments_008995.json:
```json
{
    "body": "The new ticket is #9599.",
    "created_at": "2010-07-26T08:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8995",
    "user": "ddrake"
}
```

The new ticket is #9599.



---

archive/issue_comments_008996.json:
```json
{
    "body": "Replying to [comment:13 ddrake]:\n> Replying to [comment:11 mpatel]:\n> > This ticket *might* be the source of an \"Unhandled SIGSEGV\" on t2.  Please see #9583, a blocker for Sage 4.5.2.\n> \n> Backing out the patch does allow Sage to start on t2.math, so for 4.5.2, I'm going to yank this patch, and open another ticket; this patch can go back in, along with the necessary spkg, in the next release. Sorry.\n> \n> We don't have an \"unmerged in:\" field, but this patch is getting \"unmerged\" in 4.5.2.alpha1.\n\nShould it not be set back to \"needs work\" then? That seems the most accurate description of the status - more accurate so than \"fixed\". \n\nDave",
    "created_at": "2010-08-02T16:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8996",
    "user": "drkirkby"
}
```

Replying to [comment:13 ddrake]:
> Replying to [comment:11 mpatel]:
> > This ticket *might* be the source of an "Unhandled SIGSEGV" on t2.  Please see #9583, a blocker for Sage 4.5.2.
> 
> Backing out the patch does allow Sage to start on t2.math, so for 4.5.2, I'm going to yank this patch, and open another ticket; this patch can go back in, along with the necessary spkg, in the next release. Sorry.
> 
> We don't have an "unmerged in:" field, but this patch is getting "unmerged" in 4.5.2.alpha1.

Should it not be set back to "needs work" then? That seems the most accurate description of the status - more accurate so than "fixed". 

Dave



---

archive/issue_comments_008997.json:
```json
{
    "body": "> Should it not be set back to \"needs work\" then? That seems the most accurate description of the status - more accurate so than \"fixed\".\n\nI think we should just change focus to #9599, the new ticket for re-merging this patch.",
    "created_at": "2010-08-03T23:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8997",
    "user": "jhpalmieri"
}
```

> Should it not be set back to "needs work" then? That seems the most accurate description of the status - more accurate so than "fixed".

I think we should just change focus to #9599, the new ticket for re-merging this patch.



---

archive/issue_comments_008998.json:
```json
{
    "body": "Resolution changed from fixed to duplicate",
    "created_at": "2011-01-23T20:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1396#issuecomment-8998",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to duplicate
