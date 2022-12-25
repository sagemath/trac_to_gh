# Issue 2300: A copy method for SingularElement [with patch, needs review]

archive/issues_002300.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nCC:  malb@informatik.uni-bremen.de\n\nKeywords: copy SingularElement\n\nSo far, there was no method for copying a `SingularElement`. Calling `copy` on a `SingularElement` resulted in an `(invalid object -- defined in terms of closed session)`.\n\nThe patch provides a `__copy__` method. In fact, this is quite easy: For most objects `S` of type `SingularElement`, it suffices to return `singular(S.name())`. One has to make an exception when `S` is a ring, because `singular(S.name)())` would just yield another name for *the same* ring. Therefore, `(S.ringlist()).ring()` is used for duplication of a ring. Examples:\n\n\n```\nsage: R=singular.ring(0,'(x,y)','dp')\nsage: M=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')\nsage: N=copy(M)\nsage: N[1,1]=singular('x+y')\nsage: N\nx+y,0,-x,\n0,  y,0,\nx*y,0,0\nsage: M\n0,  0,-x,\n0,  y,0,\nx*y,0,0\n```\n\nHence, N really is a copy of M. Changing N does not affect M\n\n```\nsage: S=copy(R)\nsage: S.set_ring()\nsage: S\n//   characteristic : 0\n//   number of vars : 2\n//        block   1 : ordering dp\n//                  : names    x y\n//        block   2 : ordering C\nsage: R.fetch(M)\n0,  0,-x,\n0,  y,0,\nx*y,0,0\nsage: M\n`sage1`\n```\n\nNote that in the last example, `M` is unknown after making `S` active. So, `S` is a copy of `R`, but not identical to `R`.\nDefining `S=singular(R.name())` would be a mistake: The matrix `M` would be known in `S`, and any change to `M` when `S` is active would persist after returning to `R`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2300\n\n",
    "created_at": "2008-02-25T09:57:08Z",
    "labels": [
        "component: commutative algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "A copy method for SingularElement [with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2300",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @simon-king-jena

CC:  malb@informatik.uni-bremen.de

Keywords: copy SingularElement

So far, there was no method for copying a `SingularElement`. Calling `copy` on a `SingularElement` resulted in an `(invalid object -- defined in terms of closed session)`.

The patch provides a `__copy__` method. In fact, this is quite easy: For most objects `S` of type `SingularElement`, it suffices to return `singular(S.name())`. One has to make an exception when `S` is a ring, because `singular(S.name)())` would just yield another name for *the same* ring. Therefore, `(S.ringlist()).ring()` is used for duplication of a ring. Examples:


```
sage: R=singular.ring(0,'(x,y)','dp')
sage: M=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')
sage: N=copy(M)
sage: N[1,1]=singular('x+y')
sage: N
x+y,0,-x,
0,  y,0,
x*y,0,0
sage: M
0,  0,-x,
0,  y,0,
x*y,0,0
```

Hence, N really is a copy of M. Changing N does not affect M

```
sage: S=copy(R)
sage: S.set_ring()
sage: S
//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
sage: R.fetch(M)
0,  0,-x,
0,  y,0,
x*y,0,0
sage: M
`sage1`
```

Note that in the last example, `M` is unknown after making `S` active. So, `S` is a copy of `R`, but not identical to `R`.
Defining `S=singular(R.name())` would be a mistake: The matrix `M` would be known in `S`, and any change to `M` when `S` is active would persist after returning to `R`.

Issue created by migration from https://trac.sagemath.org/ticket/2300





---

archive/issue_comments_015230.json:
```json
{
    "body": "Remark: The exception must be done both for `SingularElement` of type `ring` and of type `qring`. Done in the new patch.",
    "created_at": "2008-02-25T10:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15230",
    "user": "https://github.com/simon-king-jena"
}
```

Remark: The exception must be done both for `SingularElement` of type `ring` and of type `qring`. Done in the new patch.



---

archive/issue_comments_015231.json:
```json
{
    "body": "I observed that the words [with patch, needs review] are usually prepended and not appended to the ticket's summary.",
    "created_at": "2008-02-25T12:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15231",
    "user": "https://github.com/simon-king-jena"
}
```

I observed that the words [with patch, needs review] are usually prepended and not appended to the ticket's summary.



---

archive/issue_comments_015232.json:
```json
{
    "body": "**Referee Report**\n* `singular(self.name())` should be `self.parent()(self.name())` such that it also works if one uses a non standard instance of the Singular interface\n* I think the examples should be shifted four spaces too the right, e.g.:\n\n```\nEXAMPLE:\n    sage: foo\n    bar\n```\n",
    "created_at": "2008-02-26T11:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15232",
    "user": "https://github.com/malb"
}
```

**Referee Report**
* `singular(self.name())` should be `self.parent()(self.name())` such that it also works if one uses a non standard instance of the Singular interface
* I think the examples should be shifted four spaces too the right, e.g.:

```
EXAMPLE:
    sage: foo
    bar
```




---

archive/issue_comments_015233.json:
```json
{
    "body": "Attachment [SingularElementCopy.patch](tarball://root/attachments/some-uuid/ticket2300/SingularElementCopy.patch) by @simon-king-jena created at 2008-02-26 23:29:10\n\nSorry for being late, and sorry for accidentally adding the same patch twice.\n\nI changed the patch according to the referee report, hence, the examples are indented, and it is `self.parent()(self.name())`. \n\nThe patch is relative to sage-2.10.3.alpha0",
    "created_at": "2008-02-26T23:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15233",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [SingularElementCopy.patch](tarball://root/attachments/some-uuid/ticket2300/SingularElementCopy.patch) by @simon-king-jena created at 2008-02-26 23:29:10

Sorry for being late, and sorry for accidentally adding the same patch twice.

I changed the patch according to the referee report, hence, the examples are indented, and it is `self.parent()(self.name())`. 

The patch is relative to sage-2.10.3.alpha0



---

archive/issue_comments_015234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T03:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002475.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-27T03:29:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2300#event-2475"
}
```



---

archive/issue_comments_015235.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T03:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_015236.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-02-28T12:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15236",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002476.json:
```json
{
    "actor": "@simon-king-jena",
    "created_at": "2008-02-28T12:01:17Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2300#event-2476"
}
```



---

archive/issue_comments_015237.json:
```json
{
    "body": "Attachment [bugfix__copy__.patch](tarball://root/attachments/some-uuid/ticket2300/bugfix__copy__.patch) by @simon-king-jena created at 2008-02-28 12:01:17\n\nSorry, i have to re-open the ticket because i found a bug in my patch:\n\n\n```\nsage: R=singular.ring(0,'(x,y)','dp')\nsage: L=R.ringlist()\nsage: L[4]=singular.ideal('x**2-5')\nsage: Q=L.ring()\nsage: otherR=singular.ring(5,'(x)','dp')\nsage: cpQ=copy(Q)\n<snip>\n<type 'exceptions.TypeError'>: Singular error:\n   ? ring with polynomial data must be the base ring or compatible\n   ? error occurred in STDIN line 36: `def sage12=ringlist(sage10);`\n```\n\n\nThe problem is that `ringlist` contains polynomial data, and thus only works if the basering fits.\n\nSolution: If `self` is a ring/qring then we first make it active `basering`, copy `self` using `ringlist`, return to the old `basering`, and return the copy of `self`.\n\nI extended the doc tests accordingly. The new doc test would fail with the old version of `__copy__`.\n\nThe patch `bugfix__copy__.patch` is relative to `sage-2.10.3.rc0`.",
    "created_at": "2008-02-28T12:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15237",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [bugfix__copy__.patch](tarball://root/attachments/some-uuid/ticket2300/bugfix__copy__.patch) by @simon-king-jena created at 2008-02-28 12:01:17

Sorry, i have to re-open the ticket because i found a bug in my patch:


```
sage: R=singular.ring(0,'(x,y)','dp')
sage: L=R.ringlist()
sage: L[4]=singular.ideal('x**2-5')
sage: Q=L.ring()
sage: otherR=singular.ring(5,'(x)','dp')
sage: cpQ=copy(Q)
<snip>
<type 'exceptions.TypeError'>: Singular error:
   ? ring with polynomial data must be the base ring or compatible
   ? error occurred in STDIN line 36: `def sage12=ringlist(sage10);`
```


The problem is that `ringlist` contains polynomial data, and thus only works if the basering fits.

Solution: If `self` is a ring/qring then we first make it active `basering`, copy `self` using `ringlist`, return to the old `basering`, and return the copy of `self`.

I extended the doc tests accordingly. The new doc test would fail with the old version of `__copy__`.

The patch `bugfix__copy__.patch` is relative to `sage-2.10.3.rc0`.



---

archive/issue_comments_015238.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-02-28T12:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15238",
    "user": "https://github.com/simon-king-jena"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_015239.json:
```json
{
    "body": "Because the patches attached to this ticket were already merged, I guess it would be best to open a new ticket for the bugfixes attached after the merge.",
    "created_at": "2008-03-03T15:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15239",
    "user": "https://github.com/malb"
}
```

Because the patches attached to this ticket were already merged, I guess it would be best to open a new ticket for the bugfixes attached after the merge.



---

archive/issue_comments_015240.json:
```json
{
    "body": "The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.",
    "created_at": "2008-03-03T15:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15240",
    "user": "https://github.com/malb"
}
```

The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.



---

archive/issue_comments_015241.json:
```json
{
    "body": "Replying to [comment:9 malb]:\n> The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.\n\nOK, it is #2377.\n\nSorry, i thought when a bug is found in a patch then it is still the same ticket.",
    "created_at": "2008-03-03T17:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15241",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:9 malb]:
> The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.

OK, it is #2377.

Sorry, i thought when a bug is found in a patch then it is still the same ticket.



---

archive/issue_comments_015242.json:
```json
{
    "body": "Replying to [comment:10 SimonKing]:\n> Replying to [comment:9 malb]:\n> > The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.\n> \n> OK, it is #2377.\n> \n> Sorry, i thought when a bug is found in a patch then it is still the same ticket.\n\nSome times it is, some times it isn't, but generally you should open a new ticket if a bugfix is found post merge when an rc or alpha has been released.\n\nI will also quote malb on the new ticket with his positive review and merge the patch then.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T17:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:10 SimonKing]:
> Replying to [comment:9 malb]:
> > The code looks good, I don't know a better Singular solution. I'm happy to give the bugfix a 'positive review' once it is attached to a new ticket.
> 
> OK, it is #2377.
> 
> Sorry, i thought when a bug is found in a patch then it is still the same ticket.

Some times it is, some times it isn't, but generally you should open a new ticket if a bugfix is found post merge when an rc or alpha has been released.

I will also quote malb on the new ticket with his positive review and merge the patch then.

Cheers,

Michael



---

archive/issue_comments_015243.json:
```json
{
    "body": "I hope i am allowed to close the ticket, since it is resolved in #2377",
    "created_at": "2008-03-04T12:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15243",
    "user": "https://github.com/simon-king-jena"
}
```

I hope i am allowed to close the ticket, since it is resolved in #2377



---

archive/issue_comments_015244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-04T12:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15244",
    "user": "https://github.com/simon-king-jena"
}
```

Resolution: fixed



---

archive/issue_events_002477.json:
```json
{
    "actor": "@simon-king-jena",
    "created_at": "2008-03-04T12:11:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2300#event-2477"
}
```



---

archive/issue_comments_015245.json:
```json
{
    "body": "Replying to [comment:12 SimonKing]:\n> I hope i am allowed to close the ticket, since it is resolved in #2377\n\nYeah, sorry that I didn't close this. I was an oversight on my end and it was clear that it must be closed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-04T16:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2300#issuecomment-15245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:12 SimonKing]:
> I hope i am allowed to close the ticket, since it is resolved in #2377

Yeah, sorry that I didn't close this. I was an oversight on my end and it was clear that it must be closed.

Cheers,

Michael
