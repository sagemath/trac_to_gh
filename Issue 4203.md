# Issue 4203: Make a suboption decorator to complement #4201

archive/issues_004203.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  anakha\n\n\n```\n[17:06] <mhansen> Yeah -- suboption should take a prefix, defaults, and then return something like an arrow_options dict.\n[17:07] <mhansen> @suboption('arrow', color='red', line='+')\n[17:07] <jason-> okay, yeah, even better.\n[17:07] <mhansen> And that would pick up things like arrow_color='blue'.\n[17:07] <jason-> then I don't have to type the dictionary explicitly\n[17:09] <mhansen> I think doing something like that might be a good idea.  It'd at least be a nice consistent way to handle all of these options.\n```\n\n\nThe idea is that we'd like to get a bunch of options to pass on to, say, an arrow_drawing routine.  It'd be really nice if we could rename the suboptions too, so the original arrow_color argument could be returned as the rgbcolor element of the arrow_options dict.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4203\n\n",
    "created_at": "2008-09-26T22:45:34Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Make a suboption decorator to complement #4201",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4203",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

CC:  anakha


```
[17:06] <mhansen> Yeah -- suboption should take a prefix, defaults, and then return something like an arrow_options dict.
[17:07] <mhansen> @suboption('arrow', color='red', line='+')
[17:07] <jason-> okay, yeah, even better.
[17:07] <mhansen> And that would pick up things like arrow_color='blue'.
[17:07] <jason-> then I don't have to type the dictionary explicitly
[17:09] <mhansen> I think doing something like that might be a good idea.  It'd at least be a nice consistent way to handle all of these options.
```


The idea is that we'd like to get a bunch of options to pass on to, say, an arrow_drawing routine.  It'd be really nice if we could rename the suboptions too, so the original arrow_color argument could be returned as the rgbcolor element of the arrow_options dict.


Issue created by migration from https://trac.sagemath.org/ticket/4203





---

archive/issue_comments_030440.json:
```json
{
    "body": "Use case:\n\n\n```\n@suboption('arrow', color='red', line_style='+')\n@options(vertices=True, edge_labels=True)\ndef plot_graph():\n    draw vertices\n    for each edge:\n        draw_arrow(**arrow_options)\n    draw edge labels\n```\n\nso the plot_graph function has options arrow_color and arrow_line_style, but inside the function, it just sees an arrow_options dictionary populated from these.",
    "created_at": "2008-09-26T22:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30440",
    "user": "https://github.com/jasongrout"
}
```

Use case:


```
@suboption('arrow', color='red', line_style='+')
@options(vertices=True, edge_labels=True)
def plot_graph():
    draw vertices
    for each edge:
        draw_arrow(**arrow_options)
    draw edge labels
```

so the plot_graph function has options arrow_color and arrow_line_style, but inside the function, it just sees an arrow_options dictionary populated from these.



---

archive/issue_comments_030441.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-23T16:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30441",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030442.json:
```json
{
    "body": "I put up an initial implementation of this.",
    "created_at": "2008-10-23T16:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30442",
    "user": "https://github.com/mwhansen"
}
```

I put up an initial implementation of this.



---

archive/issue_comments_030443.json:
```json
{
    "body": "Very nice.  Positive review.\n\nEventually, we ought to present a nice documentation interface to the user of the combined effect of the suboptions, the options and the rename_keyword decorators.  In other words, some automated way of getting exactly everything that a person can do to a function.  But that should be another trac ticket. \n\nAll doctests in plot/*.py pass with this patch.",
    "created_at": "2008-10-23T17:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30443",
    "user": "https://github.com/jasongrout"
}
```

Very nice.  Positive review.

Eventually, we ought to present a nice documentation interface to the user of the combined effect of the suboptions, the options and the rename_keyword decorators.  In other words, some automated way of getting exactly everything that a person can do to a function.  But that should be another trac ticket. 

All doctests in plot/*.py pass with this patch.



---

archive/issue_comments_030444.json:
```json
{
    "body": "I got this with a quick test.\n\n\n```\nsage: @suboptions('test')\ndef f(**kwds):\n....:     print kwds\n....:     \nsage: f(test_size=2)\n{'test_options': {'ize': 2}}\n```\n\n\nstr.lstrip removes all characters given from the front of the string:\n\n\n```\nsage: 'baba_baca'.lstrip('ab_')\n'ca'\n```\n",
    "created_at": "2008-10-23T19:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30444",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

I got this with a quick test.


```
sage: @suboptions('test')
def f(**kwds):
....:     print kwds
....:     
sage: f(test_size=2)
{'test_options': {'ize': 2}}
```


str.lstrip removes all characters given from the front of the string:


```
sage: 'baba_baca'.lstrip('ab_')
'ca'
```




---

archive/issue_comments_030445.json:
```json
{
    "body": "Attachment [trac_4203.patch](tarball://root/attachments/some-uuid/ticket4203/trac_4203.patch) by @mwhansen created at 2008-10-23 20:21:05\n\nI put up a new patch which addresses that issue.",
    "created_at": "2008-10-23T20:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30445",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4203.patch](tarball://root/attachments/some-uuid/ticket4203/trac_4203.patch) by @mwhansen created at 2008-10-23 20:21:05

I put up a new patch which addresses that issue.



---

archive/issue_comments_030446.json:
```json
{
    "body": "Very nice.  It's all good now.",
    "created_at": "2008-10-23T21:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30446",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Very nice.  It's all good now.



---

archive/issue_comments_030447.json:
```json
{
    "body": "I guess my one last comment is to compute len(self.name) outside of the inner loop, but if it doesn't get changed, I'm not going to cry.",
    "created_at": "2008-10-23T23:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30447",
    "user": "https://github.com/jasongrout"
}
```

I guess my one last comment is to compute len(self.name) outside of the inner loop, but if it doesn't get changed, I'm not going to cry.



---

archive/issue_events_009522.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-25T21:22:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4203#event-9522"
}
```



---

archive/issue_comments_030448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-25T21:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30448",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030449.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-25T21:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4203#issuecomment-30449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1
