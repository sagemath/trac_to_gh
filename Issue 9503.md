# Issue 9503: FreeModule_submodule_with_basis_pid calls wrong constructor

archive/issues_009503.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis is a piece of the current code in `FreeModule_submodule_with_basis_pid` after #9502 (before it was the same without explanations)\n\n```\n# The following is WRONG - we should call __init__ of\n# FreeModule_generic_pid. However, it leads to a bunch of errors.\nFreeModule_generic.__init__(self, R,\n                            rank=len(basis), degree=ambient.degree(),\n                            sparse=ambient.is_sparse())\n\n```\n\nThe errors seem to be related to number fields and their rings of integers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9503\n\n",
    "created_at": "2010-07-15T07:15:10Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "FreeModule_submodule_with_basis_pid calls wrong constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9503",
    "user": "https://github.com/novoselt"
}
```
Assignee: @aghitza

This is a piece of the current code in `FreeModule_submodule_with_basis_pid` after #9502 (before it was the same without explanations)

```
# The following is WRONG - we should call __init__ of
# FreeModule_generic_pid. However, it leads to a bunch of errors.
FreeModule_generic.__init__(self, R,
                            rank=len(basis), degree=ambient.degree(),
                            sparse=ambient.is_sparse())

```

The errors seem to be related to number fields and their rings of integers.

Issue created by migration from https://trac.sagemath.org/ticket/9503


