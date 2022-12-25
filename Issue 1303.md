# Issue 1303: Cayley graph class

archive/issues_001303.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: graphs\n\nFrom Chris Godsil's wishlist and Robert Miller's reply:\n\n\n```\n>>> (b) Cayley graphs: These can be dealt with in GAP, but I think it would be\n>>> useful to have a class, with the group and generating set explicit. Cayley\n>>> graphs could be directed or undirected. Circulants and Cayley graphs\n>>> for Zd (where p is prime) could be useful special cases.\n> Cayley graphs are implemented, but most likely not to the extent\n> anyone wants. For example, you can call cayley_graph on some groups,\n> and get the graph back, but the functionality is very limited. There\n> is certainly no CayleyGraph class, which would be a thousand times\n> better than the current situation. Definitely create a ticket for\n> this.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1303\n\n",
    "created_at": "2007-11-28T19:45:42Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Cayley graph class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1303",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

Keywords: graphs

From Chris Godsil's wishlist and Robert Miller's reply:


```
>>> (b) Cayley graphs: These can be dealt with in GAP, but I think it would be
>>> useful to have a class, with the group and generating set explicit. Cayley
>>> graphs could be directed or undirected. Circulants and Cayley graphs
>>> for Zd (where p is prime) could be useful special cases.
> Cayley graphs are implemented, but most likely not to the extent
> anyone wants. For example, you can call cayley_graph on some groups,
> and get the graph back, but the functionality is very limited. There
> is certainly no CayleyGraph class, which would be a thousand times
> better than the current situation. Definitely create a ticket for
> this.
```


Issue created by migration from https://trac.sagemath.org/ticket/1303





---

archive/issue_comments_008171.json:
```json
{
    "body": "Changing assignee from @mwhansen to @rlmill.",
    "created_at": "2007-12-17T15:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1303#issuecomment-8171",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @mwhansen to @rlmill.



---

archive/issue_comments_008172.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"groups\".",
    "created_at": "2007-12-17T15:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1303#issuecomment-8172",
    "user": "https://github.com/rlmill"
}
```

Changing keywords from "graphs" to "groups".



---

archive/issue_comments_008173.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1303#issuecomment-8173",
    "user": "https://github.com/rlmill"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008174.json:
```json
{
    "body": "Closing this ticket as fixed, as suggested by Nathann Cohen and Robert Miller:\n\n```\nHello Minh !!!\n\nThis is a short conversation about ticket #1303 I had with Robert Miller, who concluded this ticket should be closed. As he says, what we need concerning Cayley graph is but the function Group.cayley_graph which already exists.\n\nNathann\n\n---------- Forwarded message ----------\nFrom: Robert Miller <rlm@rlmiller.org>\nDate: 2009/9/2\nSubject: Re: Cayley Graphs in Sage\nTo: Nathann Cohen <nathann.cohen@gmail.com>\n\n\nNathann,\n\nWe should probably get rid of this ticket. The guy who requested it is\nessentially happy with what we already have. Cayley graphs are more of\na way of constructing graphs than an object on their own, i.e. a\n*constructor,* which is what we already have.\n\nOn Sat, Aug 22, 2009 at 9:34 AM, Nathann Cohen<nathann.cohen@gmail.com> wrote:\n> Hello !!!\n>\n> I am contacting you about the following ticket :\n> http://trac.sagemath.org/sage_trac/ticket/1303\n>\n> You are writing about the creation of a Cayley Graph class, and it is a\n> subject that interests me, even though I do not understand what you expect\n> of it.... For me a Cayley Graph is just a group, so could you tell me with\n> some details what you would expect for such a class ? I would like to spend\n> some time on this :-)\n>\n> Thank you !\n>\n> Nathann\n```\n",
    "created_at": "2009-09-13T10:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1303#issuecomment-8174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this ticket as fixed, as suggested by Nathann Cohen and Robert Miller:

```
Hello Minh !!!

This is a short conversation about ticket #1303 I had with Robert Miller, who concluded this ticket should be closed. As he says, what we need concerning Cayley graph is but the function Group.cayley_graph which already exists.

Nathann

---------- Forwarded message ----------
From: Robert Miller <rlm@rlmiller.org>
Date: 2009/9/2
Subject: Re: Cayley Graphs in Sage
To: Nathann Cohen <nathann.cohen@gmail.com>


Nathann,

We should probably get rid of this ticket. The guy who requested it is
essentially happy with what we already have. Cayley graphs are more of
a way of constructing graphs than an object on their own, i.e. a
*constructor,* which is what we already have.

On Sat, Aug 22, 2009 at 9:34 AM, Nathann Cohen<nathann.cohen@gmail.com> wrote:
> Hello !!!
>
> I am contacting you about the following ticket :
> http://trac.sagemath.org/sage_trac/ticket/1303
>
> You are writing about the creation of a Cayley Graph class, and it is a
> subject that interests me, even though I do not understand what you expect
> of it.... For me a Cayley Graph is just a group, so could you tell me with
> some details what you would expect for such a class ? I would like to spend
> some time on this :-)
>
> Thank you !
>
> Nathann
```




---

archive/issue_comments_008175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-13T10:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1303#issuecomment-8175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
