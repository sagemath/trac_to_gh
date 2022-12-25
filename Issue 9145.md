# Issue 9145: Expand math symbols available in documentation, remove doc/common/macros.tex

archive/issues_009145.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri\n\nSee discussion at\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/d62ea229829048f7\n\nIssue created by migration from https://trac.sagemath.org/ticket/9145\n\n",
    "created_at": "2010-06-05T04:03:42Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Expand math symbols available in documentation, remove doc/common/macros.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9145",
    "user": "https://github.com/rbeezer"
}
```
Assignee: mvngu

CC:  @jhpalmieri

See discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/d62ea229829048f7

Issue created by migration from https://trac.sagemath.org/ticket/9145





---

archive/issue_comments_085257.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-05T04:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9145#issuecomment-85257",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085258.json:
```json
{
    "body": "Attachment [trac_9145_math_symbols_docs.patch](tarball://root/attachments/some-uuid/ticket9145/trac_9145_math_symbols_docs.patch) by @rbeezer created at 2010-06-05 04:14:02\n\nPatch removes doc/common/macros.tex, replaces amsfonts by amssymb in latex preamble string of doc/common/conf.py.\n\n4.4.3.alpha3 HTMl and PDF documentation all build without halting when this patch is applied and a limited survey indicates they look good as well.",
    "created_at": "2010-06-05T04:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9145#issuecomment-85258",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_9145_math_symbols_docs.patch](tarball://root/attachments/some-uuid/ticket9145/trac_9145_math_symbols_docs.patch) by @rbeezer created at 2010-06-05 04:14:02

Patch removes doc/common/macros.tex, replaces amsfonts by amssymb in latex preamble string of doc/common/conf.py.

4.4.3.alpha3 HTMl and PDF documentation all build without halting when this patch is applied and a limited survey indicates they look good as well.



---

archive/issue_comments_085259.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T21:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9145#issuecomment-85259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085260.json:
```json
{
    "body": "Without the patch, when building the PDF version of the reference manual for Sage 4.4.3, I got:\n\n```\n! Undefined control sequence.\nl.217693 ...als}(\\mathrm{pos}_{i+1})]_{1 \\leqslant \n                                                   i \\leqslant n}$\n```\n\nNote that the HTML version built OK. With the patch, the PDF version built successfully on these machines:\n\n* sage.math, Ubuntu 8.04.4 LTS, with latex and pdflatex\n* bsd.math, Mac OS X 10.6.3, with latex and pdflatex\n\nBut failed on these machines:\n\n* eno.skynet, Fedora 12, no latex or pdflatex\n* rh.math, Ubuntu 10.04 LTS, no latex or pdflatex\n* rosemary.math, Red Hat Enterprise Linux Server 5.5, with latex and pdflatex, but I got the following error when building the PDF version:\n {{{\n! LaTeX Error: File `utf8x.def' not found.\n }}}\n This also happens without the patch. The issue is more likely due to the LaTeX installation on rosemary.math.\n\nAs for `doc/common/macros.tex`, that file was during the days when Sage's documentation followed how Python did it. Since switching over to Sphinx, we don't need that file any more.",
    "created_at": "2010-06-05T21:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9145#issuecomment-85260",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Without the patch, when building the PDF version of the reference manual for Sage 4.4.3, I got:

```
! Undefined control sequence.
l.217693 ...als}(\mathrm{pos}_{i+1})]_{1 \leqslant 
                                                   i \leqslant n}$
```

Note that the HTML version built OK. With the patch, the PDF version built successfully on these machines:

* sage.math, Ubuntu 8.04.4 LTS, with latex and pdflatex
* bsd.math, Mac OS X 10.6.3, with latex and pdflatex

But failed on these machines:

* eno.skynet, Fedora 12, no latex or pdflatex
* rh.math, Ubuntu 10.04 LTS, no latex or pdflatex
* rosemary.math, Red Hat Enterprise Linux Server 5.5, with latex and pdflatex, but I got the following error when building the PDF version:
 {{{
! LaTeX Error: File `utf8x.def' not found.
 }}}
 This also happens without the patch. The issue is more likely due to the LaTeX installation on rosemary.math.

As for `doc/common/macros.tex`, that file was during the days when Sage's documentation followed how Python did it. Since switching over to Sphinx, we don't need that file any more.



---

archive/issue_events_009305.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T00:44:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9145",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9145#event-9305"
}
```



---

archive/issue_comments_085261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T00:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9145#issuecomment-85261",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
