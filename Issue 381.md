# Issue 381: Sage daemon mode

archive/issues_000381.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: Sage server background process service\n\n```\nOn May 28, 5:11 pm, Marshall Hampton <hampto...@gmail.com> wrote:\n> This is more of a unixy process control question but I am applying it\n> to sage.\n>\n> I would like to start a notebook on my office machine while I am at a\n> conference.  I tried logging in with ssh, starting the notebook,\n> suspending it with ctrl-z, and then putting the suspended process in\n> the background with bg.  This didn't really work, although I could\n> still restart the notebook server with a browser.  I could figure this\n> out eventually but I am hoping someone reading this list already knows\n> how to do this.\n\nThere are several options:\n\n1) use screen - see www.gnu.org/software/screen/\n2) use nohup - see man nohup\n3) use disown - see http://www.faqs.org/docs/bashman/bashref_79.html\n\nAll have their specific advantages, I would just go with screen.\n\nIt might be worthwhile to offer an option for SAGE to demonize itself.\n\nCheers,\nMichael Abshoff\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/381\n\n",
    "closed_at": "2016-06-12T12:02:30Z",
    "created_at": "2007-05-28T21:14:39Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage daemon mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/381",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Keywords: Sage server background process service

```
On May 28, 5:11 pm, Marshall Hampton <hampto...@gmail.com> wrote:
> This is more of a unixy process control question but I am applying it
> to sage.
>
> I would like to start a notebook on my office machine while I am at a
> conference.  I tried logging in with ssh, starting the notebook,
> suspending it with ctrl-z, and then putting the suspended process in
> the background with bg.  This didn't really work, although I could
> still restart the notebook server with a browser.  I could figure this
> out eventually but I am hoping someone reading this list already knows
> how to do this.

There are several options:

1) use screen - see www.gnu.org/software/screen/
2) use nohup - see man nohup
3) use disown - see http://www.faqs.org/docs/bashman/bashref_79.html

All have their specific advantages, I would just go with screen.

It might be worthwhile to offer an option for SAGE to demonize itself.

Cheers,
Michael Abshoff
```

Issue created by migration from https://trac.sagemath.org/ticket/381





---

archive/issue_comments_001836.json:
```json
{
    "body": "```\n\n\nWell, the idea is to detach the running SAGE instance from the shell\nto let it run in the background until it is killed or the system is\nrebooted.\n\nThere is more than one way to do it: For a good C example see\nhttp://www.enderunix.org/docs/eng/daemon.php - for a python example\nsee http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66012\n\nThe python example could be more or less copied (I guess because I am\nnot a python expert), but it should be done very early in the SAGE\nstartup as far as I can tell. Writing a little C wrapper that just\ndoes\n\n i=fork();\n if (i<0) exit(1); /* fork error */\n if (i>0) exit(0); /* parent exits */\n /* child (daemon) continues */\n execv(\"./sage\");\n\nmight be easier.\n```",
    "created_at": "2007-05-28T22:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1836",
    "user": "https://github.com/williamstein"
}
```

```


Well, the idea is to detach the running SAGE instance from the shell
to let it run in the background until it is killed or the system is
rebooted.

There is more than one way to do it: For a good C example see
http://www.enderunix.org/docs/eng/daemon.php - for a python example
see http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66012

The python example could be more or less copied (I guess because I am
not a python expert), but it should be done very early in the SAGE
startup as far as I can tell. Writing a little C wrapper that just
does

 i=fork();
 if (i<0) exit(1); /* fork error */
 if (i>0) exit(0); /* parent exits */
 /* child (daemon) continues */
 execv("./sage");

might be easier.
```



---

archive/issue_comments_001837.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-08-23T11:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_events_000877.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-23T11:20:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-877"
}
```



---

archive/issue_comments_001838.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-23T11:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_000878.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-23T11:20:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-878"
}
```



---

archive/issue_events_000879.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-23T11:20:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-879"
}
```



---

archive/issue_comments_001839.json:
```json
{
    "body": "Look at #7893 ([http://trac.sagemath.org/sage_trac/ticket/7893](http://trac.sagemath.org/sage_trac/ticket/7893)).\n\nIt would be good to incorporate the idea of the example to the script in the previous ticket.",
    "created_at": "2010-10-17T04:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1839",
    "user": "https://github.com/kwankyu"
}
```

Look at #7893 ([http://trac.sagemath.org/sage_trac/ticket/7893](http://trac.sagemath.org/sage_trac/ticket/7893)).

It would be good to incorporate the idea of the example to the script in the previous ticket.



---

archive/issue_comments_001840.json:
```json
{
    "body": "Ping.\n\nThe Sage Installation Guide currently lacks this topic.  (There's only a reference from the [online FAQ](http://wiki.sagemath.org/faq#Other_questions) to *this* ticket.)",
    "created_at": "2012-12-02T16:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1840",
    "user": "https://github.com/nexttime"
}
```

Ping.

The Sage Installation Guide currently lacks this topic.  (There's only a reference from the [online FAQ](http://wiki.sagemath.org/faq#Other_questions) to *this* ticket.)



---

archive/issue_comments_001841.json:
```json
{
    "body": "Changing keywords from \"\" to \"Sage server background process service\".",
    "created_at": "2012-12-02T16:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1841",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "Sage server background process service".



---

archive/issue_comments_001842.json:
```json
{
    "body": "What's wrong with nohup? It does exactly what you want, why add a Sage option to emulate nohup?",
    "created_at": "2013-06-13T12:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1842",
    "user": "https://github.com/jdemeyer"
}
```

What's wrong with nohup? It does exactly what you want, why add a Sage option to emulate nohup?



---

archive/issue_comments_001843.json:
```json
{
    "body": "I think nohup doesn't daemonize.  There is a long list of things that should happen when a process is damonized:\n\n     http://en.wikipedia.org/wiki/Daemon_(computing) \n\nThe right way to solve this problem would almost certainly involve including this Python module:  https://pypi.python.org/pypi/python-daemon/",
    "created_at": "2013-06-13T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1843",
    "user": "https://github.com/williamstein"
}
```

I think nohup doesn't daemonize.  There is a long list of things that should happen when a process is damonized:

     http://en.wikipedia.org/wiki/Daemon_(computing) 

The right way to solve this problem would almost certainly involve including this Python module:  https://pypi.python.org/pypi/python-daemon/



---

archive/issue_comments_001844.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> I think nohup doesn't daemonize.\n\nTrue, `nohup` itself doesn't daemonize. But normally you would do\n\n```\n$ nohup sage -n &\n```\nIt's the `&` at the end which does the \"daemonization\".\n\n> There is a long list of things that should happen when a process is damonized:\n> \n>      http://en.wikipedia.org/wiki/Daemon_(computing) \n\nThis refers to traditional Unix daemons, which would be quite different from a Sage \"daemon\" started by an ordinary user.\n\nSo it's not clear to me what would be needed for a Sage daemon which is not covered by\n\n```\n$ nohup sage &\n```",
    "created_at": "2013-06-13T18:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1844",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:8 was]:
> I think nohup doesn't daemonize.

True, `nohup` itself doesn't daemonize. But normally you would do

```
$ nohup sage -n &
```
It's the `&` at the end which does the "daemonization".

> There is a long list of things that should happen when a process is damonized:
> 
>      http://en.wikipedia.org/wiki/Daemon_(computing) 

This refers to traditional Unix daemons, which would be quite different from a Sage "daemon" started by an ordinary user.

So it's not clear to me what would be needed for a Sage daemon which is not covered by

```
$ nohup sage &
```



---

archive/issue_comments_001845.json:
```json
{
    "body": "> This refers to traditional Unix daemons, which would be quite different from a Sage \"daemon\" started by an ordinary user.\n\n\nI think traditional daemonization is the right way to solve this problem.  Moreover, it would be a useful step for making it easy to run a sage server as part of the usual system-wide daemons on Unix.",
    "created_at": "2013-06-13T18:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1845",
    "user": "https://github.com/williamstein"
}
```

> This refers to traditional Unix daemons, which would be quite different from a Sage "daemon" started by an ordinary user.


I think traditional daemonization is the right way to solve this problem.  Moreover, it would be a useful step for making it easy to run a sage server as part of the usual system-wide daemons on Unix.



---

archive/issue_comments_001846.json:
```json
{
    "body": "Replying to [comment:10 was]:\n> it would be a useful step for making it easy to run a sage server as part of the usual system-wide daemons on Unix. \n\nWhich is #7893, this ticket seems to be about single-user use.",
    "created_at": "2013-06-13T18:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1846",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:10 was]:
> it would be a useful step for making it easy to run a sage server as part of the usual system-wide daemons on Unix. 

Which is #7893, this ticket seems to be about single-user use.



---

archive/issue_comments_001847.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> Replying to [comment:8 was]:\n> > I think nohup doesn't daemonize.\n\n> True, `nohup` itself doesn't daemonize. But normally you would do\n> {{{\n> $ nohup sage -n &\n> }}}\n> It's the `&` at the end which does the \"daemonization\".\n> \n> > There is a long list of things that should happen when a process is damonized:\n> > \n> >      http://en.wikipedia.org/wiki/Daemon_(computing) \n\n> This refers to traditional Unix daemons, which would be quite different from a Sage \"daemon\" started by an ordinary user.\n> \n> So it's not clear to me what would be needed for a Sage daemon which is not covered by\n> \n> ```\n> $ nohup sage &\n> ```\n\n\nWell, you'd at least also have to `>/dev/null`.\n\nInherited file descriptors other than 0, 1 and 2 are left untouched.\n\n`nohup` doesn't change the working directory, nor e.g. modify the umask.\n\nThe background process doesn't get adopted by `init` until you logout, and similar process group specific stuff I think.\n\n(...)",
    "created_at": "2013-06-13T18:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1847",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 was]:
> > I think nohup doesn't daemonize.

> True, `nohup` itself doesn't daemonize. But normally you would do
> {{{
> $ nohup sage -n &
> }}}
> It's the `&` at the end which does the "daemonization".
> 
> > There is a long list of things that should happen when a process is damonized:
> > 
> >      http://en.wikipedia.org/wiki/Daemon_(computing) 

> This refers to traditional Unix daemons, which would be quite different from a Sage "daemon" started by an ordinary user.
> 
> So it's not clear to me what would be needed for a Sage daemon which is not covered by
> 
> ```
> $ nohup sage &
> ```


Well, you'd at least also have to `>/dev/null`.

Inherited file descriptors other than 0, 1 and 2 are left untouched.

`nohup` doesn't change the working directory, nor e.g. modify the umask.

The background process doesn't get adopted by `init` until you logout, and similar process group specific stuff I think.

(...)



---

archive/issue_events_000880.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-880"
}
```



---

archive/issue_events_000881.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-881"
}
```



---

archive/issue_events_000882.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-882"
}
```



---

archive/issue_events_000883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-883"
}
```



---

archive/issue_events_000884.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-884"
}
```



---

archive/issue_events_000885.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-885"
}
```



---

archive/issue_events_000886.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-886"
}
```



---

archive/issue_events_000887.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-887"
}
```



---

archive/issue_comments_001848.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-23T04:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1848",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001849.json:
```json
{
    "body": "The problem that this ticket deals with is nowadays solved by using the OS tools such as Upstart in Ubuntu for example. So I think there needs no further discussion on this matter.",
    "created_at": "2016-03-23T04:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1849",
    "user": "https://github.com/kwankyu"
}
```

The problem that this ticket deals with is nowadays solved by using the OS tools such as Upstart in Ubuntu for example. So I think there needs no further discussion on this matter.



---

archive/issue_events_000888.json:
```json
{
    "actor": "https://github.com/kwankyu",
    "created_at": "2016-03-23T04:38:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-888"
}
```



---

archive/issue_events_000889.json:
```json
{
    "actor": "https://github.com/kwankyu",
    "created_at": "2016-03-23T04:38:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-889"
}
```



---

archive/issue_comments_001850.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-16T18:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1850",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_000890.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-06-12T12:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/381#event-890"
}
```



---

archive/issue_comments_001851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/381#issuecomment-1851",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
