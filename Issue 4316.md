# Issue 4316: notebook: '%html $x<y$' doesn't work right

archive/issues_004316.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: notebook, %html\n\nIf I type\n\n```\n%html some math: $x<y$.\n```\n\nin the notebook, then the \"<y\" gets swallowed. (If I \"Edit\" the worksheet, I see\n\n```\n<html><font color='black'>some math: <span class=\"math\">x<y</span>.</font></html>\n```\n\nbut in the worksheet view I see \"some math: x.\")\n\nPutting a space between \"<\" and \"y\" fixes the problem. Also,\n\n```\n%html some math: $x<6y$.\n```\n \nworks just fine, and the same with $x<-y$ and similar things; the problem seems to just be with \"<\" followed by a letter.  The greater than sign seems to present no problems.\n\nIs this related to (or the same problem as) #4245?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4316\n\n",
    "created_at": "2008-10-17T23:20:57Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook: '%html $x<y$' doesn't work right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4316",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: boothby

Keywords: notebook, %html

If I type

```
%html some math: $x<y$.
```

in the notebook, then the "<y" gets swallowed. (If I "Edit" the worksheet, I see

```
<html><font color='black'>some math: <span class="math">x<y</span>.</font></html>
```

but in the worksheet view I see "some math: x.")

Putting a space between "<" and "y" fixes the problem. Also,

```
%html some math: $x<6y$.
```
 
works just fine, and the same with $x<-y$ and similar things; the problem seems to just be with "<" followed by a letter.  The greater than sign seems to present no problems.

Is this related to (or the same problem as) #4245?

Issue created by migration from https://trac.sagemath.org/ticket/4316





---

archive/issue_events_009751.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-24T07:35:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4316",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4316#event-9751"
}
```



---

archive/issue_events_009752.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-24T07:35:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4316",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4316#event-9752"
}
```



---

archive/issue_comments_031529.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-24T07:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4316#issuecomment-31529",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_031530.json:
```json
{
    "body": "This is a duplicate of #4245.",
    "created_at": "2009-01-24T07:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4316#issuecomment-31530",
    "user": "https://github.com/mwhansen"
}
```

This is a duplicate of #4245.
