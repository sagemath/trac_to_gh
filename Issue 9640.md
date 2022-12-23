# Issue 9640: Change PARI error catching mechanism

Issue created by migration from https://trac.sagemath.org/ticket/9640

Original creator: jdemeyer

Original creation time: 2010-07-29 15:47:12

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


---

Comment by jdemeyer created at 2010-10-17 18:31:00

Old patch for reference


---

Attachment


---

Comment by jdemeyer created at 2010-10-17 18:32:31

Changing keywords from "" to "pari error interrupt".


---

Comment by pbruin created at 2013-09-11 14:09:46

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

Attachment

based on 5.12.beta4 + #15124


---

Comment by pbruin created at 2013-09-11 15:24:59

Changing status from new to needs_review.


---

Comment by pbruin created at 2013-09-11 15:24:59

The attached patch passes doctests on x86_64 GNU/Linux, except for two tests expecting a PARI warning (see above).


---

Comment by pbruin created at 2013-09-11 15:25:08

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2013-09-11 15:37:08

It would be better practice to move `_pari_init_err()`, `_pari_handle_exception()` and `_pari_err_recover()` from `pari_err.h` to a C file or to translate them to Cython.  At the moment I don't think it is worth the trouble.


---

Comment by pbruin created at 2013-09-12 19:42:22

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2013-09-12 19:42:22

The latest patch does everything that I think it should do.  I hope it is reasonably self-explanatory.  A few remarks:

- The error text is now passed to `PariError` and can be accessed using `PariError.errtext()`; is is not printed automatically.  Using this text to improve messages like `PariError:  (15)` will probably have to wait until another ticket.  (Edit: `user` errors are an exception, since they are converted into `RuntimeError`; here we append the error text to the currently used "PARI user exception".)

- There is no problem with PARI sending escape sequences for colours in error messages; this is disabled by default.

- The printing of a possible extra newline before the error message is easily avoided using `pari_set_last_newline(1)`.

- The callback functions are now Cython functions in the new file `pari_error.pyx`.  It is important that this does _not_ include `pari_err.pxi`; because of the way Cython imports functions, `pari_err.pxi` and `pari_err.h` use function pointers with the same names as the functions defined in `pari_error.pyx`.


---

Comment by pbruin created at 2013-09-23 10:28:55

Patchbot:

```
apply 9640-pari_error_callbacks.patch​
```



---

Comment by jdemeyer created at 2013-10-03 09:56:02

Why not set `cb_pari_handle_exception = _pari_handle_exception` globally and have `pari_catch_sig_on()` simply be *equal* to `sig_on()` (and then of course change `pari_catch_sig_on()` back to `sig_on()`).


---

Comment by jdemeyer created at 2013-10-03 10:05:35

Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...


---

Comment by pbruin created at 2013-10-03 10:06:34

Replying to [comment:12 jdemeyer]:
> Why not set `cb_pari_handle_exception = _pari_handle_exception` globally and have `pari_catch_sig_on()` simply be *equal* to `sig_on()` (and then of course change `pari_catch_sig_on()` back to `sig_on()`).
Good question.  That would mean we simply always have PARI exception handling enabled, which would be more efficient and should not make any difference since PARI shouldn't be called outside of `sig_on()/sig_off()` anyway.  I'll try it out.


---

Comment by jdemeyer created at 2013-10-03 10:08:00

Anyway, I am thinking about a review patch so I will make these changes myself.

Peter, is there any chance you could review #14029 and #13311 because those tickets also make changes to the interrupt code.


---

Comment by pbruin created at 2013-10-03 10:08:27

Replying to [comment:13 jdemeyer]:
> Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...
Why `abort()` and not `raise(SIGUSR1)` or another signal code?


---

Comment by jdemeyer created at 2013-10-03 10:10:02

I am thinking about merging (parts of) #10018 here, especially the doctests.


---

Comment by jdemeyer created at 2013-10-03 10:11:04

Replying to [comment:16 pbruin]:
> Replying to [comment:13 jdemeyer]:
> > Instead of using `sage_siglongjmp()`, I think it's safer to call `abort()` and use the normal signal handling mechanism. Otherwise we have to consider race conditions like a `SIGINT` arriving during the `sage_siglongjmp()` call...
> Why `abort()` and not `raise(SIGUSR1)` or another signal code?
Because we already handle `abort()` anyway and because I see no gain of adding an extra signal, with the risk that `SIGUSR1` is used by other Sage packages.


---

Comment by pbruin created at 2013-10-03 10:23:35

Replying to [comment:18 jdemeyer]:
> Replying to [comment:16 pbruin]:
> > Why `abort()` and not `raise(SIGUSR1)` or another signal code?
> Because we already handle `abort()` anyway and because I see no gain of adding an extra signal, with the risk that `SIGUSR1` is used by other Sage packages.
But we handle it by raising a new `RuntimeError`, among other things, unless I misunderstand `interrupt.c`.  So wouldn't the `SIGABRT` handler need to have a special case for the case where it is called in this way?  This would be rather inelegant.


---

Comment by jdemeyer created at 2013-10-03 10:26:05

Replying to [comment:19 pbruin]:
> This would be rather inelegant.
I personally don't find it inelegant. In any case, we would encapsalate this through some call like `sig_error()`.


---

Comment by pbruin created at 2013-10-03 20:22:55

Replying to [comment:15 jdemeyer]:
> Peter, is there any chance you could review #14029 and #13311 because those tickets also make changes to the interrupt code.
Not very soon, unfortunately (lots of work at the moment), but I'll put my name in the CC list.


---

Comment by jdemeyer created at 2013-11-01 10:31:08

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2013-11-01 10:31:24

Working/thinking about this...


---

Attachment

based on 5.12.beta4 + #15124


---

Comment by jdemeyer created at 2013-11-01 22:42:18

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2013-11-02 18:14:59

What is the use of `PariError.parimessage()`?  It doesn't seem to be used, and appears to normally be a substring of `PariError.__str__()`.  Do you have any application for it in mind, or can it be removed?


---

Comment by jdemeyer created at 2013-11-02 20:03:11

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

Comment by pbruin created at 2013-11-03 00:46:58

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

Attachment

Removed `PariError.parimessage()` method and moved the `cdef extern from "misc.h":` block to the top of `gen.pyx`.


---

Comment by pbruin created at 2013-11-04 12:08:51

I'm happy with this now.  Hopefully someone wants to review it.


---

Comment by jdemeyer created at 2013-11-04 12:44:47

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-11-04 12:45:30

Replying to [comment:32 pbruin]:
> I'm happy with this now.  Hopefully someone wants to review it.
Since we both looked at eachother's work, I guess that counts as positive review.


---

Comment by jdemeyer created at 2013-11-06 12:48:56

Resolution: fixed
