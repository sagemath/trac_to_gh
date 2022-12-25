# Issue 5758: weird "hello" bug in homset coerce!

archive/issues_005758.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @robertwb\n\nWith a 100% clean sage-3.4.1.rc2:\n\n```\nwstein@sage:~/build/sage-3.4.1.rc2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: ref\nsage: Zmod(8).lift() == 1\ninit_coerce() for  <class 'sage.categories.homset.Homset'>\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |\n| Type notebook() for the GUI, and license() for information.        |\n/scratch/wstein/sage/temp/sage.math.washington.edu/4833/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__richcmp__ (sage/rings/integer.c:7457)()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:5714)()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7434)()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:9262)()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:11046)()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:9337)()\n\n/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.init_coerce (sage/structure/parent.c:3085)()\n\nZeroDivisionError: hello\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5758\n\n",
    "created_at": "2009-04-11T18:03:27Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "weird \"hello\" bug in homset coerce!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5758",
    "user": "https://github.com/williamstein"
}
```
Assignee: @robertwb

CC:  @robertwb

With a 100% clean sage-3.4.1.rc2:

```
wstein@sage:~/build/sage-3.4.1.rc2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: ref
sage: Zmod(8).lift() == 1
init_coerce() for  <class 'sage.categories.homset.Homset'>
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
/scratch/wstein/sage/temp/sage.math.washington.edu/4833/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__richcmp__ (sage/rings/integer.c:7457)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:5714)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7434)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:9262)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:11046)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:9337)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.init_coerce (sage/structure/parent.c:3085)()

ZeroDivisionError: hello
```


Issue created by migration from https://trac.sagemath.org/ticket/5758





---

archive/issue_comments_044917.json:
```json
{
    "body": "NOTE: When this is fixed, be sure to add this test to rings/morphism.pyx:\n\n```\nsage: Zmod(8).lift() == 1\nFalse\n```\n\nSee #5756.",
    "created_at": "2009-04-11T18:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5758#issuecomment-44917",
    "user": "https://github.com/williamstein"
}
```

NOTE: When this is fixed, be sure to add this test to rings/morphism.pyx:

```
sage: Zmod(8).lift() == 1
False
```

See #5756.



---

archive/issue_comments_044918.json:
```json
{
    "body": "Bouncing to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5758#issuecomment-44918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bouncing to 3.4.2.

Cheers,

Michael



---

archive/issue_events_013501.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-13T03:39:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5758#event-13501"
}
```



---

archive/issue_comments_044919.json:
```json
{
    "body": "The cuplrit here is in parent.pyx, \n\n```\n    cdef int init_coerce(self, bint warn=True) except -1:\n        if self._coerce_from_hash is None:\n            if warn:\n                print \"init_coerce() for \", type(self)\n                raise ZeroDivisionError, \"hello\"\n        ...\n```\nI'm attaching a patch which I think fixes the problem, but maybe someone familiar with the coercion code should take a look.  (It's a one-line patch, plus the doctest that William requested.)",
    "created_at": "2009-07-21T21:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5758#issuecomment-44919",
    "user": "https://github.com/jhpalmieri"
}
```

The cuplrit here is in parent.pyx, 

```
    cdef int init_coerce(self, bint warn=True) except -1:
        if self._coerce_from_hash is None:
            if warn:
                print "init_coerce() for ", type(self)
                raise ZeroDivisionError, "hello"
        ...
```
I'm attaching a patch which I think fixes the problem, but maybe someone familiar with the coercion code should take a look.  (It's a one-line patch, plus the doctest that William requested.)



---

archive/issue_comments_044920.json:
```json
{
    "body": "Attachment [trac_5758-hello.patch](tarball://root/attachments/some-uuid/ticket5758/trac_5758-hello.patch) by @mwhansen created at 2009-09-08 23:46:01\n\nLooks good to me.",
    "created_at": "2009-09-08T23:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5758#issuecomment-44920",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5758-hello.patch](tarball://root/attachments/some-uuid/ticket5758/trac_5758-hello.patch) by @mwhansen created at 2009-09-08 23:46:01

Looks good to me.



---

archive/issue_events_013502.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T05:09:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5758#event-13502"
}
```



---

archive/issue_comments_044921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T05:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5758#issuecomment-44921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
