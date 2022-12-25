# Issue 8489: New `sageexample` environment for sagetex

archive/issues_008489.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dandrake @zimmermann6\n\nKeywords: sagetex, doctest\n\nThe attached patch for sagetex adds a new sageexample environment for sagetex:\n\n\n```\n\\begin{sageexample}\n  sage: 1+1\n  2\n  sage: x^3\n  x^3\n\\end{sageexample}\n```\n\n\nThe (ultimate) goal is to allow for straightforward copy paste of\npieces of sage doctests into one's latex document. See the attached\npdf (the sources of which are included in the patch) for details.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8489\n\n",
    "created_at": "2010-03-10T15:24:32Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "New `sageexample` environment for sagetex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8489",
    "user": "https://github.com/nthiery"
}
```
Assignee: mvngu

CC:  @dandrake @zimmermann6

Keywords: sagetex, doctest

The attached patch for sagetex adds a new sageexample environment for sagetex:


```
\begin{sageexample}
  sage: 1+1
  2
  sage: x^3
  x^3
\end{sageexample}
```


The (ultimate) goal is to allow for straightforward copy paste of
pieces of sage doctests into one's latex document. See the attached
pdf (the sources of which are included in the patch) for details.



Issue created by migration from https://trac.sagemath.org/ticket/8489





---

archive/issue_comments_076411.json:
```json
{
    "body": "Attachment [trac_8489-sagetex_sageexample-nt.patch](tarball://root/attachments/some-uuid/ticket8489/trac_8489-sagetex_sageexample-nt.patch) by @nthiery created at 2010-03-10 15:25:44",
    "created_at": "2010-03-10T15:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76411",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8489-sagetex_sageexample-nt.patch](tarball://root/attachments/some-uuid/ticket8489/trac_8489-sagetex_sageexample-nt.patch) by @nthiery created at 2010-03-10 15:25:44



---

archive/issue_comments_076412.json:
```json
{
    "body": "Attachment [example-sageexample.pdf](tarball://root/attachments/some-uuid/ticket8489/example-sageexample.pdf) by @nthiery created at 2010-03-10 15:27:06",
    "created_at": "2010-03-10T15:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76412",
    "user": "https://github.com/nthiery"
}
```

Attachment [example-sageexample.pdf](tarball://root/attachments/some-uuid/ticket8489/example-sageexample.pdf) by @nthiery created at 2010-03-10 15:27:06



---

archive/issue_comments_076413.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T15:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76413",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076414.json:
```json
{
    "body": "Attachment [sagetex-2.2.3.p0.spkg](tarball://root/attachments/some-uuid/ticket8489/sagetex-2.2.3.p0.spkg) by @nthiery created at 2010-03-10 15:41:28\n\nClone of the current spkg, with patch applied, but version number not bumped up",
    "created_at": "2010-03-10T15:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76414",
    "user": "https://github.com/nthiery"
}
```

Attachment [sagetex-2.2.3.p0.spkg](tarball://root/attachments/some-uuid/ticket8489/sagetex-2.2.3.p0.spkg) by @nthiery created at 2010-03-10 15:41:28

Clone of the current spkg, with patch applied, but version number not bumped up



---

archive/issue_comments_076415.json:
```json
{
    "body": "Hrm, your spkg contains a core dump from pdflatex. Perhaps that's a bad sign? :)\n\nI'll take a look at this, and probably include it. My long-term goal is that you shouldn't need to include the answer -- you should just put `((x+1)^3).expand()` and it would automatically insert the nicely typeset version of `x^3 + 3*x^2 + 3*x + 1`.",
    "created_at": "2010-03-11T07:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76415",
    "user": "https://github.com/dandrake"
}
```

Hrm, your spkg contains a core dump from pdflatex. Perhaps that's a bad sign? :)

I'll take a look at this, and probably include it. My long-term goal is that you shouldn't need to include the answer -- you should just put `((x+1)^3).expand()` and it would automatically insert the nicely typeset version of `x^3 + 3*x^2 + 3*x + 1`.



---

archive/issue_comments_076416.json:
```json
{
    "body": "Also, I should add that a nice way to make improvements to SageTeX is to clone http://bitbucket.org/ddrake/sagetex/ and send me patches. :)  In the spkg, you added your changes into the root hg repo, which just tracks SPKG.txt, spkg-install, and so on.",
    "created_at": "2010-03-11T08:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76416",
    "user": "https://github.com/dandrake"
}
```

Also, I should add that a nice way to make improvements to SageTeX is to clone http://bitbucket.org/ddrake/sagetex/ and send me patches. :)  In the spkg, you added your changes into the root hg repo, which just tracks SPKG.txt, spkg-install, and so on.



---

archive/issue_comments_076417.json:
```json
{
    "body": "There's a spkg at http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.4.spkg that includes these changes. It needs further documentation, but you should be able to take the example file included in attachment:trac_8489-sagetex_sageexample-nt.patch and typeset it with the new spkg. There's also some examples in the usual example.tex file.\n\nI have had troubles getting doctesting to work -- every time I try `sage -t my_file.sage`, it fails with a \"mysterious error\". Same thing if I try with the .py file.",
    "created_at": "2010-03-15T01:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76417",
    "user": "https://github.com/dandrake"
}
```

There's a spkg at http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.4.spkg that includes these changes. It needs further documentation, but you should be able to take the example file included in attachment:trac_8489-sagetex_sageexample-nt.patch and typeset it with the new spkg. There's also some examples in the usual example.tex file.

I have had troubles getting doctesting to work -- every time I try `sage -t my_file.sage`, it fails with a "mysterious error". Same thing if I try with the .py file.



---

archive/issue_comments_076418.json:
```json
{
    "body": "Replying to [comment:4 ddrake]:\n> Also, I should add that a nice way to make improvements to SageTeX is to clone http://bitbucket.org/ddrake/sagetex/ and send me patches. :)  In the spkg, you added your changes into the root hg repo, which just tracks SPKG.txt, spkg-install, and so on.\n\nAh, great, thanks for the link! I googled for it, somehow missed it, and went for the quickest way to send you a patch.",
    "created_at": "2010-03-17T22:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76418",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 ddrake]:
> Also, I should add that a nice way to make improvements to SageTeX is to clone http://bitbucket.org/ddrake/sagetex/ and send me patches. :)  In the spkg, you added your changes into the root hg repo, which just tracks SPKG.txt, spkg-install, and so on.

Ah, great, thanks for the link! I googled for it, somehow missed it, and went for the quickest way to send you a patch.



---

archive/issue_comments_076419.json:
```json
{
    "body": "Replying to [comment:3 ddrake]:\n> Hrm, your spkg contains a core dump from pdflatex. Perhaps that's a bad sign? :)\n\nYeah, I am not patient, and did kill pdflatex the hard way a couple times while trying things around :-)",
    "created_at": "2010-03-17T22:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76419",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 ddrake]:
> Hrm, your spkg contains a core dump from pdflatex. Perhaps that's a bad sign? :)

Yeah, I am not patient, and did kill pdflatex the hard way a couple times while trying things around :-)



---

archive/issue_comments_076420.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> I have had troubles getting doctesting to work -- every time I try `sage -t my_file.sage`, it fails with a \"mysterious error\". Same thing if I try with the .py file. \n\nYeah, just reusing my_file.sage looked cool, and worked on trivial examples, but that is not robust. I am about to upload a new patch which produces a separate file with just the doctests, and that seems to work fine (and is probably more readable by the user in case of trouble).",
    "created_at": "2010-03-17T23:00:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76420",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 ddrake]:
> I have had troubles getting doctesting to work -- every time I try `sage -t my_file.sage`, it fails with a "mysterious error". Same thing if I try with the .py file. 

Yeah, just reusing my_file.sage looked cool, and worked on trivial examples, but that is not robust. I am about to upload a new patch which produces a separate file with just the doctests, and that seems to work fine (and is probably more readable by the user in case of trouble).



---

archive/issue_comments_076421.json:
```json
{
    "body": "Attachment [doctest-spacing-nt.patch](tarball://root/attachments/some-uuid/ticket8489/doctest-spacing-nt.patch) by @nthiery created at 2010-03-17 23:34:17",
    "created_at": "2010-03-17T23:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76421",
    "user": "https://github.com/nthiery"
}
```

Attachment [doctest-spacing-nt.patch](tarball://root/attachments/some-uuid/ticket8489/doctest-spacing-nt.patch) by @nthiery created at 2010-03-17 23:34:17



---

archive/issue_comments_076422.json:
```json
{
    "body": "Changing assignee from mvngu to @nthiery.",
    "created_at": "2010-03-17T23:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76422",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from mvngu to @nthiery.



---

archive/issue_comments_076423.json:
```json
{
    "body": "I've merged your doctest-spacing patch into SageTeX, and made some improvements -- the doctest file is now called `\\jobname_doctest.sage`, and is only created if the user actually has a `sageexample` environment. It also includes a bit of explanatory text.\n\nI also changed your vertical space fix to use `\\abovedisplayskip` and friends, which I just learned about from http://www.ctan.org/tex-archive/info/math/voss/mathmode/.\n\nThere's more fixups to the documentation that should be done, but it seems to be working properly. Please pull from the bitbucket repo and test. I think I'll make a spkg for this new version and see if we can get it into the next Sage release.",
    "created_at": "2010-03-25T03:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76423",
    "user": "https://github.com/dandrake"
}
```

I've merged your doctest-spacing patch into SageTeX, and made some improvements -- the doctest file is now called `\jobname_doctest.sage`, and is only created if the user actually has a `sageexample` environment. It also includes a bit of explanatory text.

I also changed your vertical space fix to use `\abovedisplayskip` and friends, which I just learned about from http://www.ctan.org/tex-archive/info/math/voss/mathmode/.

There's more fixups to the documentation that should be done, but it seems to be working properly. Please pull from the bitbucket repo and test. I think I'll make a spkg for this new version and see if we can get it into the next Sage release.



---

archive/issue_comments_076424.json:
```json
{
    "body": "This should be closed when #8605 is merged (possibly just closed now, since the changes are for upstream, not for something that is Sage code).",
    "created_at": "2010-03-30T03:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76424",
    "user": "https://github.com/jasongrout"
}
```

This should be closed when #8605 is merged (possibly just closed now, since the changes are for upstream, not for something that is Sage code).



---

archive/issue_comments_076425.json:
```json
{
    "body": "For reference: Copy-paste from a PDF document to a Sage session won't necessarily work. That is, if a sageexample environment contains strings defined using (simple) quotes, those quotes can be rendered in PDF by differents characters: backquotes and quotes. The encoding used in TeX sources files seems to have its role here.\n\n\n```\n\\documentclass[12pt]{book}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}\n\\usepackage{sagetex}\n\\usepackage[frenchb]{babel}\n\\begin{document}\n\\begin{sageexample}\n    sage: x, y, a, b, c, d = var('x y a b c d')\n\\end{sageexample}\n\\end{document}\n```\n\nReplying to [ticket:8489 nthiery]:\n\n> The (ultimate) goal is to allow for straightforward copy paste of pieces of sage doctests into one's latex document. See the attached pdf (the sources of which are included in the patch) for details.^^",
    "created_at": "2010-03-30T21:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76425",
    "user": "https://github.com/orontee"
}
```

For reference: Copy-paste from a PDF document to a Sage session won't necessarily work. That is, if a sageexample environment contains strings defined using (simple) quotes, those quotes can be rendered in PDF by differents characters: backquotes and quotes. The encoding used in TeX sources files seems to have its role here.


```
\documentclass[12pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{sagetex}
\usepackage[frenchb]{babel}
\begin{document}
\begin{sageexample}
    sage: x, y, a, b, c, d = var('x y a b c d')
\end{sageexample}
\end{document}
```

Replying to [ticket:8489 nthiery]:

> The (ultimate) goal is to allow for straightforward copy paste of pieces of sage doctests into one's latex document. See the attached pdf (the sources of which are included in the patch) for details.^^



---

archive/issue_comments_076426.json:
```json
{
    "body": "Example of quotes changed to backquotes in PDF",
    "created_at": "2010-03-30T21:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76426",
    "user": "https://github.com/orontee"
}
```

Example of quotes changed to backquotes in PDF



---

archive/issue_comments_076427.json:
```json
{
    "body": "Attachment [test.pdf](tarball://root/attachments/some-uuid/ticket8489/test.pdf) by @jasongrout created at 2010-04-15 02:28:57\n\nddrake: what do you say about the last comment about quotes being changed?",
    "created_at": "2010-04-15T02:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76427",
    "user": "https://github.com/jasongrout"
}
```

Attachment [test.pdf](tarball://root/attachments/some-uuid/ticket8489/test.pdf) by @jasongrout created at 2010-04-15 02:28:57

ddrake: what do you say about the last comment about quotes being changed?



---

archive/issue_comments_076428.json:
```json
{
    "body": "The following has no effect on sageexample environments:\n\n\\setlength{\\sagetexindent}{15ex}\n\nSeems to be a bug, no?",
    "created_at": "2010-04-19T22:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76428",
    "user": "https://github.com/orontee"
}
```

The following has no effect on sageexample environments:

\setlength{\sagetexindent}{15ex}

Seems to be a bug, no?



---

archive/issue_comments_076429.json:
```json
{
    "body": "Replying to [comment:13 jason]:\n> ddrake: what do you say about the last comment about quotes being changed?\n\nI'm not sure how to fix that. I don't think it's an issue about encoding in the document; a single straight quote (ASCII character 39) should be the same in any non-crazy encoding, since all reasonable encodings that I know of agree for characters 0 to 127.\n\nThe issue, I think, is the character that gets put into the final PDF. I'm not sure how to bypass the usual TeX behavior of turning single quotes into curly final quotes.\n\nIn any case, Nicolas' original goal is cut and paste from Sage into a LaTeX document, which works now.\n\nIf this is a highly desired feature, I could work on it, but since cut and paste of things with single quotes generally doesn't work from TeX-generated PDFs anyway, I'm not sure how important this should be.",
    "created_at": "2010-04-20T06:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76429",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:13 jason]:
> ddrake: what do you say about the last comment about quotes being changed?

I'm not sure how to fix that. I don't think it's an issue about encoding in the document; a single straight quote (ASCII character 39) should be the same in any non-crazy encoding, since all reasonable encodings that I know of agree for characters 0 to 127.

The issue, I think, is the character that gets put into the final PDF. I'm not sure how to bypass the usual TeX behavior of turning single quotes into curly final quotes.

In any case, Nicolas' original goal is cut and paste from Sage into a LaTeX document, which works now.

If this is a highly desired feature, I could work on it, but since cut and paste of things with single quotes generally doesn't work from TeX-generated PDFs anyway, I'm not sure how important this should be.



---

archive/issue_comments_076430.json:
```json
{
    "body": "Replying to [comment:14 mmeulien]:\n> The following has no effect on sageexample environments:\n> \n> \\setlength{\\sagetexindent}{15ex}\n> \n> Seems to be a bug, no?\n\nHmmm. I tried to get the indent to work, but adding an hspace in the obvious places didn't work. I can investigate this more, but one problem is that the example environment works in a completely different way than the other verbatim-like environments. I'll look into this and see if I can figure it out. Changing the parindent might work.",
    "created_at": "2010-04-20T07:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76430",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:14 mmeulien]:
> The following has no effect on sageexample environments:
> 
> \setlength{\sagetexindent}{15ex}
> 
> Seems to be a bug, no?

Hmmm. I tried to get the indent to work, but adding an hspace in the obvious places didn't work. I can investigate this more, but one problem is that the example environment works in a completely different way than the other verbatim-like environments. I'll look into this and see if I can figure it out. Changing the parindent might work.



---

archive/issue_comments_076431.json:
```json
{
    "body": "Since #8605 is closed, should this be closed also?  It looks like there is still discussion going on here...",
    "created_at": "2010-04-23T17:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76431",
    "user": "https://github.com/jhpalmieri"
}
```

Since #8605 is closed, should this be closed also?  It looks like there is still discussion going on here...



---

archive/issue_comments_076432.json:
```json
{
    "body": "This ticket is marked as \"needs review\", but is there anything still to review here?  Have the relevant pieces been merged into the sagetex spkg by now?",
    "created_at": "2010-07-22T22:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76432",
    "user": "https://github.com/jhpalmieri"
}
```

This ticket is marked as "needs review", but is there anything still to review here?  Have the relevant pieces been merged into the sagetex spkg by now?



---

archive/issue_comments_076433.json:
```json
{
    "body": "I think this ticket should be closed, since the sageexample environment has been implemented, and we ship a version of SageTeX with it. If there are further problems with sageexample, someone should open a new ticket.",
    "created_at": "2010-07-28T03:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76433",
    "user": "https://github.com/dandrake"
}
```

I think this ticket should be closed, since the sageexample environment has been implemented, and we ship a version of SageTeX with it. If there are further problems with sageexample, someone should open a new ticket.



---

archive/issue_comments_076434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-28T03:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8489#issuecomment-76434",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
