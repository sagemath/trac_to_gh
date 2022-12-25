# Issue 8486: Xelatex and Sage notebook

archive/issues_008486.json:
```json
{
    "body": "Assignee: tbd\n\nI think I want, e.g., the following works in Sage notebook.\n\n%latex\n\uc2e4\uc218 $x$\uc5d0 \ub300\ud574\uc11c \ub2e4\uc74c\uc774 \uc131\ub9bd\ud55c\ub2e4.\n\\[\n    \\sqrt{x^2}=|x|\n\\] \n\nDan writes:\n\nI've recently learned about xelatex and think it's awesome -- I can\n*finally* include Hangeul in my documents! We should definitely have a xelatex function, although it would usually be necessary to add stuff to the preamble to get the right fonts set up. But we already have\nlatex.add_to_preamble(), so it should be easy to get xelatex working.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8486\n\n",
    "created_at": "2010-03-10T07:38:38Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Xelatex and Sage notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8486",
    "user": "https://github.com/kwankyu"
}
```
Assignee: tbd

I think I want, e.g., the following works in Sage notebook.

%latex
실수 $x$에 대해서 다음이 성립한다.
\[
    \sqrt{x^2}=|x|
\] 

Dan writes:

I've recently learned about xelatex and think it's awesome -- I can
*finally* include Hangeul in my documents! We should definitely have a xelatex function, although it would usually be necessary to add stuff to the preamble to get the right fonts set up. But we already have
latex.add_to_preamble(), so it should be easy to get xelatex working.

Issue created by migration from https://trac.sagemath.org/ticket/8486





---

archive/issue_comments_076344.json:
```json
{
    "body": "Example Sage notebook",
    "created_at": "2010-03-10T07:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76344",
    "user": "https://github.com/kwankyu"
}
```

Example Sage notebook



---

archive/issue_comments_076345.json:
```json
{
    "body": "Attachment [download_worksheets.zip](tarball://root/attachments/some-uuid/ticket8486/download_worksheets.zip) by @kwankyu created at 2010-03-10 07:46:41",
    "created_at": "2010-03-10T07:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76345",
    "user": "https://github.com/kwankyu"
}
```

Attachment [download_worksheets.zip](tarball://root/attachments/some-uuid/ticket8486/download_worksheets.zip) by @kwankyu created at 2010-03-10 07:46:41



---

archive/issue_comments_076346.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T07:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76346",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076347.json:
```json
{
    "body": "The example Sage notebook use the font AppleGothic which is perhaps only found in Mac OS.",
    "created_at": "2010-03-10T07:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76347",
    "user": "https://github.com/kwankyu"
}
```

The example Sage notebook use the font AppleGothic which is perhaps only found in Mac OS.



---

archive/issue_comments_076348.json:
```json
{
    "body": "This looks pretty good. I have some comments and it will need some minor changes, but already it seems to work!\n\nFor anyone else wanting to test this who's using Linux, you can replace the `latex.extra_preamble` with something like\n\n```\nlatex.extra_preamble(\"\\\\\"+r\"usepackage{fontspec,xunicode,xltxtra}\\setmainfont[Mapping=tex-text]{UnBatang}\\setmonofont[Mapping=tex-text,Colour=0000AA]{UnDotum}\")\n```\n\nIn Linux, you should be able to do `fc-list :lang=ko` to get a list of fonts installed that support Korean; pick one and put that in and try this out. XeTeX is a standard part of TeXLive as of TL 2008, so it's not too hard to get.\n\nI'll look over this patch and post my comments soon.",
    "created_at": "2010-03-12T07:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76348",
    "user": "https://github.com/dandrake"
}
```

This looks pretty good. I have some comments and it will need some minor changes, but already it seems to work!

For anyone else wanting to test this who's using Linux, you can replace the `latex.extra_preamble` with something like

```
latex.extra_preamble("\\"+r"usepackage{fontspec,xunicode,xltxtra}\setmainfont[Mapping=tex-text]{UnBatang}\setmonofont[Mapping=tex-text,Colour=0000AA]{UnDotum}")
```

In Linux, you should be able to do `fc-list :lang=ko` to get a list of fonts installed that support Korean; pick one and put that in and try this out. XeTeX is a standard part of TeXLive as of TL 2008, so it's not too hard to get.

I'll look over this patch and post my comments soon.



---

archive/issue_comments_076349.json:
```json
{
    "body": "Hrm, this doesn't pass doctests. The first problem is that the \"official\" way to do deprecation is like this: for the `pdflatex` function (line 1188), you should do:\n\n```\nfrom sage.misc.misc import deprecation\ndeprecation('Use engine(\"pdflatex\") instead.')\nif t is None:\n    return _Latex_prefs._option[\"engine\"] == \"pdflatex\"\nself.engine(\"pdflatex\")\n```\n\nand then in the first doctest that uses the function:\n\n```\nsage: latex.pdflatex()\ndoctest:1: DeprecationWarning: Use engine(\"pdflatex\") instead.\nFalse\n```\n\nAlso, I see that the `pdflatex` function never unsets the pdflatex engine -- I think we need\n\n```\nif t is None:\n    return _Latex_prefs._option[\"engine\"] == \"pdflatex\"\nelif t:\n    self.engine(\"pdflatex\")\nelse:\n    self.engine(\"latex\")\n```\n\nso that `pdflatex(False)` does properly reset the engine.\n\nFinally, in the `png` function (line 1749 or so), you need to change the pdflatex keyword to engine, and change the `_run_latex_` command on line 1795 or so.\n\nHmmm, it seems like the `view` command can call {{{png}} with the pdflatex keyword: see line 1721 or so (I've fiddled with latex.py, so my line numbers are a bit off):\n\n```\npng(objects, os.path.join(base_dir, png_file),\n                debug=debug, do_in_background=False, pdflatex=pdflatex)\n```\n\nI think you'll need to move up the little snippet where you use the pdflatex keyword to decide what engine to use.\n\nWith these changes, doctests should pass.",
    "created_at": "2010-03-16T02:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76349",
    "user": "https://github.com/dandrake"
}
```

Hrm, this doesn't pass doctests. The first problem is that the "official" way to do deprecation is like this: for the `pdflatex` function (line 1188), you should do:

```
from sage.misc.misc import deprecation
deprecation('Use engine("pdflatex") instead.')
if t is None:
    return _Latex_prefs._option["engine"] == "pdflatex"
self.engine("pdflatex")
```

and then in the first doctest that uses the function:

```
sage: latex.pdflatex()
doctest:1: DeprecationWarning: Use engine("pdflatex") instead.
False
```

Also, I see that the `pdflatex` function never unsets the pdflatex engine -- I think we need

```
if t is None:
    return _Latex_prefs._option["engine"] == "pdflatex"
elif t:
    self.engine("pdflatex")
else:
    self.engine("latex")
```

so that `pdflatex(False)` does properly reset the engine.

Finally, in the `png` function (line 1749 or so), you need to change the pdflatex keyword to engine, and change the `_run_latex_` command on line 1795 or so.

Hmmm, it seems like the `view` command can call {{{png}} with the pdflatex keyword: see line 1721 or so (I've fiddled with latex.py, so my line numbers are a bit off):

```
png(objects, os.path.join(base_dir, png_file),
                debug=debug, do_in_background=False, pdflatex=pdflatex)
```

I think you'll need to move up the little snippet where you use the pdflatex keyword to decide what engine to use.

With these changes, doctests should pass.



---

archive/issue_comments_076350.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-16T02:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76350",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076351.json:
```json
{
    "body": "Thank you, Dan. I will work on that.",
    "created_at": "2010-03-16T03:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76351",
    "user": "https://github.com/kwankyu"
}
```

Thank you, Dan. I will work on that.



---

archive/issue_comments_076352.json:
```json
{
    "body": "Attachment [trac_8486.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486.patch) by @kwankyu created at 2010-03-16 13:17:40\n\nUpdated the patch. Now all doctests pass.",
    "created_at": "2010-03-16T13:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76352",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac_8486.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486.patch) by @kwankyu created at 2010-03-16 13:17:40

Updated the patch. Now all doctests pass.



---

archive/issue_comments_076353.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-16T13:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76353",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076354.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-17T08:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76354",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076355.json:
```json
{
    "body": "Doctests pass, and the code looks good. Positive review.\n\nI did write up a little bit of extra documentation; I'll post that patch in a moment. Could you look it over? It just adds a bit of explanation about adding to the preamble.",
    "created_at": "2010-03-17T08:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76355",
    "user": "https://github.com/dandrake"
}
```

Doctests pass, and the code looks good. Positive review.

I did write up a little bit of extra documentation; I'll post that patch in a moment. Could you look it over? It just adds a bit of explanation about adding to the preamble.



---

archive/issue_comments_076356.json:
```json
{
    "body": "add a bit of new documentation.",
    "created_at": "2010-03-17T08:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76356",
    "user": "https://github.com/dandrake"
}
```

add a bit of new documentation.



---

archive/issue_comments_076357.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-17T15:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76357",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076358.json:
```json
{
    "body": "Attachment [trac_8486_extra_documentation.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486_extra_documentation.patch) by @jhpalmieri created at 2010-03-17 15:47:19\n\nUsing `os.system('which xelatex >/dev/null')` won't work right on Solaris: on that OS, \"which\" has a return value of 0 even if the command is not found, so \n\n```\nnot bool(os.system('which xelatex >/dev/null'))\n```\n\nwill always return True there.  Use the function `have_program` from #8474 instead.",
    "created_at": "2010-03-17T15:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76358",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8486_extra_documentation.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486_extra_documentation.patch) by @jhpalmieri created at 2010-03-17 15:47:19

Using `os.system('which xelatex >/dev/null')` won't work right on Solaris: on that OS, "which" has a return value of 0 even if the command is not found, so 

```
not bool(os.system('which xelatex >/dev/null'))
```

will always return True there.  Use the function `have_program` from #8474 instead.



---

archive/issue_comments_076359.json:
```json
{
    "body": "Expanding on this a bit: there has been a fair amount of work getting Sage to work on Solaris, and I think it does as of version 4.3.4.alpha1.  So I think that it is not a good time to put in a patch that doesn't work on Solaris; hence I've marked this as \"needs work\".  All you have to do to fix it is apply the patch at #8474 (now merged in 4.3.4.rc0) and then make the obvious change to this one line of the program...",
    "created_at": "2010-03-17T16:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76359",
    "user": "https://github.com/jhpalmieri"
}
```

Expanding on this a bit: there has been a fair amount of work getting Sage to work on Solaris, and I think it does as of version 4.3.4.alpha1.  So I think that it is not a good time to put in a patch that doesn't work on Solaris; hence I've marked this as "needs work".  All you have to do to fix it is apply the patch at #8474 (now merged in 4.3.4.rc0) and then make the obvious change to this one line of the program...



---

archive/issue_comments_076360.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> Expanding on this a bit: there has been a fair amount of work getting Sage to work on Solaris, and I think it does as of version 4.3.4.alpha1.  So I think that it is not a good time to put in a patch that doesn't work on Solaris; hence I've marked this as \"needs work\".  All you have to do to fix it is apply the patch at #8474 (now merged in 4.3.4.rc0) and then make the obvious change to this one line of the program...\n\nThat sounds good. I was aware of #8474 and decided to ignore that problem and open #8552, so that Kwankyu wouldn't have to rebase his patch -- but if it's a simple one-line change, then I suppose that's more reasonable.\n\nIf I rebase his patch, will you do a quick review?",
    "created_at": "2010-03-17T23:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76360",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:12 jhpalmieri]:
> Expanding on this a bit: there has been a fair amount of work getting Sage to work on Solaris, and I think it does as of version 4.3.4.alpha1.  So I think that it is not a good time to put in a patch that doesn't work on Solaris; hence I've marked this as "needs work".  All you have to do to fix it is apply the patch at #8474 (now merged in 4.3.4.rc0) and then make the obvious change to this one line of the program...

That sounds good. I was aware of #8474 and decided to ignore that problem and open #8552, so that Kwankyu wouldn't have to rebase his patch -- but if it's a simple one-line change, then I suppose that's more reasonable.

If I rebase his patch, will you do a quick review?



---

archive/issue_comments_076361.json:
```json
{
    "body": "Replying to [comment:13 ddrake]:\n> If I rebase his patch, will you do a quick review? \n\nSure, and thanks for offering to rebase it.  (I understand your point, but I don't want to break Solaris support right away.  Let's wait a few weeks instead.  :)",
    "created_at": "2010-03-17T23:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76361",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:13 ddrake]:
> If I rebase his patch, will you do a quick review? 

Sure, and thanks for offering to rebase it.  (I understand your point, but I don't want to break Solaris support right away.  Let's wait a few weeks instead.  :)



---

archive/issue_comments_076362.json:
```json
{
    "body": "Attachment [trac_8486_use_have_program.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486_use_have_program.patch) by @dandrake created at 2010-03-18 01:08:09\n\none-line change to use have_program",
    "created_at": "2010-03-18T01:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76362",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_8486_use_have_program.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486_use_have_program.patch) by @dandrake created at 2010-03-18 01:08:09

one-line change to use have_program



---

archive/issue_comments_076363.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-18T01:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76363",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076364.json:
```json
{
    "body": "John, could you take a look at attachment:trac_8486_use_have_program.patch and attachment:trac_8486_extra_documentation.patch? The first fixes the problem you mentioned and preserves Solaris compatibility (I'm sure Dave Kirkby will appreciate that) and the second just adds a bit of extra documentation.",
    "created_at": "2010-03-18T01:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76364",
    "user": "https://github.com/dandrake"
}
```

John, could you take a look at attachment:trac_8486_use_have_program.patch and attachment:trac_8486_extra_documentation.patch? The first fixes the problem you mentioned and preserves Solaris compatibility (I'm sure Dave Kirkby will appreciate that) and the second just adds a bit of extra documentation.



---

archive/issue_comments_076365.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-18T01:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76365",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076366.json:
```json
{
    "body": "Looks good to me.  One docstring is missing the \"r\" before the triple quotes, so I've added that.",
    "created_at": "2010-03-18T01:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76366",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  One docstring is missing the "r" before the triple quotes, so I've added that.



---

archive/issue_comments_076367.json:
```json
{
    "body": "Attachment [trac_8486-referee.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486-referee.patch) by @kwankyu created at 2010-03-18 01:56:27\n\ncombines and replaces all previous patches",
    "created_at": "2010-03-18T01:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76367",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac_8486-referee.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486-referee.patch) by @kwankyu created at 2010-03-18 01:56:27

combines and replaces all previous patches



---

archive/issue_comments_076368.json:
```json
{
    "body": "Attachment [trac_8486_v2.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486_v2.patch) by @kwankyu created at 2010-03-18 02:04:27\n\nI looked at Dan's extra documentation. It is nice. But I deleted the last comment in the doc of \"engine\" because r\"\\usepackage...\" only fails in the notebook. See the discussion in \n\n!http://groups.google.com/group/sage-devel/browse_frm/thread/71cd8ec6313b7e16/da96b8c19ab45224#da96b8c19ab45224\n\nSee also the ticket 3154 at \n\nhttp://trac.sagemath.org/sage_trac/ticket/3154\n\nSo I think the problem of \"\\u\" in the raw string in notebook is only temporary, assuming the ticket 3154 is reviewed sooner or later.",
    "created_at": "2010-03-18T02:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76368",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac_8486_v2.patch](tarball://root/attachments/some-uuid/ticket8486/trac_8486_v2.patch) by @kwankyu created at 2010-03-18 02:04:27

I looked at Dan's extra documentation. It is nice. But I deleted the last comment in the doc of "engine" because r"\usepackage..." only fails in the notebook. See the discussion in 

!http://groups.google.com/group/sage-devel/browse_frm/thread/71cd8ec6313b7e16/da96b8c19ab45224#da96b8c19ab45224

See also the ticket 3154 at 

http://trac.sagemath.org/sage_trac/ticket/3154

So I think the problem of "\u" in the raw string in notebook is only temporary, assuming the ticket 3154 is reviewed sooner or later.



---

archive/issue_comments_076369.json:
```json
{
    "body": "Okay, the new \"v2\" patch doesn't require the \"referee\" patch.  Only apply the \"v2\" patch.",
    "created_at": "2010-03-18T02:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76369",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, the new "v2" patch doesn't require the "referee" patch.  Only apply the "v2" patch.



---

archive/issue_comments_076370.json:
```json
{
    "body": "Merged \"trac_8486_v2.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76370",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8486_v2.patch" into 4.4.alpha0.



---

archive/issue_comments_076371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8486#issuecomment-76371",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
