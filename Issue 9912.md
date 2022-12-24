# Issue 9912: n() returns symbolic expression

archive/issues_009912.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  cwitty\n\nfrom sage-support:\nhttp://groups.google.com/group/sage-support/browse_thread/thread/b36c90f1490eac19#\n\n```\nsage: a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5) \nsage: a.imag().n()\n0.939469338708203*sin(0.500000000000000*pi)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9913\n\n",
    "created_at": "2010-09-16T01:57:27Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "n() returns symbolic expression",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9912",
    "user": "zimmerma"
}
```
Assignee: AlexGhitza

CC:  cwitty

from sage-support:
http://groups.google.com/group/sage-support/browse_thread/thread/b36c90f1490eac19#

```
sage: a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5) 
sage: a.imag().n()
0.939469338708203*sin(0.500000000000000*pi)
```


Issue created by migration from https://trac.sagemath.org/ticket/9913





---

archive/issue_comments_098599.json:
```json
{
    "body": "Even simpler:\n\n\n```\nsage: n(arctan2(0,-log(2)))\npi\n```\n",
    "created_at": "2010-09-16T23:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98599",
    "user": "jason"
}
```

Even simpler:


```
sage: n(arctan2(0,-log(2)))
pi
```




---

archive/issue_comments_098600.json:
```json
{
    "body": "Note also the strange tty output (look in the 2nd argument of `arctan2`):\n\n```\nsage: a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5)\nsage: a.imag()\nsin(1/2*arctan2(0, -88* + 48))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48))/(sqrt(3) + 5)\n```\n\n\nShould I open a separate ticket for that?\nPaul",
    "created_at": "2010-09-16T23:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98600",
    "user": "zimmerma"
}
```

Note also the strange tty output (look in the 2nd argument of `arctan2`):

```
sage: a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5)
sage: a.imag()
sin(1/2*arctan2(0, -88* + 48))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48))/(sqrt(3) + 5)
```


Should I open a separate ticket for that?
Paul



---

archive/issue_comments_098601.json:
```json
{
    "body": "Changing component from basic arithmetic to symbolics.",
    "created_at": "2010-09-18T21:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98601",
    "user": "burcin"
}
```

Changing component from basic arithmetic to symbolics.



---

archive/issue_comments_098602.json:
```json
{
    "body": "I'm changing the component to `symbolics`, since this is probably a bug in pynac.\n\nRegarding the problem with the output Carl mentions in comment:2: This is also present in GiNaC, but the printing is better:\n\n\n```\nginsh - GiNaC Interactive Shell (ginac V1.5.7)\n  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,\n (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.\n  ._) i N a C | You are welcome to redistribute it under certain conditions.\n<-------------' For details type `warranty;'.\n\nType ?? for a list of help topics.\n> a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5);\n(sqrt(48+4*(5+sqrt(3))*(-5+sqrt(3)))+4*sqrt(3))*(5+sqrt(3))^(-1)\n> imag_part(a);\n(5+sqrt(3))^(-1)*sqrt(abs(48+4*(5+sqrt(3))*(-5+sqrt(3))))*sin(1/2*atan2(0,48+4*(-22)))\n```\n\n\nNote the term `4*(-22)` at the end of the last line.\n\nWe should open a new ticket for this and report it on the GiNaC list. I'm not sure if this has anything to do with this ticket ATM. Numeric evaluation seems to work fine in GiNaC:\n\n\n```\n> evalf(imag_part(a));\n0.9394693387082032295\n```\n",
    "created_at": "2010-09-18T21:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98602",
    "user": "burcin"
}
```

I'm changing the component to `symbolics`, since this is probably a bug in pynac.

Regarding the problem with the output Carl mentions in comment:2: This is also present in GiNaC, but the printing is better:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.7)
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> a=(sqrt(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 48) + 4*sqrt(3))/ (sqrt(3) + 5);
(sqrt(48+4*(5+sqrt(3))*(-5+sqrt(3)))+4*sqrt(3))*(5+sqrt(3))^(-1)
> imag_part(a);
(5+sqrt(3))^(-1)*sqrt(abs(48+4*(5+sqrt(3))*(-5+sqrt(3))))*sin(1/2*atan2(0,48+4*(-22)))
```


Note the term `4*(-22)` at the end of the last line.

We should open a new ticket for this and report it on the GiNaC list. I'm not sure if this has anything to do with this ticket ATM. Numeric evaluation seems to work fine in GiNaC:


```
> evalf(imag_part(a));
0.9394693387082032295
```




---

archive/issue_comments_098603.json:
```json
{
    "body": "Changing assignee from AlexGhitza to burcin.",
    "created_at": "2010-09-18T21:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98603",
    "user": "burcin"
}
```

Changing assignee from AlexGhitza to burcin.



---

archive/issue_comments_098604.json:
```json
{
    "body": "Burcin,\n\n> We should open a new ticket for this and report it on the GiNaC list. \n\nI've reported a new ticket (#9947). I let you report it on the GiNaC list.\n\nPaul",
    "created_at": "2010-09-19T08:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98604",
    "user": "zimmerma"
}
```

Burcin,

> We should open a new ticket for this and report it on the GiNaC list. 

I've reported a new ticket (#9947). I let you report it on the GiNaC list.

Paul



---

archive/issue_comments_098605.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-09-24T11:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98605",
    "user": "burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_098606.json:
```json
{
    "body": "Replying to [comment:4 zimmerma]:\n> Burcin,\n> \n> > We should open a new ticket for this and report it on the GiNaC list. \n> \n> I've reported a new ticket (#9947). I let you report it on the GiNaC list.\n\nThis issue was fixed upstream by Richard Kreckel.\n\nWhile the fix makes the original example on this ticket work, Jason's example from comment:1 or the one reported by Tian Wei on sage-support (below) still don't work.\n\n\n```\nsage: b = sqrt(-log(2))\nsage: print b.imag().n()\n0.832554611157698*sin(0.500000000000000*pi)\n```\n",
    "created_at": "2010-09-24T11:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98606",
    "user": "burcin"
}
```

Replying to [comment:4 zimmerma]:
> Burcin,
> 
> > We should open a new ticket for this and report it on the GiNaC list. 
> 
> I've reported a new ticket (#9947). I let you report it on the GiNaC list.

This issue was fixed upstream by Richard Kreckel.

While the fix makes the original example on this ticket work, Jason's example from comment:1 or the one reported by Tian Wei on sage-support (below) still don't work.


```
sage: b = sqrt(-log(2))
sage: print b.imag().n()
0.832554611157698*sin(0.500000000000000*pi)
```




---

archive/issue_comments_098607.json:
```json
{
    "body": "Attachment [trac_9913-arctan2_evalf.patch](tarball://root/attachments/some-uuid/ticket9913/trac_9913-arctan2_evalf.patch) by burcin created at 2010-10-10 19:53:51",
    "created_at": "2010-10-10T19:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98607",
    "user": "burcin"
}
```

Attachment [trac_9913-arctan2_evalf.patch](tarball://root/attachments/some-uuid/ticket9913/trac_9913-arctan2_evalf.patch) by burcin created at 2010-10-10 19:53:51



---

archive/issue_comments_098608.json:
```json
{
    "body": "I uploaded a patch to fix this. The problem wasn't in pynac after all, it was the numeric approximation function for `arctan2()`.",
    "created_at": "2010-10-10T19:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98608",
    "user": "burcin"
}
```

I uploaded a patch to fix this. The problem wasn't in pynac after all, it was the numeric approximation function for `arctan2()`.



---

archive/issue_comments_098609.json:
```json
{
    "body": "Changing keywords from \"pynac\" to \"\".",
    "created_at": "2010-10-10T19:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98609",
    "user": "burcin"
}
```

Changing keywords from "pynac" to "".



---

archive/issue_comments_098610.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-10T19:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98610",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098611.json:
```json
{
    "body": "positive review, good work Burcin!\n\nPaul",
    "created_at": "2010-10-11T07:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98611",
    "user": "zimmerma"
}
```

positive review, good work Burcin!

Paul



---

archive/issue_comments_098612.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-11T07:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98612",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098613.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9912#issuecomment-98613",
    "user": "jdemeyer"
}
```

Resolution: fixed
