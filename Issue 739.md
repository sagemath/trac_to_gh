# Issue 739: hang doctesting const.tex

archive/issues_000739.json:
```json
{
    "body": "Assignee: failure\n\nMany people (John Cremona and David Harvey at least) had the following problem:\n\n\n```\nI upgraded to 2.8.5 ok (kubuntu 7.04, kernel 2.6.20-16-generic, gcc\nversion 4.1.2).\n\nsage --testall hangs at this point:\nTesting SAGE constructions guide\nsage -t  const.tex\n\nand \"ps -ux\" shows that all the processes are in swap (S status).\nAlso Ctrl-C did not kill it, I am having to kill all the processes one\nby one.\n\nJohn\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/739\n\n",
    "created_at": "2007-09-22T22:02:03Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "hang doctesting const.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/739",
    "user": "was"
}
```
Assignee: failure

Many people (John Cremona and David Harvey at least) had the following problem:


```
I upgraded to 2.8.5 ok (kubuntu 7.04, kernel 2.6.20-16-generic, gcc
version 4.1.2).

sage --testall hangs at this point:
Testing SAGE constructions guide
sage -t  const.tex

and "ps -ux" shows that all the processes are in swap (S status).
Also Ctrl-C did not kill it, I am having to kill all the processes one
by one.

John
```


Issue created by migration from https://trac.sagemath.org/ticket/739





---

archive/issue_comments_004327.json:
```json
{
    "body": "It turns out that \"hangs forever\" means takes longer than 30 seconds for many people :-). \nThis actually works fine -- it's just that const.tex is really long (nearly a minute!).",
    "created_at": "2007-09-23T21:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/739#issuecomment-4327",
    "user": "was"
}
```

It turns out that "hangs forever" means takes longer than 30 seconds for many people :-). 
This actually works fine -- it's just that const.tex is really long (nearly a minute!).



---

archive/issue_comments_004328.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-09-23T21:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/739#issuecomment-4328",
    "user": "was"
}
```

Resolution: invalid
