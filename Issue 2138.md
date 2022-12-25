# Issue 2138: bugs in word_problem for AbelianGroupElement

archive/issues_002138.json:
```json
{
    "body": "Assignee: joyner\n\nsage: G = AbelianGroup(2,[2,3], names=\"xy\")\nsage: x,y = G.gens()\nsage: x.word_problem([x,y],display=False)\n[This is the Trac macro *x, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x, 1-macro)\nsage: x.word_problem([x,y],display=True)\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/mnt/drive_hda1/sagefiles/sage-2.9.alpha4/<ipython console> in <module>()\n\n/home/wdj/wdj/sagefiles/sage-2.9.alpha4/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group_element.py in word_problem(self, words, display)\n    341         #print LL1,LL2\n    342         if display:\n--> 343             s = str(g)+\" = \"+add([\"(\"+str(words[LL2[i]-1])+\")^\"+str(LL1[i])+\"*\" for i in range(nn)])\n    344             m = len(s)\n    345             #print \"      \",s[:m-1]\n\n<type 'exceptions.NameError'>: global name 'add' is not defined\n\n\nThis is obviously a problem. Also, the docstring should be written better. The first\nexample is hard to understand.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2138\n\n",
    "created_at": "2008-02-11T00:42:10Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "bugs in word_problem for AbelianGroupElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2138",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: joyner

sage: G = AbelianGroup(2,[2,3], names="xy")
sage: x,y = G.gens()
sage: x.word_problem([x,y],display=False)
[This is the Trac macro *x, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x, 1-macro)
sage: x.word_problem([x,y],display=True)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/mnt/drive_hda1/sagefiles/sage-2.9.alpha4/<ipython console> in <module>()

/home/wdj/wdj/sagefiles/sage-2.9.alpha4/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group_element.py in word_problem(self, words, display)
    341         #print LL1,LL2
    342         if display:
--> 343             s = str(g)+" = "+add(["("+str(words[LL2[i]-1])+")^"+str(LL1[i])+"*" for i in range(nn)])
    344             m = len(s)
    345             #print "      ",s[:m-1]

<type 'exceptions.NameError'>: global name 'add' is not defined


This is obviously a problem. Also, the docstring should be written better. The first
example is hard to understand.

Issue created by migration from https://trac.sagemath.org/ticket/2138





---

archive/issue_comments_013989.json:
```json
{
    "body": "> Also, the docstring should be written better. The first example is hard to understand.\n\nWhoever fixes this (maybe me) please keep in mind trac #1849 and the attached patch.  \n\nWilliam",
    "created_at": "2008-02-11T01:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2138#issuecomment-13989",
    "user": "https://github.com/williamstein"
}
```

> Also, the docstring should be written better. The first example is hard to understand.

Whoever fixes this (maybe me) please keep in mind trac #1849 and the attached patch.  

William



---

archive/issue_comments_013990.json:
```json
{
    "body": "I think this was fixed as part of another ticket? Anyway, I think I removed the display option. It wasn't necessary and I got some (offlist) complaints that it was hard to understand what the output meant. So, I think this ticket is resolved, isn't it?",
    "created_at": "2008-04-09T11:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2138#issuecomment-13990",
    "user": "https://github.com/wdjoyner"
}
```

I think this was fixed as part of another ticket? Anyway, I think I removed the display option. It wasn't necessary and I got some (offlist) complaints that it was hard to understand what the output meant. So, I think this ticket is resolved, isn't it?



---

archive/issue_events_002300.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-09T15:20:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2138",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2138#event-2300"
}
```



---

archive/issue_comments_013991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T15:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2138#issuecomment-13991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013992.json:
```json
{
    "body": "Replying to [comment:3 wdj]:\n> I think this was fixed as part of another ticket? Anyway, I think I removed the display option. It wasn't necessary and I got some (offlist) complaints that it was hard to understand what the output meant. So, I think this ticket is resolved, isn't it?\n\nYes. I can confirm that the `display` property is gone. Closed as fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T15:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2138#issuecomment-13992",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 wdj]:
> I think this was fixed as part of another ticket? Anyway, I think I removed the display option. It wasn't necessary and I got some (offlist) complaints that it was hard to understand what the output meant. So, I think this ticket is resolved, isn't it?

Yes. I can confirm that the `display` property is gone. Closed as fixed.

Cheers,

Michael
