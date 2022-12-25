# Issue 8998: galois_action on cusps has a bug

archive/issues_008998.json:
```json
{
    "body": "Assignee: @craigcitro\n\nTicket  #5822 implemented the action of Galois on cusps.  I think the algorithm was only designed to work for Gamma_0(N).  However, the code runs for other groups, and doesn't raise an error.  Unfortunately, it gives completely wrong results in some cases, e.g., \n\n```\nsage: G = Gamma1(19)\nsage: rational_cusps = [c for c in G.cusps() if c.galois_action(2,19).is_gamma1_equiv(c,19)]\nsage: rational_cusps\n[0, 2/19, 1/9, 1/8, 1/7, 3/19, 1/6, 1/5, 4/19, 1/4, 5/19, 6/19, 1/3,\n7/19, 8/19, 9/19, 1/2, Infinity]\n```\n\n\nHowever, exactly half the cusps are rational (see, e.g., my paper http://wstein.org/papers/j1p/ or the work of Kubert-Lang).  \n\nThis came up in research that Michael Stoll and I were doing, and it was temporarily very confusing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8998\n\n",
    "created_at": "2010-05-20T05:29:16Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "galois_action on cusps has a bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8998",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

Ticket  #5822 implemented the action of Galois on cusps.  I think the algorithm was only designed to work for Gamma_0(N).  However, the code runs for other groups, and doesn't raise an error.  Unfortunately, it gives completely wrong results in some cases, e.g., 

```
sage: G = Gamma1(19)
sage: rational_cusps = [c for c in G.cusps() if c.galois_action(2,19).is_gamma1_equiv(c,19)]
sage: rational_cusps
[0, 2/19, 1/9, 1/8, 1/7, 3/19, 1/6, 1/5, 4/19, 1/4, 5/19, 6/19, 1/3,
7/19, 8/19, 9/19, 1/2, Infinity]
```


However, exactly half the cusps are rational (see, e.g., my paper http://wstein.org/papers/j1p/ or the work of Kubert-Lang).  

This came up in research that Michael Stoll and I were doing, and it was temporarily very confusing. 

Issue created by migration from https://trac.sagemath.org/ticket/8998





---

archive/issue_comments_083074.json:
```json
{
    "body": "Attachment [trac_8998.patch](tarball://root/attachments/some-uuid/ticket8998/trac_8998.patch) by @williamstein created at 2011-03-22 00:59:48\n\nIt turns out that cusps (P^1(Q)) don't know their group of course. This function is thus somewhat badly named.  A minimal invasive change without breaking backwards compatibility is to clarify the *documentation* and do nothing else.  I think that is enough to close this ticket, though I may want to make another ticket later to add other actions, etc.   But for now, it is certainly a big improvement to at least fix a major incorrect statement in the documentation!     This patch is pretty safe, since it *only* changes documentation.",
    "created_at": "2011-03-22T00:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83074",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8998.patch](tarball://root/attachments/some-uuid/ticket8998/trac_8998.patch) by @williamstein created at 2011-03-22 00:59:48

It turns out that cusps (P^1(Q)) don't know their group of course. This function is thus somewhat badly named.  A minimal invasive change without breaking backwards compatibility is to clarify the *documentation* and do nothing else.  I think that is enough to close this ticket, though I may want to make another ticket later to add other actions, etc.   But for now, it is certainly a big improvement to at least fix a major incorrect statement in the documentation!     This patch is pretty safe, since it *only* changes documentation.



---

archive/issue_comments_083075.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-22T00:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83075",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083076.json:
```json
{
    "body": "Looks good -- testing now.",
    "created_at": "2011-03-22T19:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83076",
    "user": "https://github.com/JohnCremona"
}
```

Looks good -- testing now.



---

archive/issue_comments_083077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-22T19:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83077",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083078.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> Looks good -- testing now.\n\nOK, tests passed.",
    "created_at": "2011-03-22T19:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83078",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 cremona]:
> Looks good -- testing now.

OK, tests passed.



---

archive/issue_comments_083079.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-13T07:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83079",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022025.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-13T07:42:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8998#event-22025"
}
```



---

archive/issue_comments_083080.json:
```json
{
    "body": "This ticket is a false ticket. I just looked in to the article and the code in the article is really general. The problem is that is_gamma1_equiv does not do what you expect it to!\n\n\n```\nif Cusp(0).is_gamma1_equiv(Cusp(infinity),101):\n    print \"You would not expect to see something printed\"\n```\n\nActually prints the above statement.\nThe reason for this is that is_gamma1_equiv does not return a bool but a tuple. The first element of this tuple is the bool you were actually looking for.\n\nBy the way, I find the claim in this ticket that the code of 5882 only works for Gamma0(N) quite stupid because for Gamma0(n) one might as well implement the following:\n\n```\ndef galois_action(self,t,N):\n    return self\n```\n\nSince all cusps on X_0(N).\n\nHowever there is still a bug in the code because:\n\n```\nN=5\nG=Gamma1(N)\nfor i in G.cusps():\n    print [j.galois_action(2,N).is_gamma1_equiv(i,N)[0] for j in G.cusps()].count(True)\n```\n\nPrints\n\n```\n2\n1\n0\n1\n```\n\nSo the the galois action is not even a permutation!\n\nWhat would be the right thing to do? Reopen this ticket, open a new one?",
    "created_at": "2012-07-08T01:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83080",
    "user": "https://github.com/koffie"
}
```

This ticket is a false ticket. I just looked in to the article and the code in the article is really general. The problem is that is_gamma1_equiv does not do what you expect it to!


```
if Cusp(0).is_gamma1_equiv(Cusp(infinity),101):
    print "You would not expect to see something printed"
```

Actually prints the above statement.
The reason for this is that is_gamma1_equiv does not return a bool but a tuple. The first element of this tuple is the bool you were actually looking for.

By the way, I find the claim in this ticket that the code of 5882 only works for Gamma0(N) quite stupid because for Gamma0(n) one might as well implement the following:

```
def galois_action(self,t,N):
    return self
```

Since all cusps on X_0(N).

However there is still a bug in the code because:

```
N=5
G=Gamma1(N)
for i in G.cusps():
    print [j.galois_action(2,N).is_gamma1_equiv(i,N)[0] for j in G.cusps()].count(True)
```

Prints

```
2
1
0
1
```

So the the galois action is not even a permutation!

What would be the right thing to do? Reopen this ticket, open a new one?



---

archive/issue_comments_083081.json:
```json
{
    "body": "Open a new one, with cross-referencing.",
    "created_at": "2012-07-08T09:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83081",
    "user": "https://github.com/JohnCremona"
}
```

Open a new one, with cross-referencing.



---

archive/issue_comments_083082.json:
```json
{
    "body": "Ok, I created #13253 for this. And uploaded the patch I already created. It now needs review.",
    "created_at": "2012-07-14T05:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8998",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8998#issuecomment-83082",
    "user": "https://github.com/koffie"
}
```

Ok, I created #13253 for this. And uploaded the patch I already created. It now needs review.
