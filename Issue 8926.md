# Issue 8926: Family cannot completely handle a class as an argument

archive/issues_008926.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\n\n```\nsage: F = Family(NonNegativeIntegers(), PerfectMatchings)\nsage: F\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\n/home/saliola/Applications/sage-4.4/local/lib/python2.6/site-packages/sage/sets/family.pyc in _repr_(self)\n    873             name = name+\"(i)\"\n    874         else:\n--> 875             name = self.function.__repr__()\n    876             if isinstance(self.function, AttrCallObject):\n    877                 name = \"i\"+name[1:]\n\nTypeError: descriptor '__repr__' of 'sage.structure.sage_object.SageObject' object needs an argument\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8926\n\n",
    "created_at": "2010-05-07T20:32:47Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Family cannot completely handle a class as an argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8926",
    "user": "https://github.com/saliola"
}
```
Assignee: sage-combinat

CC:  sage-combinat


```
sage: F = Family(NonNegativeIntegers(), PerfectMatchings)
sage: F
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
/home/saliola/Applications/sage-4.4/local/lib/python2.6/site-packages/sage/sets/family.pyc in _repr_(self)
    873             name = name+"(i)"
    874         else:
--> 875             name = self.function.__repr__()
    876             if isinstance(self.function, AttrCallObject):
    877                 name = "i"+name[1:]

TypeError: descriptor '__repr__' of 'sage.structure.sage_object.SageObject' object needs an argument
```



Issue created by migration from https://trac.sagemath.org/ticket/8926





---

archive/issue_comments_082098.json:
```json
{
    "body": "Attachment [trac_8926_family_repr-fh.patch](tarball://root/attachments/some-uuid/ticket8926/trac_8926_family_repr-fh.patch) by @hivert created at 2010-05-07 23:02:25",
    "created_at": "2010-05-07T23:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82098",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8926_family_repr-fh.patch](tarball://root/attachments/some-uuid/ticket8926/trac_8926_family_repr-fh.patch) by @hivert created at 2010-05-07 23:02:25



---

archive/issue_comments_082099.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-07T23:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82099",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082100.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T17:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82100",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082101.json:
```json
{
    "body": "From a private e-mail from Nicolas M. Thi\u00e9ry:\n\n```\n - trac_8926_family_repr-fh.patch   # Positive review, assuming test pass\n```\n\nWe had a all tests passed on the server massena. Therefore I allow myself to put a positive review on behalf of Nicolas.",
    "created_at": "2010-05-12T17:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82101",
    "user": "https://github.com/hivert"
}
```

From a private e-mail from Nicolas M. Thiéry:

```
 - trac_8926_family_repr-fh.patch   # Positive review, assuming test pass
```

We had a all tests passed on the server massena. Therefore I allow myself to put a positive review on behalf of Nicolas.



---

archive/issue_comments_082102.json:
```json
{
    "body": "Changing assignee from sage-combinat to @hivert.",
    "created_at": "2010-06-02T18:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82102",
    "user": "https://github.com/hivert"
}
```

Changing assignee from sage-combinat to @hivert.



---

archive/issue_comments_082103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82103",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021789.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:12:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8926#event-21789"
}
```
