# Issue 2356: Bug in discrete_log_generic

archive/issues_002356.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  marshbuck@gmail.com\n\nMarshall Buck reports (email to sage-support 2008-02-29):\n\nProblem 1.  Fails because the list sizes in the baby step giant step\nmethod are too small.\n\nExample. [NB This particular example does *not* fail with 2.10.2]\n\n```\nF.<w> = GF(121)\nv = w^120\nv.log(w)\n```\nbombs with:\n\n```\nFile \"/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/\narith.py\", line 2164, in discrete_log_generic\n   raise ValueError, \"Log of %s to the base %s does not exist.\"%(a,b)\nValueError: Log of 2*w + 10 to the base w does not exist.\n```\nThis can be fixed by changing the append loop to make \"g\"  to {{{range(m\n+1)}}} instead of `range(m)`.  This makes g m+2 long and S2 m-long.  Then {{{(m\n+2)*m >= ord}}}.\n\n```\n   m = ord.isqrt()\n   g = [a]\n   c = b**(-m)\n   S2 = [1]\n   for i in range(m+1):  # suggested line change   ---  was range(m)\n       g.append(g[i]*c)\n       if i < m-1:\n           S2.append(S2[i]*b)\n   for y in g:\n       if y in S2:\n           x = S2.index(y)\n           return Z(m*(g.index(y)) + x)\n```\n\n2. The other problem is the inefficiency in the lookup \" {{{for y in g:\nif y in S2:}}} \".  The work is proportional to  \"ord\", insead of\nproportional to  \"m\" as intended by BSGS method.  It is quicker to do\na set lookup:\n\n```\n S2set = set(S2)\n for y in g:\n     if y in S2set:\n         x = S2.index(y)...\n```\n\n---\n\nComents by John Cremona:\n\n1. Note that this is related to #277\n\n2. I already suggested using a dict for the lookup instead of using lists or sets\n\nI will post a patch.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2356\n\n",
    "created_at": "2008-02-29T21:41:10Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Bug in discrete_log_generic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2356",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: joyner

CC:  marshbuck@gmail.com

Marshall Buck reports (email to sage-support 2008-02-29):

Problem 1.  Fails because the list sizes in the baby step giant step
method are too small.

Example. [NB This particular example does *not* fail with 2.10.2]

```
F.<w> = GF(121)
v = w^120
v.log(w)
```
bombs with:

```
File "/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/
arith.py", line 2164, in discrete_log_generic
   raise ValueError, "Log of %s to the base %s does not exist."%(a,b)
ValueError: Log of 2*w + 10 to the base w does not exist.
```
This can be fixed by changing the append loop to make "g"  to {{{range(m
+1)}}} instead of `range(m)`.  This makes g m+2 long and S2 m-long.  Then {{{(m
+2)*m >= ord}}}.

```
   m = ord.isqrt()
   g = [a]
   c = b**(-m)
   S2 = [1]
   for i in range(m+1):  # suggested line change   ---  was range(m)
       g.append(g[i]*c)
       if i < m-1:
           S2.append(S2[i]*b)
   for y in g:
       if y in S2:
           x = S2.index(y)
           return Z(m*(g.index(y)) + x)
```

2. The other problem is the inefficiency in the lookup " {{{for y in g:
if y in S2:}}} ".  The work is proportional to  "ord", insead of
proportional to  "m" as intended by BSGS method.  It is quicker to do
a set lookup:

```
 S2set = set(S2)
 for y in g:
     if y in S2set:
         x = S2.index(y)...
```

---

Coments by John Cremona:

1. Note that this is related to #277

2. I already suggested using a dict for the lookup instead of using lists or sets

I will post a patch.


Issue created by migration from https://trac.sagemath.org/ticket/2356





---

archive/issue_comments_015830.json:
```json
{
    "body": "Attachment [8682.patch](tarball://root/attachments/some-uuid/ticket2356/8682.patch) by @JohnCremona created at 2008-02-29 22:48:48\n\nAttached patch 8682 fixes both issues:  increases m by 1 and uses a dict() for fast lookup of the table.",
    "created_at": "2008-02-29T22:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15830",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8682.patch](tarball://root/attachments/some-uuid/ticket2356/8682.patch) by @JohnCremona created at 2008-02-29 22:48:48

Attached patch 8682 fixes both issues:  increases m by 1 and uses a dict() for fast lookup of the table.



---

archive/issue_events_005558.json:
```json
{
    "actor": "https://github.com/JohnCremona",
    "created_at": "2008-03-02T17:35:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2356#event-5558"
}
```



---

archive/issue_comments_015831.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-02T17:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15831",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015832.json:
```json
{
    "body": "Changing assignee from joyner to @JohnCremona.",
    "created_at": "2008-03-02T17:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15832",
    "user": "https://github.com/JohnCremona"
}
```

Changing assignee from joyner to @JohnCremona.



---

archive/issue_comments_015833.json:
```json
{
    "body": "Applied cleanly to 2.10.3.rc0 and passed sage -testall. Also,\n\n```\nsage: F.<w> = GF(121)\nsage: v = w^120\nsage: v.log(w)\n0\n```\nworks as it should. Recommend acceptance.",
    "created_at": "2008-03-02T19:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15833",
    "user": "https://github.com/wdjoyner"
}
```

Applied cleanly to 2.10.3.rc0 and passed sage -testall. Also,

```
sage: F.<w> = GF(121)
sage: v = w^120
sage: v.log(w)
0
```
works as it should. Recommend acceptance.



---

archive/issue_comments_015834.json:
```json
{
    "body": "The two new patches to #2356 -- which have a positive review! -- need to be applied after this one.  They do in fact supercede this one, there therefore this one gets another positive review by default.  I'm sure I am breaking protocol by adding that myself but seriously!",
    "created_at": "2008-03-04T18:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15834",
    "user": "https://github.com/JohnCremona"
}
```

The two new patches to #2356 -- which have a positive review! -- need to be applied after this one.  They do in fact supercede this one, there therefore this one gets another positive review by default.  I'm sure I am breaking protocol by adding that myself but seriously!



---

archive/issue_comments_015835.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> The two new patches to #2356 -- which have a positive review! -- need to be applied after this one.  They do in fact supercede this one, there therefore this one gets another positive review by default.  I'm sure I am breaking protocol by adding that myself but seriously!\n\n\nHi John,\n\nI assume you refer to the two patches at #277 instead of \"The two new patches to #2356 -- which have a positive review!\". The positive review is fine in this case and not a breaking of protocol - we shouldn't and don't enforce rules for the sake of rules :) \n\nI will merge both patches shortly and close the tickets assuming the patches apply.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-04T18:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 cremona]:
> The two new patches to #2356 -- which have a positive review! -- need to be applied after this one.  They do in fact supercede this one, there therefore this one gets another positive review by default.  I'm sure I am breaking protocol by adding that myself but seriously!


Hi John,

I assume you refer to the two patches at #277 instead of "The two new patches to #2356 -- which have a positive review!". The positive review is fine in this case and not a breaking of protocol - we shouldn't and don't enforce rules for the sake of rules :) 

I will merge both patches shortly and close the tickets assuming the patches apply.

Cheers,

Michael



---

archive/issue_events_005559.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-05T00:19:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2356#event-5559"
}
```



---

archive/issue_comments_015836.json:
```json
{
    "body": "Merged both in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T00:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both in Sage 2.10.3.rc2



---

archive/issue_comments_015837.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T00:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015838.json:
```json
{
    "body": "Merged the *only* patch in Sage 2.10.3.rc2 - sorry for the confusion - I meant ticket #277.",
    "created_at": "2008-03-05T00:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2356#issuecomment-15838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged the *only* patch in Sage 2.10.3.rc2 - sorry for the confusion - I meant ticket #277.
