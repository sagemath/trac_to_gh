# Issue 9710: Assumptions not passed to differential equation solver

archive/issues_009710.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robert-marik @kcrisman @jdemeyer\n\nKeywords: differential equations, assumptions\n\nThe assume function doesn't seem to work with the differential equation solver, despite what the documentation for desolve suggests. This returns an error:\n\n```\nsage: x = var('x')\nsage: k = var('k')\nsage: y = function('y',x)\nsage: assume(k>0)\nsage: print desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_25.py\", line 10, in <module>\n    exec compile(u'open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"eCA9IHZhcigneCcpCmsgPSB2YXIoJ2snKQp5ID0gZnVuY3Rpb24oJ3knLHgpCmFzc3VtZShrPjApCnByaW50IGRlc29sdmUoZGlmZih5LHgseCkrayp5LWV4cCgtayp4KSxbeSx4XSk=\"),globals())+\"\\\\n\"); execfile(os.path.abspath(\"___code___.py\"))\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpyNFGr0/___code___.py\", line 7, in <module>\n    exec compile(u'print desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])\n  File \"\", line 1, in <module>\n    \n  File \"/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/calculus/desolvers.py\", line 340, in desolve\n    soln = maxima(cmd)\n  File \"/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 1032, in __call__\n    return cls(self, x, name=name)\n  File \"/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/interfaces/expect.py\", line 1451, in __init__\n    raise TypeError, x\nTypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(k>0)' before integral or limit evaluation, for example):\nIs  k  positive, negative, or zero?\n```\nFound by Praveen N. and Aashita during Sage Days 25 coding sprint.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9710\n\n",
    "created_at": "2010-08-09T14:27:20Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Assumptions not passed to differential equation solver",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9710",
    "user": "https://github.com/kedlaya"
}
```
Assignee: @burcin

CC:  @robert-marik @kcrisman @jdemeyer

Keywords: differential equations, assumptions

The assume function doesn't seem to work with the differential equation solver, despite what the documentation for desolve suggests. This returns an error:

```
sage: x = var('x')
sage: k = var('k')
sage: y = function('y',x)
sage: assume(k>0)
sage: print desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_25.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("eCA9IHZhcigneCcpCmsgPSB2YXIoJ2snKQp5ID0gZnVuY3Rpb24oJ3knLHgpCmFzc3VtZShrPjApCnByaW50IGRlc29sdmUoZGlmZih5LHgseCkrayp5LWV4cCgtayp4KSxbeSx4XSk="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpyNFGr0/___code___.py", line 7, in <module>
    exec compile(u'print desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])
  File "", line 1, in <module>
    
  File "/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/calculus/desolvers.py", line 340, in desolve
    soln = maxima(cmd)
  File "/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1032, in __call__
    return cls(self, x, name=name)
  File "/home/kedlaya/sage-complete/local/lib/python2.6/site-packages/sage/interfaces/expect.py", line 1451, in __init__
    raise TypeError, x
TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(k>0)' before integral or limit evaluation, for example):
Is  k  positive, negative, or zero?
```
Found by Praveen N. and Aashita during Sage Days 25 coding sprint.


Issue created by migration from https://trac.sagemath.org/ticket/9710





---

archive/issue_comments_094477.json:
```json
{
    "body": "Observed later: ticket #8931 is similar, possibly enough so for this to be considered a duplicate. Also, I misread the documentation:\n\n```\n       This equation can be solved within Maxima but not within Sage. It\n       needs assumptions assume(x>0,y>0) and works in Maxima, but not in\n       Sage:\n    \n          sage: assume(x>0) # not tested\n          sage: assume(y>0) # not tested\n          sage: desolve(x*diff(y,x)-x*sqrt(y^2+x^2)-y,y,show_method=True) # not tested\n```\nSo no promise is being made, but nonetheless I think this needs to be fixed.",
    "created_at": "2010-08-10T02:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94477",
    "user": "https://github.com/kedlaya"
}
```

Observed later: ticket #8931 is similar, possibly enough so for this to be considered a duplicate. Also, I misread the documentation:

```
       This equation can be solved within Maxima but not within Sage. It
       needs assumptions assume(x>0,y>0) and works in Maxima, but not in
       Sage:
    
          sage: assume(x>0) # not tested
          sage: assume(y>0) # not tested
          sage: desolve(x*diff(y,x)-x*sqrt(y^2+x^2)-y,y,show_method=True) # not tested
```
So no promise is being made, but nonetheless I think this needs to be fixed.



---

archive/issue_comments_094478.json:
```json
{
    "body": "with #9961:\n\n```\nmarik@um-bc107:/opt/sage$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: x=var('x'); f=function('f',x); k=var('k'); assume(k>0)\nsage: desolve(diff(f,x,2)/f==k,f,ivar=x)\nk1*e^(sqrt(k)*x) + k2*e^(-sqrt(k)*x)\n```",
    "created_at": "2010-09-21T20:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94478",
    "user": "https://github.com/robert-marik"
}
```

with #9961:

```
marik@um-bc107:/opt/sage$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x=var('x'); f=function('f',x); k=var('k'); assume(k>0)
sage: desolve(diff(f,x,2)/f==k,f,ivar=x)
k1*e^(sqrt(k)*x) + k2*e^(-sqrt(k)*x)
```



---

archive/issue_comments_094479.json:
```json
{
    "body": "In fact, #9835 is sufficient to solve this problem. The patch #9961 which is on the top of #9835 is not necessary. For the problem from the description we have with #9835:\n\n```\nmarik@um-bc107:/opt/sage$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: x = var('x')\nsage: k = var('k')\nsage: y = function('y',x)\nsage: assume(k>0)\nsage: desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])\nk1*sin(sqrt(k)*x) + k2*cos(sqrt(k)*x) + e^(-k*x)/(k^2 + k)\nsage:\n| Sage Version 4.5.3, Release Date: 2010-09-04                       |\n| Type notebook() for the GUI, and license() for information.        |\n```",
    "created_at": "2010-09-21T20:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94479",
    "user": "https://github.com/robert-marik"
}
```

In fact, #9835 is sufficient to solve this problem. The patch #9961 which is on the top of #9835 is not necessary. For the problem from the description we have with #9835:

```
marik@um-bc107:/opt/sage$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x = var('x')
sage: k = var('k')
sage: y = function('y',x)
sage: assume(k>0)
sage: desolve(diff(y,x,x)+k*y-exp(-k*x),[y,x])
k1*sin(sqrt(k)*x) + k2*cos(sqrt(k)*x) + e^(-k*x)/(k^2 + k)
sage:
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
```



---

archive/issue_events_024285.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2011-03-14T20:45:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "milestone": "sage-4.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9710#event-24285"
}
```



---

archive/issue_comments_094480.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-14T20:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94480",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094481.json:
```json
{
    "body": "Yup, and still works.  Definitely same issue as #8931, which now has positive review.  \n\nWe could add yet another doctest, but in this case there are already so many tests of it, with another one coming at #8931, that it seems appropriate to simply say this is a dup.  \n\nTo release manager: please close this ticket.",
    "created_at": "2011-03-14T20:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94481",
    "user": "https://github.com/kcrisman"
}
```

Yup, and still works.  Definitely same issue as #8931, which now has positive review.  

We could add yet another doctest, but in this case there are already so many tests of it, with another one coming at #8931, that it seems appropriate to simply say this is a dup.  

To release manager: please close this ticket.



---

archive/issue_comments_094482.json:
```json
{
    "body": "> We could add yet another doctest, but in this case there are already so many tests of it, with another one coming at #8931, that it seems appropriate to simply say this is a dup.  \n\n\nThe other tests being from #9961 and #9835.",
    "created_at": "2011-03-14T20:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94482",
    "user": "https://github.com/kcrisman"
}
```

> We could add yet another doctest, but in this case there are already so many tests of it, with another one coming at #8931, that it seems appropriate to simply say this is a dup.  


The other tests being from #9961 and #9835.



---

archive/issue_comments_094483.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-14T20:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94483",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094484.json:
```json
{
    "body": "Sorry, forgot to actually cc: the release manager.",
    "created_at": "2011-03-14T21:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94484",
    "user": "https://github.com/kcrisman"
}
```

Sorry, forgot to actually cc: the release manager.



---

archive/issue_events_024286.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-16T11:09:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "milestone": "sage-4.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9710#event-24286"
}
```



---

archive/issue_events_024287.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-16T11:09:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9710#event-24287"
}
```



---

archive/issue_comments_094485.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-03-17T09:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9710#issuecomment-94485",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_024288.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-03-17T09:46:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9710",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9710#event-24288"
}
```
