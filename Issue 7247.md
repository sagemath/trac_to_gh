# Issue 7247: sage-4.2.alpha0: mercurial doesn't build on OS X 10.6

archive/issues_007247.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\ncreating locale\ncreating locale/da\ncreating locale/da/LC_MESSAGES\ngenerating locale/da/LC_MESSAGES/hg.mo from i18n/da.po\nmsgfmt -v -o locale/da/LC_MESSAGES/hg.mo i18n/da.po -c\ndyld: Library not loaded: /usr/local/lib/libgettextsrc-0.14.5.dylib\n  Referenced from: /usr/local/bin/msgfmt\n  Reason: image not found\nerror: command 'msgfmt' terminated by signal 5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7247\n\n",
    "created_at": "2009-10-19T07:17:28Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sage-4.2.alpha0: mercurial doesn't build on OS X 10.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7247",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/7247





---

archive/issue_comments_060167.json:
```json
{
    "body": "I think this is because gettext isn't installed.  We either need to include gettext (which may have its own benefits) or see if we can build mercurial without gettext support.",
    "created_at": "2009-10-19T13:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7247#issuecomment-60167",
    "user": "mhansen"
}
```

I think this is because gettext isn't installed.  We either need to include gettext (which may have its own benefits) or see if we can build mercurial without gettext support.



---

archive/issue_comments_060168.json:
```json
{
    "body": "Hmm.  Mercurial built fine on OS X 10.6 on my machine.  At various points in install.log, it says\n\n```\nchecking for xgettext... no\n...\nchecking for GNU gettext in libc... no\n...\nchecking for GNU gettext in libintl... no\n```\n\nso I don't seem to have gettext installed.",
    "created_at": "2009-10-19T18:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7247#issuecomment-60168",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_060169.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-10-20T21:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7247#issuecomment-60169",
    "user": "was"
}
```

Resolution: invalid



---

archive/issue_comments_060170.json:
```json
{
    "body": "Thanks for checking into this guys.  It turns out there were a copy of gettext in my /usr/local/bin/ directory from 2006 -- probably from installing tex or something, and it was now broken.  Mercurial I guess was never broken by it before.  Anyway, removing it and also the broken msgfmt and now mercurial builds.  Thus I'm closing this ticket as invalid.  Thanks again!",
    "created_at": "2009-10-20T21:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7247#issuecomment-60170",
    "user": "was"
}
```

Thanks for checking into this guys.  It turns out there were a copy of gettext in my /usr/local/bin/ directory from 2006 -- probably from installing tex or something, and it was now broken.  Mercurial I guess was never broken by it before.  Anyway, removing it and also the broken msgfmt and now mercurial builds.  Thus I'm closing this ticket as invalid.  Thanks again!
