# Issue 7858: Declare KEY_* binding variables explicitly

Issue created by migration from https://trac.sagemath.org/ticket/7858

Original creator: mpatel

Original creation time: 2010-01-06 18:51:25

Assignee: was

CC:  mhansen timdumol

From Firebug's console:

```
syntax error
    KEY_SHIFT = "16,16"
```

We should declare each variable explicitly (to avoid implicit globals), e.g.,

```js
var KEY_SHIFT = "16,16";
```



---

Attachment

Use proper `Content-Type`.  Explicitly declare vars.  sagenb repo.


---

Comment by mpatel created at 2010-01-06 19:34:00

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-06 19:34:33

This depends on #7786.


---

Comment by timdumol created at 2010-01-06 19:57:41

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-06 19:57:41

LGTM.


---

Comment by timdumol created at 2010-01-06 20:07:30

Replying to [comment:4 timdumol]:
> LGTM.
It seems I have been too zealous: the SageNB tests work, but shift+enter is not detected by my browser (FF 3.5.2/Linux).


---

Comment by timdumol created at 2010-01-06 20:07:30

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-01-06 20:09:00

Other browsers, too.  Tracking...


---

Comment by mpatel created at 2010-01-06 20:19:32

Eval bindings in global namespace.  Replaces previous.


---

Comment by mpatel created at 2010-01-06 20:21:07

Changing status from needs_work to needs_review.


---

Attachment

V2 _should_ preserve the bindings.  I mistrans*ed from #7666.  I apologize for this.


---

Comment by timdumol created at 2010-01-06 20:28:53

Works in FF 3.5.2/Linux and in Chromium 4.0.249.43/Linux. Anyone care to test for other browsers? (Safari and IE)


---

Comment by mpatel created at 2010-01-07 01:53:32

For what it's worth, the keys still work for me in various browsers on Windows XP, too.


---

Comment by timdumol created at 2010-01-17 09:18:45

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 09:18:45

Works perfectly, so far as I can tell.


---

Comment by timdumol created at 2010-01-19 03:33:47

Resolution: fixed
