# Issue 8926: Family cannot completely handle a class as an argument

archive/issues_008926.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\n\n```\nsage: F = Family(NonNegativeIntegers(), PerfectMatchings)\nsage: F\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\n/home/saliola/Applications/sage-4.4/local/lib/python2.6/site-packages/sage/sets/family.pyc in _repr_(self)\n    873             name = name+\"(i)\"\n    874         else:\n--> 875             name = self.function.__repr__()\n    876             if isinstance(self.function, AttrCallObject):\n    877                 name = \"i\"+name[1:]\n\nTypeError: descriptor '__repr__' of 'sage.structure.sage_object.SageObject' object needs an argument\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8926\n\n",
    "created_at": "2010-05-07T20:32:47Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Family cannot completely handle a class as an argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8926",
    "user": "saliola"
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

archive/issue_comments_082233.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-07T23:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82233",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_082234.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-07T23:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82234",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082235.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T17:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82235",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082236.json:
```json
{
    "body": "From a private e-mail from Nicolas M. Thi\u00e9ry:\n\n```\n - trac_8926_family_repr-fh.patch   # Positive review, assuming test pass\n```\n\nWe had a all tests passed on the server massena. Therefore I allow myself to put a positive review on behalf of Nicolas.",
    "created_at": "2010-05-12T17:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82236",
    "user": "hivert"
}
```

From a private e-mail from Nicolas M. Thiéry:

```
 - trac_8926_family_repr-fh.patch   # Positive review, assuming test pass
```

We had a all tests passed on the server massena. Therefore I allow myself to put a positive review on behalf of Nicolas.



---

archive/issue_comments_082237.json:
```json
{
    "body": "Changing assignee from sage-combinat to hivert.",
    "created_at": "2010-06-02T18:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82237",
    "user": "hivert"
}
```

Changing assignee from sage-combinat to hivert.



---

archive/issue_comments_082238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8926#issuecomment-82238",
    "user": "mhansen"
}
```

Resolution: fixed
