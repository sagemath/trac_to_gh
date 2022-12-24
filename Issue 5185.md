# Issue 5185: [with patch, needs review] is_zero is broken for sparse vectors

archive/issues_005185.json:
```json
{
    "body": "Assignee: tbd\n\nConsider this:\n\n```\nsage: v = vector({1: 1, 3: -1})\nsage: w = vector({1: -1, 3: 1})\nsage: v+w\n(0, 0, 0, 0)\nsage: (v+w).is_zero()\nFalse\n```\n\n\nI see two things wrong with the source code:\n\n1. in modules/free_module_element.pyx, it says\n\n```\n    def __nonzero__(self):\n        \"\"\"\n        EXAMPLES:\n            sage: V = vector(ZZ, [0, 0, 0, 0])\n            sage: bool(V)\n            False\n            sage: V = vector(ZZ, [1, 2, 3, 5])\n            sage: bool(V)\n            True\n        \"\"\"\n        return self != 0\n```\n\nI don't understand the relevance of the doctest at all, and the actual code should probably say something like `self != self.parent()(0)`.  In fact, this is completely unnecessary, because this class inherits from ModuleElement, which has `__nonzero__` defined in precisely this way -- see structure/element.pyx.\n\n2. in structure/element.pyx, it says\n\n```\n    def is_zero(self):\n        \"\"\"\n        Return True if self equals self.parent()(0). The default\n        implementation is to fall back to 'not self.__nonzero__'.\n\n        NOTE: Do not re-implement this method in your subclass but\n        implement __nonzero__ instead.\n        \"\"\"\n        return not self\n```\n\nThe code `return not self` looks like a typo: it should be `return not self.__nonzero__()` -- read the docstring!\n\nThe patch deals with both of these issues by fixing the code in element.pyx and by deleting the code in free_module_element.pyx.  It also adds a doctest to element.pyx, verifying that the above vector example now works.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5185\n\n",
    "created_at": "2009-02-05T04:05:51Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] is_zero is broken for sparse vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5185",
    "user": "jhpalmieri"
}
```
Assignee: tbd

Consider this:

```
sage: v = vector({1: 1, 3: -1})
sage: w = vector({1: -1, 3: 1})
sage: v+w
(0, 0, 0, 0)
sage: (v+w).is_zero()
False
```


I see two things wrong with the source code:

1. in modules/free_module_element.pyx, it says

```
    def __nonzero__(self):
        """
        EXAMPLES:
            sage: V = vector(ZZ, [0, 0, 0, 0])
            sage: bool(V)
            False
            sage: V = vector(ZZ, [1, 2, 3, 5])
            sage: bool(V)
            True
        """
        return self != 0
```

I don't understand the relevance of the doctest at all, and the actual code should probably say something like `self != self.parent()(0)`.  In fact, this is completely unnecessary, because this class inherits from ModuleElement, which has `__nonzero__` defined in precisely this way -- see structure/element.pyx.

2. in structure/element.pyx, it says

```
    def is_zero(self):
        """
        Return True if self equals self.parent()(0). The default
        implementation is to fall back to 'not self.__nonzero__'.

        NOTE: Do not re-implement this method in your subclass but
        implement __nonzero__ instead.
        """
        return not self
```

The code `return not self` looks like a typo: it should be `return not self.__nonzero__()` -- read the docstring!

The patch deals with both of these issues by fixing the code in element.pyx and by deleting the code in free_module_element.pyx.  It also adds a doctest to element.pyx, verifying that the above vector example now works.



Issue created by migration from https://trac.sagemath.org/ticket/5185





---

archive/issue_comments_039763.json:
```json
{
    "body": "Attachment [5185.patch](tarball://root/attachments/some-uuid/ticket5185/5185.patch) by jhpalmieri created at 2009-02-05 04:06:45",
    "created_at": "2009-02-05T04:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39763",
    "user": "jhpalmieri"
}
```

Attachment [5185.patch](tarball://root/attachments/some-uuid/ticket5185/5185.patch) by jhpalmieri created at 2009-02-05 04:06:45



---

archive/issue_comments_039764.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-08T22:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39764",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_039765.json:
```json
{
    "body": "Changing assignee from tbd to cwitty.",
    "created_at": "2009-02-08T22:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39765",
    "user": "mabshoff"
}
```

Changing assignee from tbd to cwitty.



---

archive/issue_comments_039766.json:
```json
{
    "body": "Oops, sounds like another 3.3 blocker or at least critical ticket to me. I don't think this is \"algebra\", but other than \"misc\" I can't come up with any better category.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T22:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39766",
    "user": "mabshoff"
}
```

Oops, sounds like another 3.3 blocker or at least critical ticket to me. I don't think this is "algebra", but other than "misc" I can't come up with any better category.

Cheers,

Michael



---

archive/issue_comments_039767.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2009-02-08T22:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39767",
    "user": "mabshoff"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_039768.json:
```json
{
    "body": "Changing assignee from cwitty to jhpalmieri.",
    "created_at": "2009-02-08T22:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39768",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to jhpalmieri.



---

archive/issue_comments_039769.json:
```json
{
    "body": "John,\n\nplease accept tickets once you post a patch since you should own all tickets you resolved. As a first step I am reassigning this to you.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T22:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39769",
    "user": "mabshoff"
}
```

John,

please accept tickets once you post a patch since you should own all tickets you resolved. As a first step I am reassigning this to you.

Cheers,

Michael



---

archive/issue_comments_039770.json:
```json
{
    "body": "With this patch applied to my current 3.3.rc0 merge tree all doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T12:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39770",
    "user": "mabshoff"
}
```

With this patch applied to my current 3.3.rc0 merge tree all doctests pass.

Cheers,

Michael



---

archive/issue_comments_039771.json:
```json
{
    "body": "Actually, if `__nonzero__` is implemented for a class, then `not self` is totally equivalent to `not self.__nonzero__()`, except faster.  (Checking to see if an object is \"true\" calls the `__nonzero__` method using an optimized C calling convention; calling the method directly uses a slower, Python calling convention.)\n\nSo the change to the body of is_zero should be reverted.  (Maybe some comments could be added to clarify the situation.)",
    "created_at": "2009-02-10T06:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39771",
    "user": "cwitty"
}
```

Actually, if `__nonzero__` is implemented for a class, then `not self` is totally equivalent to `not self.__nonzero__()`, except faster.  (Checking to see if an object is "true" calls the `__nonzero__` method using an optimized C calling convention; calling the method directly uses a slower, Python calling convention.)

So the change to the body of is_zero should be reverted.  (Maybe some comments could be added to clarify the situation.)



---

archive/issue_comments_039772.json:
```json
{
    "body": "Oh, I didn't know that.  Here's a new patch which just deletes the `__nonzero__` method from free_module_element.pyx, leaving element.pyx unchanged.",
    "created_at": "2009-02-10T16:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39772",
    "user": "jhpalmieri"
}
```

Oh, I didn't know that.  Here's a new patch which just deletes the `__nonzero__` method from free_module_element.pyx, leaving element.pyx unchanged.



---

archive/issue_comments_039773.json:
```json
{
    "body": "Attachment [5185-new.patch](tarball://root/attachments/some-uuid/ticket5185/5185-new.patch) by jhpalmieri created at 2009-02-10 16:13:53",
    "created_at": "2009-02-10T16:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39773",
    "user": "jhpalmieri"
}
```

Attachment [5185-new.patch](tarball://root/attachments/some-uuid/ticket5185/5185-new.patch) by jhpalmieri created at 2009-02-10 16:13:53



---

archive/issue_comments_039774.json:
```json
{
    "body": "(Just apply 5185-new.patch.)",
    "created_at": "2009-02-10T16:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39774",
    "user": "jhpalmieri"
}
```

(Just apply 5185-new.patch.)



---

archive/issue_comments_039775.json:
```json
{
    "body": "Attachment [5185-reviewer.patch](tarball://root/attachments/some-uuid/ticket5185/5185-reviewer.patch) by cwitty created at 2009-02-11 02:26:54",
    "created_at": "2009-02-11T02:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39775",
    "user": "cwitty"
}
```

Attachment [5185-reviewer.patch](tarball://root/attachments/some-uuid/ticket5185/5185-reviewer.patch) by cwitty created at 2009-02-11 02:26:54



---

archive/issue_comments_039776.json:
```json
{
    "body": "Since every bug fix should have a doctest, I rescued John's doctest from his first patch, and added a tiny bit of documentation.\n\nPositive review.  Apply 5185-new.patch, then 5185-reviewer.patch.",
    "created_at": "2009-02-11T02:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39776",
    "user": "cwitty"
}
```

Since every bug fix should have a doctest, I rescued John's doctest from his first patch, and added a tiny bit of documentation.

Positive review.  Apply 5185-new.patch, then 5185-reviewer.patch.



---

archive/issue_comments_039777.json:
```json
{
    "body": "Excellent.",
    "created_at": "2009-02-11T02:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39777",
    "user": "jhpalmieri"
}
```

Excellent.



---

archive/issue_comments_039778.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-11T04:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39778",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039779.json:
```json
{
    "body": "Merged 5185-new.patch and 5185-reviewer.patch in Sage 3.3.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T04:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5185#issuecomment-39779",
    "user": "mabshoff"
}
```

Merged 5185-new.patch and 5185-reviewer.patch in Sage 3.3.rc0.

Cheers,

Michael
