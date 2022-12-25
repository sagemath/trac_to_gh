# Issue 9834: Make desolve more informative when solving BVP

archive/issues_009834.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  mhampton\n\nFrom Sage Bugreports :\nconfusing error message\n\n\n```\nTraceback (click to the left of this block for traceback)\n...\nUnboundLocalError: local variable 'maxima_method' referenced before\nassignment\n```\n\nwhen trying\n\n```\nepsilon = 1e-2; vars = var('x'); y = function('y',x);\nde = epsilon*diff(y,x,2)+y*(1-y^2)==0;\nsoln = desolve(de,y[0,-1,1,1]);\n```\n\n\nExplanation: Currently Sage allows to use BVP only if the result is symbolic expression. In this case the result is list of two expresions and Sage fails, as mentioned very briefly in documentation of desolve. However, we could try to improve desolve or make the error message more informative.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9835\n\n",
    "created_at": "2010-08-28T21:18:27Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Make desolve more informative when solving BVP",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9834",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

CC:  mhampton

From Sage Bugreports :
confusing error message


```
Traceback (click to the left of this block for traceback)
...
UnboundLocalError: local variable 'maxima_method' referenced before
assignment
```

when trying

```
epsilon = 1e-2; vars = var('x'); y = function('y',x);
de = epsilon*diff(y,x,2)+y*(1-y^2)==0;
soln = desolve(de,y[0,-1,1,1]);
```


Explanation: Currently Sage allows to use BVP only if the result is symbolic expression. In this case the result is list of two expresions and Sage fails, as mentioned very briefly in documentation of desolve. However, we could try to improve desolve or make the error message more informative.

Issue created by migration from https://trac.sagemath.org/ticket/9835





---

archive/issue_comments_096875.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T19:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96875",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096876.json:
```json
{
    "body": "The patch\n\n* solves the problem\n\n* fixes documentation\n\n* decreases number of spawned Maxima sessions into one session",
    "created_at": "2010-08-29T19:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96876",
    "user": "https://github.com/robert-marik"
}
```

The patch

* solves the problem

* fixes documentation

* decreases number of spawned Maxima sessions into one session



---

archive/issue_comments_096877.json:
```json
{
    "body": "One very minor comment - no time to review now:\n\n```\n. Remove the initial contition t\n```\n\nat the very end of the patch should be \"condition\".\n\nDo you think it would be worth adding another doctest to show that the sage-support request is fixed as well:\n\n```\nvar('t alpha beta n') \nx=function('x',t) \neq=diff(x,t)^2==alpha-beta abs(x)^n \nassume(n,'integer') \ndesolve(eq,x,ivar=t,contrib_ode=True) \n```\n\n\nThanks for finding and fixing this!",
    "created_at": "2010-09-21T13:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96877",
    "user": "https://github.com/kcrisman"
}
```

One very minor comment - no time to review now:

```
. Remove the initial contition t
```

at the very end of the patch should be "condition".

Do you think it would be worth adding another doctest to show that the sage-support request is fixed as well:

```
var('t alpha beta n') 
x=function('x',t) 
eq=diff(x,t)^2==alpha-beta abs(x)^n 
assume(n,'integer') 
desolve(eq,x,ivar=t,contrib_ode=True) 
```


Thanks for finding and fixing this!



---

archive/issue_events_024760.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2010-09-21T13:15:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9834#event-24760"
}
```



---

archive/issue_comments_096878.json:
```json
{
    "body": "Thanks, I will update the patch as time permits.\n\nThe equation from sage-support still fails, since Maxima fails to solve it.  Anyway. Sage and Maxima now know that n is integer.\n\n```\nmarik@um-bc107:/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux$ ./sage --maxima\n;;; Loading #P\"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/defsys tem.fas\"\n;;; Loading #P\"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/cmp.fa s\"\n;;; Loading #P\"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/sysfun .lsp\"\nMaxima 5.20.1 http://maxima.sourceforge.net\nusing Lisp ECL 10.2.1\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThe function bug_report() provides bug reporting information.\n(%i1) declare(n,integer);\n(%o1)                                done\n(%i2) eq: 'diff(x,t)^2=alpha-beta*abs(x)^n;\n                          dx 2                      n\n(%o2)                    (--)  = alpha - beta abs(x)\n                          dt\n(%i3) load('contrib_ode)$\n\n(%i4) contrib_ode(eq,x,t);\n                          dx 2                      n\n(%t4)                    (--)  = alpha - beta abs(x)\n                          dt\n\n                     first order equation not linear in y'\n\nImproper argument to ratcoeff:\n0\n#0: linear2(expr=x,x=0)(ode2.mac line 75)\n#1: ode1_a(phi=-sqrt(alpha-beta*abs(x)^n),y=x,x=t)(ode1_lie.mac line 176)\n#2: ode1_lie(phi=-sqrt(alpha-beta*abs(x)^n),y=x,x=t)(ode1_lie.mac line 54)\n -- an error. To debug this try: debugmode(true);\n\n```\n",
    "created_at": "2010-09-21T13:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96878",
    "user": "https://github.com/robert-marik"
}
```

Thanks, I will update the patch as time permits.

The equation from sage-support still fails, since Maxima fails to solve it.  Anyway. Sage and Maxima now know that n is integer.

```
marik@um-bc107:/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux$ ./sage --maxima
;;; Loading #P"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/defsys tem.fas"
;;; Loading #P"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/cmp.fa s"
;;; Loading #P"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/sysfun .lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) declare(n,integer);
(%o1)                                done
(%i2) eq: 'diff(x,t)^2=alpha-beta*abs(x)^n;
                          dx 2                      n
(%o2)                    (--)  = alpha - beta abs(x)
                          dt
(%i3) load('contrib_ode)$

(%i4) contrib_ode(eq,x,t);
                          dx 2                      n
(%t4)                    (--)  = alpha - beta abs(x)
                          dt

                     first order equation not linear in y'

Improper argument to ratcoeff:
0
#0: linear2(expr=x,x=0)(ode2.mac line 75)
#1: ode1_a(phi=-sqrt(alpha-beta*abs(x)^n),y=x,x=t)(ode1_lie.mac line 176)
#2: ode1_lie(phi=-sqrt(alpha-beta*abs(x)^n),y=x,x=t)(ode1_lie.mac line 54)
 -- an error. To debug this try: debugmode(true);

```




---

archive/issue_comments_096879.json:
```json
{
    "body": "This doesn't seem fixed to me:\n\n```\nsage: epsilon = 1e-2; vars = var('x'); y = function('y',x);\nsage: de = epsilon*diff(y,x,2)+y*(1-y^2)==0;\nsage: soln = desolve(de,y[0,-1,1,1])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/mh/<ipython console> in <module>()\n\nTypeError: 'sage.symbolic.expression.Expression' object is unsubscriptable\n```\n",
    "created_at": "2010-09-21T13:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This doesn't seem fixed to me:

```
sage: epsilon = 1e-2; vars = var('x'); y = function('y',x);
sage: de = epsilon*diff(y,x,2)+y*(1-y^2)==0;
sage: soln = desolve(de,y[0,-1,1,1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/mh/<ipython console> in <module>()

TypeError: 'sage.symbolic.expression.Expression' object is unsubscriptable
```




---

archive/issue_comments_096880.json:
```json
{
    "body": "Even after fixing the sytax I still get an error:\n\n```\nsage: vars = var('x'); y = function('y',x);\nsage: soln = desolve(diff(y,x,2) + 100*y*(1-y^2),dvar=y,ivar=x,ics=[0,-1,1,1])\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/Users/mh/<ipython console> in <module>()\n\n/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sage/calculus/desolvers.pyc in desolve(de, dvar, ics, ivar, show_method, contrib_ode)\n    436             maxima_method=P(\"method\")\n    437         if not is_SymbolicEquation(soln.sage()):\n--> 438              raise NotImplementedError, \"Unable to use initial condition for this equation (%s).\"%(str(maxima_method).strip())   \n    439         if len(ics) == 2:\n    440             tempic=(ivar==ics[0])._maxima_().str()\n\nNotImplementedError: Unable to use initial condition for this equation (freeofx).\n```\n",
    "created_at": "2010-09-21T13:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Even after fixing the sytax I still get an error:

```
sage: vars = var('x'); y = function('y',x);
sage: soln = desolve(diff(y,x,2) + 100*y*(1-y^2),dvar=y,ivar=x,ics=[0,-1,1,1])
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/Users/mh/<ipython console> in <module>()

/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sage/calculus/desolvers.pyc in desolve(de, dvar, ics, ivar, show_method, contrib_ode)
    436             maxima_method=P("method")
    437         if not is_SymbolicEquation(soln.sage()):
--> 438              raise NotImplementedError, "Unable to use initial condition for this equation (%s)."%(str(maxima_method).strip())   
    439         if len(ics) == 2:
    440             tempic=(ivar==ics[0])._maxima_().str()

NotImplementedError: Unable to use initial condition for this equation (freeofx).
```




---

archive/issue_comments_096881.json:
```json
{
    "body": "Changing assignee from @burcin to mhampton.",
    "created_at": "2010-09-21T13:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from @burcin to mhampton.



---

archive/issue_comments_096882.json:
```json
{
    "body": "Thanks for menitioning this. \n\nWihtout this patch we get\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe Sage install tree may have moved.\nRegenerating Python.pyo and .pyc files that hardcode the install PATH\n(please wait at most a few minutes)...\nDo not interrupt this.\nsage: vars = var('x'); y = function('y',x);\nsage: soln = desolve(diff(y,x,2) + 100*y*(1-y^2),dvar=y,ivar=x,ics=[0,-1,1,1])\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n| Sage Version 4.5.3, Release Date: 2010-09-04                       |\n| Type notebook() for the GUI, and license() for information.        |\n/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/<ipython console> in <module>()\n\n/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/python2.6/site-packages/sage/calculus/desolvers.py in desolve(de, dvar, ics, ivar, show_method, contrib_ode)\n    358     if (ics is not None):\n    359         if not is_SymbolicEquation(soln.sage()):\n--> 360              raise NotImplementedError, \"Maxima was unable to use initial condition for this equation (%s)\"%(maxima_method.str())\n    361         if len(ics) == 2:\n    362             tempic=(ivar==ics[0])._maxima_().str()\n\nUnboundLocalError: local variable 'maxima_method' referenced before assignment\n```\n\nand the user does not know, what went wrong. With this patch the user knows, that it Sage is not capable to use initial conditions for this ODE.",
    "created_at": "2010-09-21T14:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96882",
    "user": "https://github.com/robert-marik"
}
```

Thanks for menitioning this. 

Wihtout this patch we get

```
----------------------------------------------------------------------
----------------------------------------------------------------------
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
sage: vars = var('x'); y = function('y',x);
sage: soln = desolve(diff(y,x,2) + 100*y*(1-y^2),dvar=y,ivar=x,ics=[0,-1,1,1])
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/<ipython console> in <module>()

/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/python2.6/site-packages/sage/calculus/desolvers.py in desolve(de, dvar, ics, ivar, show_method, contrib_ode)
    358     if (ics is not None):
    359         if not is_SymbolicEquation(soln.sage()):
--> 360              raise NotImplementedError, "Maxima was unable to use initial condition for this equation (%s)"%(maxima_method.str())
    361         if len(ics) == 2:
    362             tempic=(ivar==ics[0])._maxima_().str()

UnboundLocalError: local variable 'maxima_method' referenced before assignment
```

and the user does not know, what went wrong. With this patch the user knows, that it Sage is not capable to use initial conditions for this ODE.



---

archive/issue_comments_096883.json:
```json
{
    "body": "Attachment [trac_9835.patch](tarball://root/attachments/some-uuid/ticket9835/trac_9835.patch) by @robert-marik created at 2010-09-21 14:43:06\n\nrebased for Sage 4.5.3., fixed typo, replaces previous patch with the same name",
    "created_at": "2010-09-21T14:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96883",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_9835.patch](tarball://root/attachments/some-uuid/ticket9835/trac_9835.patch) by @robert-marik created at 2010-09-21 14:43:06

rebased for Sage 4.5.3., fixed typo, replaces previous patch with the same name



---

archive/issue_comments_096884.json:
```json
{
    "body": "solves also #9710 and #8931",
    "created_at": "2010-09-21T20:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96884",
    "user": "https://github.com/robert-marik"
}
```

solves also #9710 and #8931



---

archive/issue_comments_096885.json:
```json
{
    "body": "Attachment [trac_9835.take2.patch](tarball://root/attachments/some-uuid/ticket9835/trac_9835.take2.patch) by @burcin created at 2010-09-26 13:25:25\n\nminor change - apply only this patch",
    "created_at": "2010-09-26T13:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96885",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9835.take2.patch](tarball://root/attachments/some-uuid/ticket9835/trac_9835.take2.patch) by @burcin created at 2010-09-26 13:25:25

minor change - apply only this patch



---

archive/issue_comments_096886.json:
```json
{
    "body": "Patch looks good and it solves a whole bunch of problems, so I'd like to give this a positive review.\n\nI have one minor suggestion. The if clause on line 435-436 only serves the purpose of assigning a value to `maxima_method` to show in the error message. attachment:trac_9835.take2.patch moves these lines right before we raise the error, so that they are not executed unnecessarily.\n\nI give a positive review to Robert's changes. Please switch this to a positive review if you agree with mine.",
    "created_at": "2010-09-26T13:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96886",
    "user": "https://github.com/burcin"
}
```

Patch looks good and it solves a whole bunch of problems, so I'd like to give this a positive review.

I have one minor suggestion. The if clause on line 435-436 only serves the purpose of assigning a value to `maxima_method` to show in the error message. attachment:trac_9835.take2.patch moves these lines right before we raise the error, so that they are not executed unnecessarily.

I give a positive review to Robert's changes. Please switch this to a positive review if you agree with mine.



---

archive/issue_comments_096887.json:
```json
{
    "body": "Positive review to Burcin's change. Thank you.\n\nRelease manager: apply only attachment:trac_9835.take2.patch",
    "created_at": "2010-09-27T07:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96887",
    "user": "https://github.com/robert-marik"
}
```

Positive review to Burcin's change. Thank you.

Release manager: apply only attachment:trac_9835.take2.patch



---

archive/issue_comments_096888.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-27T07:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96888",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024761.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T09:11:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9834#event-24761"
}
```



---

archive/issue_comments_096889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96889",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024762.json:
```json
{
    "actor": "https://github.com/loefflerd",
    "created_at": "2010-09-28T10:35:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9834#event-24762"
}
```



---

archive/issue_events_024763.json:
```json
{
    "actor": "https://github.com/loefflerd",
    "created_at": "2010-09-28T10:35:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9834#event-24763"
}
```



---

archive/issue_comments_096890.json:
```json
{
    "body": "Thanks, David!",
    "created_at": "2010-09-28T10:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9834#issuecomment-96890",
    "user": "https://github.com/qed777"
}
```

Thanks, David!
