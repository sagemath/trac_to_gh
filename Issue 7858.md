# Issue 7858: Declare KEY_* binding variables explicitly

archive/issues_007858.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mwhansen @TimDumol\n\nFrom Firebug's console:\n\n```\nsyntax error\n    KEY_SHIFT = \"16,16\"\n```\n\nWe should declare each variable explicitly (to avoid implicit globals), e.g.,\n\n```js\nvar KEY_SHIFT = \"16,16\";\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7858\n\n",
    "created_at": "2010-01-06T18:51:25Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Declare KEY_* binding variables explicitly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7858",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @mwhansen @TimDumol

From Firebug's console:

```
syntax error
    KEY_SHIFT = "16,16"
```

We should declare each variable explicitly (to avoid implicit globals), e.g.,

```js
var KEY_SHIFT = "16,16";
```


Issue created by migration from https://trac.sagemath.org/ticket/7858





---

archive/issue_comments_067987.json:
```json
{
    "body": "Attachment [trac_7858-key_binding_vars.patch](tarball://root/attachments/some-uuid/ticket7858/trac_7858-key_binding_vars.patch) by @qed777 created at 2010-01-06 19:28:01\n\nUse proper `Content-Type`.  Explicitly declare vars.  sagenb repo.",
    "created_at": "2010-01-06T19:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67987",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7858-key_binding_vars.patch](tarball://root/attachments/some-uuid/ticket7858/trac_7858-key_binding_vars.patch) by @qed777 created at 2010-01-06 19:28:01

Use proper `Content-Type`.  Explicitly declare vars.  sagenb repo.



---

archive/issue_comments_067988.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-06T19:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67988",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067989.json:
```json
{
    "body": "This depends on #7786.",
    "created_at": "2010-01-06T19:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67989",
    "user": "https://github.com/qed777"
}
```

This depends on #7786.



---

archive/issue_comments_067990.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T19:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67990",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067991.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-01-06T19:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67991",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_comments_067992.json:
```json
{
    "body": "Replying to [comment:4 timdumol]:\n> LGTM.\nIt seems I have been too zealous: the SageNB tests work, but shift+enter is not detected by my browser (FF 3.5.2/Linux).",
    "created_at": "2010-01-06T20:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67992",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:4 timdumol]:
> LGTM.
It seems I have been too zealous: the SageNB tests work, but shift+enter is not detected by my browser (FF 3.5.2/Linux).



---

archive/issue_comments_067993.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-06T20:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67993",
    "user": "https://github.com/TimDumol"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067994.json:
```json
{
    "body": "Other browsers, too.  Tracking...",
    "created_at": "2010-01-06T20:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67994",
    "user": "https://github.com/qed777"
}
```

Other browsers, too.  Tracking...



---

archive/issue_comments_067995.json:
```json
{
    "body": "Eval bindings in global namespace.  Replaces previous.",
    "created_at": "2010-01-06T20:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67995",
    "user": "https://github.com/qed777"
}
```

Eval bindings in global namespace.  Replaces previous.



---

archive/issue_comments_067996.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T20:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67996",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067997.json:
```json
{
    "body": "Attachment [trac_7858-key_binding_vars_v2.patch](tarball://root/attachments/some-uuid/ticket7858/trac_7858-key_binding_vars_v2.patch) by @qed777 created at 2010-01-06 20:21:07\n\nV2 *should* preserve the bindings.  I mistrans*ed from #7666.  I apologize for this.",
    "created_at": "2010-01-06T20:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67997",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7858-key_binding_vars_v2.patch](tarball://root/attachments/some-uuid/ticket7858/trac_7858-key_binding_vars_v2.patch) by @qed777 created at 2010-01-06 20:21:07

V2 *should* preserve the bindings.  I mistrans*ed from #7666.  I apologize for this.



---

archive/issue_comments_067998.json:
```json
{
    "body": "Works in FF 3.5.2/Linux and in Chromium 4.0.249.43/Linux. Anyone care to test for other browsers? (Safari and IE)",
    "created_at": "2010-01-06T20:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67998",
    "user": "https://github.com/TimDumol"
}
```

Works in FF 3.5.2/Linux and in Chromium 4.0.249.43/Linux. Anyone care to test for other browsers? (Safari and IE)



---

archive/issue_comments_067999.json:
```json
{
    "body": "For what it's worth, the keys still work for me in various browsers on Windows XP, too.",
    "created_at": "2010-01-07T01:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-67999",
    "user": "https://github.com/qed777"
}
```

For what it's worth, the keys still work for me in various browsers on Windows XP, too.



---

archive/issue_comments_068000.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T09:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-68000",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068001.json:
```json
{
    "body": "Works perfectly, so far as I can tell.",
    "created_at": "2010-01-17T09:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-68001",
    "user": "https://github.com/TimDumol"
}
```

Works perfectly, so far as I can tell.



---

archive/issue_events_018785.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:33:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7858#event-18785"
}
```



---

archive/issue_comments_068002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7858#issuecomment-68002",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed
