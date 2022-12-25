# Issue 3836: notebook interact -- make it so one control can depend on others

archive/issues_003836.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @TimDumol @qed777 @jasongrout\n\n```\n\nI really like the @interact functionality! I'm trying to do something\nlike this:\n\n@interact\ndef _(p=5,q=range(p)):\n   ...\n\nSo I'd like the range of q to depend on the current value of p. This\ndoesn't seem to be possible. Is there any way to make it work?\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3836\n\n",
    "created_at": "2008-08-13T16:12:38Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "notebook interact -- make it so one control can depend on others",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3836",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @TimDumol @qed777 @jasongrout

```

I really like the @interact functionality! I'm trying to do something
like this:

@interact
def _(p=5,q=range(p)):
   ...

So I'd like the range of q to depend on the current value of p. This
doesn't seem to be possible. Is there any way to make it work?
```

Issue created by migration from https://trac.sagemath.org/ticket/3836





---

archive/issue_comments_027214.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2008-09-09T19:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3836#issuecomment-27214",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing component from notebook to interact.



---

archive/issue_comments_027215.json:
```json
{
    "body": "Changing assignee from boothby to @itolkov.",
    "created_at": "2008-09-09T19:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3836#issuecomment-27215",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from boothby to @itolkov.



---

archive/issue_comments_027216.json:
```json
{
    "body": "Here is another request from [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a0292dca53c3be16/682f8ae33df29761?show_docid=682f8ae33df29761) which seems very similar.\n\nI want to know if there is any way to \"create\" new buttons while \nalready in execution. \n\nThis is a testing code i wrote (of course, just for testing \npurposes :P) \n\n```\n@interact \ndef _(n1=input_box(0,label='Testing', type=int),a=selector([1,2,7], \nbuttons=True), n2=input_box(1,label='Testing2',type=int), \njuega=input_box(0,label='Testing3',type=int)): \n    if(n1>0): \n        print 'hi' \n        another_function() \ndef another_function(t1=input_box(0,label='Testing123')): \n    print 'hola' \n```\nThing is, when i run it, i can get it to print 'Hola' but no input_box \nis created again. I've managed to \"make\" one using html, but i can't \nget to \"interact\" with it. \n\nWhat i'm thinking on doing is a program that has several options using \na selector, e.g. if you choose 1 then it should appear a grid so that \nwhen u enter matrix values it does some calcs, if you choose 2 then it \nshould appear an input box, and so on...",
    "created_at": "2009-10-21T15:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3836#issuecomment-27216",
    "user": "https://github.com/kcrisman"
}
```

Here is another request from [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a0292dca53c3be16/682f8ae33df29761?show_docid=682f8ae33df29761) which seems very similar.

I want to know if there is any way to "create" new buttons while 
already in execution. 

This is a testing code i wrote (of course, just for testing 
purposes :P) 

```
@interact 
def _(n1=input_box(0,label='Testing', type=int),a=selector([1,2,7], 
buttons=True), n2=input_box(1,label='Testing2',type=int), 
juega=input_box(0,label='Testing3',type=int)): 
    if(n1>0): 
        print 'hi' 
        another_function() 
def another_function(t1=input_box(0,label='Testing123')): 
    print 'hola' 
```
Thing is, when i run it, i can get it to print 'Hola' but no input_box 
is created again. I've managed to "make" one using html, but i can't 
get to "interact" with it. 

What i'm thinking on doing is a program that has several options using 
a selector, e.g. if you choose 1 then it should appear a grid so that 
when u enter matrix values it does some calcs, if you choose 2 then it 
should appear an input box, and so on...



---

archive/issue_comments_027217.json:
```json
{
    "body": "Turns out that this is going to be available once it makes its way back from the single-cell server code!  See [this ask.sagemath.org question](http://ask.sagemath.org/question/1061/), in particular Jason's answer.",
    "created_at": "2012-01-17T23:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3836#issuecomment-27217",
    "user": "https://github.com/kcrisman"
}
```

Turns out that this is going to be available once it makes its way back from the single-cell server code!  See [this ask.sagemath.org question](http://ask.sagemath.org/question/1061/), in particular Jason's answer.



---

archive/issue_events_008783.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8783"
}
```



---

archive/issue_events_008784.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8784"
}
```



---

archive/issue_events_008785.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8785"
}
```



---

archive/issue_events_008786.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8786"
}
```



---

archive/issue_events_008787.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8787"
}
```



---

archive/issue_events_008788.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8788"
}
```



---

archive/issue_events_008789.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3836#event-8789"
}
```



---

archive/issue_comments_027218.json:
```json
{
    "body": "This can be done in Jupyter, using traitlets links.",
    "created_at": "2017-03-21T11:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3836#issuecomment-27218",
    "user": "https://github.com/jdemeyer"
}
```

This can be done in Jupyter, using traitlets links.
