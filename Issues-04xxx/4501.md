# Issue 4501: preparser does not know about python notation for complex numbers

archive/issues_004501.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: 1j\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     Integer(1)j\n               ^\nSyntaxError: invalid syntax\n```\n\nbut in python:\n\n```\nsage: preparser(False)\nsage: 1j\n1j\nsage: type(1j)\n<type 'complex'>\n```\n\nNote that this does work now:\n\n```\nsage: 1rj\n1j\nsage: 1rj == complex('j')\nTrue\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4501\n\n",
    "closed_at": "2009-01-24T11:42:39Z",
    "created_at": "2008-11-12T16:57:58Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "preparser does not know about python notation for complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4501",
    "user": "https://github.com/jasongrout"
}
```
Assignee: somebody

```
sage: 1j
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(1)j
               ^
SyntaxError: invalid syntax
```

but in python:

```
sage: preparser(False)
sage: 1j
1j
sage: type(1j)
<type 'complex'>
```

Note that this does work now:

```
sage: 1rj
1j
sage: 1rj == complex('j')
True
```



Issue created by migration from https://trac.sagemath.org/ticket/4501





---

archive/issue_comments_033270.json:
```json
{
    "body": "According to [http://docs.python.org/reference/lexical_analysis.html#id7](http://docs.python.org/reference/lexical_analysis.html#id7), python supports imaginary numbers being declared as:\n\nimagnumber ::=  (floatnumber | intpart) (\"j\" | \"J\")",
    "created_at": "2008-11-12T17:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33270",
    "user": "https://github.com/jasongrout"
}
```

According to [http://docs.python.org/reference/lexical_analysis.html#id7](http://docs.python.org/reference/lexical_analysis.html#id7), python supports imaginary numbers being declared as:

imagnumber ::=  (floatnumber | intpart) ("j" | "J")



---

archive/issue_comments_033271.json:
```json
{
    "body": "```\n[10:57] <mhansen> jason-: I don't have time to make a patch now, but the following two lines around line 805 in sage/misc/preparser.py are the correct fix if we want 1j to return a <type 'complex'>:\n[10:57] <mhansen>                 elif i < len(line) and line[i] == 'j':\n[10:57] <mhansen>                     pass\n[10:57] <jason-> I can make a quick patch\n[10:57] <jason-> It needs to support \"J\"\n[10:57] <jason-> and also work for floating numbers too\n[10:58] <jason-> and then there's the issue of if we want to construct Sage complex numbers instead of python complex numbers\n```",
    "created_at": "2008-11-12T17:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33271",
    "user": "https://github.com/jasongrout"
}
```

```
[10:57] <mhansen> jason-: I don't have time to make a patch now, but the following two lines around line 805 in sage/misc/preparser.py are the correct fix if we want 1j to return a <type 'complex'>:
[10:57] <mhansen>                 elif i < len(line) and line[i] == 'j':
[10:57] <mhansen>                     pass
[10:57] <jason-> I can make a quick patch
[10:57] <jason-> It needs to support "J"
[10:57] <jason-> and also work for floating numbers too
[10:58] <jason-> and then there's the issue of if we want to construct Sage complex numbers instead of python complex numbers
```



---

archive/issue_comments_033272.json:
```json
{
    "body": "and the next line:\n\n```\n[10:58] <mhansen> Just change == \"j\" to in 'jJ'\n```",
    "created_at": "2008-11-12T17:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33272",
    "user": "https://github.com/jasongrout"
}
```

and the next line:

```
[10:58] <mhansen> Just change == "j" to in 'jJ'
```



---

archive/issue_comments_033273.json:
```json
{
    "body": "I think 1j should be a Sage complex number.",
    "created_at": "2008-11-12T18:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33273",
    "user": "https://github.com/robertwb"
}
```

I think 1j should be a Sage complex number.



---

archive/issue_comments_033274.json:
```json
{
    "body": "> I think 1j should be a Sage complex number. \n\n\nAnd I think it should return a Python complex number. :-)",
    "created_at": "2008-11-13T01:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33274",
    "user": "https://github.com/williamstein"
}
```

> I think 1j should be a Sage complex number. 


And I think it should return a Python complex number. :-)



---

archive/issue_comments_033275.json:
```json
{
    "body": "Your reasoning (that the userbase for this feature is almost entirely numeric users) has convinced me.",
    "created_at": "2008-11-13T02:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33275",
    "user": "https://github.com/robertwb"
}
```

Your reasoning (that the userbase for this feature is almost entirely numeric users) has convinced me.



---

archive/issue_events_010193.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-15T11:04:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4501#event-10193"
}
```



---

archive/issue_comments_033276.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-24T11:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33276",
    "user": "https://github.com/robertwb"
}
```

Resolution: duplicate



---

archive/issue_comments_033277.json:
```json
{
    "body": "See #5079",
    "created_at": "2009-01-24T11:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4501#issuecomment-33277",
    "user": "https://github.com/robertwb"
}
```

See #5079



---

archive/issue_events_010194.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2009-01-24T11:42:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4501#event-10194"
}
```



---

archive/issue_events_010195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T15:34:22Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4501#event-10195"
}
```



---

archive/issue_events_010196.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T15:34:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4501",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4501#event-10196"
}
```
