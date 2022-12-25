# Issue 7380: Replace Graph.vertices() by Graph.vertex_iterator when possible

archive/issues_007380.json:
```json
{
    "body": "Assignee: @rlmill\n\nAs the title says, there are many places where Graph.vertices() is used when Graph.vertex_iterator ( or even self ) would be better. The same goes for edges.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7380\n\n",
    "created_at": "2009-11-03T11:25:56Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Replace Graph.vertices() by Graph.vertex_iterator when possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7380",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

As the title says, there are many places where Graph.vertices() is used when Graph.vertex_iterator ( or even self ) would be better. The same goes for edges.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7380





---

archive/issue_comments_061964.json:
```json
{
    "body": "Useless.",
    "created_at": "2010-02-28T18:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61964",
    "user": "https://github.com/nathanncohen"
}
```

Useless.



---

archive/issue_comments_061965.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-28T18:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61965",
    "user": "https://github.com/nathanncohen"
}
```

Resolution: wontfix



---

archive/issue_comments_061966.json:
```json
{
    "body": "Read [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) before closing tickets. Can you explain why you want to close this ticket?",
    "created_at": "2010-02-28T20:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Read [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) before closing tickets. Can you explain why you want to close this ticket?



---

archive/issue_comments_061967.json:
```json
{
    "body": "Well, as I created it I thought it would not be so bad to close it too ^^;\n\nThe thing is that I do not feel anymore that this should be done, or just useful in any way. It would just slow down most functions as creating an iterator has no real sense when the whole set is already stored in memory, and it would make the code harder to read for no real purpose :p\n\nNathann",
    "created_at": "2010-02-28T20:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61967",
    "user": "https://github.com/nathanncohen"
}
```

Well, as I created it I thought it would not be so bad to close it too ^^;

The thing is that I do not feel anymore that this should be done, or just useful in any way. It would just slow down most functions as creating an iterator has no real sense when the whole set is already stored in memory, and it would make the code harder to read for no real purpose :p

Nathann



---

archive/issue_comments_061968.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Well, as I created it I thought it would not be so bad to close it too ^^;\n\nAs long as you provide a good reason to close the ticket. Don't just close a ticket without any good reasons.",
    "created_at": "2010-02-28T21:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61968",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 ncohen]:
> Well, as I created it I thought it would not be so bad to close it too ^^;

As long as you provide a good reason to close the ticket. Don't just close a ticket without any good reasons.



---

archive/issue_comments_061969.json:
```json
{
    "body": "Sorry for commenting a closed ticket, but...\n\nIf I look at the docstring for `vertices` I see (in the default case):\n\n```\nreturn sorted(list(self.vertex_iterator()))\n```\n\n\nA new list is created, doubling the memory needed, and this list is sorted which might take time too.\n\nI still think it might make sense to replace `vertices` with `vertex_iterator` when possible.",
    "created_at": "2010-03-01T06:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61969",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Sorry for commenting a closed ticket, but...

If I look at the docstring for `vertices` I see (in the default case):

```
return sorted(list(self.vertex_iterator()))
```


A new list is created, doubling the memory needed, and this list is sorted which might take time too.

I still think it might make sense to replace `vertices` with `vertex_iterator` when possible.



---

archive/issue_comments_061970.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-03-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61970",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from closed to new.



---

archive/issue_comments_061971.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-03-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61971",
    "user": "https://github.com/nathanncohen"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_061972.json:
```json
{
    "body": "oops... Well, if \"vertices()\" is calling vertex_iterator, plus sorts it, then I said nothing...",
    "created_at": "2010-03-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61972",
    "user": "https://github.com/nathanncohen"
}
```

oops... Well, if "vertices()" is calling vertex_iterator, plus sorts it, then I said nothing...



---

archive/issue_comments_061973.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> oops... Well, if \"vertices()\" is calling vertex_iterator, plus sorts it, then I said nothing...\n**Do not** reopen this ticket. Let it die and open a new ticket.",
    "created_at": "2010-03-01T10:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:6 ncohen]:
> oops... Well, if "vertices()" is calling vertex_iterator, plus sorts it, then I said nothing...
**Do not** reopen this ticket. Let it die and open a new ticket.



---

archive/issue_comments_061974.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-03-01T10:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-61974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: worksforme
