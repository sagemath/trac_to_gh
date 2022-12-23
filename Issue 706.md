# Issue 706: irange --- also add range that includes the endpoints by default

archive/issues_000706.json:
```json
{
    "body": "Assignee: somebody\n\nFrom Jaap Spies (see attached):\n\n```\nForgot to add a few examples:\n\nsage: v = irange(0,5); v\n[0, 1, 2, 3, 4, 5]\nsage: v = irange(1,10); v\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nsage: v = irange(10,-1,-1); v\n[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]\nsage: v = irange(1,8, 1/2); v\n[1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8]\nsage: v = irange(1,2, 0.4); v\n[1, 1.40000000000000, 1.80000000000000]\nsage: v = irange(1, 2, 0.5); v\n[1, 1.50000000000000, 2]\nsage: v = irange(1, 2, -0.5); v\n[]\nsage: v = irange(2, -2, -0.5); v\n[2, 1.50000000000000, 1.00000000000000, 0.500000000000000, 0.000000000000000, -0.500000000000000, -1.00000000000000, -1.50000000000000, -2]\nsage: v = irange(10,1); v\n[]\nsage: v = irange(10,10); v\n[10]\nsage: v = irange(10); v\nTraceback (most recent call last):\n...\nTypeError: irange() takes at least 2 arguments (1 given)\nsage: v = irange(0.5, 2.5, 0.5); v\n[0.500000000000000, 1.00000000000000, 1.50000000000000, 2.00000000000000, 2.50000000000000]\nsage: [n^2 for n in irange(-1, 10)]\n[1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n\nAnd this one from the calculus thread!\n> --  I think that the Python convention of not including the upper bound\n>> > in a sum is a real problem.\n>> >\n>> > sage: sum(i for i in range(1,10))\n>> > 45\n>> >\n>> > I understand this is a fundamental convention in Python, and that it is\n>> > very\n>> > natural for people used to malloc(), but I worry that this will be a\n>> > constant\n>> > headache for students (and professors!).\n\n\nsage: sum(i for i in irange(1, 10))\n55\n```\n\n\nI think including this is a good idea, modulo serious optimization issues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/706\n\n",
    "created_at": "2007-09-20T14:33:20Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "irange --- also add range that includes the endpoints by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/706",
    "user": "was"
}
```
Assignee: somebody

From Jaap Spies (see attached):

```
Forgot to add a few examples:

sage: v = irange(0,5); v
[0, 1, 2, 3, 4, 5]
sage: v = irange(1,10); v
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: v = irange(10,-1,-1); v
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
sage: v = irange(1,8, 1/2); v
[1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8]
sage: v = irange(1,2, 0.4); v
[1, 1.40000000000000, 1.80000000000000]
sage: v = irange(1, 2, 0.5); v
[1, 1.50000000000000, 2]
sage: v = irange(1, 2, -0.5); v
[]
sage: v = irange(2, -2, -0.5); v
[2, 1.50000000000000, 1.00000000000000, 0.500000000000000, 0.000000000000000, -0.500000000000000, -1.00000000000000, -1.50000000000000, -2]
sage: v = irange(10,1); v
[]
sage: v = irange(10,10); v
[10]
sage: v = irange(10); v
Traceback (most recent call last):
...
TypeError: irange() takes at least 2 arguments (1 given)
sage: v = irange(0.5, 2.5, 0.5); v
[0.500000000000000, 1.00000000000000, 1.50000000000000, 2.00000000000000, 2.50000000000000]
sage: [n^2 for n in irange(-1, 10)]
[1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

And this one from the calculus thread!
> --  I think that the Python convention of not including the upper bound
>> > in a sum is a real problem.
>> >
>> > sage: sum(i for i in range(1,10))
>> > 45
>> >
>> > I understand this is a fundamental convention in Python, and that it is
>> > very
>> > natural for people used to malloc(), but I worry that this will be a
>> > constant
>> > headache for students (and professors!).


sage: sum(i for i in irange(1, 10))
55
```


I think including this is a good idea, modulo serious optimization issues.

Issue created by migration from https://trac.sagemath.org/ticket/706





---

archive/issue_comments_003712.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-20T14:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/706#issuecomment-3712",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_003713.json:
```json
{
    "body": "Changing assignee from somebody to jaap spies.",
    "created_at": "2007-09-20T15:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/706#issuecomment-3713",
    "user": "was"
}
```

Changing assignee from somebody to jaap spies.



---

archive/issue_comments_003714.json:
```json
{
    "body": "Attachment\n\nReplying to [ticket:706 was]:\n> From Jaap Spies (see attached):\n> {{{\n> \n> sage: v = irange(0,5); v\n> [0, 1, 2, 3, 4, 5]\n> sage: v = irange(1,10); v\n> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n> sage: v = irange(10,-1,-1); v\n> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]\n> sage: v = irange(1,8, 1/2); v\n> [1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8]\n> sage: v = irange(1,2, 0.4); v\n> [1, 1.40000000000000, 1.80000000000000]\n> sage: v = irange(1, 2, 0.5); v\n> [1, 1.50000000000000, 2]\n> sage: v = irange(1, 2, -0.5); v\n> []\n> sage: v = irange(2, -2, -0.5); v\n> [2, 1.50000000000000, 1.00000000000000, 0.500000000000000, 0.000000000000000, -0.500000000000000, -1.00000000000000, -1.50000000000000, -2]\n> sage: v = irange(10,1); v\n> []\n> sage: v = irange(10,10); v\n> [10]\n> sage: v = irange(10); v\n> Traceback (most recent call last):\n> ...\n> TypeError: irange() takes at least 2 arguments (1 given)\n> sage: v = irange(0.5, 2.5, 0.5); v\n> [0.500000000000000, 1.00000000000000, 1.50000000000000, 2.00000000000000, 2.50000000000000]\n> sage: [n^2 for n in irange(-1, 10)]\n> [1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n> \n> And this one from the calculus thread!\n> > --  I think that the Python convention of not including the upper bound\n> >> > in a sum is a real problem.\n> >> >\n> >> > sage: sum(i for i in range(1,10))\n> >> > 45\n> >> >\n> >> > I understand this is a fundamental convention in Python, and that it is\n> >> > very\n> >> > natural for people used to malloc(), but I worry that this will be a\n> >> > constant\n> >> > headache for students (and professors!).\n> \n> \n> sage: sum(i for i in irange(1, 10))\n> 55\n> }}}\n> \n> I think including this is a good idea, modulo serious optimization issues. \n\nirange now only depends on srange. So ticket #701 will solve this issue.\n\npatch 'irange_improved.hg' is relative to 'irange.hg'",
    "created_at": "2007-09-20T17:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/706#issuecomment-3714",
    "user": "jsp"
}
```

Attachment

Replying to [ticket:706 was]:
> From Jaap Spies (see attached):
> {{{
> 
> sage: v = irange(0,5); v
> [0, 1, 2, 3, 4, 5]
> sage: v = irange(1,10); v
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
> sage: v = irange(10,-1,-1); v
> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
> sage: v = irange(1,8, 1/2); v
> [1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8]
> sage: v = irange(1,2, 0.4); v
> [1, 1.40000000000000, 1.80000000000000]
> sage: v = irange(1, 2, 0.5); v
> [1, 1.50000000000000, 2]
> sage: v = irange(1, 2, -0.5); v
> []
> sage: v = irange(2, -2, -0.5); v
> [2, 1.50000000000000, 1.00000000000000, 0.500000000000000, 0.000000000000000, -0.500000000000000, -1.00000000000000, -1.50000000000000, -2]
> sage: v = irange(10,1); v
> []
> sage: v = irange(10,10); v
> [10]
> sage: v = irange(10); v
> Traceback (most recent call last):
> ...
> TypeError: irange() takes at least 2 arguments (1 given)
> sage: v = irange(0.5, 2.5, 0.5); v
> [0.500000000000000, 1.00000000000000, 1.50000000000000, 2.00000000000000, 2.50000000000000]
> sage: [n^2 for n in irange(-1, 10)]
> [1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
> 
> And this one from the calculus thread!
> > --  I think that the Python convention of not including the upper bound
> >> > in a sum is a real problem.
> >> >
> >> > sage: sum(i for i in range(1,10))
> >> > 45
> >> >
> >> > I understand this is a fundamental convention in Python, and that it is
> >> > very
> >> > natural for people used to malloc(), but I worry that this will be a
> >> > constant
> >> > headache for students (and professors!).
> 
> 
> sage: sum(i for i in irange(1, 10))
> 55
> }}}
> 
> I think including this is a good idea, modulo serious optimization issues. 

irange now only depends on srange. So ticket #701 will solve this issue.

patch 'irange_improved.hg' is relative to 'irange.hg'



---

archive/issue_comments_003715.json:
```json
{
    "body": "I think http://trac.sagemath.org/sage_trac/ticket/702 is actually much nicer to use, so for now I think\nirange isn't needed.",
    "created_at": "2007-09-21T07:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/706#issuecomment-3715",
    "user": "was"
}
```

I think http://trac.sagemath.org/sage_trac/ticket/702 is actually much nicer to use, so for now I think
irange isn't needed.



---

archive/issue_comments_003716.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-09-21T07:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/706#issuecomment-3716",
    "user": "was"
}
```

Resolution: wontfix
