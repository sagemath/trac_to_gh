# Issue 1660: maxima interface bug caused by bad use of file when evaluating large input

archive/issues_001660.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\n> That's weird.  Can you post the _exact_ input\n> and output from a complete session where you get\n> sage1 as the output from maxima.eval('...')?  Thanks.\n>\n\nThis is it:\nlwdrob@lwdrob-comp:~/Disertatie$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.9.1, Release Date: 2007-12-24                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage:\nmaxima.eval('plot2d([-7.5/-0.5*(x-0.5)+8,-7.5/7.5*(x-0.5)+8,-6.5/-0.5*(x-0.5)+8,-6.5/7.5*(x-0.5)+8,-5.5/-0.5*(x-0.5)+8,'+\n\\\n....:\n'-5.5/7.5*(x-0.5)+8,-4.5/-0.5*(x-0.5)+8,-4.5/7.5*(x-0.5)+8,-3.5/-0.5*(x-0.5)+8,-3.5/7.5*(x-0.5)+8,-2.5/-0.5*(x-0.5)+8,'+\n\\\n....:\n'-2.5/7.5*(x-0.5)+8,-1.5/-0.5*(x-0.5)+8,-1.5/7.5*(x-0.5)+8,-0.5/-0.5*(x-0.5)+8,-0.5/7.5*(x-0.5)+8],'+\n\\\n....: '[x,0,n],[plot_format,gnuplot_pipes],[y, 0, 8],[ylabel,\"y\"],\n[gnuplot_preamble, \"set grid xtics ytics\"],[legend,false])')\n'sage0'\nsage:\n\nThere is a tmp file containing the above cmd:\n$cat /home/lwdrob/.sage/temp/lwdrob_comp/7280/interface/tmp\nsage0 :\nplot2d([-7.5/-0.5*(x-0.5)+8,-7.5/7.5*(x-0.5)+8,-6.5/-0.5*(x-0.5)+8,-6.5/7.5*(x-0.5)+8,-5.5/-0.5*(x-0.5)+8,\n-5.5/7.5*(x-0.5)+8,-4.5/-0.5*(x-0.5)+8,-4.5/7.5*(x-0.5)+8,-3.5/-0.5*(x-0.5)+8,-3.5/7.5*(x-0.5)+8,-2.5/-0.5*(x-0.5)+8,\n-2.5/7.5*(x-0.5)+8,-1.5/-0.5*(x-0.5)+8,-1.5/7.5*(x-0.5)+8,-0.5/-0.5*(x-0.5)+8,-0.5/7.5*(x-0.5)+8],\n[x,0,n], [plot_format,gnuplot_pipes], [y,0,8],[ylabel,\"y\"],\n[gnuplot_preamble, \"set grid xtics ytics\"],[legend,false])$\n\nBest regards,\n```\n\nThe problem is that the maxima interface should not be assigning to a variable when using a file to evaluate a large input. \n\nWilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/1660\n\n",
    "created_at": "2008-01-02T21:07:38Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "maxima interface bug caused by bad use of file when evaluating large input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1660",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
> That's weird.  Can you post the _exact_ input
> and output from a complete session where you get
> sage1 as the output from maxima.eval('...')?  Thanks.
>

This is it:
lwdrob@lwdrob-comp:~/Disertatie$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.1, Release Date: 2007-12-24                       |
| Type notebook() for the GUI, and license() for information.        |
sage:
maxima.eval('plot2d([-7.5/-0.5*(x-0.5)+8,-7.5/7.5*(x-0.5)+8,-6.5/-0.5*(x-0.5)+8,-6.5/7.5*(x-0.5)+8,-5.5/-0.5*(x-0.5)+8,'+
\
....:
'-5.5/7.5*(x-0.5)+8,-4.5/-0.5*(x-0.5)+8,-4.5/7.5*(x-0.5)+8,-3.5/-0.5*(x-0.5)+8,-3.5/7.5*(x-0.5)+8,-2.5/-0.5*(x-0.5)+8,'+
\
....:
'-2.5/7.5*(x-0.5)+8,-1.5/-0.5*(x-0.5)+8,-1.5/7.5*(x-0.5)+8,-0.5/-0.5*(x-0.5)+8,-0.5/7.5*(x-0.5)+8],'+
\
....: '[x,0,n],[plot_format,gnuplot_pipes],[y, 0, 8],[ylabel,"y"],
[gnuplot_preamble, "set grid xtics ytics"],[legend,false])')
'sage0'
sage:

There is a tmp file containing the above cmd:
$cat /home/lwdrob/.sage/temp/lwdrob_comp/7280/interface/tmp
sage0 :
plot2d([-7.5/-0.5*(x-0.5)+8,-7.5/7.5*(x-0.5)+8,-6.5/-0.5*(x-0.5)+8,-6.5/7.5*(x-0.5)+8,-5.5/-0.5*(x-0.5)+8,
-5.5/7.5*(x-0.5)+8,-4.5/-0.5*(x-0.5)+8,-4.5/7.5*(x-0.5)+8,-3.5/-0.5*(x-0.5)+8,-3.5/7.5*(x-0.5)+8,-2.5/-0.5*(x-0.5)+8,
-2.5/7.5*(x-0.5)+8,-1.5/-0.5*(x-0.5)+8,-1.5/7.5*(x-0.5)+8,-0.5/-0.5*(x-0.5)+8,-0.5/7.5*(x-0.5)+8],
[x,0,n], [plot_format,gnuplot_pipes], [y,0,8],[ylabel,"y"],
[gnuplot_preamble, "set grid xtics ytics"],[legend,false])$

Best regards,
```

The problem is that the maxima interface should not be assigning to a variable when using a file to evaluate a large input. 

William

Issue created by migration from https://trac.sagemath.org/ticket/1660





---

archive/issue_events_004092.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4092"
}
```



---

archive/issue_events_004093.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4093"
}
```



---

archive/issue_events_004094.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4094"
}
```



---

archive/issue_events_004095.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4095"
}
```



---

archive/issue_events_004096.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4096"
}
```



---

archive/issue_events_004097.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4097"
}
```



---

archive/issue_events_004098.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4098"
}
```



---

archive/issue_events_004099.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-06-23T15:19:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4099"
}
```



---

archive/issue_events_004100.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-06-23T15:19:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1660",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1660#event-4100"
}
```
