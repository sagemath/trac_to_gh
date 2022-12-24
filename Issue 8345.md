# Issue 8345: cannot convert symbolic functions back from maxima

archive/issues_008345.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\nFrom sage-devel:\n\n\n```\nOn Mon, 22 Feb 2010 07:02:21 -0800 (PST)\nH\u00e5kan Granath <hakan.granath@googlemail.com> wrote:\n\n> Typesetting conjugates of variables (that has been passed to\n> Maxima and back?) is strange. In e.g. Sage 4.2 this did not\n> happen.\n> \n> ----------------------------------------------------------------------\n> | Sage Version 4.3.3, Release Date: 2010-02-21                       |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> sage: assume(x,'complex')\n> sage: latex(x.conjugate())\n> \\overline{x}\n> sage: latex(x.conjugate().factor())\n> {\\rm conjugate}\\left(x\\right)\n```\n\n\nSomehow we don't recognize the conjugate function in the string we get back from maxima, and create a new one. The last line above is the default latex typesetting for symbolic functions.\n\n\nThe thread is here:\n\nhttp://groups.google.com/group/sage-devel/t/cd43a14bee6e9be\n\nIssue created by migration from https://trac.sagemath.org/ticket/8345\n\n",
    "created_at": "2010-02-24T11:36:28Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "cannot convert symbolic functions back from maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8345",
    "user": "burcin"
}
```
Assignee: was

CC:  kcrisman

From sage-devel:


```
On Mon, 22 Feb 2010 07:02:21 -0800 (PST)
Håkan Granath <hakan.granath@googlemail.com> wrote:

> Typesetting conjugates of variables (that has been passed to
> Maxima and back?) is strange. In e.g. Sage 4.2 this did not
> happen.
> 
> ----------------------------------------------------------------------
> | Sage Version 4.3.3, Release Date: 2010-02-21                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: assume(x,'complex')
> sage: latex(x.conjugate())
> \overline{x}
> sage: latex(x.conjugate().factor())
> {\rm conjugate}\left(x\right)
```


Somehow we don't recognize the conjugate function in the string we get back from maxima, and create a new one. The last line above is the default latex typesetting for symbolic functions.


The thread is here:

http://groups.google.com/group/sage-devel/t/cd43a14bee6e9be

Issue created by migration from https://trac.sagemath.org/ticket/8345





---

archive/issue_comments_074505.json:
```json
{
    "body": "This seems to be fixed in the meanwhile. attachment:trac_8345-doctest.patch adds a doctest.",
    "created_at": "2011-06-01T14:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74505",
    "user": "burcin"
}
```

This seems to be fixed in the meanwhile. attachment:trac_8345-doctest.patch adds a doctest.



---

archive/issue_comments_074506.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-01T14:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74506",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074507.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-08T19:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74507",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074508.json:
```json
{
    "body": "This patch does not apply to 4.7.1.alpha1 because of a blank line someone must have removed earlier.  Unfortunately, I can't figure out how to fix the patch easily (so that Burcin remains the author of the patch), so it will have to be rebased.  Hopefully that won't be too much trouble :(\n\nThis also exposes a different problem - that our variables are assumed to be real.  This is known elsewhere.\n\n```\nsage: latex(x.conjugate())\n\\overline{x}\nsage: latex(x.conjugate().simplify())\nx\n```\n\n\nNot sure if that needs to be addressed on this ticket, though.",
    "created_at": "2011-06-08T19:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74508",
    "user": "kcrisman"
}
```

This patch does not apply to 4.7.1.alpha1 because of a blank line someone must have removed earlier.  Unfortunately, I can't figure out how to fix the patch easily (so that Burcin remains the author of the patch), so it will have to be rebased.  Hopefully that won't be too much trouble :(

This also exposes a different problem - that our variables are assumed to be real.  This is known elsewhere.

```
sage: latex(x.conjugate())
\overline{x}
sage: latex(x.conjugate().simplify())
x
```


Not sure if that needs to be addressed on this ticket, though.



---

archive/issue_comments_074509.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-09T11:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74509",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074510.json:
```json
{
    "body": "Attachment [trac_8345-doctest.patch](tarball://root/attachments/some-uuid/ticket8345/trac_8345-doctest.patch) by burcin created at 2011-06-09 11:17:47\n\nReplying to [comment:3 kcrisman]:\n> This patch does not apply to 4.7.1.alpha1 because of a blank line someone must have removed earlier.  Unfortunately, I can't figure out how to fix the patch easily (so that Burcin remains the author of the patch), so it will have to be rebased.  Hopefully that won't be too much trouble :(\n\nI uploaded a rebased patch with the same name.\n\nIf you `qimport` a patch which already has mercurial headers, make changes, then `qrefresh` and `export`, the author shouldn't change. In this case, it wouldn't matter even if you changed it. :)\n\n> This also exposes a different problem - that our variables are assumed to be real.  This is known elsewhere.\n> {{{\n> sage: latex(x.conjugate())\n> \\overline{x}\n> sage: latex(x.conjugate().simplify())\n> x\n> }}}\n> \n> Not sure if that needs to be addressed on this ticket, though.\n\nThat is #6882, well beyond the scope of this ticket.",
    "created_at": "2011-06-09T11:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74510",
    "user": "burcin"
}
```

Attachment [trac_8345-doctest.patch](tarball://root/attachments/some-uuid/ticket8345/trac_8345-doctest.patch) by burcin created at 2011-06-09 11:17:47

Replying to [comment:3 kcrisman]:
> This patch does not apply to 4.7.1.alpha1 because of a blank line someone must have removed earlier.  Unfortunately, I can't figure out how to fix the patch easily (so that Burcin remains the author of the patch), so it will have to be rebased.  Hopefully that won't be too much trouble :(

I uploaded a rebased patch with the same name.

If you `qimport` a patch which already has mercurial headers, make changes, then `qrefresh` and `export`, the author shouldn't change. In this case, it wouldn't matter even if you changed it. :)

> This also exposes a different problem - that our variables are assumed to be real.  This is known elsewhere.
> {{{
> sage: latex(x.conjugate())
> \overline{x}
> sage: latex(x.conjugate().simplify())
> x
> }}}
> 
> Not sure if that needs to be addressed on this ticket, though.

That is #6882, well beyond the scope of this ticket.



---

archive/issue_comments_074511.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-09T13:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74511",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074512.json:
```json
{
    "body": "Okay, thanks - and thanks for the tip, in the last few months I've finally started using queues.\n\nI already tried several things yesterday, so all is well.  Positive review.\n\nIncidentally, this has been fixed for a *while*:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: hackbranch\nsage: assume(x,'complex')\nsage: latex(x.conjugate().simplify())\n\\overline{x}\nsage: \n```\n\n| Sage Version 4.4.4, Release Date: 2010-06-23                       |\n| Type notebook() for the GUI, and license() for information.        |\n----\nApply [attachment:trac_8345-doctest.patch].",
    "created_at": "2011-06-09T13:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74512",
    "user": "kcrisman"
}
```

Okay, thanks - and thanks for the tip, in the last few months I've finally started using queues.

I already tried several things yesterday, so all is well.  Positive review.

Incidentally, this has been fixed for a *while*:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: hackbranch
sage: assume(x,'complex')
sage: latex(x.conjugate().simplify())
\overline{x}
sage: 
```

| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |
----
Apply [attachment:trac_8345-doctest.patch].



---

archive/issue_comments_074513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-15T20:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8345#issuecomment-74513",
    "user": "jdemeyer"
}
```

Resolution: fixed
