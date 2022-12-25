# Issue 874: Implement Jordan and Rational Canonical Form

archive/issues_000874.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/874\n\n",
    "created_at": "2007-10-13T05:57:48Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Implement Jordan and Rational Canonical Form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/874",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/874





---

archive/issue_comments_005371.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-01-29T12:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5371",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_005372.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-29T12:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5372",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005373.json:
```json
{
    "body": "I have naive code (= compute Smith Normal Form) written to do both of these now. I need to get it cleaned up and included (which means figuring out where it goes in sage/matrix/), but I wanted to put a note up to avoid duplication of work. \n\nThat said, if someone has an interesting/clever algorithm, it's probably better than what I've written, so that should be submitted.\n\nWilliam points out that for JCF over exact fields, using A.decomposition() will probably be much better.",
    "created_at": "2008-01-29T12:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5373",
    "user": "https://github.com/craigcitro"
}
```

I have naive code (= compute Smith Normal Form) written to do both of these now. I need to get it cleaned up and included (which means figuring out where it goes in sage/matrix/), but I wanted to put a note up to avoid duplication of work. 

That said, if someone has an interesting/clever algorithm, it's probably better than what I've written, so that should be submitted.

William points out that for JCF over exact fields, using A.decomposition() will probably be much better.



---

archive/issue_comments_005374.json:
```json
{
    "body": "I mean RCF not JCF over exact fields...",
    "created_at": "2008-01-29T12:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5374",
    "user": "https://github.com/williamstein"
}
```

I mean RCF not JCF over exact fields...



---

archive/issue_comments_005375.json:
```json
{
    "body": "Compute Jordan Canonical form extremely naively.",
    "created_at": "2008-01-29T16:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5375",
    "user": "https://github.com/jasongrout"
}
```

Compute Jordan Canonical form extremely naively.



---

archive/issue_comments_005376.json:
```json
{
    "body": "Attachment [jordan-form.patch](tarball://root/attachments/some-uuid/ticket874/jordan-form.patch) by @jasongrout created at 2008-01-29 16:14:23\n\nThat's funny, I just wrote some code last night to compute jordan canonical form using the powers of A-xI, the by-hand method you learn in linear algebra.  I've attached it above.  Your code probably blows this out of the water, but it would be interesting to see the speed comparison anyway.  The patch is a bit faster after you apply the patch in #1973.",
    "created_at": "2008-01-29T16:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5376",
    "user": "https://github.com/jasongrout"
}
```

Attachment [jordan-form.patch](tarball://root/attachments/some-uuid/ticket874/jordan-form.patch) by @jasongrout created at 2008-01-29 16:14:23

That's funny, I just wrote some code last night to compute jordan canonical form using the powers of A-xI, the by-hand method you learn in linear algebra.  I've attached it above.  Your code probably blows this out of the water, but it would be interesting to see the speed comparison anyway.  The patch is a bit faster after you apply the patch in #1973.



---

archive/issue_comments_005377.json:
```json
{
    "body": "The article:\n\nhttp://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6WM7-45M2XHC-M&_user=716796&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000040078&_version=1&_urlVersion=0&_userid=716796&md5=10649e53c80185bed8cf7ff212858f11\n\nmight be useful to implement a fast algorithm (and may be what William is talking about above mentioning decompositions).",
    "created_at": "2008-01-29T16:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5377",
    "user": "https://github.com/jasongrout"
}
```

The article:

http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6WM7-45M2XHC-M&_user=716796&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000040078&_version=1&_urlVersion=0&_userid=716796&md5=10649e53c80185bed8cf7ff212858f11

might be useful to implement a fast algorithm (and may be what William is talking about above mentioning decompositions).



---

archive/issue_comments_005378.json:
```json
{
    "body": "It's interesting that Jason had so much faith in my code -- apparently William's skepticism was warranted. :) It turns out that it's terrible right now -- on small examples, it's roughly 5X slower than Jason's, and it's still running on a large example (where your code took 7.5 sec). \n\nThe problem is easy to understand when you look at the code: to compute the Smith Normal Form of T-x*I, I work over a polynomial ring, and there's neither (1) specialized polynomial arithmetic (i.e. as in the ZZ[X] case) nor (2) a specific type for matrices of polynomials (at least that I know about!). As a result, lots of things that should be C calls are instead Python calls. \n\nI glanced at the Allan Steel paper above -- we should probably go ahead and implement something like this in the long-term. In the short term, though, Jason's code is definitely superior. I think we should add one thing, though -- passing in a base_ring argument, and just changing \n\n  evals = self.charpoly().roots()\n\nto \n\n  evals = self.charpoly().roots(base_ring)\n\nwe'd have something that would work over an arbitrary base ring (indeed, the error checking is already there!). I'm making one implicit assumption, namely that the coercion model could handle coercing matrices around for us, but that doesn't seem unlikely at all -- if nothing else, we'd find coercion bugs to fix.",
    "created_at": "2008-01-30T09:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5378",
    "user": "https://github.com/craigcitro"
}
```

It's interesting that Jason had so much faith in my code -- apparently William's skepticism was warranted. :) It turns out that it's terrible right now -- on small examples, it's roughly 5X slower than Jason's, and it's still running on a large example (where your code took 7.5 sec). 

The problem is easy to understand when you look at the code: to compute the Smith Normal Form of T-x*I, I work over a polynomial ring, and there's neither (1) specialized polynomial arithmetic (i.e. as in the ZZ[X] case) nor (2) a specific type for matrices of polynomials (at least that I know about!). As a result, lots of things that should be C calls are instead Python calls. 

I glanced at the Allan Steel paper above -- we should probably go ahead and implement something like this in the long-term. In the short term, though, Jason's code is definitely superior. I think we should add one thing, though -- passing in a base_ring argument, and just changing 

  evals = self.charpoly().roots()

to 

  evals = self.charpoly().roots(base_ring)

we'd have something that would work over an arbitrary base ring (indeed, the error checking is already there!). I'm making one implicit assumption, namely that the coercion model could handle coercing matrices around for us, but that doesn't seem unlikely at all -- if nothing else, we'd find coercion bugs to fix.



---

archive/issue_comments_005379.json:
```json
{
    "body": "Jason's code might be naive, but at least it seems to work. Implementing an efficient/fast version of the algorithm should be another ticket once we merged this version.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T22:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5379",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason's code might be naive, but at least it seems to work. Implementing an efficient/fast version of the algorithm should be another ticket once we merged this version.

Cheers,

Michael



---

archive/issue_comments_005380.json:
```json
{
    "body": "Attachment [jordan-form.2.patch](tarball://root/attachments/some-uuid/ticket874/jordan-form.2.patch) by @jasongrout created at 2008-02-16 05:49:22\n\nApply (and review) instead of original jordan-form.patch.",
    "created_at": "2008-02-16T05:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5380",
    "user": "https://github.com/jasongrout"
}
```

Attachment [jordan-form.2.patch](tarball://root/attachments/some-uuid/ticket874/jordan-form.2.patch) by @jasongrout created at 2008-02-16 05:49:22

Apply (and review) instead of original jordan-form.patch.



---

archive/issue_comments_005381.json:
```json
{
    "body": "The jordan-form.2.patch replaces jordan-form.patch and:\n\n1. rebases against 2.10.1\n\n2. implements the base_ring argument mentioned above\n\n3. uses the Partition object instead of the deprecated partitions_associated function.",
    "created_at": "2008-02-16T05:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5381",
    "user": "https://github.com/jasongrout"
}
```

The jordan-form.2.patch replaces jordan-form.patch and:

1. rebases against 2.10.1

2. implements the base_ring argument mentioned above

3. uses the Partition object instead of the deprecated partitions_associated function.



---

archive/issue_comments_005382.json:
```json
{
    "body": "I agree with Michael's sentiment above that this should get merged -- maybe merge it, and: \n\n- make another ticket saying we still need a rational canonical form algorithm\n- note in the docstring for Jordan canonical form that the algorithm is the naive one\n\nDoes that seem reasonable?",
    "created_at": "2008-02-16T06:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5382",
    "user": "https://github.com/craigcitro"
}
```

I agree with Michael's sentiment above that this should get merged -- maybe merge it, and: 

- make another ticket saying we still need a rational canonical form algorithm
- note in the docstring for Jordan canonical form that the algorithm is the naive one

Does that seem reasonable?



---

archive/issue_comments_005383.json:
```json
{
    "body": "Yes, I agree with craig.  It's very good to have a step 1 that implements something naive, then a step 2 that greatly optimizes it in special cases.  It is also a very good idea to be bluntly clear that an implementation is naive if it is.",
    "created_at": "2008-02-16T06:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5383",
    "user": "https://github.com/williamstein"
}
```

Yes, I agree with craig.  It's very good to have a step 1 that implements something naive, then a step 2 that greatly optimizes it in special cases.  It is also a very good idea to be bluntly clear that an implementation is naive if it is.



---

archive/issue_comments_005384.json:
```json
{
    "body": "Attachment [jordan-form.3.patch](tarball://root/attachments/some-uuid/ticket874/jordan-form.3.patch) by @jasongrout created at 2008-02-22 20:37:11\n\nAdds a note saying that the computation is naive.",
    "created_at": "2008-02-22T20:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5384",
    "user": "https://github.com/jasongrout"
}
```

Attachment [jordan-form.3.patch](tarball://root/attachments/some-uuid/ticket874/jordan-form.3.patch) by @jasongrout created at 2008-02-22 20:37:11

Adds a note saying that the computation is naive.



---

archive/issue_comments_005385.json:
```json
{
    "body": "The jordan-form.3.patch adds a note to the docs saying that the computation is naive.",
    "created_at": "2008-02-22T20:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5385",
    "user": "https://github.com/jasongrout"
}
```

The jordan-form.3.patch adds a note to the docs saying that the computation is naive.



---

archive/issue_comments_005386.json:
```json
{
    "body": "jordan-form.3.patch should be applied instead of any of the previous ones.",
    "created_at": "2008-02-22T20:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5386",
    "user": "https://github.com/jasongrout"
}
```

jordan-form.3.patch should be applied instead of any of the previous ones.



---

archive/issue_comments_005387.json:
```json
{
    "body": "So I agree with Jason's earlier comments on IRC that this ticket should be put to bed already. I have only two minor nitpicks:\n\n* it's going to need to be re-based against 2.10.2 when it's out\n* I think `jordan_form()` should take an optional argument `subdivide=True`, \n which it passes off to `block_diagonal_matrix`. (This is just so that the user can \n control whether or not the matrix gets printed with blocks shown, which I know \n most people probably like, but I personally find annoying.)\n\nJason, if you want to do that real quick when 2.10.2 is out, I'll give it a positive review.\n\n-cc",
    "created_at": "2008-02-23T01:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5387",
    "user": "https://github.com/craigcitro"
}
```

So I agree with Jason's earlier comments on IRC that this ticket should be put to bed already. I have only two minor nitpicks:

* it's going to need to be re-based against 2.10.2 when it's out
* I think `jordan_form()` should take an optional argument `subdivide=True`, 
 which it passes off to `block_diagonal_matrix`. (This is just so that the user can 
 control whether or not the matrix gets printed with blocks shown, which I know 
 most people probably like, but I personally find annoying.)

Jason, if you want to do that real quick when 2.10.2 is out, I'll give it a positive review.

-cc



---

archive/issue_comments_005388.json:
```json
{
    "body": "I get the following on 2.10.3.alpha0\n\n```\ncd \"/home/mhansen/sage-2.10.3.alpha0/devel/sage\" && hg status\ncd \"/home/mhansen/sage-2.10.3.alpha0/devel/sage\" && hg status\ncd \"/home/mhansen/sage-2.10.3.alpha0/devel/sage\" && hg import   \"/home/mhansen/.sage/temp/sage/15288/tmp_2.patch\"\napplying /home/mhansen/.sage/temp/sage/15288/tmp_2.patch\npatching file sage/matrix/matrix2.pyx\nHunk #1 FAILED at 3035\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-02-27T18:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5388",
    "user": "https://github.com/mwhansen"
}
```

I get the following on 2.10.3.alpha0

```
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg import   "/home/mhansen/.sage/temp/sage/15288/tmp_2.patch"
applying /home/mhansen/.sage/temp/sage/15288/tmp_2.patch
patching file sage/matrix/matrix2.pyx
Hunk #1 FAILED at 3035
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_005389.json:
```json
{
    "body": "Attachment [874.patch](tarball://root/attachments/some-uuid/ticket874/874.patch) by @mwhansen created at 2008-02-27 20:10:11\n\nNew patch posted which applies cleanly against 2.10.3.alpha0 + #1186. Just apply 874.patch.\n\n\nPositive review from me.",
    "created_at": "2008-02-27T20:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5389",
    "user": "https://github.com/mwhansen"
}
```

Attachment [874.patch](tarball://root/attachments/some-uuid/ticket874/874.patch) by @mwhansen created at 2008-02-27 20:10:11

New patch posted which applies cleanly against 2.10.3.alpha0 + #1186. Just apply 874.patch.


Positive review from me.



---

archive/issue_comments_005390.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000988.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-28T00:41:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/874#event-988"
}
```



---

archive/issue_comments_005391.json:
```json
{
    "body": "Merged 874.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 874.patch in Sage 2.10.3.rc0



---

archive/issue_comments_005392.json:
```json
{
    "body": "So did the algorithm for rational canonical form not get implemented?  (This would follow from a Smith normal form for a matrix over F[x], if it is computed...)\n\nJV",
    "created_at": "2008-03-12T19:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5392",
    "user": "https://github.com/jvoight"
}
```

So did the algorithm for rational canonical form not get implemented?  (This would follow from a Smith normal form for a matrix over F[x], if it is computed...)

JV



---

archive/issue_comments_005393.json:
```json
{
    "body": "I implemented rational canonical form in precisely that way. It's horrendously slow. William has already written code that can be used to make a usable rational canonical form algorithm (which is mentioned above) -- someone should open another ticket about this, probably.",
    "created_at": "2008-03-12T19:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/874#issuecomment-5393",
    "user": "https://github.com/craigcitro"
}
```

I implemented rational canonical form in precisely that way. It's horrendously slow. William has already written code that can be used to make a usable rational canonical form algorithm (which is mentioned above) -- someone should open another ticket about this, probably.
