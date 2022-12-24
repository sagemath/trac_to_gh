# Issue 7890: [new] Improve conversion of GAP objects into sage objects.

archive/issues_007890.json:
```json
{
    "body": "Assignee: was\n\nAs of now, certain kinds of sage objects can be converted into GAP objects, but the resulting GAP objects cannot be converted back to sage objects.\n\nExamples of this are matrices over finite fields:\n\n\n```\nsage: g = matrix(GF(5),2,[1,2, -1, 1])\nsage: gg = g._gap_()\nsage: gg.sage()\n---------------------------------------------------------------------------\nNotImplementedError\n```\n\n\n\n```\nsage: a = gap('E(9)')\nsage: a\n-E(9)^4-E(9)^7\nsage: a.sage()\n---------------------------------------------------------------------------\nNotImplementedError  \n```\n\n\nBeing able to translate gap field elements into sage ones would help accesing GAP character tables, and a good conversion of matrices would allow many methods to be available for matrix groups.\n\nSee this thread at sage devel for more details:\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a04006e5da578bd\n\nIssue created by migration from https://trac.sagemath.org/ticket/7890\n\n",
    "created_at": "2010-01-10T10:45:46Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[new] Improve conversion of GAP objects into sage objects.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7890",
    "user": "jlopez"
}
```
Assignee: was

As of now, certain kinds of sage objects can be converted into GAP objects, but the resulting GAP objects cannot be converted back to sage objects.

Examples of this are matrices over finite fields:


```
sage: g = matrix(GF(5),2,[1,2, -1, 1])
sage: gg = g._gap_()
sage: gg.sage()
---------------------------------------------------------------------------
NotImplementedError
```



```
sage: a = gap('E(9)')
sage: a
-E(9)^4-E(9)^7
sage: a.sage()
---------------------------------------------------------------------------
NotImplementedError  
```


Being able to translate gap field elements into sage ones would help accesing GAP character tables, and a good conversion of matrices would allow many methods to be available for matrix groups.

See this thread at sage devel for more details:
http://groups.google.com/group/sage-devel/browse_thread/thread/a04006e5da578bd

Issue created by migration from https://trac.sagemath.org/ticket/7890





---

archive/issue_comments_068632.json:
```json
{
    "body": "Added a _sage_ method in GapElement class (gap.py) that tries to convert matrices into sage matrices. This only work if the coefficient ring can be converted into a sage ring. Also, modified _matrix_ in the same class so that it tries to find a ring if none is given.",
    "created_at": "2010-01-10T15:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68632",
    "user": "jlopez"
}
```

Added a _sage_ method in GapElement class (gap.py) that tries to convert matrices into sage matrices. This only work if the coefficient ring can be converted into a sage ring. Also, modified _matrix_ in the same class so that it tries to find a ring if none is given.



---

archive/issue_comments_068633.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-10T15:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68633",
    "user": "jlopez"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068634.json:
```json
{
    "body": "Attachment [13590.patch](tarball://root/attachments/some-uuid/ticket7890/13590.patch) by jlopez created at 2010-01-10 15:55:11",
    "created_at": "2010-01-10T15:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68634",
    "user": "jlopez"
}
```

Attachment [13590.patch](tarball://root/attachments/some-uuid/ticket7890/13590.patch) by jlopez created at 2010-01-10 15:55:11



---

archive/issue_comments_068635.json:
```json
{
    "body": "Conversion for finite and cyclotomic fields and their elements.",
    "created_at": "2010-01-12T00:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68635",
    "user": "jlopez"
}
```

Conversion for finite and cyclotomic fields and their elements.



---

archive/issue_comments_068636.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-12T00:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68636",
    "user": "jlopez"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068637.json:
```json
{
    "body": "Attachment [13591.patch](tarball://root/attachments/some-uuid/ticket7890/13591.patch) by jlopez created at 2010-01-12 00:13:29\n\nThe patches should be applied in order.\nThis provides conversion of finite fields, cyclotomic fields and their elements, as well as gap matrices.",
    "created_at": "2010-01-12T00:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68637",
    "user": "jlopez"
}
```

Attachment [13591.patch](tarball://root/attachments/some-uuid/ticket7890/13591.patch) by jlopez created at 2010-01-12 00:13:29

The patches should be applied in order.
This provides conversion of finite fields, cyclotomic fields and their elements, as well as gap matrices.



---

archive/issue_comments_068638.json:
```json
{
    "body": "Simplification of one of the previous functions",
    "created_at": "2010-01-12T00:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68638",
    "user": "jlopez"
}
```

Simplification of one of the previous functions



---

archive/issue_comments_068639.json:
```json
{
    "body": "Attachment [13592.patch](tarball://root/attachments/some-uuid/ticket7890/13592.patch) by jlopez created at 2010-01-12 00:39:06\n\nFurther simplifications and merging. Apply only this patch.",
    "created_at": "2010-01-12T00:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68639",
    "user": "jlopez"
}
```

Attachment [13592.patch](tarball://root/attachments/some-uuid/ticket7890/13592.patch) by jlopez created at 2010-01-12 00:39:06

Further simplifications and merging. Apply only this patch.



---

archive/issue_comments_068640.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-12T03:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68640",
    "user": "wdj"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068641.json:
```json
{
    "body": "Attachment [gap_to_sage.patch](tarball://root/attachments/some-uuid/ticket7890/gap_to_sage.patch) by wdj created at 2010-01-12 03:06:28\n\nLast patch applied fine to sage-4.3.a0 on a 64bit ubuntu machine, but the following tests failed:\n\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/groups/perm_gps/permgroup.py\"\n        sage -t  \"devel/sage/sage/structure/parent.pyx\"\n        sage -t  \"devel/sage/sage/structure/parent_old.pyx\"\n        sage -t  \"devel/sage/sage/misc/sagedoc.py\"\n        sage -t  \"devel/sage/sage/misc/sage_eval.py\"\n\n```\n",
    "created_at": "2010-01-12T03:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68641",
    "user": "wdj"
}
```

Attachment [gap_to_sage.patch](tarball://root/attachments/some-uuid/ticket7890/gap_to_sage.patch) by wdj created at 2010-01-12 03:06:28

Last patch applied fine to sage-4.3.a0 on a 64bit ubuntu machine, but the following tests failed:


```
The following tests failed:


        sage -t  "devel/sage/sage/groups/perm_gps/permgroup.py"
        sage -t  "devel/sage/sage/structure/parent.pyx"
        sage -t  "devel/sage/sage/structure/parent_old.pyx"
        sage -t  "devel/sage/sage/misc/sagedoc.py"
        sage -t  "devel/sage/sage/misc/sage_eval.py"

```




---

archive/issue_comments_068642.json:
```json
{
    "body": "Hi Javier,\n\nWhat are your intentions regarding http://trac.sagemath.org/sage_trac/ticket/7890\nIt seems to have got dropped over two years ago.  Now none of the patches apply to recent\nversions of Sage.  I wonder if you're planning to clean this up and finish it?\n\n -- William",
    "created_at": "2012-03-19T20:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68642",
    "user": "was"
}
```

Hi Javier,

What are your intentions regarding http://trac.sagemath.org/sage_trac/ticket/7890
It seems to have got dropped over two years ago.  Now none of the patches apply to recent
versions of Sage.  I wonder if you're planning to clean this up and finish it?

 -- William



---

archive/issue_comments_068643.json:
```json
{
    "body": "Hi William,\n\nyeah, sorry about that. I changed jobs in 2010 and my whole work plan went south.\nI would like to get this thing working eventually, but I don't believe the approach I was trying is a good one. The lack of types in GAP creates some ambiguity in gap elements that can have different parents and where a choice needs to be made.\n\nProbably a better approach would be to provide an optional argument `sage_parent` to the `_sage_` function in GapElement, and then put the heavy lift into the sage parent where an ad-hoc gap-to-sage function can be defined, something like this:\n\n\n```\ndef _sage_(self, sage_parent = None):\n    if sage_parent is not None:\n        return sage_parent._call_from_gap(self)\n    else:\n        .... # The function as it used to work\n\n```\n\n\nIn this way, anyone creating a sage structure could implement their own \"take an element from gap here\" function rather than mess up with the interface. How does that sound?\n\nIn any case it might make sense to wait a little bit and get GAP 4.5 working first, as it seems [the representation of some objects has changed](http://www.gap-system.org/Manuals/doc/changes/chap2.html).",
    "created_at": "2012-06-15T07:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68643",
    "user": "jlopez"
}
```

Hi William,

yeah, sorry about that. I changed jobs in 2010 and my whole work plan went south.
I would like to get this thing working eventually, but I don't believe the approach I was trying is a good one. The lack of types in GAP creates some ambiguity in gap elements that can have different parents and where a choice needs to be made.

Probably a better approach would be to provide an optional argument `sage_parent` to the `_sage_` function in GapElement, and then put the heavy lift into the sage parent where an ad-hoc gap-to-sage function can be defined, something like this:


```
def _sage_(self, sage_parent = None):
    if sage_parent is not None:
        return sage_parent._call_from_gap(self)
    else:
        .... # The function as it used to work

```


In this way, anyone creating a sage structure could implement their own "take an element from gap here" function rather than mess up with the interface. How does that sound?

In any case it might make sense to wait a little bit and get GAP 4.5 working first, as it seems [the representation of some objects has changed](http://www.gap-system.org/Manuals/doc/changes/chap2.html).



---

archive/issue_comments_068644.json:
```json
{
    "body": "Hello,\n\nWith #18152, it works fine for cyclotomic elements (because I introduced a function `E` in the global namespace)\n\n```\nsage: a = gap('E(9)')\nsage: a.sage()\n-E(9)^4 - E(9)^7\n```\n\n\nVincent",
    "created_at": "2015-04-09T22:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68644",
    "user": "vdelecroix"
}
```

Hello,

With #18152, it works fine for cyclotomic elements (because I introduced a function `E` in the global namespace)

```
sage: a = gap('E(9)')
sage: a.sage()
-E(9)^4 - E(9)^7
```


Vincent



---

archive/issue_comments_068645.json:
```json
{
    "body": "Note that with the new `libgap` the conversion works almost fine for matrices (it is converted into a list of lists instead of a matrix)\n\n```\nsage: m = matrix(GF(5), 2, [1,2,-1,1])\nsage: a = m._libgap_().sage()\nsage: a\n[[1, 2], [4, 1]]\nsage: matrix(a) == m\nTrue\n```\n",
    "created_at": "2015-04-11T22:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7890#issuecomment-68645",
    "user": "vdelecroix"
}
```

Note that with the new `libgap` the conversion works almost fine for matrices (it is converted into a list of lists instead of a matrix)

```
sage: m = matrix(GF(5), 2, [1,2,-1,1])
sage: a = m._libgap_().sage()
sage: a
[[1, 2], [4, 1]]
sage: matrix(a) == m
True
```

