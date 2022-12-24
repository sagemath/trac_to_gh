# Issue 5530: add absolute_diameter and relative_diameter to CIF (ComplexIntervalField)

archive/issues_005530.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: complex interval field diameter absolute relative\n\nRIF has the above methods; it would be nice if CIF did too, defined (like diameter()) as the max of the real and imaginary diameters.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5530\n\n",
    "created_at": "2009-03-16T17:31:00Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "add absolute_diameter and relative_diameter to CIF (ComplexIntervalField)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5530",
    "user": "ncalexan"
}
```
Assignee: somebody

Keywords: complex interval field diameter absolute relative

RIF has the above methods; it would be nice if CIF did too, defined (like diameter()) as the max of the real and imaginary diameters.

Issue created by migration from https://trac.sagemath.org/ticket/5530





---

archive/issue_comments_043007.json:
```json
{
    "body": "Is that the right definition for relative_diameter?  Another possibility would be the absolute diameter divided by the absolute value of the center of the interval.\n\nFor example, a tiny interval centered at 1+eps*I (for tiny eps) would have a huge relative diameter under Nick's definition and a tiny relative diameter under mine.",
    "created_at": "2009-03-16T20:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5530#issuecomment-43007",
    "user": "cwitty"
}
```

Is that the right definition for relative_diameter?  Another possibility would be the absolute diameter divided by the absolute value of the center of the interval.

For example, a tiny interval centered at 1+eps*I (for tiny eps) would have a huge relative diameter under Nick's definition and a tiny relative diameter under mine.
