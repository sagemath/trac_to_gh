# Issue 7380: Replace Graph.vertices() by Graph.vertex_iterator when possible

archive/issues_007380.json:
```json
{
    "body": "Assignee: rlm\n\nAs the title says, there are many places where Graph.vertices() is used when Graph.vertex_iterator ( or even self ) would be better. The same goes for edges.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7380\n\n",
    "created_at": "2009-11-03T11:25:56Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Replace Graph.vertices() by Graph.vertex_iterator when possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7380",
    "user": "ncohen"
}
```
Assignee: rlm

As the title says, there are many places where Graph.vertices() is used when Graph.vertex_iterator ( or even self ) would be better. The same goes for edges.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7380





---

archive/issue_comments_062079.json:
```json
{
    "body": "Useless.",
    "created_at": "2010-02-28T18:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62079",
    "user": "ncohen"
}
```

Useless.



---

archive/issue_comments_062080.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-28T18:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62080",
    "user": "ncohen"
}
```

Resolution: wontfix



---

archive/issue_comments_062081.json:
```json
{
    "body": "Read [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) before closing tickets. Can you explain why you want to close this ticket?",
    "created_at": "2010-02-28T20:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62081",
    "user": "mvngu"
}
```

Read [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) before closing tickets. Can you explain why you want to close this ticket?



---

archive/issue_comments_062082.json:
```json
{
    "body": "Well, as I created it I thought it would not be so bad to close it too ^^;\n\nThe thing is that I do not feel anymore that this should be done, or just useful in any way. It would just slow down most functions as creating an iterator has no real sense when the whole set is already stored in memory, and it would make the code harder to read for no real purpose :p\n\nNathann",
    "created_at": "2010-02-28T20:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62082",
    "user": "ncohen"
}
```

Well, as I created it I thought it would not be so bad to close it too ^^;

The thing is that I do not feel anymore that this should be done, or just useful in any way. It would just slow down most functions as creating an iterator has no real sense when the whole set is already stored in memory, and it would make the code harder to read for no real purpose :p

Nathann



---

archive/issue_comments_062083.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Well, as I created it I thought it would not be so bad to close it too ^^;\n\nAs long as you provide a good reason to close the ticket. Don't just close a ticket without any good reasons.",
    "created_at": "2010-02-28T21:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62083",
    "user": "mvngu"
}
```

Replying to [comment:3 ncohen]:
> Well, as I created it I thought it would not be so bad to close it too ^^;

As long as you provide a good reason to close the ticket. Don't just close a ticket without any good reasons.



---

archive/issue_comments_062084.json:
```json
{
    "body": "Sorry for commenting a closed ticket, but...\n\nIf I look at the docstring for `vertices` I see (in the default case):\n\n```\nreturn sorted(list(self.vertex_iterator()))\n```\n\n\nA new list is created, doubling the memory needed, and this list is sorted which might take time too.\n\nI still think it might make sense to replace `vertices` with `vertex_iterator` when possible.",
    "created_at": "2010-03-01T06:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62084",
    "user": "ylchapuy"
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

archive/issue_comments_062085.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-03-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62085",
    "user": "ncohen"
}
```

Changing status from closed to new.



---

archive/issue_comments_062086.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-03-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62086",
    "user": "ncohen"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_062087.json:
```json
{
    "body": "oops... Well, if \"vertices()\" is calling vertex_iterator, plus sorts it, then I said nothing...",
    "created_at": "2010-03-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62087",
    "user": "ncohen"
}
```

oops... Well, if "vertices()" is calling vertex_iterator, plus sorts it, then I said nothing...



---

archive/issue_comments_062088.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> oops... Well, if \"vertices()\" is calling vertex_iterator, plus sorts it, then I said nothing...\n**Do not** reopen this ticket. Let it die and open a new ticket.",
    "created_at": "2010-03-01T10:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62088",
    "user": "mvngu"
}
```

Replying to [comment:6 ncohen]:
> oops... Well, if "vertices()" is calling vertex_iterator, plus sorts it, then I said nothing...
**Do not** reopen this ticket. Let it die and open a new ticket.



---

archive/issue_comments_062089.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-03-01T10:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7380#issuecomment-62089",
    "user": "mvngu"
}
```

Resolution: worksforme
