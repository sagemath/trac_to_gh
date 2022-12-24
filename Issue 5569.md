# Issue 5569: [with patch, needs review] weil restriction of scalars

archive/issues_005569.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @JohnCremona\n\nWhile cleaning up `mq.MPolynomialSystem` I moved its misnamed `change_ring()` function to a more proper place, i.e. `weil_restriction()` on ideals. Note, that these are defined on varieties but we don't have any variety objects and the function indeed works with ideal generators.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5569\n\n",
    "created_at": "2009-03-19T22:28:05Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] weil restriction of scalars",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5569",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @JohnCremona

While cleaning up `mq.MPolynomialSystem` I moved its misnamed `change_ring()` function to a more proper place, i.e. `weil_restriction()` on ideals. Note, that these are defined on varieties but we don't have any variety objects and the function indeed works with ideal generators.

Issue created by migration from https://trac.sagemath.org/ticket/5569





---

archive/issue_comments_043392.json:
```json
{
    "body": "\n```\n15:43 < wstein> The patch looks good, except why not define the Weil restriction of scalars\n15:43 < wstein> functor.\n15:43 < wstein> You don't define it, but giving a complete valid mathematical definition only\n15:43 < wstein> takes about 2-3 sentences.\n15:43 < wstein> I can't see why not to do that.\n15:43 < malb> okay\n15:44 < wstein> Serge Lang first taught me about that construction using equations\n15:44 < wstein> when I was having lunch with him once in grad school.\n15:44 < wstein> Then I personally realized it is a functor and used that to prove that\n15:44 < malb> I knew about this for a while but learned the proper name just now\n15:44 < wstein> it is unique up to whatever...\n15:44 < wstein> It was just an exercise for me, of course, since it is all well known.\n15:45 < wstein> Also, could you add an example that involves an elliptic curve (affine patch \n                of one, at least)\n15:45 < wstein> over a quadratic field?\n15:45 < wstein> That would be cool.\n```\n",
    "created_at": "2009-03-19T22:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5569#issuecomment-43392",
    "user": "@williamstein"
}
```


```
15:43 < wstein> The patch looks good, except why not define the Weil restriction of scalars
15:43 < wstein> functor.
15:43 < wstein> You don't define it, but giving a complete valid mathematical definition only
15:43 < wstein> takes about 2-3 sentences.
15:43 < wstein> I can't see why not to do that.
15:43 < malb> okay
15:44 < wstein> Serge Lang first taught me about that construction using equations
15:44 < wstein> when I was having lunch with him once in grad school.
15:44 < wstein> Then I personally realized it is a functor and used that to prove that
15:44 < malb> I knew about this for a while but learned the proper name just now
15:44 < wstein> it is unique up to whatever...
15:44 < wstein> It was just an exercise for me, of course, since it is all well known.
15:45 < wstein> Also, could you add an example that involves an elliptic curve (affine patch 
                of one, at least)
15:45 < wstein> over a quadratic field?
15:45 < wstein> That would be cool.
```




---

archive/issue_comments_043393.json:
```json
{
    "body": "Attachment [weil_restriction.patch](tarball://root/attachments/some-uuid/ticket5569/weil_restriction.patch) by @malb created at 2009-03-20 00:06:15",
    "created_at": "2009-03-20T00:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5569#issuecomment-43393",
    "user": "@malb"
}
```

Attachment [weil_restriction.patch](tarball://root/attachments/some-uuid/ticket5569/weil_restriction.patch) by @malb created at 2009-03-20 00:06:15



---

archive/issue_comments_043394.json:
```json
{
    "body": "I give this a positive review.  Great work on the docstring!  \n\nOne comment.  It is sad that we have to write code like this to do a coercion:\n\n```\n l = [helper(str(f))  for f in self.gens()] \n```\n\n\nAs a challenge to Martin -- can you improve Sage so this decimal string conversion (which could be a killer show stopper if the ideal had huge elements) isn't needed, and instead one can use a homomorphism?",
    "created_at": "2009-03-22T00:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5569#issuecomment-43394",
    "user": "@williamstein"
}
```

I give this a positive review.  Great work on the docstring!  

One comment.  It is sad that we have to write code like this to do a coercion:

```
 l = [helper(str(f))  for f in self.gens()] 
```


As a challenge to Martin -- can you improve Sage so this decimal string conversion (which could be a killer show stopper if the ideal had huge elements) isn't needed, and instead one can use a homomorphism?



---

archive/issue_comments_043395.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> As a challenge to Martin -- can you improve Sage so this decimal string conversion (which \n> could be a killer show stopper if the ideal had huge elements) isn't needed, and instead one \n> can use a homomorphism?\n\nThis is now #5590",
    "created_at": "2009-03-23T12:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5569#issuecomment-43395",
    "user": "@malb"
}
```

Replying to [comment:4 was]:
> As a challenge to Martin -- can you improve Sage so this decimal string conversion (which 
> could be a killer show stopper if the ideal had huge elements) isn't needed, and instead one 
> can use a homomorphism?

This is now #5590



---

archive/issue_comments_043396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5569#issuecomment-43396",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043397.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T20:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5569#issuecomment-43397",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
