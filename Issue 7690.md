# Issue 7690: maxima stats too many files on startup, which is a performance issue

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-15 19:43:27

Assignee: tbd


```
Hi,

This email is a followup about  "1. maxima opens the root directory /
and stats each file found there. Then it does the same thing for the
/u (home) directory..."

Thanks to everybody that responded to my query below.  The
"MAXIMA-SHAREDIR" variable looks fine according to the output of
"maxima --directories".
Off list, Andrej Vodopivec remarked "It could be share-subdirs-list in
init-cl.lisp. If that is true, then it should be easy to remove the
call to share-subdirs-list.".    I tried doing what Andrej suggested,
and it worked perfectly.  Before doing that, Maxima would state about
4000 files (including all users' home directories) on startup, and
afterwards it stat'd only about 70 files.   The difference in
performance on some NSF filesystems is huge -- a second versus
potentially *minutes*.    Even the difference on
sage.math.washington.edu is quite noticeable (a very fast machine with
a fast network).  Looking at the output of makes this very clear:

   strace maxima --directories  > out 2>&1; grep stat out|wc -l


For now we'll be patching the Maxima in Sage so that
share-subdirs-list (in init-cl.lisp) falls back to the old "default
behavior" instead of the new behavior that was introduced in the
recent rewrite of init-cl.lisp.    I really hope whoever rewrote
init-cl.lisp can think about the significant performance regression
that was caused, and find a better solution.

Thanks again for all the incredibly helpful feedback!

 -- William
```


By the way, what I did to init-cl.lisp was stupid.  I changed

```
#+ecl
(defun share-subdirs-list ()
  ;; This doesn't work yet on windows.  Give up in that case and use
  ;; the default list.
  (if (string= *autoconf-win32* "true")
```

to

```
#+ecl
(defun share-subdirs-list ()
  ;; This doesn't work yet on windows.  Give up in that case and use
  ;; the default list.
  (if (string= *autoconf-win32* "false")
```




---

Comment by was created at 2009-12-18 06:04:37


```
On Wed, Dec 16, 2009 at 6:14 AM, Robert Dodier <robert.dodier`@`gmail.com> wrote:

    Hello,

    We got a report about Maxima calling stat on a lot
    of files when the program is launched.
    Aside from all the files in the Maxima share directory,
    which we expect Maxima to look at, stat was called
    on a lot of other files as well (stuff outside the Maxima
    directory structure).


An unfortunate mistake: DIRECTORY used stat() on all entries in a directory, not only those that matched the mask. It was just a matter of switching lines. Now things are better. Thanks a lot for reporting. 

$ echo '(directory "/Users/jjgarcia/tmp/")(quit)' > foo.lsp; sudo dtrace -n 'pid$target::safe_stat:entry  { printf("%s\n", copyinstr((uintptr_t)arg0)); }' -c "ecl -norc -load foo"
dtrace: description 'pid$target::safe_stat:entry  ' matched 1 probe
;;; Loading #P"/Users/jjgarcia/foo.lsp"
dtrace: pid 39532 has exited
CPU     ID                    FUNCTION:NAME
  0  19180                  safe_stat:entry jjgarcia

  0  19180                  safe_stat:entry tmp
```



---

Comment by jhpalmieri created at 2010-04-23 04:42:19

No patch available, so I'm deferring this to Sage 5.0.


---

Comment by jason created at 2010-05-13 04:22:19

This might be fixed by #8808


---

Comment by was created at 2010-06-03 04:10:31

No patch, so deferring...


---

Comment by rlm created at 2010-07-08 18:33:46

Resolution: fixed
