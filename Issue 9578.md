# Issue 9578: Add even more customization of ticks in plots

archive/issues_009578.json:
```json
{
    "body": "Assignee: jason, was\n\nSuch as arbitrary ticks, color... Here are some hints for this from [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/64aee5700d4f7ff4/34a82a725be9e2a5?show_docid=34a82a725be9e2a5)\n\n```\n> I figure with some polishing it could go into Sage. Part of that \n> polishing would require to figure out how one can make \n> sage: pylab.clf() \n> sage: _ = pylab.pcolor(pylab.rand(2,2)) \n> sage: pylab.savefig('foo.png',dpi=96) \n> not print out indices for x and y from 0 to n but from a to b. I \n> couldn't figure this out. Maybe someone on this list knows from the \n> top of the head? \n\n\nHere's one way to do it, just by changing the tick labels.  There are \nother more flexible ways too: \nsage: import pylab \nsage: pylab.clf() \nsage: p = pylab.pcolor(pylab.rand(2,2)) \nsage: p.axes.get_xticks() # see what ticks are in the plot \narray([ 0. ,  0.5,  1. ,  1.5,  2. ]) \nsage: _=p.axes.set_xticklabels(['0','1000','2000','3000','4000']) \nsage: pylab.savefig('foo.png',dpi=96) \nOr if you just want to multiply each tick label by a certain amount: \nsage: _=p.axes.set_xticklabels([str(i) for i in 1000*p.axes.get_xticks()]) \nsage: pylab.savefig('foo.png',dpi=96) \nThanks, \nJason \n```\nand\n\n```\nYes, I think it would be pretty easy.  Note that matplotlib just added \nsome nice convenience functions for dealing with changing the styles of \nticks too, so we could easy change the colors or weights or whatever as \nwell. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9578\n\n",
    "created_at": "2010-07-23T01:55:04Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add even more customization of ticks in plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9578",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

Such as arbitrary ticks, color... Here are some hints for this from [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/64aee5700d4f7ff4/34a82a725be9e2a5?show_docid=34a82a725be9e2a5)

```
> I figure with some polishing it could go into Sage. Part of that 
> polishing would require to figure out how one can make 
> sage: pylab.clf() 
> sage: _ = pylab.pcolor(pylab.rand(2,2)) 
> sage: pylab.savefig('foo.png',dpi=96) 
> not print out indices for x and y from 0 to n but from a to b. I 
> couldn't figure this out. Maybe someone on this list knows from the 
> top of the head? 


Here's one way to do it, just by changing the tick labels.  There are 
other more flexible ways too: 
sage: import pylab 
sage: pylab.clf() 
sage: p = pylab.pcolor(pylab.rand(2,2)) 
sage: p.axes.get_xticks() # see what ticks are in the plot 
array([ 0. ,  0.5,  1. ,  1.5,  2. ]) 
sage: _=p.axes.set_xticklabels(['0','1000','2000','3000','4000']) 
sage: pylab.savefig('foo.png',dpi=96) 
Or if you just want to multiply each tick label by a certain amount: 
sage: _=p.axes.set_xticklabels([str(i) for i in 1000*p.axes.get_xticks()]) 
sage: pylab.savefig('foo.png',dpi=96) 
Thanks, 
Jason 
```
and

```
Yes, I think it would be pretty easy.  Note that matplotlib just added 
some nice convenience functions for dealing with changing the styles of 
ticks too, so we could easy change the colors or weights or whatever as 
well. 
```

Issue created by migration from https://trac.sagemath.org/ticket/9578





---

archive/issue_comments_092360.json:
```json
{
    "body": "#1431 and #2189 are also relevant.",
    "created_at": "2010-07-23T01:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9578#issuecomment-92360",
    "user": "https://github.com/kcrisman"
}
```

#1431 and #2189 are also relevant.



---

archive/issue_comments_092361.json:
```json
{
    "body": "We have arbitrary ticks now, and some formatting.  Since this is a little vague, I'm making it be about color.\n\nSee also #13078.",
    "created_at": "2012-07-07T03:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9578#issuecomment-92361",
    "user": "https://github.com/kcrisman"
}
```

We have arbitrary ticks now, and some formatting.  Since this is a little vague, I'm making it be about color.

See also #13078.



---

archive/issue_events_023851.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23851"
}
```



---

archive/issue_events_023852.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23852"
}
```



---

archive/issue_events_023853.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23853"
}
```



---

archive/issue_events_023854.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23854"
}
```



---

archive/issue_events_023855.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23855"
}
```



---

archive/issue_events_023856.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23856"
}
```



---

archive/issue_events_023857.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9578",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9578#event-23857"
}
```
