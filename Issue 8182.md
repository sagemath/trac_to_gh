# Issue 8182: Camino browser crashed when notebook started using Mac OSX

archive/issues_008182.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: OSX, Snow Leopard\n\nI just installed SAGE on a Macbook Pro running Snow Leopard.  I got sage running in Terminal and typed notebook().  A notebook came up in Camino (which I use) and asked for me to set a password.  After I did that the browser crashed with this bug report:\n\n```\n2/3/10 5:26:47 PM Camino[480] *** Terminating app due to uncaught exception 'JavaNativeException', reason: 'java.lang.NoClassDefFoundError: sun/plugin/javascript/webkit/JSObject'\n*** Call stack at first throw:\n(\n0   CoreFoundation                      0x969d240a __raiseError + 410\n1   libobjc.A.dylib                     0x922ed509 objc_exception_throw + 56\n2   CoreFoundation                      0x96a1ca21 -[NSException raise] + 17\n3   JavaPluginCocoa                     0x197438ce registerNatives + 129\n4   JavaEmbeddingPlugin                 0x1cd5da65 Java_callRegisterNatives + 402\n5   ???                                 0x3100b839 0x0 + 822130745\n)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8182\n\n",
    "closed_at": "2014-12-11T18:35:16Z",
    "created_at": "2010-02-03T23:45:58Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Camino browser crashed when notebook started using Mac OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8182",
    "user": "https://trac.sagemath.org/admin/accounts/users/jhelffrich"
}
```
Assignee: @williamstein

Keywords: OSX, Snow Leopard

I just installed SAGE on a Macbook Pro running Snow Leopard.  I got sage running in Terminal and typed notebook().  A notebook came up in Camino (which I use) and asked for me to set a password.  After I did that the browser crashed with this bug report:

```
2/3/10 5:26:47 PM Camino[480] *** Terminating app due to uncaught exception 'JavaNativeException', reason: 'java.lang.NoClassDefFoundError: sun/plugin/javascript/webkit/JSObject'
*** Call stack at first throw:
(
0   CoreFoundation                      0x969d240a __raiseError + 410
1   libobjc.A.dylib                     0x922ed509 objc_exception_throw + 56
2   CoreFoundation                      0x96a1ca21 -[NSException raise] + 17
3   JavaPluginCocoa                     0x197438ce registerNatives + 129
4   JavaEmbeddingPlugin                 0x1cd5da65 Java_callRegisterNatives + 402
5   ???                                 0x3100b839 0x0 + 822130745
)
```

Issue created by migration from https://trac.sagemath.org/ticket/8182





---

archive/issue_comments_071990.json:
```json
{
    "body": "Given that [Camino itself says it has come to an end](http://caminobrowser.org/), I guess it's time to close this ticket.",
    "created_at": "2014-12-10T21:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-71990",
    "user": "https://github.com/kcrisman"
}
```

Given that [Camino itself says it has come to an end](http://caminobrowser.org/), I guess it's time to close this ticket.



---

archive/issue_events_019587.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-12-10T21:44:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8182#event-19587"
}
```



---

archive/issue_comments_071991.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T21:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-71991",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071992.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T21:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-71992",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071993.json:
```json
{
    "body": "Not that there couldn't be a bug here!  But how could we find it...",
    "created_at": "2014-12-10T21:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-71993",
    "user": "https://github.com/kcrisman"
}
```

Not that there couldn't be a bug here!  But how could we find it...



---

archive/issue_comments_071994.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-12-11T18:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-71994",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_019588.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-12-11T18:35:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8182#event-19588"
}
```
