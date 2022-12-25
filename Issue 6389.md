# Issue 6389: expose building documentation for user modules not in the Sage library

archive/issues_006389.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @mkoeppe @jdemeyer @vbraun @fchapoton @williamstein @dimpase @nthiery fhivert @embray\n\nKeywords: documentation, sphinx\n\nIt would be neat to be able to do:\n\n`sage -docbuild foo.py`\n\nfor a single file not in the library\n\nIssue created by migration from https://trac.sagemath.org/ticket/6389\n\n",
    "created_at": "2009-06-23T14:34:27Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "expose building documentation for user modules not in the Sage library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6389",
    "user": "https://github.com/malb"
}
```
Assignee: tba

CC:  @mkoeppe @jdemeyer @vbraun @fchapoton @williamstein @dimpase @nthiery fhivert @embray

Keywords: documentation, sphinx

It would be neat to be able to do:

`sage -docbuild foo.py`

for a single file not in the library

Issue created by migration from https://trac.sagemath.org/ticket/6389





---

archive/issue_comments_051061.json:
```json
{
    "body": "This used to work, but no longer\n\n```\nsage -docbuild file=my_own_code.py html\n```\n",
    "created_at": "2016-07-15T11:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51061",
    "user": "https://github.com/fchapoton"
}
```

This used to work, but no longer

```
sage -docbuild file=my_own_code.py html
```




---

archive/issue_comments_051062.json:
```json
{
    "body": "The line\n\n```\n    assert app.outdir.startswith(SAGE_DOC)\n```\n\nin `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.",
    "created_at": "2016-08-01T02:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51062",
    "user": "https://github.com/jhpalmieri"
}
```

The line

```
    assert app.outdir.startswith(SAGE_DOC)
```

in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.



---

archive/issue_comments_051063.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> The line\n> {{{\n>     assert app.outdir.startswith(SAGE_DOC)\n> }}}\n> in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.\n\nThis assert is in `citation_dir`. \nHow should single-file docbuilds handle citations?",
    "created_at": "2016-08-03T19:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51063",
    "user": "https://github.com/mkoeppe"
}
```

Replying to [comment:3 jhpalmieri]:
> The line
> {{{
>     assert app.outdir.startswith(SAGE_DOC)
> }}}
> in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.

This assert is in `citation_dir`. 
How should single-file docbuilds handle citations?



---

archive/issue_comments_051064.json:
```json
{
    "body": "Replying to [comment:5 mkoeppe]:\n> Replying to [comment:3 jhpalmieri]:\n> > The line\n> > {{{\n> >     assert app.outdir.startswith(SAGE_DOC)\n> > }}}\n> > in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.\n> \n> This assert is in `citation_dir`. \n> How should single-file docbuilds handle citations?\n\nIgnore them? Or at least ignore references to citations in the Sage library: I think it should treat the single file as being unconnected to the Sage library.",
    "created_at": "2016-08-03T20:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51064",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:5 mkoeppe]:
> Replying to [comment:3 jhpalmieri]:
> > The line
> > {{{
> >     assert app.outdir.startswith(SAGE_DOC)
> > }}}
> > in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.
> 
> This assert is in `citation_dir`. 
> How should single-file docbuilds handle citations?

Ignore them? Or at least ignore references to citations in the Sage library: I think it should treat the single file as being unconnected to the Sage library.



---

archive/issue_comments_051065.json:
```json
{
    "body": "Cc'ing people who are currently working on the documentation infrastructure (#20080, #20893, #20577).",
    "created_at": "2016-08-03T20:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51065",
    "user": "https://github.com/mkoeppe"
}
```

Cc'ing people who are currently working on the documentation infrastructure (#20080, #20893, #20577).



---

archive/issue_comments_051066.json:
```json
{
    "body": "See also #21841 -- per that ticket, I think that if Sage's docbuild facilities are made available to third-party code (as I think it should be) then either it should be moved into the sage library itself (i.e. `sage.docbuild`) or its own package (`sage_docbuild`)--`sage_setup` is not otherwise a good place for it.",
    "created_at": "2016-11-10T11:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51066",
    "user": "https://github.com/embray"
}
```

See also #21841 -- per that ticket, I think that if Sage's docbuild facilities are made available to third-party code (as I think it should be) then either it should be moved into the sage library itself (i.e. `sage.docbuild`) or its own package (`sage_docbuild`)--`sage_setup` is not otherwise a good place for it.



---

archive/issue_comments_051067.json:
```json
{
    "body": "I don't fully understand how citations are handled, but would it not be desirable for third-party docs to either have their own citation list, or to be able to point to citations in Sage's docs (if available)?",
    "created_at": "2016-11-10T11:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6389#issuecomment-51067",
    "user": "https://github.com/embray"
}
```

I don't fully understand how citations are handled, but would it not be desirable for third-party docs to either have their own citation list, or to be able to point to citations in Sage's docs (if available)?
