# Issue 7709: Graph constructor : Graph(edges=[ ... ] )

archive/issues_007709.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nthiery @rlmill\n\nI often need to create graphs defined by a set of edges, and it should not be hard to add a new constructor of this shape :\n\n```\ng = Graph(edges=[ ... ] )\n```\n\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7709\n\n",
    "created_at": "2009-12-16T11:55:26Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Graph constructor : Graph(edges=[ ... ] )",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7709",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  @nthiery @rlmill

I often need to create graphs defined by a set of edges, and it should not be hard to add a new constructor of this shape :

```
g = Graph(edges=[ ... ] )
```


Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7709





---

archive/issue_comments_066050.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66050",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_066051.json:
```json
{
    "body": "Here is a patch to update graph.py. I have been sitting a while, trying to find a efficient way to write this, and found none, so I ended up converting it all to a dict_of_lists of dict_of_dicts... As it took some time to write, I would gladly ask for your advice before rewriting it all for digraphs.py (if you agree). Otherwise, let's try to find a better solution together :-)\n\nNathann",
    "created_at": "2010-08-02T11:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66051",
    "user": "https://github.com/nathanncohen"
}
```

Here is a patch to update graph.py. I have been sitting a while, trying to find a efficient way to write this, and found none, so I ended up converting it all to a dict_of_lists of dict_of_dicts... As it took some time to write, I would gladly ask for your advice before rewriting it all for digraphs.py (if you agree). Otherwise, let's try to find a better solution together :-)

Nathann



---

archive/issue_comments_066052.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-08-02T11:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66052",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_066053.json:
```json
{
    "body": "Oh, by the way... This is no a new feature, as it was already possible to create a Graph by giving as an argument a list of edges, but until now it was forwarded to NetworkX..\n\nNathann",
    "created_at": "2010-08-02T11:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66053",
    "user": "https://github.com/nathanncohen"
}
```

Oh, by the way... This is no a new feature, as it was already possible to create a Graph by giving as an argument a list of edges, but until now it was forwarded to NetworkX..

Nathann



---

archive/issue_comments_066054.json:
```json
{
    "body": "I think `data.setdefault(u, [])` instead of `if not u in data: data[u] = []` could make it a litte bit faster  ;-)",
    "created_at": "2010-08-02T12:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66054",
    "user": "https://github.com/haraldschilly"
}
```

I think `data.setdefault(u, [])` instead of `if not u in data: data[u] = []` could make it a litte bit faster  ;-)



---

archive/issue_comments_066055.json:
```json
{
    "body": "Actually, I wondered... Faster to write, of course, but do you think it is also more efficient ? I had no idea, so I stuck to the most basic tools :-)\n\nNathann",
    "created_at": "2010-08-02T14:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66055",
    "user": "https://github.com/nathanncohen"
}
```

Actually, I wondered... Faster to write, of course, but do you think it is also more efficient ? I had no idea, so I stuck to the most basic tools :-)

Nathann



---

archive/issue_comments_066056.json:
```json
{
    "body": "sorry, forget my comment, data.setdefault(...[]).append(u) is slower than your solution.",
    "created_at": "2010-08-02T16:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66056",
    "user": "https://github.com/haraldschilly"
}
```

sorry, forget my comment, data.setdefault(...[]).append(u) is slower than your solution.



---

archive/issue_comments_066057.json:
```json
{
    "body": "I would change the ValueError message to something much shorter and more comprehensive, such as \"Edges input must all be of the same format\" or length or something...",
    "created_at": "2010-08-04T01:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66057",
    "user": "https://github.com/rlmill"
}
```

I would change the ValueError message to something much shorter and more comprehensive, such as "Edges input must all be of the same format" or length or something...



---

archive/issue_comments_066058.json:
```json
{
    "body": "Replying to [comment:9 rlm]:\n> I would change the ValueError message to something much shorter and more comprehensive, such as \"Edges input must all be of the same format\" or length or something...\n\nAlso, the doctests don't expose this error.",
    "created_at": "2010-08-04T01:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66058",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:9 rlm]:
> I would change the ValueError message to something much shorter and more comprehensive, such as "Edges input must all be of the same format" or length or something...

Also, the doctests don't expose this error.



---

archive/issue_comments_066059.json:
```json
{
    "body": "I just updated the ticket to fix it ! Do you think this method is acceptable and I can now do the same for DiGraphs ?\n\nNathann",
    "created_at": "2010-08-04T03:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66059",
    "user": "https://github.com/nathanncohen"
}
```

I just updated the ticket to fix it ! Do you think this method is acceptable and I can now do the same for DiGraphs ?

Nathann



---

archive/issue_comments_066060.json:
```json
{
    "body": "Replying to [comment:11 ncohen]:\n> I just updated the ticket to fix it ! Do you think this method is acceptable and I can now do the same for DiGraphs ?\n\nNathann,\n\nThis looks good (maybe in the multiedges=False test you can show the list of edges afterward to demonstrate what actually happens). Please implement this in the DiGraph case as well!",
    "created_at": "2010-08-06T14:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66060",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:11 ncohen]:
> I just updated the ticket to fix it ! Do you think this method is acceptable and I can now do the same for DiGraphs ?

Nathann,

This looks good (maybe in the multiedges=False test you can show the list of edges afterward to demonstrate what actually happens). Please implement this in the DiGraph case as well!



---

archive/issue_comments_066061.json:
```json
{
    "body": "Here it is ! Actually, the constructor raises an exception when the same edge receives different labels with multiedges = False. I had forgotten to fill the doctests, as it was just a preview !`:-)`\n\nNathann",
    "created_at": "2010-08-08T11:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66061",
    "user": "https://github.com/nathanncohen"
}
```

Here it is ! Actually, the constructor raises an exception when the same edge receives different labels with multiedges = False. I had forgotten to fill the doctests, as it was just a preview !`:-)`

Nathann



---

archive/issue_comments_066062.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-08T11:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66062",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066063.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-10T13:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66063",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066064.json:
```json
{
    "body": "Attachment [trac_7709.patch](tarball://root/attachments/some-uuid/ticket7709/trac_7709.patch) by @rlmill created at 2010-11-10 13:53:54",
    "created_at": "2010-11-10T13:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66064",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7709.patch](tarball://root/attachments/some-uuid/ticket7709/trac_7709.patch) by @rlmill created at 2010-11-10 13:53:54



---

archive/issue_comments_066065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T13:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7709#issuecomment-66065",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_007926.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-11T13:01:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7709",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7709#event-7926"
}
```
