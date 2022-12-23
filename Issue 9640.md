# Issue 9640: Change PARI error catching mechanism

archive/issues_009640.json:
```json
{
    "body": "Assignee: was\n\nCC:  leif jdemeyer\n\nCurrently, the exceptions thrown by PARI are rather cryptic, like\n\n```\nTraceback (most recent call last):\n...\nPariError:  (15)\n```\n\n\nUsing a mechanism similar to #9636, it should be possible to catch the full text of the exception and use it to throw PariError.  We should change to using cb_pari_handle_exception() instead of err_catch() to catch PARI exceptions.\n\nDependencies: #9343, #9636\n\nIssue created by migration from https://trac.sagemath.org/ticket/9640\n\n",
    "created_at": "2010-07-29T15:47:12Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "Change PARI error catching mechanism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9640",
    "user": "jdemeyer"
}
```
Assignee: was

CC:  leif jdemeyer

Currently, the exceptions thrown by PARI are rather cryptic, like

```
Traceback (most recent call last):
...
PariError:  (15)
```


Using a mechanism similar to #9636, it should be possible to catch the full text of the exception and use it to throw PariError.  We should change to using cb_pari_handle_exception() instead of err_catch() to catch PARI exceptions.

Dependencies: #9343, #9636

Issue created by migration from https://trac.sagemath.org/ticket/9640





---

archive/issue_comments_093424.json:
```json
{
    "body": "Old patch for reference",
    "created_at": "2010-10-17T18:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93424",
    "user": "jdemeyer"
}
```

Old patch for reference



---

archive/issue_comments_093425.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-10-17T18:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93425",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_093426.json:
```json
{
    "body": "Changing keywords from \"\" to \"pari error interrupt\".",
    "created_at": "2010-10-17T18:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93426",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "pari error interrupt".



---

archive/issue_comments_093427.json:
```json
{
    "body": "I am working on a patch that does the following things suggested by the ticket description:\n- Rewrite `pari_catch_sig_on()` and `pari_catch_sig_off()` to use the callbacks `cb_pari_handle_exception` and `cb_pari_err_recover` (defined by the PARI library) in combination with `sig_on()`/`sig_off()`, as opposed to the additional `setjmp()` of the current implementation.\n- Catch output sent to `pariErr` and store it in a string attribute `pari_instance.error_string` for later use by `PariError`.\n\nIt seems to work quite well; the only doctest failures I've seen so far are a few tests expecting a PARI warning message.  With the patch, these are not printed because they also go to `pariErr`.\n\nTo be done:\n- Make `PariError` aware of the stored string to give a more informative error message.  This should probably simply be extracted from the lines starting with `***` in `pari_instance.error_string`.\n- Minor change in PARI: send any extra newline at the start of the error message to `pariErr` instead of `pariOut` (this happens if the last printed character was not a newline).\n- Distinguish between errors and warnings; the latter should probably be printed to `stderr` as before.  This should be done either by filtering the text sent to `pariErr` or by having `pari_catch_sig_off()` check if `pari_instance.error_string` is non-empty even if no error occurred.\n\nThis may make #14894 redundant, although that ticket could be used for general things to be done for the upgrade to PARI 2.6.",
    "created_at": "2013-09-11T14:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93427",
    "user": "pbruin"
}
```

I am working on a patch that does the following things suggested by the ticket description:
- Rewrite `pari_catch_sig_on()` and `pari_catch_sig_off()` to use the callbacks `cb_pari_handle_exception` and `cb_pari_err_recover` (defined by the PARI library) in combination with `sig_on()`/`sig_off()`, as opposed to the additional `setjmp()` of the current implementation.
- Catch output sent to `pariErr` and store it in a string attribute `pari_instance.error_string` for later use by `PariError`.

It seems to work quite well; the only doctest failures I've seen so far are a few tests expecting a PARI warning message.  With the patch, these are not printed because they also go to `pariErr`.

To be done:
- Make `PariError` aware of the stored string to give a more informative error message.  This should probably simply be extracted from the lines starting with `***` in `pari_instance.error_string`.
- Minor change in PARI: send any extra newline at the start of the error message to `pariErr` instead of `pariOut` (this happens if the last printed character was not a newline).
- Distinguish between errors and warnings; the latter should probably be printed to `stderr` as before.  This should be done either by filtering the text sent to `pariErr` or by having `pari_catch_sig_off()` check if `pari_instance.error_string` is non-empty even if no error occurred.

This may make #14894 redundant, although that ticket could be used for general things to be done for the upgrade to PARI 2.6.



---

archive/issue_comments_093428.json:
```json
{
    "body": "Attachment\n\nbased on 5.12.beta4 + #15124",
    "created_at": "2013-09-11T15:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93428",
    "user": "pbruin"
}
```

Attachment

based on 5.12.beta4 + #15124



---

archive/issue_comments_093429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-09-11T15:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93429",
    "user": "pbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093430.json:
```json
{
    "body": "The attached patch passes doctests on x86_64 GNU/Linux, except for two tests expecting a PARI warning (see above).",
    "created_at": "2013-09-11T15:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93430",
    "user": "pbruin"
}
```

The attached patch passes doctests on x86_64 GNU/Linux, except for two tests expecting a PARI warning (see above).



---

archive/issue_comments_093431.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-09-11T15:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93431",
    "user": "pbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093432.json:
```json
{
    "body": "It would be better practice to move `_pari_init_err()`, `_pari_handle_exception()` and `_pari_err_recover()` from `pari_err.h` to a C file or to translate them to Cython.  At the moment I don't think it is worth the trouble.",
    "created_at": "2013-09-11T15:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93432",
    "user": "pbruin"
}
```

It would be better practice to move `_pari_init_err()`, `_pari_handle_exception()` and `_pari_err_recover()` from `pari_err.h` to a C file or to translate them to Cython.  At the moment I don't think it is worth the trouble.



---

archive/issue_comments_093433.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-09-12T19:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93433",
    "user": "pbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093434.json:
```json
{
    "body": "The latest patch does everything that I think it should do.  I hope it is reasonably self-explanatory.  A few remarks:\n\n- The error text is now passed to `PariError` and can be accessed using `PariError.errtext()`; is is not printed automatically.  Using this text to improve messages like `PariError:  (15)` will probably have to wait until another ticket.  (Edit: `user` errors are an exception, since they are converted into `RuntimeError`; here we append the error text to the currently used \"PARI user exception\".)\n\n- There is no problem with PARI sending escape sequences for colours in error messages; this is disabled by default.\n\n- The printing of a possible extra newline before the error message is easily avoided using `pari_set_last_newline(1)`.\n\n- The callback functions are now Cython functions in the new file `pari_error.pyx`.  It is important that this does *not* include `pari_err.pxi`; because of the way Cython imports functions, `pari_err.pxi` and `pari_err.h` use function pointers with the same names as the functions defined in `pari_error.pyx`.",
    "created_at": "2013-09-12T19:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93434",
    "user": "pbruin"
}
```

The latest patch does everything that I think it should do.  I hope it is reasonably self-explanatory.  A few remarks:

- The error text is now passed to `PariError` and can be accessed using `PariError.errtext()`; is is not printed automatically.  Using this text to improve messages like `PariError:  (15)` will probably have to wait until another ticket.  (Edit: `user` errors are an exception, since they are converted into `RuntimeError`; here we append the error text to the currently used "PARI user exception".)

- There is no problem with PARI sending escape sequences for colours in error messages; this is disabled by default.

- The printing of a possible extra newline before the error message is easily avoided using `pari_set_last_newline(1)`.

- The callback functions are now Cython functions in the new file `pari_error.pyx`.  It is important that this does *not* include `pari_err.pxi`; because of the way Cython imports functions, `pari_err.pxi` and `pari_err.h` use function pointers with the same names as the functions defined in `pari_error.pyx`.



---

archive/issue_comments_093435.json:
```json
{
    "body": "Patchbot:\n\n```\napply 9640-pari_error_callbacks.patch\u200b\n```\n",
    "created_at": "2013-09-23T10:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93435",
    "user": "pbruin"
}
```

Patchbot:

```
apply 9640-pari_error_callbacks.patch​
```




---

archive/issue_comments_093436.json:
```json
{
    "body": "Why not set `cb_pari_handle_exception = _pari_handle_exception` globally and have `pari_catch_sig_on()` simply be **equal** to `sig_on()` (and then of course change `pari_catch_sig_on()` back to `sig_on()`).",
    "created_at": "2013-10-03T09:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93436",
    "user": "jdemeyer"
}
```

Why not set `cb_pari_handle_exception = _pari_handle_exception` globally and have `pari_catch_sig_on()` simply be **equal** to `sig_on()` (and then of course change `pari_catch_sig_on()` back to `sig_on()`).



---

archive/issue_comments_093437.json:
```json
{
    "body": "Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...",
    "created_at": "2013-10-03T10:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93437",
    "user": "jdemeyer"
}
```

Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...



---

archive/issue_comments_093438.json:
```json
{
    "body": "Replying to [comment:12 jdemeyer]:\n> Why not set `cb_pari_handle_exception = _pari_handle_exception` globally and have `pari_catch_sig_on()` simply be **equal** to `sig_on()` (and then of course change `pari_catch_sig_on()` back to `sig_on()`).\nGood question.  That would mean we simply always have PARI exception handling enabled, which would be more efficient and should not make any difference since PARI shouldn't be called outside of `sig_on()/sig_off()` anyway.  I'll try it out.",
    "created_at": "2013-10-03T10:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93438",
    "user": "pbruin"
}
```

Replying to [comment:12 jdemeyer]:
> Why not set `cb_pari_handle_exception = _pari_handle_exception` globally and have `pari_catch_sig_on()` simply be **equal** to `sig_on()` (and then of course change `pari_catch_sig_on()` back to `sig_on()`).
Good question.  That would mean we simply always have PARI exception handling enabled, which would be more efficient and should not make any difference since PARI shouldn't be called outside of `sig_on()/sig_off()` anyway.  I'll try it out.



---

archive/issue_comments_093439.json:
```json
{
    "body": "Anyway, I am thinking about a review patch so I will make these changes myself.\n\nPeter, is there any chance you could review #14029 and #13311 because those tickets also make changes to the interrupt code.",
    "created_at": "2013-10-03T10:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93439",
    "user": "jdemeyer"
}
```

Anyway, I am thinking about a review patch so I will make these changes myself.

Peter, is there any chance you could review #14029 and #13311 because those tickets also make changes to the interrupt code.



---

archive/issue_comments_093440.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...\nWhy `abort()` and not `raise(SIGUSR1)` or another signal code?",
    "created_at": "2013-10-03T10:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93440",
    "user": "pbruin"
}
```

Replying to [comment:13 jdemeyer]:
> Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...
Why `abort()` and not `raise(SIGUSR1)` or another signal code?



---

archive/issue_comments_093441.json:
```json
{
    "body": "I am thinking about merging (parts of) #10018 here, especially the doctests.",
    "created_at": "2013-10-03T10:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93441",
    "user": "jdemeyer"
}
```

I am thinking about merging (parts of) #10018 here, especially the doctests.



---

archive/issue_comments_093442.json:
```json
{
    "body": "Replying to [comment:16 pbruin]:\n> Replying to [comment:13 jdemeyer]:\n> > Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...\n> Why `abort()` and not `raise(SIGUSR1)` or another signal code?\nBecause we already handle `abort()` anyway and because I see no gain of adding an extra signal, with the risk that `SIGUSR1` is used by other Sage packages.",
    "created_at": "2013-10-03T10:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93442",
    "user": "jdemeyer"
}
```

Replying to [comment:16 pbruin]:
> Replying to [comment:13 jdemeyer]:
> > Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...
> Why `abort()` and not `raise(SIGUSR1)` or another signal code?
Because we already handle `abort()` anyway and because I see no gain of adding an extra signal, with the risk that `SIGUSR1` is used by other Sage packages.



---

archive/issue_comments_093443.json:
```json
{
    "body": "Replying to [comment:18 jdemeyer]:\n> Replying to [comment:16 pbruin]:\n> > Why `abort()` and not `raise(SIGUSR1)` or another signal code?\n> Because we already handle `abort()` anyway and because I see no gain of adding an extra signal, with the risk that `SIGUSR1` is used by other Sage packages.\nBut we handle it by raising a new `RuntimeError`, among other things, unless I misunderstand `interrupt.c`.  So wouldn't the `SIGABRT` handler need to have a special case for the case where it is called in this way?  This would be rather inelegant.",
    "created_at": "2013-10-03T10:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93443",
    "user": "pbruin"
}
```

Replying to [comment:18 jdemeyer]:
> Replying to [comment:16 pbruin]:
> > Why `abort()` and not `raise(SIGUSR1)` or another signal code?
> Because we already handle `abort()` anyway and because I see no gain of adding an extra signal, with the risk that `SIGUSR1` is used by other Sage packages.
But we handle it by raising a new `RuntimeError`, among other things, unless I misunderstand `interrupt.c`.  So wouldn't the `SIGABRT` handler need to have a special case for the case where it is called in this way?  This would be rather inelegant.



---

archive/issue_comments_093444.json:
```json
{
    "body": "Replying to [comment:19 pbruin]:\n> This would be rather inelegant.\nI personally don't find it inelegant. In any case, we would encapsalate this through some call like `sig_error()`.",
    "created_at": "2013-10-03T10:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93444",
    "user": "jdemeyer"
}
```

Replying to [comment:19 pbruin]:
> This would be rather inelegant.
I personally don't find it inelegant. In any case, we would encapsalate this through some call like `sig_error()`.



---

archive/issue_comments_093445.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Peter, is there any chance you could review #14029 and #13311 because those tickets also make changes to the interrupt code.\nNot very soon, unfortunately (lots of work at the moment), but I'll put my name in the CC list.",
    "created_at": "2013-10-03T20:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93445",
    "user": "pbruin"
}
```

Replying to [comment:15 jdemeyer]:
> Peter, is there any chance you could review #14029 and #13311 because those tickets also make changes to the interrupt code.
Not very soon, unfortunately (lots of work at the moment), but I'll put my name in the CC list.



---

archive/issue_comments_093446.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-11-01T10:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93446",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093447.json:
```json
{
    "body": "Working/thinking about this...",
    "created_at": "2013-11-01T10:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93447",
    "user": "jdemeyer"
}
```

Working/thinking about this...



---

archive/issue_comments_093448.json:
```json
{
    "body": "Attachment\n\nbased on 5.12.beta4 + #15124",
    "created_at": "2013-11-01T10:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93448",
    "user": "jdemeyer"
}
```

Attachment

based on 5.12.beta4 + #15124



---

archive/issue_comments_093449.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-11-01T22:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93449",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093450.json:
```json
{
    "body": "What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?",
    "created_at": "2013-11-02T18:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93450",
    "user": "pbruin"
}
```

What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?



---

archive/issue_comments_093451.json:
```json
{
    "body": "Replying to [comment:28 pbruin]:\n> What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?\nFor me, it can be removed. But it existed before (as a function `__errmessage()`) and one possible use would be to check that an error is of a given type without relying on the PARI error codes (for example, in pure Python code). Something like:\n\n```python\ntry:\n    pari.....\nexcept PariError as E:\n    if E.parimessage() == \"division by zero\":\n        raise ZeroDivisionError\n    else:\n        raise\n```\n\nPerhaps this is never going to happen, but at least the method `parimessage()` doesn't hurt either.",
    "created_at": "2013-11-02T20:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93451",
    "user": "jdemeyer"
}
```

Replying to [comment:28 pbruin]:
> What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?
For me, it can be removed. But it existed before (as a function `__errmessage()`) and one possible use would be to check that an error is of a given type without relying on the PARI error codes (for example, in pure Python code). Something like:

```python
try:
    pari.....
except PariError as E:
    if E.parimessage() == "division by zero":
        raise ZeroDivisionError
    else:
        raise
```

Perhaps this is never going to happen, but at least the method `parimessage()` doesn't hurt either.



---

archive/issue_comments_093452.json:
```json
{
    "body": "Replying to [comment:29 jdemeyer]:\n> Replying to [comment:28 pbruin]:\n> > What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?\n> For me, it can be removed. But it existed before (as a function `__errmessage()`) and one possible use would be to check that an error is of a given type without relying on the PARI error codes (for example, in pure Python code).\nThat is a possibility.  On the other hand, the global variable `errmessage` is another thing that has disappeared in PARI 2.6.  It has been replaced by a function `const char *numerr_name(long numerr)` which returns e.g. `\"e_INV\"` for zero division errors.  This means that in the near future your example will probably look like\n\n```python\nif pari.numerr_name(E.errnum()) == \"e_INV\":\n    raise ZeroDivisionError\n```\n\nOf course, one could then think of a method of `PariError` encapsulating this if necessary, but `parimessage` would no longer be an appropriate name.\n\nFor the time being (at least until we switch to PARI 2.6) or unless someone really wants a method like this, I think it is easiest to just remove it.",
    "created_at": "2013-11-03T00:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93452",
    "user": "pbruin"
}
```

Replying to [comment:29 jdemeyer]:
> Replying to [comment:28 pbruin]:
> > What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?
> For me, it can be removed. But it existed before (as a function `__errmessage()`) and one possible use would be to check that an error is of a given type without relying on the PARI error codes (for example, in pure Python code).
That is a possibility.  On the other hand, the global variable `errmessage` is another thing that has disappeared in PARI 2.6.  It has been replaced by a function `const char *numerr_name(long numerr)` which returns e.g. `"e_INV"` for zero division errors.  This means that in the near future your example will probably look like

```python
if pari.numerr_name(E.errnum()) == "e_INV":
    raise ZeroDivisionError
```

Of course, one could then think of a method of `PariError` encapsulating this if necessary, but `parimessage` would no longer be an appropriate name.

For the time being (at least until we switch to PARI 2.6) or unless someone really wants a method like this, I think it is easiest to just remove it.



---

archive/issue_comments_093453.json:
```json
{
    "body": "Attachment\n\nRemoved `PariError.parimessage()` method and moved the `cdef extern from \"misc.h\":` block to the top of `gen.pyx`.",
    "created_at": "2013-11-03T08:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93453",
    "user": "jdemeyer"
}
```

Attachment

Removed `PariError.parimessage()` method and moved the `cdef extern from "misc.h":` block to the top of `gen.pyx`.



---

archive/issue_comments_093454.json:
```json
{
    "body": "I'm happy with this now.  Hopefully someone wants to review it.",
    "created_at": "2013-11-04T12:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93454",
    "user": "pbruin"
}
```

I'm happy with this now.  Hopefully someone wants to review it.



---

archive/issue_comments_093455.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-11-04T12:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93455",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093456.json:
```json
{
    "body": "Replying to [comment:32 pbruin]:\n> I'm happy with this now.  Hopefully someone wants to review it.\nSince we both looked at eachother's work, I guess that counts as positive review.",
    "created_at": "2013-11-04T12:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93456",
    "user": "jdemeyer"
}
```

Replying to [comment:32 pbruin]:
> I'm happy with this now.  Hopefully someone wants to review it.
Since we both looked at eachother's work, I guess that counts as positive review.



---

archive/issue_comments_093457.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-11-06T12:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9640#issuecomment-93457",
    "user": "jdemeyer"
}
```

Resolution: fixed
