# Issue 8129: Install jsMath image fonts in a fixed location

archive/issues_008129.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein @jasongrout @jhpalmieri\n\nKeywords: notebook, jsmath, fonts\n\nInstalling the jsMath image fonts in `SAGE_LOCAL/lib/jsmath/fonts`, say, should make it easier to upgrade to new SageNB versions.\n\nNote: Both the notebook and the command-line can use jsMath (e.g., `browse_sage_doc(identity_matrix)`).  We could detect and check the relevant paths and make a symbolic link in `sage.all`.\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/53157b4e21f4ef86), #7467, #7778.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8129\n\n",
    "created_at": "2010-01-30T04:06:57Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Install jsMath image fonts in a fixed location",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8129",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  @williamstein @jasongrout @jhpalmieri

Keywords: notebook, jsmath, fonts

Installing the jsMath image fonts in `SAGE_LOCAL/lib/jsmath/fonts`, say, should make it easier to upgrade to new SageNB versions.

Note: Both the notebook and the command-line can use jsMath (e.g., `browse_sage_doc(identity_matrix)`).  We could detect and check the relevant paths and make a symbolic link in `sage.all`.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/53157b4e21f4ef86), #7467, #7778.

Issue created by migration from https://trac.sagemath.org/ticket/8129





---

archive/issue_comments_071353.json:
```json
{
    "body": "We could detect and check the relevant paths and make a symbolic link in `sage.all`.  We'd have a potential race condition --- two processes could try to make the link at the same time --- but it should be mostly harmless: `OSError: [Errno 17] File exists`.",
    "created_at": "2010-01-30T04:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71353",
    "user": "https://github.com/qed777"
}
```

We could detect and check the relevant paths and make a symbolic link in `sage.all`.  We'd have a potential race condition --- two processes could try to make the link at the same time --- but it should be mostly harmless: `OSError: [Errno 17] File exists`.



---

archive/issue_comments_071354.json:
```json
{
    "body": "I have no problem with jsmath image fonts (with latest Sage and #8051).\nCould the problem be limited to sagenb.org only?",
    "created_at": "2010-01-30T10:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71354",
    "user": "https://github.com/robert-marik"
}
```

I have no problem with jsmath image fonts (with latest Sage and #8051).
Could the problem be limited to sagenb.org only?



---

archive/issue_comments_071355.json:
```json
{
    "body": "Replying to [comment:3 robert.marik]:\n> I have no problem with jsmath image fonts (with latest Sage and #8051).\n> Could the problem be limited to sagenb.org only?\n\n\nForgot to write: I tested it on fresh Sage install - this means there are no old directories used by previous versions. Perhaps, the install script from the latest jsmath fonts was confused by previous installs and old jsmath directories on sageng.org? Just guessing, I do not have access there.",
    "created_at": "2010-01-30T11:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71355",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:3 robert.marik]:
> I have no problem with jsmath image fonts (with latest Sage and #8051).
> Could the problem be limited to sagenb.org only?


Forgot to write: I tested it on fresh Sage install - this means there are no old directories used by previous versions. Perhaps, the install script from the latest jsmath fonts was confused by previous installs and old jsmath directories on sageng.org? Just guessing, I do not have access there.



---

archive/issue_comments_071356.json:
```json
{
    "body": "Look for jsMath fonts in `SAGE_LOCAL/...`.  Depends on #8051.  sagenb repo.",
    "created_at": "2010-02-05T10:55:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71356",
    "user": "https://github.com/qed777"
}
```

Look for jsMath fonts in `SAGE_LOCAL/...`.  Depends on #8051.  sagenb repo.



---

archive/issue_comments_071357.json:
```json
{
    "body": "Attachment [trac_8129-jsmath_fonts.patch](tarball://root/attachments/some-uuid/ticket8129/trac_8129-jsmath_fonts.patch) by @qed777 created at 2010-02-05 11:18:50\n\nWith the patch, the server does a simple check for jsMath fonts under `SAGE_LOCAL`:\n\n```python\njsmath_fonts_path = os.path.join(os.environ['SAGE_LOCAL'],\n                                 'lib', 'jsmath', 'fonts')\nif not os.path.exists(jsmath_fonts_path):\n    jsmath_fonts_path = os.path.join(javascript_path, 'jsmath', 'fonts')\n```\n\nWe'll need to add the msbm10 fonts to the fonts spkg.  Instead of putting even more version-checking logic in `jsmath-image-fonts-*.spkg` `spkg-install`, should we give the new spkg a different name, e.g., `jsmath-image-fonts-new-*.spkg`?  Its `spkg-install` would just install the fonts in `SAGE_LOCAL/lib/jsmath/fonts`.\n\nAlso, should we try adding **all** of the [extra jsMath fonts](http://www.math.union.edu/~dpvc/jsmath/download/extra-fonts/welcome.html) to the new spkg?\n\n```\nbbold10\ncmbsy10\ncmbx10\ncmex10\ncm-fonts\ncmmi10\ncmmib10\ncmr10\ncmss10\ncmsy10\ncmti10\neufb10\neufm10\neurb10\neurm10\neusb10\neusm10\nlasy10\nlasyb10\nmsam10\nmsbm10\nrsfs10\nstmary10\nwasy10\nwasyb10\n```\n?",
    "created_at": "2010-02-05T11:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71357",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8129-jsmath_fonts.patch](tarball://root/attachments/some-uuid/ticket8129/trac_8129-jsmath_fonts.patch) by @qed777 created at 2010-02-05 11:18:50

With the patch, the server does a simple check for jsMath fonts under `SAGE_LOCAL`:

```python
jsmath_fonts_path = os.path.join(os.environ['SAGE_LOCAL'],
                                 'lib', 'jsmath', 'fonts')
if not os.path.exists(jsmath_fonts_path):
    jsmath_fonts_path = os.path.join(javascript_path, 'jsmath', 'fonts')
```

We'll need to add the msbm10 fonts to the fonts spkg.  Instead of putting even more version-checking logic in `jsmath-image-fonts-*.spkg` `spkg-install`, should we give the new spkg a different name, e.g., `jsmath-image-fonts-new-*.spkg`?  Its `spkg-install` would just install the fonts in `SAGE_LOCAL/lib/jsmath/fonts`.

Also, should we try adding **all** of the [extra jsMath fonts](http://www.math.union.edu/~dpvc/jsmath/download/extra-fonts/welcome.html) to the new spkg?

```
bbold10
cmbsy10
cmbx10
cmex10
cm-fonts
cmmi10
cmmib10
cmr10
cmss10
cmsy10
cmti10
eufb10
eufm10
eurb10
eurm10
eusb10
eusm10
lasy10
lasyb10
msam10
msbm10
rsfs10
stmary10
wasy10
wasyb10
```
?



---

archive/issue_events_019467.json:
```json
{
    "actor": "https://github.com/KPanComputes",
    "created_at": "2013-02-03T18:20:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8129#event-19467"
}
```



---

archive/issue_comments_071358.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-03T18:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71358",
    "user": "https://github.com/KPanComputes"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071359.json:
```json
{
    "body": "We now use MathJax instead of jsMath, so I think this ticket per se is invalid. But, I am not sure how we use MathJaX and whether this ticket is relevant for our implementation. Can someone look through this and also help me sort this ignorance out?",
    "created_at": "2013-02-03T18:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71359",
    "user": "https://github.com/KPanComputes"
}
```

We now use MathJax instead of jsMath, so I think this ticket per se is invalid. But, I am not sure how we use MathJaX and whether this ticket is relevant for our implementation. Can someone look through this and also help me sort this ignorance out?



---

archive/issue_comments_071360.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-17T12:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71360",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071361.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8129#issuecomment-71361",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_019468.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-21T07:24:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8129",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8129#event-19468"
}
```
