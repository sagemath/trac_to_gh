# Issue 9183: creating an expect element can modify a previously created expect element

archive/issues_009183.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: gap\n\nThe `_next_variable_name` method in the expect interface sometimes spits out a variable name that is in use. This means that a previously created element might be modified inadvertently:\n\n```\nsage: z = gap(3); z\n3\nsage: gap.clear(z.name())\nsage: gap.clear(z.name())\nsage: x = gap(3); x\n3\nsage: y = gap(4); y\n4\nsage: x\n4 \n```\n\nOf course, x should be 3 above, and not 4.\n\n(This issue was found in #8380, but it didn't get resolved there. See the ticket for more details.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9183\n\n",
    "created_at": "2010-06-08T03:16:19Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "creating an expect element can modify a previously created expect element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9183",
    "user": "@saliola"
}
```
Assignee: @williamstein

Keywords: gap

The `_next_variable_name` method in the expect interface sometimes spits out a variable name that is in use. This means that a previously created element might be modified inadvertently:

```
sage: z = gap(3); z
3
sage: gap.clear(z.name())
sage: gap.clear(z.name())
sage: x = gap(3); x
3
sage: y = gap(4); y
4
sage: x
4 
```

Of course, x should be 3 above, and not 4.

(This issue was found in #8380, but it didn't get resolved there. See the ticket for more details.)

Issue created by migration from https://trac.sagemath.org/ticket/9183


