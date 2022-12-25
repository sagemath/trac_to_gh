# Issue 3534: plot -- fix circle example in the documentation

archive/issues_003534.json:
```json
{
    "body": "Assignee: tba\n\n```\n\n> The first example here:\n> http://www.sagemath.org/doc/html/tut/node21.html\n> .. shows creating a circle plot via:\n> L = [[cos(pi*i/100),sin(pi*i/100)] for i in range(200)]\n> p = polygon(L, rgbcolor=(1,1,0))\n> p.save()          ## or   p.show()\n>\n> When I try this, I get an ellipse!  Or more precisely, the plot has\n> unequal axis scaling.\n>\n> Here's a picture:\n> http://backspaces.net/temp/Safari116.png\n\nUse this instead:\n\nL = [[cos(pi*i/100),sin(pi*i/100)] for i in range(200)]\np = polygon(L, rgbcolor=(1,1,0))\np.save(aspect_ratio=1)          ## or   p.show()\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3534\n\n",
    "created_at": "2008-06-30T00:37:59Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "plot -- fix circle example in the documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3534",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

```

> The first example here:
> http://www.sagemath.org/doc/html/tut/node21.html
> .. shows creating a circle plot via:
> L = [[cos(pi*i/100),sin(pi*i/100)] for i in range(200)]
> p = polygon(L, rgbcolor=(1,1,0))
> p.save()          ## or   p.show()
>
> When I try this, I get an ellipse!  Or more precisely, the plot has
> unequal axis scaling.
>
> Here's a picture:
> http://backspaces.net/temp/Safari116.png

Use this instead:

L = [[cos(pi*i/100),sin(pi*i/100)] for i in range(200)]
p = polygon(L, rgbcolor=(1,1,0))
p.save(aspect_ratio=1)          ## or   p.show()

```

Issue created by migration from https://trac.sagemath.org/ticket/3534





---

archive/issue_comments_024895.json:
```json
{
    "body": "The attached patch fixes the above issue.  It also greatly improves all the examples to simply\nshow the plots instead of having hacking notes outside the examples to show the plots, which was\ndone before when the doctesting framework couldn't handle plotting.",
    "created_at": "2008-06-30T00:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24895",
    "user": "https://github.com/williamstein"
}
```

The attached patch fixes the above issue.  It also greatly improves all the examples to simply
show the plots instead of having hacking notes outside the examples to show the plots, which was
done before when the doctesting framework couldn't handle plotting.



---

archive/issue_comments_024896.json:
```json
{
    "body": "Attachment [doc-3534.patch](tarball://root/attachments/some-uuid/ticket3534/doc-3534.patch) by @jhpalmieri created at 2008-06-30 02:07:01\n\nIt would be better to patch against the new version of the tutorial (the one in 3.0.4.alpha1): see\n[http://trac.sagemath.org/sage_trac/ticket/3347](http://trac.sagemath.org/sage_trac/ticket/3347).",
    "created_at": "2008-06-30T02:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24896",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [doc-3534.patch](tarball://root/attachments/some-uuid/ticket3534/doc-3534.patch) by @jhpalmieri created at 2008-06-30 02:07:01

It would be better to patch against the new version of the tutorial (the one in 3.0.4.alpha1): see
[http://trac.sagemath.org/sage_trac/ticket/3347](http://trac.sagemath.org/sage_trac/ticket/3347).



---

archive/issue_comments_024897.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-07-02T21:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24897",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_024898.json:
```json
{
    "body": "I'll be an editor for this since I did #3347.",
    "created_at": "2008-07-02T21:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24898",
    "user": "https://github.com/mwhansen"
}
```

I'll be an editor for this since I did #3347.



---

archive/issue_comments_024899.json:
```json
{
    "body": "Attachment [3534-new.patch](tarball://root/attachments/some-uuid/ticket3534/3534-new.patch) by @jhpalmieri created at 2008-07-15 18:49:50\n\nHere's a new patch, based on William's but done against the new version of the tutorial.  (This means that the details are different, but I've tried to preserve the ideas behind his changes.)",
    "created_at": "2008-07-15T18:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24899",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3534-new.patch](tarball://root/attachments/some-uuid/ticket3534/3534-new.patch) by @jhpalmieri created at 2008-07-15 18:49:50

Here's a new patch, based on William's but done against the new version of the tutorial.  (This means that the details are different, but I've tried to preserve the ideas behind his changes.)



---

archive/issue_comments_024900.json:
```json
{
    "body": "Looks good to me.  I'll make these changes in the ReST version too.",
    "created_at": "2008-09-16T02:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24900",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  I'll make these changes in the ReST version too.



---

archive/issue_events_008066.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-16T03:53:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3534#event-8066"
}
```



---

archive/issue_events_008067.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-16T03:53:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3534#event-8067"
}
```



---

archive/issue_comments_024901.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-16T03:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24901",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024902.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc5",
    "created_at": "2008-09-16T03:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3534#issuecomment-24902",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc5
