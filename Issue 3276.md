# Issue 3276: [with patch] more generic assumptions in calculus

archive/issues_003276.json:
```json
{
    "body": "Assignee: gfurnish\n\nFor example: \n\n\n```\nsage: var('n,m')\n(n, m)\nsage: assume(n, m, 'integer')\nsage: sin(n*m*pi)\n0\nsage: forget()\nsage: sin(n*m*pi)\nsin(pi*m*n)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3276\n\n",
    "created_at": "2008-05-23T08:13:34Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "[with patch] more generic assumptions in calculus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3276",
    "user": "robertwb"
}
```
Assignee: gfurnish

For example: 


```
sage: var('n,m')
(n, m)
sage: assume(n, m, 'integer')
sage: sin(n*m*pi)
0
sage: forget()
sage: sin(n*m*pi)
sin(pi*m*n)
```


Issue created by migration from https://trac.sagemath.org/ticket/3276





---

archive/issue_comments_022658.json:
```json
{
    "body": "Attachment [3276-assume.patch](tarball://root/attachments/some-uuid/ticket3276/3276-assume.patch) by robertwb created at 2008-05-23 08:16:38",
    "created_at": "2008-05-23T08:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22658",
    "user": "robertwb"
}
```

Attachment [3276-assume.patch](tarball://root/attachments/some-uuid/ticket3276/3276-assume.patch) by robertwb created at 2008-05-23 08:16:38



---

archive/issue_comments_022659.json:
```json
{
    "body": "Excellent work Robert -- this is really nice.  The code applies, passes, tests, and is well documented.",
    "created_at": "2008-05-23T08:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22659",
    "user": "mhansen"
}
```

Excellent work Robert -- this is really nice.  The code applies, passes, tests, and is well documented.



---

archive/issue_comments_022660.json:
```json
{
    "body": "I'm giving this a negative review - see the email I'm writing to sage-devel on how introducing more maxima-isms without serious consideration is bad. There is nothing wrong with the code (so it is probably safe to use as a patch if someone needs this feature now), but introducing code to deprecate it two weeks or three weeks later is not good practice in my opinion.",
    "created_at": "2008-05-23T17:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22660",
    "user": "gfurnish"
}
```

I'm giving this a negative review - see the email I'm writing to sage-devel on how introducing more maxima-isms without serious consideration is bad. There is nothing wrong with the code (so it is probably safe to use as a patch if someone needs this feature now), but introducing code to deprecate it two weeks or three weeks later is not good practice in my opinion.



---

archive/issue_comments_022661.json:
```json
{
    "body": "This is a feature that people have requested from me personally many times, so I think it's worthy of inclusion. I am skeptical that the new symbolics can be a drop-in replacement for maxima in two or three weeks (would be happy to be proven wrong) so I think that it has value. Also, the exposed interface, though it passes strings to maxima, is not tied to the way maxima does things and could easily be used in the new symbolics (if not, they are not a drop-in replacement). \n\nWould it be better if there was a smaller, limited set of options (e.g. \"integer\", \"even\", \"odd\", \"rational\", ...) that we will be sure to want to support in the future.",
    "created_at": "2008-05-23T18:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22661",
    "user": "robertwb"
}
```

This is a feature that people have requested from me personally many times, so I think it's worthy of inclusion. I am skeptical that the new symbolics can be a drop-in replacement for maxima in two or three weeks (would be happy to be proven wrong) so I think that it has value. Also, the exposed interface, though it passes strings to maxima, is not tied to the way maxima does things and could easily be used in the new symbolics (if not, they are not a drop-in replacement). 

Would it be better if there was a smaller, limited set of options (e.g. "integer", "even", "odd", "rational", ...) that we will be sure to want to support in the future.



---

archive/issue_comments_022662.json:
```json
{
    "body": "Drop in replacement for Maxima? doubtful.  Drop in replacement for sage.calculus? almost certainly.  Part of that is changing how assumptions work.  Like it or not assumptions are tied to the maxima way of doing things.  What makes you think I'm going to choose an assumption model that is 100% compatible with the Maxima way?  You can declare variables to be in ZZ instead of having to assume it, so immediately your method becomes very inefficient.  Also your patch has horrible error checking.  It allows for declaring a variable to be analytic or increasing.  This should almost certainly be handled better, even if your making an argument that this should go in now.  I am not going to waste time implementing complicated features in symbolics because people wern't willing to design them properly.",
    "created_at": "2008-05-23T19:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22662",
    "user": "gfurnish"
}
```

Drop in replacement for Maxima? doubtful.  Drop in replacement for sage.calculus? almost certainly.  Part of that is changing how assumptions work.  Like it or not assumptions are tied to the maxima way of doing things.  What makes you think I'm going to choose an assumption model that is 100% compatible with the Maxima way?  You can declare variables to be in ZZ instead of having to assume it, so immediately your method becomes very inefficient.  Also your patch has horrible error checking.  It allows for declaring a variable to be analytic or increasing.  This should almost certainly be handled better, even if your making an argument that this should go in now.  I am not going to waste time implementing complicated features in symbolics because people wern't willing to design them properly.



---

archive/issue_comments_022663.json:
```json
{
    "body": "To summarize, you don't want this feature because it is at odds with the way you are handling it in your symbolics package (which is a perfectly valid argument).",
    "created_at": "2008-05-23T19:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22663",
    "user": "robertwb"
}
```

To summarize, you don't want this feature because it is at odds with the way you are handling it in your symbolics package (which is a perfectly valid argument).



---

archive/issue_comments_022664.json:
```json
{
    "body": "Basically yes.",
    "created_at": "2008-05-23T20:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22664",
    "user": "gfurnish"
}
```

Basically yes.



---

archive/issue_comments_022665.json:
```json
{
    "body": "After discussion at dev1 we have decided that we should merge this but only the assume function should be considered \"public\" in that it will be supported after the symbolics rewrite.  The other support classes/methods will probably go away.",
    "created_at": "2008-06-18T21:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22665",
    "user": "gfurnish"
}
```

After discussion at dev1 we have decided that we should merge this but only the assume function should be considered "public" in that it will be supported after the symbolics rewrite.  The other support classes/methods will probably go away.



---

archive/issue_comments_022666.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T09:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22666",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022667.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T09:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3276",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3276#issuecomment-22667",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
