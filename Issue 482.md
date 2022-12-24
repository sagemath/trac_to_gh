# Issue 482: ideals for improving the SAGE tutorial

archive/issues_000482.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu kcrisman\n\nHere are some ideas from a user for improving the SAGE tutorial:\n\n* 2nd para of abstract: point reader to the official python tutorial for syntax issues\n* section 5 \"programming\": mention X? and X?? again\n* why doesn't \"print?\" work?  \"attach?\"\n* why does att[tab] give me attr and not \"attach\"?\n* Why does \"time for M in L:\" break. \n* Putting cputime(t) alone by itself in the script doesn't print anything.  Why? (Because you have to put \"print cputime(t)\")\n* In many cases using xrange instead of range can be vastly better\n* nohup sage file.sage > out&   # very useful\n* How to change a .sage file to a .spyx file:\n   1. Profile your file.sage file with %prun -- premature optimization is root of all evil\n   2. Start with file.py instead of file.sage.\n   3. Use \"from sage.all import stuff you need\" at the top\n   4. Consider cdef'ing classes, cdef'ing methods, and cdef'ing variables.\n\nIssue created by migration from https://trac.sagemath.org/ticket/482\n\n",
    "created_at": "2007-08-23T01:25:54Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "ideals for improving the SAGE tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/482",
    "user": "was"
}
```
Assignee: was

CC:  mvngu kcrisman

Here are some ideas from a user for improving the SAGE tutorial:

* 2nd para of abstract: point reader to the official python tutorial for syntax issues
* section 5 "programming": mention X? and X?? again
* why doesn't "print?" work?  "attach?"
* why does att[tab] give me attr and not "attach"?
* Why does "time for M in L:" break. 
* Putting cputime(t) alone by itself in the script doesn't print anything.  Why? (Because you have to put "print cputime(t)")
* In many cases using xrange instead of range can be vastly better
* nohup sage file.sage > out&   # very useful
* How to change a .sage file to a .spyx file:
   1. Profile your file.sage file with %prun -- premature optimization is root of all evil
   2. Start with file.py instead of file.sage.
   3. Use "from sage.all import stuff you need" at the top
   4. Consider cdef'ing classes, cdef'ing methods, and cdef'ing variables.

Issue created by migration from https://trac.sagemath.org/ticket/482





---

archive/issue_comments_002406.json:
```json
{
    "body": "Unless somebody thinks that anything here is still usefull I will close this ticket in the near future. \n\nCheers,\n\nMihcaek",
    "created_at": "2008-09-26T09:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/482#issuecomment-2406",
    "user": "mabshoff"
}
```

Unless somebody thinks that anything here is still usefull I will close this ticket in the near future. 

Cheers,

Mihcaek



---

archive/issue_comments_002407.json:
```json
{
    "body": "Some comments, based on 3.1.3.alpha1:\n\n* attach? does work (so fixed)\n* print? does not work (so still an issue)\n* att[tab] gives attach, not attr (so fixed)\n* the following works when written on one line:\n\n```\nsage: time for i in range(10000): a = i^2\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.02 s\n```\n\n* however, I cannot see how to make it work with a for loop spread over several lines\n\nSeveral of the other suggestions seem more appropriate for the FAQ (on the wiki) than for the tutorial (e.g. the cputime issue, the \"use screen instead of nohup\").  I think it is a good idea to mention screen somewhere in the tutorial, as well as a section about converting from .sage to .spyx.  I am happy to write a small paragraph about the former, but I'm not the right person for the latter.\n\nI've opened #4204 regarding screen, and someone who agrees that the \"sage 2 spyx\" section should exist should open a ticket for that.  Maybe there should also be a ticket for \"print?\".  Then we can close this ancient and somewhat vague ticket.",
    "created_at": "2008-09-27T02:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/482#issuecomment-2407",
    "user": "AlexGhitza"
}
```

Some comments, based on 3.1.3.alpha1:

* attach? does work (so fixed)
* print? does not work (so still an issue)
* att[tab] gives attach, not attr (so fixed)
* the following works when written on one line:

```
sage: time for i in range(10000): a = i^2
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
```

* however, I cannot see how to make it work with a for loop spread over several lines

Several of the other suggestions seem more appropriate for the FAQ (on the wiki) than for the tutorial (e.g. the cputime issue, the "use screen instead of nohup").  I think it is a good idea to mention screen somewhere in the tutorial, as well as a section about converting from .sage to .spyx.  I am happy to write a small paragraph about the former, but I'm not the right person for the latter.

I've opened #4204 regarding screen, and someone who agrees that the "sage 2 spyx" section should exist should open a ticket for that.  Maybe there should also be a ticket for "print?".  Then we can close this ancient and somewhat vague ticket.



---

archive/issue_comments_002408.json:
```json
{
    "body": "Replying to [comment:6 AlexGhitza]:\n> Someone who agrees that the \"sage 2 spyx\" section should exist should open a ticket for that.\n\nIsn't that covered by Cython already? What exactly would the goal of that section be?\n\n> Maybe there should also be a ticket for \"print?\".  Then we can close this ancient and somewhat vague ticket.\n\nWell, that is really a Python issue. I do not recall it ever coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T02:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/482#issuecomment-2408",
    "user": "mabshoff"
}
```

Replying to [comment:6 AlexGhitza]:
> Someone who agrees that the "sage 2 spyx" section should exist should open a ticket for that.

Isn't that covered by Cython already? What exactly would the goal of that section be?

> Maybe there should also be a ticket for "print?".  Then we can close this ancient and somewhat vague ticket.

Well, that is really a Python issue. I do not recall it ever coming up.

Cheers,

Michael



---

archive/issue_comments_002409.json:
```json
{
    "body": "CC'ing myself.",
    "created_at": "2009-06-27T00:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/482#issuecomment-2409",
    "user": "mvngu"
}
```

CC'ing myself.



---

archive/issue_comments_002410.json:
```json
{
    "body": "See also #9790.",
    "created_at": "2015-01-28T15:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/482",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/482#issuecomment-2410",
    "user": "mmezzarobba"
}
```

See also #9790.
