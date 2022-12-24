# Issue 5419: moving fraction field to new coercion broke old pickles

archive/issues_005419.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @burcin\n\nAt some point, fraction fields were moved over to the new coercion model, which is good -- except that it broke all the old pickles. This thread on `sage-support` is about someone having a problem with them: http://groups.google.com/group/sage-support/browse_thread/thread/b5519db45a141819\n\nThe problem is that the old pickles don't have `_element_class` or `_element_constructor` fields, and there was no factory function in place -- so unpickling tries to directly create the object, which totally fails. Putting the old `__call__` method back in place is an ugly hack to get these to load, but it's not a good permanent solution. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5419\n\n",
    "created_at": "2009-03-02T06:40:28Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "moving fraction field to new coercion broke old pickles",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5419",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

CC:  @burcin

At some point, fraction fields were moved over to the new coercion model, which is good -- except that it broke all the old pickles. This thread on `sage-support` is about someone having a problem with them: http://groups.google.com/group/sage-support/browse_thread/thread/b5519db45a141819

The problem is that the old pickles don't have `_element_class` or `_element_constructor` fields, and there was no factory function in place -- so unpickling tries to directly create the object, which totally fails. Putting the old `__call__` method back in place is an ugly hack to get these to load, but it's not a good permanent solution. 



Issue created by migration from https://trac.sagemath.org/ticket/5419





---

archive/issue_comments_041930.json:
```json
{
    "body": "Hmm,\n\nhow did this escape the pickle jar doctest?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T07:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5419#issuecomment-41930",
    "user": "mabshoff"
}
```

Hmm,

how did this escape the pickle jar doctest?

Cheers,

Michael



---

archive/issue_comments_041931.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2009-03-02T07:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5419#issuecomment-41931",
    "user": "mabshoff"
}
```

Changing component from algebra to misc.
