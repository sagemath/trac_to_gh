# Issue 3347: [with patches, needs review] lots of changes to the tutorial

archive/issues_003347.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nKeywords: tutorial\n\nI've been working on rewriting the tutorial, moving sections around, deleting things, adding things, etc.  I'm done with a first draft of the \"guided tour\" (chapter 2).  I'll try to get to the rest eventually.\n\nPlease let me know if I've deleted your very favorite section or something like that...\n\nIssue created by migration from https://trac.sagemath.org/ticket/3347\n\n",
    "created_at": "2008-06-01T05:46:17Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patches, needs review] lots of changes to the tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3347",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Keywords: tutorial

I've been working on rewriting the tutorial, moving sections around, deleting things, adding things, etc.  I'm done with a first draft of the "guided tour" (chapter 2).  I'll try to get to the rest eventually.

Please let me know if I've deleted your very favorite section or something like that...

Issue created by migration from https://trac.sagemath.org/ticket/3347





---

archive/issue_comments_023206.json:
```json
{
    "body": "new file macros-new.tex (this is a new version of macros.tex)",
    "created_at": "2008-06-01T05:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23206",
    "user": "https://github.com/jhpalmieri"
}
```

new file macros-new.tex (this is a new version of macros.tex)



---

archive/issue_comments_023207.json:
```json
{
    "body": "Attachment [3347-1.patch](tarball://root/attachments/some-uuid/ticket3347/3347-1.patch) by @jhpalmieri created at 2008-06-01 05:55:07\n\nTwo additional comments: first, the file macros-new.tex is very similar to macros.tex, but I didn't want to break anything in the other parts of the documentation, so tut.tex now calls macros-new.tex while macros.tex is still intact.  The main difference here is that macros-new.tex contains the line \\usepackage{html}, which allows for the use of commands which are parsed one way when the file is run through latex (or pdflatex), and another way when run through latex2html.  It also defines a few commands which rely on this.\n\nSecond, when I was editing the tutorial and running 'make tut' and 'make paper-letter/tut.pdf', for some reason the .aux file wasn't being regenerated, so it kept building with the old .aux file.  This screwed up all of the cross-references.  I don't know if this has to do with my set-up, but if not, be warned that you might get errors unless you do something like (1) manually set TEXINPUTS to be the right thing, and then (2) going to doc/tut/ and running 'pdflatex tut' a few times to update the .aux file.  (You might also want to run 'makeindex tut' while you're there, just for kicks.)",
    "created_at": "2008-06-01T05:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23207",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3347-1.patch](tarball://root/attachments/some-uuid/ticket3347/3347-1.patch) by @jhpalmieri created at 2008-06-01 05:55:07

Two additional comments: first, the file macros-new.tex is very similar to macros.tex, but I didn't want to break anything in the other parts of the documentation, so tut.tex now calls macros-new.tex while macros.tex is still intact.  The main difference here is that macros-new.tex contains the line \usepackage{html}, which allows for the use of commands which are parsed one way when the file is run through latex (or pdflatex), and another way when run through latex2html.  It also defines a few commands which rely on this.

Second, when I was editing the tutorial and running 'make tut' and 'make paper-letter/tut.pdf', for some reason the .aux file wasn't being regenerated, so it kept building with the old .aux file.  This screwed up all of the cross-references.  I don't know if this has to do with my set-up, but if not, be warned that you might get errors unless you do something like (1) manually set TEXINPUTS to be the right thing, and then (2) going to doc/tut/ and running 'pdflatex tut' a few times to update the .aux file.  (You might also want to run 'makeindex tut' while you're there, just for kicks.)



---

archive/issue_comments_023208.json:
```json
{
    "body": "Hi, \n\nCould you explain why you removed the section on Distributed Computing, section 2.13? Right now I don't agree with the removal of that section. I helped with reviewing it several months back and found it very accessible.\n\nThe Table of Contents needs to be updated, for example:\n\n```\n2.1 Arithmetical binary operator precedence\n2.2 Assignment, Equality, Functions, Indentation, and Counting\n2.3 Basic, and not-so-basic, Rings\n... etc\n```\n\nto \n\n```\n2.1 Assignment, Equality, and Arithmetic\n2.2 Getting Help\n2.3 Functions, Indentation, and Counting\n... etc\n```\n",
    "created_at": "2008-06-02T06:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23208",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Hi, 

Could you explain why you removed the section on Distributed Computing, section 2.13? Right now I don't agree with the removal of that section. I helped with reviewing it several months back and found it very accessible.

The Table of Contents needs to be updated, for example:

```
2.1 Arithmetical binary operator precedence
2.2 Assignment, Equality, Functions, Indentation, and Counting
2.3 Basic, and not-so-basic, Rings
... etc
```

to 

```
2.1 Assignment, Equality, and Arithmetic
2.2 Getting Help
2.3 Functions, Indentation, and Counting
... etc
```




---

archive/issue_comments_023209.json:
```json
{
    "body": "Hi,\n\nI made a mistake with the summary. My review is mostly positive. \n\nSorry about the mistake.",
    "created_at": "2008-06-02T06:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23209",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Hi,

I made a mistake with the summary. My review is mostly positive. 

Sorry about the mistake.



---

archive/issue_comments_023210.json:
```json
{
    "body": "Thanks for the comments.\n\nRegarding the table of contents, that may be related to the .aux file problem that I mentioned.  In any case, the table of contents should be regenerated automatically from the tex file.\n\nRegarding the distributed computing stuff, I don't mind putting it back, but I think it doesn't belong in the guided tour (chapter 2).  Maybe it belongs in its own chapter, between the current chapters 5 (programming) and 6 (afterword).  I was also thinking that maybe it didn't belong in a tutorial: a tutorial is not supposed to be a complete reference guide, and I was wondering if this material was perhaps too specialized.\n\nI also found that section choppy: several very short subsections, with titles like \"Introduction\", \"Overview\", and \"Quick start\".  These should probably be combined into one subsection, or maybe two.  I was also a little nervous about whether this whole section was actually complete, because there were some lines commented out like \n\n\n```\n% \\subsection{Deploying dsage} % (fold)\n% To be written...\n% % section deploying_workers (end)\n% \n% \\subsection{Upgrading workers} % (fold)\n% \n% % subsection upgrading_workers (end)\n```\n\n\nIf you think it's okay with these parts missing, and if you think that this material belongs in the tutorial (not just in the reference guide or somewhere else), I'm fine putting it back (but later in the tutorial).  At some point, I think it needs some tightening and rewriting.  Let me know, and I'll make a new patch reinstating it.",
    "created_at": "2008-06-02T17:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23210",
    "user": "https://github.com/jhpalmieri"
}
```

Thanks for the comments.

Regarding the table of contents, that may be related to the .aux file problem that I mentioned.  In any case, the table of contents should be regenerated automatically from the tex file.

Regarding the distributed computing stuff, I don't mind putting it back, but I think it doesn't belong in the guided tour (chapter 2).  Maybe it belongs in its own chapter, between the current chapters 5 (programming) and 6 (afterword).  I was also thinking that maybe it didn't belong in a tutorial: a tutorial is not supposed to be a complete reference guide, and I was wondering if this material was perhaps too specialized.

I also found that section choppy: several very short subsections, with titles like "Introduction", "Overview", and "Quick start".  These should probably be combined into one subsection, or maybe two.  I was also a little nervous about whether this whole section was actually complete, because there were some lines commented out like 


```
% \subsection{Deploying dsage} % (fold)
% To be written...
% % section deploying_workers (end)
% 
% \subsection{Upgrading workers} % (fold)
% 
% % subsection upgrading_workers (end)
```


If you think it's okay with these parts missing, and if you think that this material belongs in the tutorial (not just in the reference guide or somewhere else), I'm fine putting it back (but later in the tutorial).  At some point, I think it needs some tightening and rewriting.  Let me know, and I'll make a new patch reinstating it.



---

archive/issue_comments_023211.json:
```json
{
    "body": "Attachment [3347-2.patch](tarball://root/attachments/some-uuid/ticket3347/3347-2.patch) by @jhpalmieri created at 2008-06-02 19:09:20\n\nchanges to tutorial (large!)",
    "created_at": "2008-06-02T19:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23211",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3347-2.patch](tarball://root/attachments/some-uuid/ticket3347/3347-2.patch) by @jhpalmieri created at 2008-06-02 19:09:20

changes to tutorial (large!)



---

archive/issue_comments_023212.json:
```json
{
    "body": "I certainly think the DSage guide should be in the tutorial somewhere. The section is far more general than say number theory or elliptic curves. I wouldn't worry about finishing the section, but please put it back into the tutorial.",
    "created_at": "2008-06-03T02:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23212",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I certainly think the DSage guide should be in the tutorial somewhere. The section is far more general than say number theory or elliptic curves. I wouldn't worry about finishing the section, but please put it back into the tutorial.



---

archive/issue_comments_023213.json:
```json
{
    "body": "Okay, here's a new version of the patch.  This replaces the old one; the difference is that the dsage stuff has been reinstated (with minor rewordings and re-organization: I combined several sections).",
    "created_at": "2008-06-03T04:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23213",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, here's a new version of the patch.  This replaces the old one; the difference is that the dsage stuff has been reinstated (with minor rewordings and re-organization: I combined several sections).



---

archive/issue_comments_023214.json:
```json
{
    "body": "Fixed one typo in the latest version.",
    "created_at": "2008-06-04T19:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23214",
    "user": "https://github.com/jhpalmieri"
}
```

Fixed one typo in the latest version.



---

archive/issue_comments_023215.json:
```json
{
    "body": "In case it makes things easier for anyone, I've posted a pdf version of the tutorial here:\n\n[http://www.math.washington.edu/~palmieri/Sage/tut/tut.pdf](http://www.math.washington.edu/~palmieri/Sage/tut/tut.pdf)\n\n(I produced this on my linux box, which results in a first page which says \"-1 = -1\".  I don't know why.  When I do it on my mac, this doesn't happen.)\n\nThe html version is also there, in case you want to look at that (although latex2html always seems to be a bit flaky when I use it):\n\n[http://www.math.washington.edu/~palmieri/Sage/tut/index.html](http://www.math.washington.edu/~palmieri/Sage/tut/index.html)",
    "created_at": "2008-06-05T21:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23215",
    "user": "https://github.com/jhpalmieri"
}
```

In case it makes things easier for anyone, I've posted a pdf version of the tutorial here:

[http://www.math.washington.edu/~palmieri/Sage/tut/tut.pdf](http://www.math.washington.edu/~palmieri/Sage/tut/tut.pdf)

(I produced this on my linux box, which results in a first page which says "-1 = -1".  I don't know why.  When I do it on my mac, this doesn't happen.)

The html version is also there, in case you want to look at that (although latex2html always seems to be a bit flaky when I use it):

[http://www.math.washington.edu/~palmieri/Sage/tut/index.html](http://www.math.washington.edu/~palmieri/Sage/tut/index.html)



---

archive/issue_comments_023216.json:
```json
{
    "body": "I printed the tutorial and read it over. It seems to flow better but I have a few minor comments.\n\n1. It would be great if you could get rid of *all* the cases where the text runs into the margins even a tiny bit. The reason why is that for the amazon version of the book (uploaded via createspace.com, as opposed to lulu.com) *any* margin overruns result in the *entire* book being rejected automatically. I fould overruns on pages 8, 16 and 68, but may have missed some.\n2. At some point, \"SAGE Constructions'' will go away and be replaced by \"SAGE Cookbook\". It would not hurt to simply remove the references to the \"Constructions\" document now.\n3. The Examples on page 49 and 52 (which actually started on p 51) have a SAGE banner stating that SAGE is licensed under the GPLv2. Since this has changed to GPLv2+, my feeling is that the examples should be updated to prevent misleading information from leaking out.\n4. On page 82, one reads\n\n\n```\nsage: w         # random 0x number\n<generator object at 0xb0853d6c>\n```\n\nI wonder if\n\n\n```\nsage: w            # vvvvvvvvvv random 0x number\n<generator object at 0xb0853d6c>\n```\n\nmight be clearer?",
    "created_at": "2008-06-07T19:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23216",
    "user": "https://github.com/wdjoyner"
}
```

I printed the tutorial and read it over. It seems to flow better but I have a few minor comments.

1. It would be great if you could get rid of *all* the cases where the text runs into the margins even a tiny bit. The reason why is that for the amazon version of the book (uploaded via createspace.com, as opposed to lulu.com) *any* margin overruns result in the *entire* book being rejected automatically. I fould overruns on pages 8, 16 and 68, but may have missed some.
2. At some point, "SAGE Constructions'' will go away and be replaced by "SAGE Cookbook". It would not hurt to simply remove the references to the "Constructions" document now.
3. The Examples on page 49 and 52 (which actually started on p 51) have a SAGE banner stating that SAGE is licensed under the GPLv2. Since this has changed to GPLv2+, my feeling is that the examples should be updated to prevent misleading information from leaking out.
4. On page 82, one reads


```
sage: w         # random 0x number
<generator object at 0xb0853d6c>
```

I wonder if


```
sage: w            # vvvvvvvvvv random 0x number
<generator object at 0xb0853d6c>
```

might be clearer?



---

archive/issue_comments_023217.json:
```json
{
    "body": "For item 1, margin overruns, I can easily fix some of them, but some of them are verbatim output from sage, and I don't know what I can do about these.  For example, on page 56, the output from hitting '?' at the ipdb> prompt runs into the right margin.  Should I delete this output altogether?  There is a similar situation on p. 86, output from 'prun', and also on p. 29 (hard to see): the second line of output from I.primary_decomposition().  Is the issue running off of the page, or just running into the margin?\n\nAt the moment, I've cheated: I've altered the output for these commands, adding in artificial line breaks for readability.  I've only had to do this a few times, so I'm not too worried about it.\n\nFor point 2, I disagree that \"it wouldn't hurt\" to remove references to Sage Constructions: I think it's important to have pointers for where to look for more information.  So my opinion is, whenever Sage Constructions gets replaced by something else, whoever is responsible for that change should also make the corresponding change to the tutorial.  If we delete all references to Sage Constructions now, the tutorial will be less informative, hence not as good.\n\nFor point 3, that's easy enough to fix.  [Actually, taking a look, that banner is quite old, and the GPL stuff isn't mentioned at all in the banner any more.  I've replaced it with a newer banner.]\n\nFor point 4, I haven't even gotten that far in my changes, but I'll add something relevant there.\n\nI'll post a patch which adds these changes.  When I get a chance, I'll update the pdf and html versions on my web page.",
    "created_at": "2008-06-11T05:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23217",
    "user": "https://github.com/jhpalmieri"
}
```

For item 1, margin overruns, I can easily fix some of them, but some of them are verbatim output from sage, and I don't know what I can do about these.  For example, on page 56, the output from hitting '?' at the ipdb> prompt runs into the right margin.  Should I delete this output altogether?  There is a similar situation on p. 86, output from 'prun', and also on p. 29 (hard to see): the second line of output from I.primary_decomposition().  Is the issue running off of the page, or just running into the margin?

At the moment, I've cheated: I've altered the output for these commands, adding in artificial line breaks for readability.  I've only had to do this a few times, so I'm not too worried about it.

For point 2, I disagree that "it wouldn't hurt" to remove references to Sage Constructions: I think it's important to have pointers for where to look for more information.  So my opinion is, whenever Sage Constructions gets replaced by something else, whoever is responsible for that change should also make the corresponding change to the tutorial.  If we delete all references to Sage Constructions now, the tutorial will be less informative, hence not as good.

For point 3, that's easy enough to fix.  [Actually, taking a look, that banner is quite old, and the GPL stuff isn't mentioned at all in the banner any more.  I've replaced it with a newer banner.]

For point 4, I haven't even gotten that far in my changes, but I'll add something relevant there.

I'll post a patch which adds these changes.  When I get a chance, I'll update the pdf and html versions on my web page.



---

archive/issue_comments_023218.json:
```json
{
    "body": "margin overruns, Sage banner, etc.  Use this patch in addition to the earlier one.",
    "created_at": "2008-06-11T05:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23218",
    "user": "https://github.com/jhpalmieri"
}
```

margin overruns, Sage banner, etc.  Use this patch in addition to the earlier one.



---

archive/issue_comments_023219.json:
```json
{
    "body": "Attachment [3347-3.patch](tarball://root/attachments/some-uuid/ticket3347/3347-3.patch) by @jhpalmieri created at 2008-06-11 20:17:10\n\nThe latest version of the file '3347-2-with-dsage.patch' just fixes a few typos that I'd made in earlier versions.",
    "created_at": "2008-06-11T20:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23219",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3347-3.patch](tarball://root/attachments/some-uuid/ticket3347/3347-3.patch) by @jhpalmieri created at 2008-06-11 20:17:10

The latest version of the file '3347-2-with-dsage.patch' just fixes a few typos that I'd made in earlier versions.



---

archive/issue_comments_023220.json:
```json
{
    "body": "changes to tutorial (large!) -- this includes the DSAGE section, and replaces the previous patch (if people like it better)",
    "created_at": "2008-06-11T21:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23220",
    "user": "https://github.com/jhpalmieri"
}
```

changes to tutorial (large!) -- this includes the DSAGE section, and replaces the previous patch (if people like it better)



---

archive/issue_comments_023221.json:
```json
{
    "body": "Attachment [3347-2-with-dsage.patch](tarball://root/attachments/some-uuid/ticket3347/3347-2-with-dsage.patch) by @craigcitro created at 2008-06-15 21:50:34",
    "created_at": "2008-06-15T21:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23221",
    "user": "https://github.com/craigcitro"
}
```

Attachment [3347-2-with-dsage.patch](tarball://root/attachments/some-uuid/ticket3347/3347-2-with-dsage.patch) by @craigcitro created at 2008-06-15 21:50:34



---

archive/issue_comments_023222.json:
```json
{
    "body": "Changing keywords from \"tutorial\" to \"tutorial, editor_mhansen\".",
    "created_at": "2008-06-15T21:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23222",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "tutorial" to "tutorial, editor_mhansen".



---

archive/issue_comments_023223.json:
```json
{
    "body": "I tried applying 3347-1.patch and then 3347-2-with-dsage.patch errors applying the patch.  Could you clarify which patches are supposed to be applied in which order?",
    "created_at": "2008-06-19T20:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23223",
    "user": "https://github.com/mwhansen"
}
```

I tried applying 3347-1.patch and then 3347-2-with-dsage.patch errors applying the patch.  Could you clarify which patches are supposed to be applied in which order?



---

archive/issue_comments_023224.json:
```json
{
    "body": "*I tried applying 3347-1.patch and then 3347-2-with-dsage.patch errors applying the patch. Could you clarify which patches are supposed to be applied in which order?*\n\nSorry.  Apply *3347-1.patch* and *3347-2-with-dsage.patch* first (these two are independent of each other), then apply 3347-3.patch.",
    "created_at": "2008-06-19T20:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23224",
    "user": "https://github.com/jhpalmieri"
}
```

*I tried applying 3347-1.patch and then 3347-2-with-dsage.patch errors applying the patch. Could you clarify which patches are supposed to be applied in which order?*

Sorry.  Apply *3347-1.patch* and *3347-2-with-dsage.patch* first (these two are independent of each other), then apply 3347-3.patch.



---

archive/issue_comments_023225.json:
```json
{
    "body": "Attachment [3347-new.patch](tarball://root/attachments/some-uuid/ticket3347/3347-new.patch) by @jhpalmieri created at 2008-06-19 20:52:43\n\nuse 3347-1.patch and this patch (against tutorial from sage 3.0.3)",
    "created_at": "2008-06-19T20:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23225",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3347-new.patch](tarball://root/attachments/some-uuid/ticket3347/3347-new.patch) by @jhpalmieri created at 2008-06-19 20:52:43

use 3347-1.patch and this patch (against tutorial from sage 3.0.3)



---

archive/issue_comments_023226.json:
```json
{
    "body": "Ignore my previous post. I've created a new patch, *3347-new.patch*, which combines the other patches to tut.tex.  Use this and *3347-1.patch*; the order shouldn't matter, since they're patching different files.\n\nI think the issue before was that my patch was built against the tutorial in sage 3.0.2 and was breaking on the one in 3.0.3.",
    "created_at": "2008-06-19T20:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23226",
    "user": "https://github.com/jhpalmieri"
}
```

Ignore my previous post. I've created a new patch, *3347-new.patch*, which combines the other patches to tut.tex.  Use this and *3347-1.patch*; the order shouldn't matter, since they're patching different files.

I think the issue before was that my patch was built against the tutorial in sage 3.0.2 and was breaking on the one in 3.0.3.



---

archive/issue_comments_023227.json:
```json
{
    "body": "Attachment [3347.patch](tarball://root/attachments/some-uuid/ticket3347/3347.patch) by @mwhansen created at 2008-06-19 20:59:23",
    "created_at": "2008-06-19T20:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23227",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3347.patch](tarball://root/attachments/some-uuid/ticket3347/3347.patch) by @mwhansen created at 2008-06-19 20:59:23



---

archive/issue_comments_023228.json:
```json
{
    "body": "The final 3347.patch is the _only_ one that should be applied, and it applies cleanly against 3.0.3.",
    "created_at": "2008-06-19T21:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23228",
    "user": "https://github.com/mwhansen"
}
```

The final 3347.patch is the _only_ one that should be applied, and it applies cleanly against 3.0.3.



---

archive/issue_comments_023229.json:
```json
{
    "body": "Merged 3347.patch only in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T11:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23229",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3347.patch only in Sage 3.0.4.alpha0



---

archive/issue_events_003565.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-06-23T11:39:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3347#event-3565"
}
```



---

archive/issue_comments_023230.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T11:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3347#issuecomment-23230",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
