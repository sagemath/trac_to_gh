# Issue 6769: Documentation for vector() does not match behavior

archive/issues_006769.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @KPanComputes\n\nKeywords: vector documentation\n\nThe documentation for the vector constructor (vector() in sage/modules/free_module_element.pyx) could use some improvement, since the \"call formats\" do not include all the possibilities and the description is a bit confusing.  For example:\n\n1. `elts` is listed as an input, but nowhere is it stated just where this could be provided as an input.\n\n2. `vector(QQ, 3, [1,2,3])` is a legitimate construction but the documentation does not describe it anywhere.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6769\n\n",
    "created_at": "2009-08-17T06:54:19Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Documentation for vector() does not match behavior",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6769",
    "user": "@rbeezer"
}
```
Assignee: @williamstein

CC:  @KPanComputes

Keywords: vector documentation

The documentation for the vector constructor (vector() in sage/modules/free_module_element.pyx) could use some improvement, since the "call formats" do not include all the possibilities and the description is a bit confusing.  For example:

1. `elts` is listed as an input, but nowhere is it stated just where this could be provided as an input.

2. `vector(QQ, 3, [1,2,3])` is a legitimate construction but the documentation does not describe it anywhere.

Issue created by migration from https://trac.sagemath.org/ticket/6769


