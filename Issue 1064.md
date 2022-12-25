# Issue 1064: applying permutation is coded in a way that behaves badly when input isn't an "expected type"

archive/issues_001064.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n19:00 < wstein> that permuation application code in #750 is (and has always been) lame.\n19:00 < wstein> watch:\n19:00 < wstein> g = PermutationGroup(['(1,2,3)(4,5)']).gen(0)\n19:00 < wstein> g(x)\n19:00 < wstein> Get a big traceback from Gap.\n19:00 < wstein> It would be trivial to code things to give a much more sensible error.\n19:01 < wstein> This isn't a criticism of #750; just that looking at #750 immediately\n19:01 < wstein> makes me see that there are bad features to the code.\n19:02 < wstein> Even worse:\n19:02 < wstein> sage: g(3/2)\n19:02 < wstein> 1\n19:02 < wstein> That makes no sense!\n}}]\n\nThe problem is this line of code in sage/groups/perm_gps/permgroup_element.py:\n\n{{{\n            return int(gap.eval('%s^%s'%(i, self._gap_().name())))\n}}}\n\nInstead that should be\n\n{{{\n            return int(gap.eval('%s^%s'%(Integer(i), self._gap_().name())))\n}}}\n\nsince then we'll get a sensible error message if i doesn't have a natural\ninterpretation as an integer.\n\nOf course, one must import Integer. \n\nI'm not attaching a patch, since ticket #750 and a text patch would be\ntoo confusing to apply.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1064\n\n",
    "created_at": "2007-11-02T02:04:43Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "applying permutation is coded in a way that behaves badly when input isn't an \"expected type\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1064",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
19:00 < wstein> that permuation application code in #750 is (and has always been) lame.
19:00 < wstein> watch:
19:00 < wstein> g = PermutationGroup(['(1,2,3)(4,5)']).gen(0)
19:00 < wstein> g(x)
19:00 < wstein> Get a big traceback from Gap.
19:00 < wstein> It would be trivial to code things to give a much more sensible error.
19:01 < wstein> This isn't a criticism of #750; just that looking at #750 immediately
19:01 < wstein> makes me see that there are bad features to the code.
19:02 < wstein> Even worse:
19:02 < wstein> sage: g(3/2)
19:02 < wstein> 1
19:02 < wstein> That makes no sense!
}}]

The problem is this line of code in sage/groups/perm_gps/permgroup_element.py:

{{{
            return int(gap.eval('%s^%s'%(i, self._gap_().name())))
}}}

Instead that should be

{{{
            return int(gap.eval('%s^%s'%(Integer(i), self._gap_().name())))
}}}

since then we'll get a sensible error message if i doesn't have a natural
interpretation as an integer.

Of course, one must import Integer. 

I'm not attaching a patch, since ticket #750 and a text patch would be
too confusing to apply.

Issue created by migration from https://trac.sagemath.org/ticket/1064





---

archive/issue_comments_006439.json:
```json
{
    "body": "Now the stupid traceback is different, but equally stupid. Amusingly:\n\n```\nsage: g(3/2)\n2\n```\n\nNow we're starting to make some sense!?",
    "created_at": "2007-12-19T06:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1064#issuecomment-6439",
    "user": "https://github.com/rlmill"
}
```

Now the stupid traceback is different, but equally stupid. Amusingly:

```
sage: g(3/2)
2
```

Now we're starting to make some sense!?



---

archive/issue_comments_006440.json:
```json
{
    "body": "Attachment [trac-1064.patch](tarball://root/attachments/some-uuid/ticket1064/trac-1064.patch) by @rlmill created at 2007-12-19 06:39:33",
    "created_at": "2007-12-19T06:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1064#issuecomment-6440",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-1064.patch](tarball://root/attachments/some-uuid/ticket1064/trac-1064.patch) by @rlmill created at 2007-12-19 06:39:33



---

archive/issue_events_001186.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-21T00:28:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1064",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1064#event-1186"
}
```



---

archive/issue_comments_006441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-21T00:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1064#issuecomment-6441",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_006442.json:
```json
{
    "body": "Merged in 2.9.1 alpha2",
    "created_at": "2007-12-21T00:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1064#issuecomment-6442",
    "user": "https://github.com/rlmill"
}
```

Merged in 2.9.1 alpha2
