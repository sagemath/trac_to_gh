# Issue 6090: plot(x^2, (x, -2, 2), fill=2) does not match documentation

archive/issues_006090.json:
```json
{
    "body": "Assignee: @williamstein\n\nAccording to the docs, if fill is a number c, then: \"a number c: Fill the area between the function and the horizontal line y = c.\"\n\nHowever, the above plot just fills to the x-axis.  My guess is that it is because bool(2)==True, so plot thinks we have fill=True?\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6090\n\n",
    "created_at": "2009-05-20T05:27:43Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "plot(x^2, (x, -2, 2), fill=2) does not match documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6090",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

According to the docs, if fill is a number c, then: "a number c: Fill the area between the function and the horizontal line y = c."

However, the above plot just fills to the x-axis.  My guess is that it is because bool(2)==True, so plot thinks we have fill=True?






Issue created by migration from https://trac.sagemath.org/ticket/6090





---

archive/issue_comments_048529.json:
```json
{
    "body": "This is a duplicate of #5438.",
    "created_at": "2009-05-20T08:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48529",
    "user": "whuss"
}
```

This is a duplicate of #5438.



---

archive/issue_comments_048530.json:
```json
{
    "body": "Replying to [comment:1 whuss]:\n> This is a duplicate of #5438.\n\nHmm, given that this went into 3.4.2 I wonder why Jason did hit this problem?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T11:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48530",
    "user": "mabshoff"
}
```

Replying to [comment:1 whuss]:
> This is a duplicate of #5438.

Hmm, given that this went into 3.4.2 I wonder why Jason did hit this problem?

Cheers,

Michael



---

archive/issue_comments_048531.json:
```json
{
    "body": "Jason, \n\nI am marking this a potential dupe in the summary so we won't forget to close it assuming you can confirm it as one.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T11:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48531",
    "user": "mabshoff"
}
```

Jason, 

I am marking this a potential dupe in the summary so we won't forget to close it assuming you can confirm it as one.

Cheers,

Michael



---

archive/issue_comments_048532.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> Replying to [comment:1 whuss]:\n> > This is a duplicate of #5438.\n> \n> Hmm, given that this went into 3.4.2 I wonder why Jason did hit this problem?\n\n#5438 says it went into 4.0.alpha0 not 3.4.2.\n\nCheers,\n\nWilfried",
    "created_at": "2009-05-20T11:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48532",
    "user": "whuss"
}
```

Replying to [comment:2 mabshoff]:
> Replying to [comment:1 whuss]:
> > This is a duplicate of #5438.
> 
> Hmm, given that this went into 3.4.2 I wonder why Jason did hit this problem?

#5438 says it went into 4.0.alpha0 not 3.4.2.

Cheers,

Wilfried



---

archive/issue_comments_048533.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-05-20T11:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48533",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_048534.json:
```json
{
    "body": "Replying to [comment:4 whuss]:\n\n> #5438 says it went into 4.0.alpha0 not 3.4.2.\n\nOops, I must have looked at some permutation of \"5438\" then. Sorry for the screwup.\n \n> Cheers,\n\n> Wilfried\n\nClosed as dupe. Jason: If you disagree let us know.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T11:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48534",
    "user": "mabshoff"
}
```

Replying to [comment:4 whuss]:

> #5438 says it went into 4.0.alpha0 not 3.4.2.

Oops, I must have looked at some permutation of "5438" then. Sorry for the screwup.
 
> Cheers,

> Wilfried

Closed as dupe. Jason: If you disagree let us know.

Cheers,

Michael



---

archive/issue_comments_048535.json:
```json
{
    "body": "Okay, I just tested it in 4.0, and it works great.  Sorry; it seems that I should have caught the other ticket in a search.  I'm not sure why I didn't.  Thanks for the prompt response!",
    "created_at": "2009-05-20T12:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6090#issuecomment-48535",
    "user": "@jasongrout"
}
```

Okay, I just tested it in 4.0, and it works great.  Sorry; it seems that I should have caught the other ticket in a search.  I'm not sure why I didn't.  Thanks for the prompt response!
