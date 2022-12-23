# Issue 9910: Changing the LP formulation of feedback vertex/arc set to improve the speed

archive/issues_009910.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  abmasse mvngu\n\nA friend of mine had the good idea to think about the MFAS problem one evening, and told me that the LP formulation given in GLPK's examples was able to return the optimal value of a particular problem in 8ms. It took more (I did not wait) than 2 minutes for Sage.\n\nI looked at the two formulations, and they were so clode that I still do not understand why the second one is faster. I will think about it for a while, though I can already write the corresponding patch `:-)`\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9911\n\n",
    "created_at": "2010-09-14T20:59:42Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Changing the LP formulation of feedback vertex/arc set to improve the speed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9910",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  abmasse mvngu

A friend of mine had the good idea to think about the MFAS problem one evening, and told me that the LP formulation given in GLPK's examples was able to return the optimal value of a particular problem in 8ms. It took more (I did not wait) than 2 minutes for Sage.

I looked at the two formulations, and they were so clode that I still do not understand why the second one is faster. I will think about it for a while, though I can already write the corresponding patch `:-)`

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9911





---

archive/issue_comments_098577.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-15T17:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98577",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098578.json:
```json
{
    "body": "Patch rebased on top of #10151\n\nNathann",
    "created_at": "2010-10-23T16:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98578",
    "user": "ncohen"
}
```

Patch rebased on top of #10151

Nathann



---

archive/issue_comments_098579.json:
```json
{
    "body": "Hi Nathann !\n\nA question and a remark:\n\n1. If I understand correctly, your ticket is improving the speed of the minimum feedback vertex/arc set problems by providing another LP formulation. Could you detail where you took the first formulation (I assume you're the one who coded it) and where you got the new one? This could help in the review process to compare and make sure the two methods are equivalent.\n2. I a bunch of lines where lists are created without being used, such as in:\n\n```\n[p.add_constraint(d[v],min=n) for v in self]\n```\n\n  Wouldn't it be better to replace it with a loop?\n\n```\nfor v in self: p.add_constraint(d[v], min=n)\n```\n\n  I think it's useless to create a list that will be thrown to the garbage collector right away :) Moreover, the number of characters is exactly the same, so it's not a waste of space :)",
    "created_at": "2010-11-14T03:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98579",
    "user": "abmasse"
}
```

Hi Nathann !

A question and a remark:

1. If I understand correctly, your ticket is improving the speed of the minimum feedback vertex/arc set problems by providing another LP formulation. Could you detail where you took the first formulation (I assume you're the one who coded it) and where you got the new one? This could help in the review process to compare and make sure the two methods are equivalent.
2. I a bunch of lines where lists are created without being used, such as in:

```
[p.add_constraint(d[v],min=n) for v in self]
```

  Wouldn't it be better to replace it with a loop?

```
for v in self: p.add_constraint(d[v], min=n)
```

  I think it's useless to create a list that will be thrown to the garbage collector right away :) Moreover, the number of characters is exactly the same, so it's not a waste of space :)



---

archive/issue_comments_098580.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-11-14T03:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98580",
    "user": "abmasse"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_098581.json:
```json
{
    "body": "Hello !!!\n\nYou are totally right about these lists.. That's just how I coded LP at first, but it wasn't a good idea after all. You will find the \"modern LP code\" easier to read `:-D`\n\nAbout the formulations... Well, the first one was just the one I came up with when I first wanted to solve MFAS problems, and the other one was given to me by a friend who was reading glpk's examples. You will find this file there :\n\nhttp://stuff.mit.edu/afs/athena/software/glpk/examples/mfasp.mod\n\nNote that even though the speed improvement is great, I wrote #9923 some time later and wondered whether I should remove this patch because of it : there is no comparison possible between this LP formulation and #9923, which will be (when it will be merged) the default way to solve MFAS problems. This formulation will just stay as a backup, or to check both algorithms' correctness (unless people do not want it of course, but that's what I had in mind when writing #9923)...\n\n(patch updated)\n\nNathann",
    "created_at": "2010-11-16T07:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98581",
    "user": "ncohen"
}
```

Hello !!!

You are totally right about these lists.. That's just how I coded LP at first, but it wasn't a good idea after all. You will find the "modern LP code" easier to read `:-D`

About the formulations... Well, the first one was just the one I came up with when I first wanted to solve MFAS problems, and the other one was given to me by a friend who was reading glpk's examples. You will find this file there :

http://stuff.mit.edu/afs/athena/software/glpk/examples/mfasp.mod

Note that even though the speed improvement is great, I wrote #9923 some time later and wondered whether I should remove this patch because of it : there is no comparison possible between this LP formulation and #9923, which will be (when it will be merged) the default way to solve MFAS problems. This formulation will just stay as a backup, or to check both algorithms' correctness (unless people do not want it of course, but that's what I had in mind when writing #9923)...

(patch updated)

Nathann



---

archive/issue_comments_098582.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-16T07:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98582",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_098583.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-12T01:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98583",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098584.json:
```json
{
    "body": "Attachment\n\nYou're still using the list syntax for constraint addition loops at the end of the patch:\n\n```\n[p.add_constraint(d[u]-d[v]+n*(b[u]+b[v]),min=1) for (u,v) in self.edges(labels=None)] \n[p.add_constraint(d[u],max=n) for u in self]\n```\n\n\nOther than that, this patch looks good. All long tests pass against sage-4.6.1.rc1 and I'm otherwise happy. Fix the one issue, ping me and I'll set this to positive review.",
    "created_at": "2011-01-12T01:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98584",
    "user": "rlm"
}
```

Attachment

You're still using the list syntax for constraint addition loops at the end of the patch:

```
[p.add_constraint(d[u]-d[v]+n*(b[u]+b[v]),min=1) for (u,v) in self.edges(labels=None)] 
[p.add_constraint(d[u],max=n) for u in self]
```


Other than that, this patch looks good. All long tests pass against sage-4.6.1.rc1 and I'm otherwise happy. Fix the one issue, ping me and I'll set this to positive review.



---

archive/issue_comments_098585.json:
```json
{
    "body": "Added a small patch fixing the last two list comprehension liness.",
    "created_at": "2011-01-12T01:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98585",
    "user": "gbe"
}
```

Added a small patch fixing the last two list comprehension liness.



---

archive/issue_comments_098586.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-12T01:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98586",
    "user": "gbe"
}
```

Attachment



---

archive/issue_comments_098587.json:
```json
{
    "body": "Thank you!",
    "created_at": "2011-01-12T03:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98587",
    "user": "rlm"
}
```

Thank you!



---

archive/issue_comments_098588.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-12T03:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98588",
    "user": "rlm"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_098589.json:
```json
{
    "body": "Thanksssssss !! `:-)`",
    "created_at": "2011-01-12T08:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98589",
    "user": "ncohen"
}
```

Thanksssssss !! `:-)`



---

archive/issue_comments_098590.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9910#issuecomment-98590",
    "user": "jdemeyer"
}
```

Resolution: fixed
