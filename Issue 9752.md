# Issue 9752: sorting of number field elements is broken

archive/issues_009752.json:
```json
{
    "body": "Assignee: @loefflerd\n\nThe design of number field elements (and other aspects of sage) assumes that cmp defines a total ordering, which of course doesn't respect the algebraic field structure.   Unfortunately, the actual implementation (in number_field_element.pyx) is buggy and doesn't define a total ordering.   Look at the code and you'll see.  Or just look at this example:\n\n```\nsage: L.<b> = NumberField(x^3-10001)\nsage: b+1 < L(1667)\nFalse\nsage: L(1667) < b+1\nFalse\n```\n\n\n\nI think the best correct implementation of cmp should be one that is efficient and *also* agrees with the lexicographic ordering of elements based on their representation as a polynomial in the generator of the number field.   I did implement this as part of the patch bomb #9541.  The point of the present ticket is to \"backport\" something like this out of #9541, or implement a new fix from scratch.  This is motivated by #9400. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9752\n\n",
    "created_at": "2010-08-15T17:46:07Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sorting of number field elements is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9752",
    "user": "https://github.com/williamstein"
}
```
Assignee: @loefflerd

The design of number field elements (and other aspects of sage) assumes that cmp defines a total ordering, which of course doesn't respect the algebraic field structure.   Unfortunately, the actual implementation (in number_field_element.pyx) is buggy and doesn't define a total ordering.   Look at the code and you'll see.  Or just look at this example:

```
sage: L.<b> = NumberField(x^3-10001)
sage: b+1 < L(1667)
False
sage: L(1667) < b+1
False
```



I think the best correct implementation of cmp should be one that is efficient and *also* agrees with the lexicographic ordering of elements based on their representation as a polynomial in the generator of the number field.   I did implement this as part of the patch bomb #9541.  The point of the present ticket is to "backport" something like this out of #9541, or implement a new fix from scratch.  This is motivated by #9400. 

Issue created by migration from https://trac.sagemath.org/ticket/9752





---

archive/issue_comments_095340.json:
```json
{
    "body": "See also #6132, there is some code to compare number field elements.",
    "created_at": "2010-09-20T19:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9752#issuecomment-95340",
    "user": "https://github.com/jdemeyer"
}
```

See also #6132, there is some code to compare number field elements.



---

archive/issue_comments_095341.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-03-21T01:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9752#issuecomment-95341",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_events_024429.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2011-03-21T01:17:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9752",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9752#event-24429"
}
```



---

archive/issue_comments_095342.json:
```json
{
    "body": "I'm closing this as a dup of #6132.",
    "created_at": "2011-03-21T01:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9752#issuecomment-95342",
    "user": "https://github.com/williamstein"
}
```

I'm closing this as a dup of #6132.



---

archive/issue_events_024430.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-21T08:33:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9752",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9752#event-24430"
}
```
