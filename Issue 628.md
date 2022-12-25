# Issue 628: Make binomial(x,m) work for symbolic expressions when x-m is an integer

archive/issues_000628.json:
```json
{
    "body": "Assignee: somebody\n\nCurrently binomial(x,m) works for symbolic expressions if m is integer, for example\n\n[[[ \nsage: n=var('n')\nsage: binomial(n,2)\n(n - 1)*n/2 \n]]]\n \nbut binomial (n,n-2) or binomial(n+1,n-1) does not work. \n\nI'm submitting a patch for making this work, by defining \n\nbinomial(x,m) = binomial (x,x-m)\n\nwhen x-m is an integer. \n\nThis would be consistent with the way  in which maxima handles the binomial function\n(see http://maxima.sourceforge.net/docs/manual/en/maxima_31.html#SEC126)\n\nNote that the proposed rule makes sense when x is an integer. However, Sage does not have\na way to specify a domain for a symbolic variable (as for example Axiom does).\n\nIssue created by migration from https://trac.sagemath.org/ticket/628\n\n",
    "created_at": "2007-09-09T14:57:10Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4.2",
    "title": "Make binomial(x,m) work for symbolic expressions when x-m is an integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/628",
    "user": "https://github.com/pdenapo"
}
```
Assignee: somebody

Currently binomial(x,m) works for symbolic expressions if m is integer, for example

[[[ 
sage: n=var('n')
sage: binomial(n,2)
(n - 1)*n/2 
]]]
 
but binomial (n,n-2) or binomial(n+1,n-1) does not work. 

I'm submitting a patch for making this work, by defining 

binomial(x,m) = binomial (x,x-m)

when x-m is an integer. 

This would be consistent with the way  in which maxima handles the binomial function
(see http://maxima.sourceforge.net/docs/manual/en/maxima_31.html#SEC126)

Note that the proposed rule makes sense when x is an integer. However, Sage does not have
a way to specify a domain for a symbolic variable (as for example Axiom does).

Issue created by migration from https://trac.sagemath.org/ticket/628





---

archive/issue_comments_003213.json:
```json
{
    "body": "Attachment [binomial_symbolic.patch](tarball://root/attachments/some-uuid/ticket628/binomial_symbolic.patch) by @pdenapo created at 2007-09-09 14:59:41",
    "created_at": "2007-09-09T14:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3213",
    "user": "https://github.com/pdenapo"
}
```

Attachment [binomial_symbolic.patch](tarball://root/attachments/some-uuid/ticket628/binomial_symbolic.patch) by @pdenapo created at 2007-09-09 14:59:41



---

archive/issue_comments_003214.json:
```json
{
    "body": "This seems pretty nice, it has doctests, so let's shoot for 2.8.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-09T18:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3214",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This seems pretty nice, it has doctests, so let's shoot for 2.8.4.2.

Cheers,

Michael



---

archive/issue_comments_003215.json:
```json
{
    "body": "Changing assignee from somebody to @williamstein.",
    "created_at": "2007-09-09T18:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3215",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to @williamstein.



---

archive/issue_comments_003216.json:
```json
{
    "body": "Yes, I'll referee this patch...and comment after I'm done.",
    "created_at": "2007-09-10T12:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3216",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Yes, I'll referee this patch...and comment after I'm done.



---

archive/issue_comments_003217.json:
```json
{
    "body": "I'm slightly concerned about overheads on this one. By far the most common case for binomials is integer arguments. Already PARI beats Magma on the actual hard part of the computation, e.g.\n\n\n```\n> time for i := 1 to 10000 do x := Binomial(500, 250); end for;  \nTime: 1.550\n```\n\n\n```\nsage: time for i in range(10000): x = binomial(500, 250)\nWall time: 0.52\n```\n\n\nBUT the overheads are already an issue for smaller problems:\n\n```\n> time for i := 1 to 100000 do x := Binomial(20, 13); end for; \nTime: 0.070\n```\n\n\n```\nsage: time for i in range(100000): x = binomial(20, 13)\nWall time: 2.82\n```\n\n\nPerhaps this should be a new ticket, \"add fast pathway for binomials of integer arguments\"?",
    "created_at": "2007-09-10T18:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3217",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I'm slightly concerned about overheads on this one. By far the most common case for binomials is integer arguments. Already PARI beats Magma on the actual hard part of the computation, e.g.


```
> time for i := 1 to 10000 do x := Binomial(500, 250); end for;  
Time: 1.550
```


```
sage: time for i in range(10000): x = binomial(500, 250)
Wall time: 0.52
```


BUT the overheads are already an issue for smaller problems:

```
> time for i := 1 to 100000 do x := Binomial(20, 13); end for; 
Time: 0.070
```


```
sage: time for i in range(100000): x = binomial(20, 13)
Wall time: 2.82
```


Perhaps this should be a new ticket, "add fast pathway for binomials of integer arguments"?



---

archive/issue_comments_003218.json:
```json
{
    "body": "I import'ed this patch and made a few tweaks to the doc-string.\n\n* Doc-tests pass\n* Speed does not suffer for the \"fast path\" integer case (and I can't see why it should from the changes)\n\nThe only thing that gives me cause for pause is\nsage: binomial(5/2,3/2)\n5/2\nbut that only potential complaint is that this should be undefined so I don't think this is a big issue.  You could have already done similar tricks with symbolic inputs and substitution.\n\ndmharvey's speed comments are legit, but are not affected by this patch and are not at all unique to this function.  I'm going to write sage-devel about that.\n\nI've attached my patches with revised doc-strings and they pass my referee inspection.\n\n--\nJoel",
    "created_at": "2007-09-10T20:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3218",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I import'ed this patch and made a few tweaks to the doc-string.

* Doc-tests pass
* Speed does not suffer for the "fast path" integer case (and I can't see why it should from the changes)

The only thing that gives me cause for pause is
sage: binomial(5/2,3/2)
5/2
but that only potential complaint is that this should be undefined so I don't think this is a big issue.  You could have already done similar tricks with symbolic inputs and substitution.

dmharvey's speed comments are legit, but are not affected by this patch and are not at all unique to this function.  I'm going to write sage-devel about that.

I've attached my patches with revised doc-strings and they pass my referee inspection.

--
Joel



---

archive/issue_comments_003219.json:
```json
{
    "body": "Oops, sorry about the bad formatting:\n\nThis is the only code snippet which concerned me in the post-patch sage, but I've explained above why I don't think this matters.\n\n```\nsage: binomial(5/2,3/2)\n5/2\n```\n",
    "created_at": "2007-09-10T20:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3219",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Oops, sorry about the bad formatting:

This is the only code snippet which concerned me in the post-patch sage, but I've explained above why I don't think this matters.

```
sage: binomial(5/2,3/2)
5/2
```




---

archive/issue_comments_003220.json:
```json
{
    "body": "Attachment [binomial_patch.hg](tarball://root/attachments/some-uuid/ticket628/binomial_patch.hg) by jbmohler created at 2007-09-10 20:34:58\n\nhg bundle including the patch file and my doc-string revisions",
    "created_at": "2007-09-10T20:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3220",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [binomial_patch.hg](tarball://root/attachments/some-uuid/ticket628/binomial_patch.hg) by jbmohler created at 2007-09-10 20:34:58

hg bundle including the patch file and my doc-string revisions



---

archive/issue_comments_003221.json:
```json
{
    "body": "At least some of this has been merged. See\n\nhttp://www.sagemath.org/hg/sage-main/rev/8def8d03e4a2\n\nIs there more to come or can we close this ticket?\n\nCheers,\n\nMichael",
    "created_at": "2007-09-11T05:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

At least some of this has been merged. See

http://www.sagemath.org/hg/sage-main/rev/8def8d03e4a2

Is there more to come or can we close this ticket?

Cheers,

Michael



---

archive/issue_comments_003222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-12T18:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/628#issuecomment-3222",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
