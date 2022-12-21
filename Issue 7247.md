# Issue 7247: sage-4.2.alpha0: mercurial doesn't build on OS X 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-19 07:17:28

Assignee: mabshoff


```
creating locale
creating locale/da
creating locale/da/LC_MESSAGES
generating locale/da/LC_MESSAGES/hg.mo from i18n/da.po
msgfmt -v -o locale/da/LC_MESSAGES/hg.mo i18n/da.po -c
dyld: Library not loaded: /usr/local/lib/libgettextsrc-0.14.5.dylib
  Referenced from: /usr/local/bin/msgfmt
  Reason: image not found
error: command 'msgfmt' terminated by signal 5
```



---

Comment by mhansen created at 2009-10-19 13:46:54

I think this is because gettext isn't installed.  We either need to include gettext (which may have its own benefits) or see if we can build mercurial without gettext support.


---

Comment by jhpalmieri created at 2009-10-19 18:35:37

Hmm.  Mercurial built fine on OS X 10.6 on my machine.  At various points in install.log, it says

```
checking for xgettext... no
...
checking for GNU gettext in libc... no
...
checking for GNU gettext in libintl... no
```

so I don't seem to have gettext installed.


---

Comment by was created at 2009-10-20 21:15:12

Resolution: invalid


---

Comment by was created at 2009-10-20 21:15:12

Thanks for checking into this guys.  It turns out there were a copy of gettext in my /usr/local/bin/ directory from 2006 -- probably from installing tex or something, and it was now broken.  Mercurial I guess was never broken by it before.  Anyway, removing it and also the broken msgfmt and now mercurial builds.  Thus I'm closing this ticket as invalid.  Thanks again!
