# Issue 6772: increase default ecl memory limits for maxima+ecl in sage

archive/issues_006772.json:
```json
{
    "body": "Assignee: mabshoff\n\nExample:\n\n```\nHere's a simpler example to get this error:\n\nsage: m = maxima(2*10^6)\nsage: time n=m.factorial()\nMaxima encountered a Lisp error:\nMemory limit reached. Please jump to an outer point or quit program.\n\nOr, directly in Maxima:\n\n(%i3) n : factorial(10^7);\nGC Warning: Out of Memory!  Returning NIL!\nMaxima encountered a Lisp error:\n Memory limit reached. Please jump to an outer point or quit program.\nAutomatically continuing.\nTo reenable the Lisp debugger set *debugger-hook* to nil.\n```\n\n\nAnd the response from the main ECL guy:\n\n\n```\nOn Mon, Aug 17, 2009 at 10:57 AM, William Stein<wstein@gmail.com> wrote:\n> Note that Sage's Maxima uses ECL.  So the basic question is, how can\n> we increase the memory that Maxima + ECL can use?\n\nThe limits ECL has are by default too small for big applications, but\nit is intentionally done so. However, changing them is pretty easy:\nadd a call to ext:set-limit in any file of maxima that forms part of\nthe final executable.\n\nThe different memory limits that can be independently controlled are listed here\n    http://ecls.sourceforge.net/new-manual/re34.html\nSo for instance, in your case, which hits the dynamically allocated\nmemory limit, you might add the following\n    (ext:set-limit 'ext:heap-size (* 1024 1024 1024))\nto maxima/src/ecl-port.lisp in order get 1GB memory limit.\n\nJuanjo\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6772\n\n",
    "created_at": "2009-08-17T09:30:40Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "increase default ecl memory limits for maxima+ecl in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6772",
    "user": "was"
}
```
Assignee: mabshoff

Example:

```
Here's a simpler example to get this error:

sage: m = maxima(2*10^6)
sage: time n=m.factorial()
Maxima encountered a Lisp error:
Memory limit reached. Please jump to an outer point or quit program.

Or, directly in Maxima:

(%i3) n : factorial(10^7);
GC Warning: Out of Memory!  Returning NIL!
Maxima encountered a Lisp error:
 Memory limit reached. Please jump to an outer point or quit program.
Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
```


And the response from the main ECL guy:


```
On Mon, Aug 17, 2009 at 10:57 AM, William Stein<wstein@gmail.com> wrote:
> Note that Sage's Maxima uses ECL.  So the basic question is, how can
> we increase the memory that Maxima + ECL can use?

The limits ECL has are by default too small for big applications, but
it is intentionally done so. However, changing them is pretty easy:
add a call to ext:set-limit in any file of maxima that forms part of
the final executable.

The different memory limits that can be independently controlled are listed here
    http://ecls.sourceforge.net/new-manual/re34.html
So for instance, in your case, which hits the dynamically allocated
memory limit, you might add the following
    (ext:set-limit 'ext:heap-size (* 1024 1024 1024))
to maxima/src/ecl-port.lisp in order get 1GB memory limit.

Juanjo

```



Issue created by migration from https://trac.sagemath.org/ticket/6772





---

archive/issue_comments_055758.json:
```json
{
    "body": "\n```\n> My understanding is that one has to modify the maxima source code\n> itself and recompile maxima.\n\nNot so -- EXT:SET-LIMIT can be called anytime after the\nMaxima session is launched.\nTo evaluate a single Lisp expression in Maxima:\n\n:lisp (ext:set-limit 'ext:heap-size <whatever>)\n\nRobert Dodier\n```\n",
    "created_at": "2009-08-18T18:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55758",
    "user": "was"
}
```


```
> My understanding is that one has to modify the maxima source code
> itself and recompile maxima.

Not so -- EXT:SET-LIMIT can be called anytime after the
Maxima session is launched.
To evaluate a single Lisp expression in Maxima:

:lisp (ext:set-limit 'ext:heap-size <whatever>)

Robert Dodier
```




---

archive/issue_comments_055759.json:
```json
{
    "body": "Maxima changed so that big factorials are symbolic (which is bizarre, but anyways...), so the above example no longer works.  The following does work:\n\n```\nsage: a = maxima(10)^(10^5)\nsage: b = a^600\nBoom!\n```\n\n\nI suggest the way to fix this problem is to add this line to the startup of code for the Maxima interface:\n\n```\nmaxima._eval_line(\":lisp (ext:set-limit 'ext:heap-size 100000000000)\", \nwait_for_prompt=False)\n```\n",
    "created_at": "2009-11-16T16:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55759",
    "user": "was"
}
```

Maxima changed so that big factorials are symbolic (which is bizarre, but anyways...), so the above example no longer works.  The following does work:

```
sage: a = maxima(10)^(10^5)
sage: b = a^600
Boom!
```


I suggest the way to fix this problem is to add this line to the startup of code for the Maxima interface:

```
maxima._eval_line(":lisp (ext:set-limit 'ext:heap-size 100000000000)", 
wait_for_prompt=False)
```




---

archive/issue_comments_055760.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-16T16:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55760",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055761.json:
```json
{
    "body": "Even better:\n\n```\nself._sendline(\":lisp (ext:set-limit 'ext:heap-size 0)\")\n```\n\n\nThe above appears to make the heap unlimited.",
    "created_at": "2009-11-16T16:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55761",
    "user": "was"
}
```

Even better:

```
self._sendline(":lisp (ext:set-limit 'ext:heap-size 0)")
```


The above appears to make the heap unlimited.



---

archive/issue_comments_055762.json:
```json
{
    "body": "Attachment [trac_6772.patch](tarball://root/attachments/some-uuid/ticket6772/trac_6772.patch) by nbruin created at 2009-11-16 20:57:34\n\nReplying to [comment:3 was]:\n> The above appears to make the heap unlimited.\n\nSomeone should check how Boehm decides if it should extend the heap area or try to reclaim garbage and reuse memory. A side-effect of removing a limit could be that ECL just keeps allocating more memory until everything is used up, before garbage collecting. Other processes might not like that too much.\n\nI guess a sanity check would be to try some long computation that is supposed to use constant memory and see if ext:set-limit influences the memory footprint.",
    "created_at": "2009-11-16T20:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55762",
    "user": "nbruin"
}
```

Attachment [trac_6772.patch](tarball://root/attachments/some-uuid/ticket6772/trac_6772.patch) by nbruin created at 2009-11-16 20:57:34

Replying to [comment:3 was]:
> The above appears to make the heap unlimited.

Someone should check how Boehm decides if it should extend the heap area or try to reclaim garbage and reuse memory. A side-effect of removing a limit could be that ECL just keeps allocating more memory until everything is used up, before garbage collecting. Other processes might not like that too much.

I guess a sanity check would be to try some long computation that is supposed to use constant memory and see if ext:set-limit influences the memory footprint.



---

archive/issue_comments_055763.json:
```json
{
    "body": "Replying to [comment:4 nbruin]:\n> Replying to [comment:3 was]:\n> > The above appears to make the heap unlimited.\n> \n> Someone should check how Boehm decides if it should extend \n> the heap area or try to reclaim garbage and reuse memory. \n> A side-effect of removing a limit could be that ECL just \n> keeps allocating more memory until everything is used up, \n> before garbage collecting. Other processes might not like that too much.\n\nThat would be really annoying. There's only one program I know that is that annoying -- PARI. Fortunately, that does not seem to be what happens here. \n\nI tried the following while watching top:\n\n```\nsage: maxima._eval_line(\":lisp (ext:set-limit 'ext:heap-size 100000000000)\",wait_for_prompt=False)\nsage: sage: a = maxima(10)^(10^5)\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\nsage: sage: b = a^600\n```\n\nThe memory usage initially goes up from 50MB to 415MB, but then stays at 415MB ever after.",
    "created_at": "2009-11-17T15:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55763",
    "user": "was"
}
```

Replying to [comment:4 nbruin]:
> Replying to [comment:3 was]:
> > The above appears to make the heap unlimited.
> 
> Someone should check how Boehm decides if it should extend 
> the heap area or try to reclaim garbage and reuse memory. 
> A side-effect of removing a limit could be that ECL just 
> keeps allocating more memory until everything is used up, 
> before garbage collecting. Other processes might not like that too much.

That would be really annoying. There's only one program I know that is that annoying -- PARI. Fortunately, that does not seem to be what happens here. 

I tried the following while watching top:

```
sage: maxima._eval_line(":lisp (ext:set-limit 'ext:heap-size 100000000000)",wait_for_prompt=False)
sage: sage: a = maxima(10)^(10^5)
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
```

The memory usage initially goes up from 50MB to 415MB, but then stays at 415MB ever after.



---

archive/issue_comments_055764.json:
```json
{
    "body": "I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.",
    "created_at": "2009-11-18T17:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55764",
    "user": "kcrisman"
}
```

I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.



---

archive/issue_comments_055765.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.\n\nI bet you are on a 32 bit machine then, because Log(100000000000)/Log(2)=36.54\n\nAccording to\n\nhttp://ecls.sourceforge.net/new-manual/re30.html\n\nsetting a limit to 0 should indeed mean \"no limit\". If that is our intention then that would be more portable than 100000000000.\nFor safety, 2GB might not be an unreasonable limit, though. When people are debugging they might want to enforce a lower limit to see the crash sooner.",
    "created_at": "2009-11-27T21:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55765",
    "user": "nbruin"
}
```

Replying to [comment:6 kcrisman]:
> I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.

I bet you are on a 32 bit machine then, because Log(100000000000)/Log(2)=36.54

According to

http://ecls.sourceforge.net/new-manual/re30.html

setting a limit to 0 should indeed mean "no limit". If that is our intention then that would be more portable than 100000000000.
For safety, 2GB might not be an unreasonable limit, though. When people are debugging they might want to enforce a lower limit to see the crash sooner.



---

archive/issue_comments_055766.json:
```json
{
    "body": "Replying to [comment:7 nbruin]:\n> Replying to [comment:6 kcrisman]:\n> > I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.\n> \n> I bet you are on a 32 bit machine then, because Log(100000000000)/Log(2)=36.54\n\nYes, you are correct.",
    "created_at": "2009-11-28T04:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55766",
    "user": "kcrisman"
}
```

Replying to [comment:7 nbruin]:
> Replying to [comment:6 kcrisman]:
> > I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.
> 
> I bet you are on a 32 bit machine then, because Log(100000000000)/Log(2)=36.54

Yes, you are correct.



---

archive/issue_comments_055767.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-27T15:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55767",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_055768.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-27T15:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55768",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T18:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6772#issuecomment-55769",
    "user": "mhansen"
}
```

Resolution: fixed
