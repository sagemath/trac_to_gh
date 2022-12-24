# Issue 8904: libsingular: memory leak in Matrix.act_on_polynomial

archive/issues_008904.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb\n\nKeywords: libsingular act_on_polynomial memleak\n\nThere is a memory leak that occurs when mapping a multivariate polynomial using a matrix:\n\n```\nsage: R.<a,b>  =  QQ[]\nsage: M = Matrix([[0,1],[1,0]])\nsage: n = 0\nsage: p = R.random_element()\nsage: q = M.act_on_polynomial(p)\nsage: mem = get_memory_usage()\nsage: while(1):\n....:     n+=1\n....:     q = M.act_on_polynomial(p)\n....:     if get_memory_usage()>mem:\n....:         mem = get_memory_usage()\n....:         print mem,n\n....:\n801.04296875 2\n801.54296875 2011\n802.04296875 4738\n802.54296875 7406\n803.04296875 10091\n803.54296875 12809\n804.04296875 15495\n804.54296875 18171\n805.04296875 20873\n805.54296875 23561\n806.04296875 26251\n...\n```\n\n\nThis does not occur if one maps the polynomial by a proper morphism:\n\n```\nsage: f = R.hom([M.act_on_polynomial(t) for t in R.gens()],R)\nsage: while(1):\n....:     n+=1\n....:     q = f(p)\n....:     if get_memory_usage()>mem:\n....:         mem = get_memory_usage()\n....:         print mem,n\n....:\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8904\n\n",
    "created_at": "2010-05-06T12:01:33Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libsingular: memory leak in Matrix.act_on_polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8904",
    "user": "@simon-king-jena"
}
```
Assignee: tbd

CC:  @malb

Keywords: libsingular act_on_polynomial memleak

There is a memory leak that occurs when mapping a multivariate polynomial using a matrix:

```
sage: R.<a,b>  =  QQ[]
sage: M = Matrix([[0,1],[1,0]])
sage: n = 0
sage: p = R.random_element()
sage: q = M.act_on_polynomial(p)
sage: mem = get_memory_usage()
sage: while(1):
....:     n+=1
....:     q = M.act_on_polynomial(p)
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:
801.04296875 2
801.54296875 2011
802.04296875 4738
802.54296875 7406
803.04296875 10091
803.54296875 12809
804.04296875 15495
804.54296875 18171
805.04296875 20873
805.54296875 23561
806.04296875 26251
...
```


This does not occur if one maps the polynomial by a proper morphism:

```
sage: f = R.hom([M.act_on_polynomial(t) for t in R.gens()],R)
sage: while(1):
....:     n+=1
....:     q = f(p)
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:
```




Issue created by migration from https://trac.sagemath.org/ticket/8904





---

archive/issue_comments_081965.json:
```json
{
    "body": "no longer an issue in 8.3.beta2",
    "created_at": "2018-05-27T09:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8904#issuecomment-81965",
    "user": "@fchapoton"
}
```

no longer an issue in 8.3.beta2



---

archive/issue_comments_081966.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-05-27T09:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8904#issuecomment-81966",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081967.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-27T10:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8904#issuecomment-81967",
    "user": "@simon-king-jena"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081968.json:
```json
{
    "body": "Replying to [comment:5 chapoton]:\n> no longer an issue in 8.3.beta2\n\nI can confirm. So, positive review with both of us as reviewers, I guess.",
    "created_at": "2018-05-27T10:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8904#issuecomment-81968",
    "user": "@simon-king-jena"
}
```

Replying to [comment:5 chapoton]:
> no longer an issue in 8.3.beta2

I can confirm. So, positive review with both of us as reviewers, I guess.



---

archive/issue_comments_081969.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8904#issuecomment-81969",
    "user": "@embray"
}
```

Resolution: invalid



---

archive/issue_comments_081970.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8904",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8904#issuecomment-81970",
    "user": "@embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
