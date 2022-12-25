# Issue 3728: tutorial: add documentation for solving matrix equations

archive/issues_003728.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: tutorial, matrix equations\n\nI don't think that the current documentation for solving matrix equations is sufficient, so I've added a little bit in the \"linear algebra\" section of the guided tour in the tutorial.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3728\n\n",
    "created_at": "2008-07-26T16:27:11Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "tutorial: add documentation for solving matrix equations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3728",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

Keywords: tutorial, matrix equations

I don't think that the current documentation for solving matrix equations is sufficient, so I've added a little bit in the "linear algebra" section of the guided tour in the tutorial.



Issue created by migration from https://trac.sagemath.org/ticket/3728





---

archive/issue_comments_026401.json:
```json
{
    "body": "Attachment [3728.patch](tarball://root/attachments/some-uuid/ticket3728/3728.patch) by @jhpalmieri created at 2008-07-26 16:27:43\n\ndocumentation for solving matrix equations",
    "created_at": "2008-07-26T16:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26401",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3728.patch](tarball://root/attachments/some-uuid/ticket3728/3728.patch) by @jhpalmieri created at 2008-07-26 16:27:43

documentation for solving matrix equations



---

archive/issue_comments_026402.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-07-26T16:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26402",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_026403.json:
```json
{
    "body": "I tried to apply the patch but was unable to:\n\n```\nsage: hg_sage.apply(\"/home/john/3728.patch\")\ncd \"/home/john/sage-3.0.4/devel/sage\" && hg status\ncd \"/home/john/sage-3.0.4/devel/sage\" && hg status\ncd \"/home/john/sage-3.0.4/devel/sage\" && hg import   \"/home/john/3728.patch\"\napplying /home/john/3728.patch\nabort: unable to find tut/tut.tex or tut/tut.tex for patching\n```\n\n\nI'm not sure if that is my fault or the patch's.\n\nSecondly, why not include the abbreviated form :\n\n```\nsage: A\\z\n(-2, 1, 0)\n```\n\n\nOf course this is otherwise a useful addition to the tutorial.",
    "created_at": "2008-07-29T02:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26403",
    "user": "https://github.com/JohnCremona"
}
```

I tried to apply the patch but was unable to:

```
sage: hg_sage.apply("/home/john/3728.patch")
cd "/home/john/sage-3.0.4/devel/sage" && hg status
cd "/home/john/sage-3.0.4/devel/sage" && hg status
cd "/home/john/sage-3.0.4/devel/sage" && hg import   "/home/john/3728.patch"
applying /home/john/3728.patch
abort: unable to find tut/tut.tex or tut/tut.tex for patching
```


I'm not sure if that is my fault or the patch's.

Secondly, why not include the abbreviated form :

```
sage: A\z
(-2, 1, 0)
```


Of course this is otherwise a useful addition to the tutorial.



---

archive/issue_comments_026404.json:
```json
{
    "body": "For the first item, try `hg_doc.apply` instead of `hg_sage.apply`.  The second is a good idea, and I'll submit a new patch including something relevant.\n\n(a few minutes later)\n\nHaving tried to including something about backslashes, I find that I can't include lines like\n\n```\n\\begin{verbatim}\nsage: A \\ Y\n(-2, 1, 0)\n\\end{verbatim}\n```\n\nbecause the `\\` in the verbatim environment seems to mess up the doctesting, leading to a failure.  Right now I have a compromise situation, discussing the backslash in the text, without including a testable example.  Looks like we might need a trac ticket for fixing the doctesting...",
    "created_at": "2008-07-29T03:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26404",
    "user": "https://github.com/jhpalmieri"
}
```

For the first item, try `hg_doc.apply` instead of `hg_sage.apply`.  The second is a good idea, and I'll submit a new patch including something relevant.

(a few minutes later)

Having tried to including something about backslashes, I find that I can't include lines like

```
\begin{verbatim}
sage: A \ Y
(-2, 1, 0)
\end{verbatim}
```

because the `\` in the verbatim environment seems to mess up the doctesting, leading to a failure.  Right now I have a compromise situation, discussing the backslash in the text, without including a testable example.  Looks like we might need a trac ticket for fixing the doctesting...



---

archive/issue_comments_026405.json:
```json
{
    "body": "new version of patch; this replaces the old one",
    "created_at": "2008-07-29T03:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26405",
    "user": "https://github.com/jhpalmieri"
}
```

new version of patch; this replaces the old one



---

archive/issue_comments_026406.json:
```json
{
    "body": "Attachment [3728-new.patch](tarball://root/attachments/some-uuid/ticket3728/3728-new.patch) by @JohnCremona created at 2008-07-29 11:40:23\n\nThanks for the tip about hg_doc.  I applied the patch ok, but I don't know how to view the patched tutorial!",
    "created_at": "2008-07-29T11:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26406",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [3728-new.patch](tarball://root/attachments/some-uuid/ticket3728/3728-new.patch) by @JohnCremona created at 2008-07-29 11:40:23

Thanks for the tip about hg_doc.  I applied the patch ok, but I don't know how to view the patched tutorial!



---

archive/issue_comments_026407.json:
```json
{
    "body": "Here's what I do: \n\n```\ncd ...sage/devel/doc\nmake tut\n```\n\nThen you can use the notebook interface and click on the \"Help\" button at the top right to get the new version.\n\nIn addition to 'make tut', you can also do `make paper-letter/tut.pdf` or `make paper-a4/tut.pdf`, which creates those pdf files (.../sage/devel/doc/paper-letter/tut.pdf, for example).",
    "created_at": "2008-07-29T15:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26407",
    "user": "https://github.com/jhpalmieri"
}
```

Here's what I do: 

```
cd ...sage/devel/doc
make tut
```

Then you can use the notebook interface and click on the "Help" button at the top right to get the new version.

In addition to 'make tut', you can also do `make paper-letter/tut.pdf` or `make paper-a4/tut.pdf`, which creates those pdf files (.../sage/devel/doc/paper-letter/tut.pdf, for example).



---

archive/issue_events_008531.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2008-07-29T20:41:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "milestone": "sage-3.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3728#event-8531"
}
```



---

archive/issue_comments_026408.json:
```json
{
    "body": "I had another go at applying this patch, but \"make tut\" does not work for me.  Sorry, someone else will have to do this.  Of course the new paragraph looks ok when I read the raw latex.",
    "created_at": "2008-09-02T17:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26408",
    "user": "https://github.com/JohnCremona"
}
```

I had another go at applying this patch, but "make tut" does not work for me.  Sorry, someone else will have to do this.  Of course the new paragraph looks ok when I read the raw latex.



---

archive/issue_comments_026409.json:
```json
{
    "body": "I read the diff file and appears to be a useful addition to the tutorial explaining an example of solving a matrix equation. Then I tried the patch but it would not apply to 3.1.2.alpha4 using hg_doc.apply. Sorry.",
    "created_at": "2008-09-03T00:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26409",
    "user": "https://github.com/wdjoyner"
}
```

I read the diff file and appears to be a useful addition to the tutorial explaining an example of solving a matrix equation. Then I tried the patch but it would not apply to 3.1.2.alpha4 using hg_doc.apply. Sorry.



---

archive/issue_comments_026410.json:
```json
{
    "body": "I just tested it against 3.1.1 and it worked fine.  I'll try to produce a new patch against 3.1.2alpha4...",
    "created_at": "2008-09-03T01:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26410",
    "user": "https://github.com/jhpalmieri"
}
```

I just tested it against 3.1.1 and it worked fine.  I'll try to produce a new patch against 3.1.2alpha4...



---

archive/issue_comments_026411.json:
```json
{
    "body": "Well, the patch `3728-new.patch` worked for *me* with hg_doc.apply in 3.1.2.alpha4.  Could you try again?",
    "created_at": "2008-09-03T04:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26411",
    "user": "https://github.com/jhpalmieri"
}
```

Well, the patch `3728-new.patch` worked for *me* with hg_doc.apply in 3.1.2.alpha4.  Could you try again?



---

archive/issue_comments_026412.json:
```json
{
    "body": "hg_doc.apply opens a new screen containing this diff file:\n\n\n```\n\n\n\n\n\n\n\n\n\ndiff -r 493137a28022 commontex/patchlevel.tex\n--- a/commontex/patchlevel.tex  Tue Sep 02 05:22:45 2008 -0700\n+++ b/commontex/patchlevel.tex  Wed Sep 03 05:58:39 2008 -0400\n@@ -1,6 +1,6 @@\n % This file is generated by ../tools/getversioninfo;\n % do not edit manually.\n\n-\\release{3.1.2.alpha3}\n+\\release{3.1.2.alpha4}\n \\setreleaseinfo{}\n-\\setshortversion{3.1.2.alpha3}\n+\\setshortversion{3.1.2.alpha4}\n```\n\nPressing q dumps me into vi session. Then I get a runtime error:\n\n\n```\nRuntimeError: Refusing to do operation since you still have unrecorded changes. You must check in all changes in your working repository first.\n```\n",
    "created_at": "2008-09-03T10:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26412",
    "user": "https://github.com/wdjoyner"
}
```

hg_doc.apply opens a new screen containing this diff file:


```









diff -r 493137a28022 commontex/patchlevel.tex
--- a/commontex/patchlevel.tex  Tue Sep 02 05:22:45 2008 -0700
+++ b/commontex/patchlevel.tex  Wed Sep 03 05:58:39 2008 -0400
@@ -1,6 +1,6 @@
 % This file is generated by ../tools/getversioninfo;
 % do not edit manually.

-\release{3.1.2.alpha3}
+\release{3.1.2.alpha4}
 \setreleaseinfo{}
-\setshortversion{3.1.2.alpha3}
+\setshortversion{3.1.2.alpha4}
```

Pressing q dumps me into vi session. Then I get a runtime error:


```
RuntimeError: Refusing to do operation since you still have unrecorded changes. You must check in all changes in your working repository first.
```




---

archive/issue_comments_026413.json:
```json
{
    "body": "David,\n\nI keep getting this as well and it bugs the heck out of me.  But I can work around it by typing the following in the devel/doc directory:\n\n\n```\nghitza@artin:/opt/sage/devel/doc$ hg qnew -f stupid.patch\n```\n\n\n(You can give the patch your favorite name that you're unlikely to use.)\n\nThen the annoying diff's that you got above will go away and you can happily apply doc patches.  I wish someone got rid of the problem altogether, but for now this should work.\n\nJohn, I've looked at the patch and it seems ok to me; it also passes sage -t.  Unfortunately, latex fonts are broken on my ubuntu machine so I can't do build_pdf or build_dvi to look at the typeset version.  I will try to build 3.1.2.alpha4 on my gentoo machine and apply your patch there, but it might take a while.  Hopefully this will have gotten a positive review by then.",
    "created_at": "2008-09-03T11:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26413",
    "user": "https://github.com/aghitza"
}
```

David,

I keep getting this as well and it bugs the heck out of me.  But I can work around it by typing the following in the devel/doc directory:


```
ghitza@artin:/opt/sage/devel/doc$ hg qnew -f stupid.patch
```


(You can give the patch your favorite name that you're unlikely to use.)

Then the annoying diff's that you got above will go away and you can happily apply doc patches.  I wish someone got rid of the problem altogether, but for now this should work.

John, I've looked at the patch and it seems ok to me; it also passes sage -t.  Unfortunately, latex fonts are broken on my ubuntu machine so I can't do build_pdf or build_dvi to look at the typeset version.  I will try to build 3.1.2.alpha4 on my gentoo machine and apply your patch there, but it might take a while.  Hopefully this will have gotten a positive review by then.



---

archive/issue_comments_026414.json:
```json
{
    "body": "OK, I managed to fix my latex and build the tutorial with the patch applied.  Looks good!",
    "created_at": "2008-09-03T12:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26414",
    "user": "https://github.com/aghitza"
}
```

OK, I managed to fix my latex and build the tutorial with the patch applied.  Looks good!



---

archive/issue_comments_026415.json:
```json
{
    "body": "I agree. Using Alex's trick, I got the patch to apply and this addition looks good. build_dvi works without latex compiling errors.",
    "created_at": "2008-09-03T15:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26415",
    "user": "https://github.com/wdjoyner"
}
```

I agree. Using Alex's trick, I got the patch to apply and this addition looks good. build_dvi works without latex compiling errors.



---

archive/issue_comments_026416.json:
```json
{
    "body": "Alex, I'm glad you figured out the solution, because I had no idea what was going wrong or how to fix it.\n\nThanks to both of you (and to John Cremona) for the positive reviews...",
    "created_at": "2008-09-03T17:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26416",
    "user": "https://github.com/jhpalmieri"
}
```

Alex, I'm glad you figured out the solution, because I had no idea what was going wrong or how to fix it.

Thanks to both of you (and to John Cremona) for the positive reviews...



---

archive/issue_comments_026417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-03T19:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026418.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-03T19:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3728#issuecomment-26418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0



---

archive/issue_events_008532.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-03T19:18:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3728",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3728#event-8532"
}
```
