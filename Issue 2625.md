# Issue 2625: [with patch, needs review] BooleanPolynomial to Singular conversion

archive/issues_002625.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\n`BooleanPolynomialRing`\n* more general constructor\n* cover_ring\n* defining_ideal\n* _singular_init_\n* some whitespace changes for docstrings\n\n`MPolynomial`\n* is_homogenous\n\n`BooleanMonomial`\n* degree method (same as deg method)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2625\n\n",
    "created_at": "2008-03-21T01:52:52Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] BooleanPolynomial to Singular conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2625",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

`BooleanPolynomialRing`
* more general constructor
* cover_ring
* defining_ideal
* _singular_init_
* some whitespace changes for docstrings

`MPolynomial`
* is_homogenous

`BooleanMonomial`
* degree method (same as deg method)

Issue created by migration from https://trac.sagemath.org/ticket/2625





---

archive/issue_comments_017999.json:
```json
{
    "body": "Attachment [pb_singular.patch](tarball://root/attachments/some-uuid/ticket2625/pb_singular.patch) by @robertwb created at 2008-03-26 06:27:18\n\nI wasn't able to apply this to 2.10.4\n\n\n```\npatching file sage/rings/polynomial/pbori.pyx\nHunk #1 FAILED at 120\nHunk #2 FAILED at 148\n2 out of 11 hunks FAILED -- saving rejects to file sage/rings/polynomial/pbori.pyx.rej\nabort: patch failed to apply\n```\n\n\nare there other dependancies? \n\nLooking at the patch, it looks pretty good. The only comment I have is that __interface shouldn't have to be declared in `pbori.pxd`--it should already be there from ring.pxd",
    "created_at": "2008-03-26T06:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2625#issuecomment-17999",
    "user": "https://github.com/robertwb"
}
```

Attachment [pb_singular.patch](tarball://root/attachments/some-uuid/ticket2625/pb_singular.patch) by @robertwb created at 2008-03-26 06:27:18

I wasn't able to apply this to 2.10.4


```
patching file sage/rings/polynomial/pbori.pyx
Hunk #1 FAILED at 120
Hunk #2 FAILED at 148
2 out of 11 hunks FAILED -- saving rejects to file sage/rings/polynomial/pbori.pyx.rej
abort: patch failed to apply
```


are there other dependancies? 

Looking at the patch, it looks pretty good. The only comment I have is that __interface shouldn't have to be declared in `pbori.pxd`--it should already be there from ring.pxd



---

archive/issue_comments_018000.json:
```json
{
    "body": "(sorry about the underline, I meant to type `__interface`)",
    "created_at": "2008-03-26T06:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2625#issuecomment-18000",
    "user": "https://github.com/robertwb"
}
```

(sorry about the underline, I meant to type `__interface`)



---

archive/issue_comments_018001.json:
```json
{
    "body": "Replying to [comment:1 robertwb]:\n> I wasn't able to apply this to 2.10.4\n> \n> {{{\n> patching file sage/rings/polynomial/pbori.pyx\n> Hunk #1 FAILED at 120\n> Hunk #2 FAILED at 148\n> 2 out of 11 hunks FAILED -- saving rejects to file sage/rings/polynomial/pbori.pyx.rej\n> abort: patch failed to apply\n> }}}\n> \n> are there other dependancies? \n\nI just checked, this ticket depends on #2622 and #2611 . After these two have been applied it applies cleanly.\n\n> Looking at the patch, it looks pretty good. The only comment I have is that `__interface` shouldn't have to be declared in `pbori.pxd` -- it should already be there from `ring.pxd` \n\nIt isn't:\n\n```\nsage: search_src(\"__interface\")\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nstructure/sage_object.pyx:                X = self.__interface[I]\nstructure/sage_object.pyx:                    self.__interface = {}\nstructure/sage_object.pyx:                    # an __interface attribute.\nstructure/sage_object.pyx:                self.__interface[I] = X\nrings/polynomial/pbori.pyx:        self.__interface = {}\nrings/ring.pxd:    cdef public object __interface\nrings/polynomial/pbori.pxd:    cdef public object __interface\n```\n\n| SAGE Version 2.10.4, Release Date: 2008-03-17                      |\n| Type notebook() for the GUI, and license() for information.        |\nThat definition in `ring.pxd` is for `FiniteField`.",
    "created_at": "2008-03-26T11:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2625#issuecomment-18001",
    "user": "https://github.com/malb"
}
```

Replying to [comment:1 robertwb]:
> I wasn't able to apply this to 2.10.4
> 
> {{{
> patching file sage/rings/polynomial/pbori.pyx
> Hunk #1 FAILED at 120
> Hunk #2 FAILED at 148
> 2 out of 11 hunks FAILED -- saving rejects to file sage/rings/polynomial/pbori.pyx.rej
> abort: patch failed to apply
> }}}
> 
> are there other dependancies? 

I just checked, this ticket depends on #2622 and #2611 . After these two have been applied it applies cleanly.

> Looking at the patch, it looks pretty good. The only comment I have is that `__interface` shouldn't have to be declared in `pbori.pxd` -- it should already be there from `ring.pxd` 

It isn't:

```
sage: search_src("__interface")
----------------------------------------------------------------------
----------------------------------------------------------------------
structure/sage_object.pyx:                X = self.__interface[I]
structure/sage_object.pyx:                    self.__interface = {}
structure/sage_object.pyx:                    # an __interface attribute.
structure/sage_object.pyx:                self.__interface[I] = X
rings/polynomial/pbori.pyx:        self.__interface = {}
rings/ring.pxd:    cdef public object __interface
rings/polynomial/pbori.pxd:    cdef public object __interface
```

| SAGE Version 2.10.4, Release Date: 2008-03-17                      |
| Type notebook() for the GUI, and license() for information.        |
That definition in `ring.pxd` is for `FiniteField`.



---

archive/issue_comments_018002.json:
```json
{
    "body": "You are correct about `__interaface`, sorry. Still trying to figure out all the dependancies I need to test this (#2622 seems nontrivial).",
    "created_at": "2008-03-28T20:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2625#issuecomment-18002",
    "user": "https://github.com/robertwb"
}
```

You are correct about `__interaface`, sorry. Still trying to figure out all the dependancies I need to test this (#2622 seems nontrivial).



---

archive/issue_events_006130.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-04-01T13:17:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2625#event-6130"
}
```



---

archive/issue_comments_018003.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-04-01T13:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2625#issuecomment-18003",
    "user": "https://github.com/malb"
}
```

Resolution: wontfix



---

archive/issue_comments_018004.json:
```json
{
    "body": "Don't apply this patch, I'm splitting this up in the not PolyBoRi related parts and the PolyBoRi parts which I base on the 0.3.1 patch.",
    "created_at": "2008-04-01T13:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2625#issuecomment-18004",
    "user": "https://github.com/malb"
}
```

Don't apply this patch, I'm splitting this up in the not PolyBoRi related parts and the PolyBoRi parts which I base on the 0.3.1 patch.
