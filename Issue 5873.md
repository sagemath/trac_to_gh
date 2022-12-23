# Issue 5873: [with patch, needs review] Fix matplotlib build on FreeBSD

archive/issues_005873.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jason stephen\n\n1) Explicitly add SAGE_LOCAL to the dependency search path for matplotlib for FreeBSD.\n\n2) gcc-4.3 on FreeBSD (though not the base gcc4.2) appears to define putchar() in <stdio.h> in a way that breaks the putchar() definitions inside ttconv.  It's not immediately clear what the problem is (since there's no immediately obvious difference in the way putchar() is defined in <stdio.h>) so this patch takes\nthe easy way out and undef's the offending putchar() macro.\n\n3) Individual character bounding boxes in AFM files do not have to be integral so convert each bounding box to a list of floats, rather than a list of ints. This corrects a problem where most of the tests would fail with \"ValueError: invalid literal for int() with base 10: '539.621'\" on FreeBSD.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5873\n\n",
    "created_at": "2009-04-23T08:43:34Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Fix matplotlib build on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5873",
    "user": "pjeremy"
}
```
Assignee: mabshoff

CC:  jason stephen

1) Explicitly add SAGE_LOCAL to the dependency search path for matplotlib for FreeBSD.

2) gcc-4.3 on FreeBSD (though not the base gcc4.2) appears to define putchar() in <stdio.h> in a way that breaks the putchar() definitions inside ttconv.  It's not immediately clear what the problem is (since there's no immediately obvious difference in the way putchar() is defined in <stdio.h>) so this patch takes
the easy way out and undef's the offending putchar() macro.

3) Individual character bounding boxes in AFM files do not have to be integral so convert each bounding box to a list of floats, rather than a list of ints. This corrects a problem where most of the tests would fail with "ValueError: invalid literal for int() with base 10: '539.621'" on FreeBSD.

Issue created by migration from https://trac.sagemath.org/ticket/5873





---

archive/issue_comments_046377.json:
```json
{
    "body": "Attachment\n\nOf course, this should be added to the current matplotlib spkg.",
    "created_at": "2009-09-22T19:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46377",
    "user": "jason"
}
```

Attachment

Of course, this should be added to the current matplotlib spkg.



---

archive/issue_comments_046378.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-03T09:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46378",
    "user": "pjeremy"
}
```

Attachment



---

archive/issue_comments_046379.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-03T09:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46379",
    "user": "pjeremy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046380.json:
```json
{
    "body": "5873.matplotlib.patch has been updated for matplotlib-0.99.1.p2.  Of the patches mentioned in the original description, only the first part remains (and is still necessary).\n\nThe second part (related to putchar problems with gcc43) has been removed as it's no longer practical to build Sage with gcc43 on FreeBSD.\n\nThe third part (related to bounding box conversions) has been removed as an equivalent patch has been integrated into matplotlib-0.99.1",
    "created_at": "2010-01-03T09:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46380",
    "user": "pjeremy"
}
```

5873.matplotlib.patch has been updated for matplotlib-0.99.1.p2.  Of the patches mentioned in the original description, only the first part remains (and is still necessary).

The second part (related to putchar problems with gcc43) has been removed as it's no longer practical to build Sage with gcc43 on FreeBSD.

The third part (related to bounding box conversions) has been removed as an equivalent patch has been integrated into matplotlib-0.99.1



---

archive/issue_comments_046381.json:
```json
{
    "body": "The matplotlib spkg up at #9202 should take care of the remaining issue in this patch (by prepending the SAGE_LOCAL directory no matter what the platform).  Can you check to see if #9202 fixes things?",
    "created_at": "2010-06-11T06:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46381",
    "user": "jason"
}
```

The matplotlib spkg up at #9202 should take care of the remaining issue in this patch (by prepending the SAGE_LOCAL directory no matter what the platform).  Can you check to see if #9202 fixes things?



---

archive/issue_comments_046382.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> The matplotlib spkg up at #9202 should take care of the remaining issue in this patch (by prepending the SAGE_LOCAL directory no matter what the platform).  Can you check to see if #9202 fixes things?\n\nAny thoughts about this Peter? I noticed you created (or at least edited) a wiki page about the FreeBSD port, and still reference this old patch, which is probably no longer needed. \n\nDave",
    "created_at": "2010-07-13T10:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46382",
    "user": "drkirkby"
}
```

Replying to [comment:3 jason]:
> The matplotlib spkg up at #9202 should take care of the remaining issue in this patch (by prepending the SAGE_LOCAL directory no matter what the platform).  Can you check to see if #9202 fixes things?

Any thoughts about this Peter? I noticed you created (or at least edited) a wiki page about the FreeBSD port, and still reference this old patch, which is probably no longer needed. 

Dave



---

archive/issue_comments_046383.json:
```json
{
    "body": "Unfortunately, a variant of this patch is still needed to support FreeBSD later than FreeBSD6.  Whilst #9202 means prepending SAGE_LOCAL should no longer be necessary, additional OS-related lines are still needed to support recent versions of FreeBSD.",
    "created_at": "2010-07-13T19:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46383",
    "user": "pjeremy"
}
```

Unfortunately, a variant of this patch is still needed to support FreeBSD later than FreeBSD6.  Whilst #9202 means prepending SAGE_LOCAL should no longer be necessary, additional OS-related lines are still needed to support recent versions of FreeBSD.



---

archive/issue_comments_046384.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-13T19:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46384",
    "user": "pjeremy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046385.json:
```json
{
    "body": "Replying to [comment:5 pjeremy]:\n> Unfortunately, a variant of this patch is still needed to support FreeBSD later than FreeBSD6.  Whilst #9202 means prepending SAGE_LOCAL should no longer be necessary, additional OS-related lines are still needed to support recent versions of FreeBSD.\n\nIf you wish to create one, I'll try to review it reasonably quickly. It makes review a lot easier if you can include things inside \n\n\n``` \n#ifdef FREEBSD \n#endif\n```\n\n\nor if appropriate \n\n\n```\n#ifdef HAVE_BUGGY_GCC_ON_FREEBSD\n#undef putchar\n#endif\n```\n\nor similar. Otherwise, it requires the reviewer to have a much deeper knowledge of the code to evaluate if the changes are desirable or not. If it can be seen the changes only affect FreeBSD, then it will be much easier to get a positive review. That's been my experience with Solaris and OpenSolaris related problems. \n\n\n\nDave",
    "created_at": "2010-07-13T20:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46385",
    "user": "drkirkby"
}
```

Replying to [comment:5 pjeremy]:
> Unfortunately, a variant of this patch is still needed to support FreeBSD later than FreeBSD6.  Whilst #9202 means prepending SAGE_LOCAL should no longer be necessary, additional OS-related lines are still needed to support recent versions of FreeBSD.

If you wish to create one, I'll try to review it reasonably quickly. It makes review a lot easier if you can include things inside 


``` 
#ifdef FREEBSD 
#endif
```


or if appropriate 


```
#ifdef HAVE_BUGGY_GCC_ON_FREEBSD
#undef putchar
#endif
```

or similar. Otherwise, it requires the reviewer to have a much deeper knowledge of the code to evaluate if the changes are desirable or not. If it can be seen the changes only affect FreeBSD, then it will be much easier to get a positive review. That's been my experience with Solaris and OpenSolaris related problems. 



Dave



---

archive/issue_comments_046386.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-17T20:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46386",
    "user": "pjeremy"
}
```

Attachment



---

archive/issue_comments_046387.json:
```json
{
    "body": "Point 0 has been reported upstream as https://sourceforge.net/tracker/?func=detail&aid=3031051&group_id=80706&atid=560722 and an updated patch (not yet converted to spkg) uploaded.",
    "created_at": "2010-07-17T20:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46387",
    "user": "pjeremy"
}
```

Point 0 has been reported upstream as https://sourceforge.net/tracker/?func=detail&aid=3031051&group_id=80706&atid=560722 and an updated patch (not yet converted to spkg) uploaded.



---

archive/issue_comments_046388.json:
```json
{
    "body": "Replying to [comment:7 pjeremy]:\n> Point 0 has been reported upstream as https://sourceforge.net/tracker/?func=detail&aid=3031051&group_id=80706&atid=560722 and an updated patch (not yet converted to spkg) uploaded.\nUnfortunately, this link no longer works, as matplotlib has moved its bug tracker to Github.  Pleasantly, the [ticket](https://github.com/matplotlib/matplotlib/issues/225) is still there.  Sadly, the patch appears to have been lost there, though it's still here.",
    "created_at": "2011-08-19T16:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46388",
    "user": "kcrisman"
}
```

Replying to [comment:7 pjeremy]:
> Point 0 has been reported upstream as https://sourceforge.net/tracker/?func=detail&aid=3031051&group_id=80706&atid=560722 and an updated patch (not yet converted to spkg) uploaded.
Unfortunately, this link no longer works, as matplotlib has moved its bug tracker to Github.  Pleasantly, the [ticket](https://github.com/matplotlib/matplotlib/issues/225) is still there.  Sadly, the patch appears to have been lost there, though it's still here.



---

archive/issue_comments_046389.json:
```json
{
    "body": "Apparently Stephen Montgomery-Smith has gotten matplotlib [to build fine](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/) for Sage in the meantime, or possibly using a system matplotlib.",
    "created_at": "2012-01-31T01:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46389",
    "user": "kcrisman"
}
```

Apparently Stephen Montgomery-Smith has gotten matplotlib [to build fine](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/) for Sage in the meantime, or possibly using a system matplotlib.



---

archive/issue_comments_046390.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2012-06-20T15:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46390",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_046391.json:
```json
{
    "body": "More success with [this thread](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/yPGIKHRSANs).  Checking whether system variant or Sage version.",
    "created_at": "2012-06-20T15:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46391",
    "user": "kcrisman"
}
```

More success with [this thread](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/yPGIKHRSANs).  Checking whether system variant or Sage version.



---

archive/issue_comments_046392.json:
```json
{
    "body": "Some of the reason this is unnecessary is probably due to the upgrades in gcc.\n\nI don't understand, though, why the patch for newer FreeBSD is no longer necessary.  [The current mpl source (June 2012)](https://github.com/matplotlib/matplotlib/blob/master/setupext.py#L70) does not have it incorporated.\n\nThis is weird enough that I'm not putting positive review; it seems like there should be a key error at [this spot](https://github.com/matplotlib/matplotlib/blob/master/setupext.py#L184) if we don't have something in the dictionary for this system.",
    "created_at": "2012-06-20T18:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46392",
    "user": "kcrisman"
}
```

Some of the reason this is unnecessary is probably due to the upgrades in gcc.

I don't understand, though, why the patch for newer FreeBSD is no longer necessary.  [The current mpl source (June 2012)](https://github.com/matplotlib/matplotlib/blob/master/setupext.py#L70) does not have it incorporated.

This is weird enough that I'm not putting positive review; it seems like there should be a key error at [this spot](https://github.com/matplotlib/matplotlib/blob/master/setupext.py#L184) if we don't have something in the dictionary for this system.



---

archive/issue_comments_046393.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-06-20T18:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46393",
    "user": "kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_046394.json:
```json
{
    "body": "I just wanted to chime in with the reason that the patch for newer FreeBSD was not necessary on FreeBSD itself, is because their ports tree incorporates it itself downstream. So that's the reason it is not in the current MPL source (we haven't heard enough people building it natively complain, they were probably using the system variant).\n\nAs it stands, either [MPL PR #982](https://github.com/matplotlib/matplotlib/pull/982) or [MPL PR #985](https://github.com/matplotlib/matplotlib/pull/985) will make this a non-issue (and you can grab either of those patches in the meantime, they will both also work for FreeBSD10, and MPL !#985 will work for any other future releases, as well any other POSIX systems that got left out.",
    "created_at": "2012-07-03T08:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46394",
    "user": "pi"
}
```

I just wanted to chime in with the reason that the patch for newer FreeBSD was not necessary on FreeBSD itself, is because their ports tree incorporates it itself downstream. So that's the reason it is not in the current MPL source (we haven't heard enough people building it natively complain, they were probably using the system variant).

As it stands, either [MPL PR #982](https://github.com/matplotlib/matplotlib/pull/982) or [MPL PR #985](https://github.com/matplotlib/matplotlib/pull/985) will make this a non-issue (and you can grab either of those patches in the meantime, they will both also work for FreeBSD10, and MPL !#985 will work for any other future releases, as well any other POSIX systems that got left out.



---

archive/issue_comments_046395.json:
```json
{
    "body": "Thanks for this info.  Strange, though, because the testing in question was not using the system mpl, as far as I know.\n\nStephen, any thoughts on this?  We *could* make a custom spkg with one of these patches.",
    "created_at": "2012-07-03T13:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46395",
    "user": "kcrisman"
}
```

Thanks for this info.  Strange, though, because the testing in question was not using the system mpl, as far as I know.

Stephen, any thoughts on this?  We *could* make a custom spkg with one of these patches.



---

archive/issue_comments_046396.json:
```json
{
    "body": "I am going to have to say that I don't know why the FreeBSD port of sage doesn't build without this patch.  I looked at the FreeBSD port of matplotlib, and this patch was included there.  I just don't understand what is going on.  Let me look into it some more.",
    "created_at": "2012-07-03T18:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46396",
    "user": "stephen"
}
```

I am going to have to say that I don't know why the FreeBSD port of sage doesn't build without this patch.  I looked at the FreeBSD port of matplotlib, and this patch was included there.  I just don't understand what is going on.  Let me look into it some more.



---

archive/issue_comments_046397.json:
```json
{
    "body": "TLDR: you don't need this patch.\n\nThe mpl `setupext.py` code in question gets used when there is not an entry for `basedirlist` in `setup.cfg`, in which case it'll grab it from this pre-defined `basedir` dictionary using `sys.platform` as they key. From what I see that's checked into hg for SAGE, you do define `basedirlist` in `setup.cfg`, which is why this patch is un-necessary. The code is in the SPKG `matplotlib.../make-setup-config.py:7`\n\n\n\n```\nconfig.set('directories', 'basedirlist', os.environ['SAGE_LOCAL'])\n```\n\n\n\nwhich is why this patch is not needed for SPKG matplotlib being built on **any** platform.\n\nFrom what I understand from the discussion at [Python Bug #12326](http://bugs.python.org/issue12326), it seems like we (MPL) should not have been using `sys.platform` in the first place for making these decisions (but given the somewhat exotic nature of the platforms which have exceptions there now, it's best to remain conservative about re-writing that portion of the code to use something like the `platform` modules). But to reiterate, the approach taken in the SPKG bypasses this fragility for SAGE that is completely platform independent.",
    "created_at": "2012-07-03T20:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46397",
    "user": "pi"
}
```

TLDR: you don't need this patch.

The mpl `setupext.py` code in question gets used when there is not an entry for `basedirlist` in `setup.cfg`, in which case it'll grab it from this pre-defined `basedir` dictionary using `sys.platform` as they key. From what I see that's checked into hg for SAGE, you do define `basedirlist` in `setup.cfg`, which is why this patch is un-necessary. The code is in the SPKG `matplotlib.../make-setup-config.py:7`



```
config.set('directories', 'basedirlist', os.environ['SAGE_LOCAL'])
```



which is why this patch is not needed for SPKG matplotlib being built on **any** platform.

From what I understand from the discussion at [Python Bug #12326](http://bugs.python.org/issue12326), it seems like we (MPL) should not have been using `sys.platform` in the first place for making these decisions (but given the somewhat exotic nature of the platforms which have exceptions there now, it's best to remain conservative about re-writing that portion of the code to use something like the `platform` modules). But to reiterate, the approach taken in the SPKG bypasses this fragility for SAGE that is completely platform independent.



---

archive/issue_comments_046398.json:
```json
{
    "body": "`@`pi:\nSo it sounds like between the practical experience of stephen and the upstream and our config you are pointing out, that we don't have to do anything.  Even though eventually mpl will have some other workaround.\n\nIf that's correct, I've put what I think is your real name here - just switch to \"positive review\"! I'm switching the upstream to \"none of the above\" since this is a somewhat unusual situation.  Is this your first contribution?  If so, welcome to the Sage team!",
    "created_at": "2012-07-03T20:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46398",
    "user": "kcrisman"
}
```

`@`pi:
So it sounds like between the practical experience of stephen and the upstream and our config you are pointing out, that we don't have to do anything.  Even though eventually mpl will have some other workaround.

If that's correct, I've put what I think is your real name here - just switch to "positive review"! I'm switching the upstream to "none of the above" since this is a somewhat unusual situation.  Is this your first contribution?  If so, welcome to the Sage team!



---

archive/issue_comments_046399.json:
```json
{
    "body": "`@`kcrisman it is my first direct Sage contribution, thanks!",
    "created_at": "2012-07-03T21:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46399",
    "user": "pi"
}
```

`@`kcrisman it is my first direct Sage contribution, thanks!



---

archive/issue_comments_046400.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-03T21:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46400",
    "user": "pi"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046401.json:
```json
{
    "body": "Great!",
    "created_at": "2012-07-03T21:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46401",
    "user": "kcrisman"
}
```

Great!



---

archive/issue_comments_046402.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-07-04T07:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5873#issuecomment-46402",
    "user": "jdemeyer"
}
```

Resolution: worksforme
