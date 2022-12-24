# Issue 8182: Camino browser crashed when notebook started using Mac OSX

archive/issues_008182.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: OSX, Snow Leopard\n\nI just installed SAGE on a Macbook Pro running Snow Leopard.  I got sage running in Terminal and typed notebook().  A notebook came up in Camino (which I use) and asked for me to set a password.  After I did that the browser crashed with this bug report:\n\n2/3/10 5:26:47 PM\tCamino[480]\t*** Terminating app due to uncaught exception 'JavaNativeException', reason: 'java.lang.NoClassDefFoundError: sun/plugin/javascript/webkit/JSObject'\n*** Call stack at first throw:\n(\n\t0   CoreFoundation                      0x969d240a __raiseError + 410\n\t1   libobjc.A.dylib                     0x922ed509 objc_exception_throw + 56\n\t2   CoreFoundation                      0x96a1ca21 -[NSException raise] + 17\n\t3   JavaPluginCocoa                     0x197438ce registerNatives + 129\n\t4   JavaEmbeddingPlugin                 0x1cd5da65 Java_callRegisterNatives + 402\n\t5   ???                                 0x3100b839 0x0 + 822130745\n)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8182\n\n",
    "created_at": "2010-02-03T23:45:58Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Camino browser crashed when notebook started using Mac OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8182",
    "user": "jhelffrich"
}
```
Assignee: @williamstein

Keywords: OSX, Snow Leopard

I just installed SAGE on a Macbook Pro running Snow Leopard.  I got sage running in Terminal and typed notebook().  A notebook came up in Camino (which I use) and asked for me to set a password.  After I did that the browser crashed with this bug report:

2/3/10 5:26:47 PM	Camino[480]	*** Terminating app due to uncaught exception 'JavaNativeException', reason: 'java.lang.NoClassDefFoundError: sun/plugin/javascript/webkit/JSObject'
*** Call stack at first throw:
(
	0   CoreFoundation                      0x969d240a __raiseError + 410
	1   libobjc.A.dylib                     0x922ed509 objc_exception_throw + 56
	2   CoreFoundation                      0x96a1ca21 -[NSException raise] + 17
	3   JavaPluginCocoa                     0x197438ce registerNatives + 129
	4   JavaEmbeddingPlugin                 0x1cd5da65 Java_callRegisterNatives + 402
	5   ???                                 0x3100b839 0x0 + 822130745
)

Issue created by migration from https://trac.sagemath.org/ticket/8182





---

archive/issue_comments_072112.json:
```json
{
    "body": "Given that [Camino itself says it has come to an end](http://caminobrowser.org/), I guess it's time to close this ticket.",
    "created_at": "2014-12-10T21:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-72112",
    "user": "@kcrisman"
}
```

Given that [Camino itself says it has come to an end](http://caminobrowser.org/), I guess it's time to close this ticket.



---

archive/issue_comments_072113.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T21:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-72113",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072114.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T21:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-72114",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072115.json:
```json
{
    "body": "Not that there couldn't be a bug here!  But how could we find it...",
    "created_at": "2014-12-10T21:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-72115",
    "user": "@kcrisman"
}
```

Not that there couldn't be a bug here!  But how could we find it...



---

archive/issue_comments_072116.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-12-11T18:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8182#issuecomment-72116",
    "user": "@vbraun"
}
```

Resolution: wontfix
