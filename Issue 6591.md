# Issue 6591: Implement view(object, viewer='pdf') and view(object, tightpage = True)

archive/issues_006591.json:
```json
{
    "body": "Assignee: was\n\nCC:  sage-combinat rbeezer fidelbarrera jhpalmieri\n\nThis small patch implements:\n\n```\nsage: view(object, viewer = \"pdf\")\n```\n\nwhich works even under the notebook.\n\nTypical use cases:\n\n* you prefer your pdf browser to your dvi browser\n* you want to view latex snippets which are not displayed well in dvi viewers or jsmath (e.g. tikzpicture) \n\nPotential extensions: view(object, viewer='png'), view(object, viewer='html') \n\nThis partially reinstates #5920 which got a positive review and was said to be merged and closed, but apparently later discarded upon the merge of the overlapping #6012 (pdflatex option)\n\n\nThis patch also adds a tightpage option, which uses the preview package to create a document with each displaymath on a single page whose size is exactly that of the displaymath. This is for example useful for very large pictures (graphs!) generated with tikz.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6591\n\n",
    "created_at": "2009-07-22T14:38:27Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "Implement view(object, viewer='pdf') and view(object, tightpage = True)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6591",
    "user": "nthiery"
}
```
Assignee: was

CC:  sage-combinat rbeezer fidelbarrera jhpalmieri

This small patch implements:

```
sage: view(object, viewer = "pdf")
```

which works even under the notebook.

Typical use cases:

* you prefer your pdf browser to your dvi browser
* you want to view latex snippets which are not displayed well in dvi viewers or jsmath (e.g. tikzpicture) 

Potential extensions: view(object, viewer='png'), view(object, viewer='html') 

This partially reinstates #5920 which got a positive review and was said to be merged and closed, but apparently later discarded upon the merge of the overlapping #6012 (pdflatex option)


This patch also adds a tightpage option, which uses the preview package to create a document with each displaymath on a single page whose size is exactly that of the displaymath. This is for example useful for very large pictures (graphs!) generated with tikz.

Issue created by migration from https://trac.sagemath.org/ticket/6591





---

archive/issue_comments_053937.json:
```json
{
    "body": "Changing assignee from was to nthiery.",
    "created_at": "2009-07-22T14:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53937",
    "user": "nthiery"
}
```

Changing assignee from was to nthiery.



---

archive/issue_comments_053938.json:
```json
{
    "body": "Changing keywords from \"\" to \"view, pdflatex, tightpage, tikz\".",
    "created_at": "2009-07-22T14:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53938",
    "user": "nthiery"
}
```

Changing keywords from "" to "view, pdflatex, tightpage, tikz".



---

archive/issue_comments_053939.json:
```json
{
    "body": "Everything works as advertised, both from the command-line and the notebook (except that tightpage=True has no effect in the notebook if viewer is None).  I would give it a positive review except that the new options aren't documented at all.  I'm attaching a patch with documentation; if you're happy with it, the whole thing can get a positive review.\n\nI have no idea how to doctest this, by the way...",
    "created_at": "2009-07-22T21:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53939",
    "user": "jhpalmieri"
}
```

Everything works as advertised, both from the command-line and the notebook (except that tightpage=True has no effect in the notebook if viewer is None).  I would give it a positive review except that the new options aren't documented at all.  I'm attaching a patch with documentation; if you're happy with it, the whole thing can get a positive review.

I have no idea how to doctest this, by the way...



---

archive/issue_comments_053940.json:
```json
{
    "body": "Attachment\n\napply on top of the other patch",
    "created_at": "2009-07-22T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53940",
    "user": "jhpalmieri"
}
```

Attachment

apply on top of the other patch



---

archive/issue_comments_053941.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> Everything works as advertised, both from the command-line and the notebook (except that tightpage=True has no effect in the notebook if viewer is None).  I would give it a positive review except that the new options aren't documented at all.  I'm attaching a patch with documentation; if you're happy with it, the whole thing can get a positive review.\n> \n> I have no idea how to doctest this, by the way...\n\nOops, sorry, I forgot about the doc ... Thanks!\n\nIn the meantime, I actually found a shortcoming in tightpage. I'll probably add a little fix later today.",
    "created_at": "2009-07-23T07:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53941",
    "user": "nthiery"
}
```

Replying to [comment:3 jhpalmieri]:
> Everything works as advertised, both from the command-line and the notebook (except that tightpage=True has no effect in the notebook if viewer is None).  I would give it a positive review except that the new options aren't documented at all.  I'm attaching a patch with documentation; if you're happy with it, the whole thing can get a positive review.
> 
> I have no idea how to doctest this, by the way...

Oops, sorry, I forgot about the doc ... Thanks!

In the meantime, I actually found a shortcoming in tightpage. I'll probably add a little fix later today.



---

archive/issue_comments_053942.json:
```json
{
    "body": "I folded the patches together, and fixed the shortcoming in tightpage (using displaymath did put a limit on the width of the page). I also updated and reedited a bit the documentation.\nBtw: I am wondering whether the description of what happens in notebook mode should not go first.",
    "created_at": "2009-07-23T21:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53942",
    "user": "nthiery"
}
```

I folded the patches together, and fixed the shortcoming in tightpage (using displaymath did put a limit on the width of the page). I also updated and reedited a bit the documentation.
Btw: I am wondering whether the description of what happens in notebook mode should not go first.



---

archive/issue_comments_053943.json:
```json
{
    "body": "Apply only this one (it includes the doc patch)",
    "created_at": "2009-07-23T21:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53943",
    "user": "nthiery"
}
```

Apply only this one (it includes the doc patch)



---

archive/issue_comments_053944.json:
```json
{
    "body": "Attachment\n\napply on top of the other patch",
    "created_at": "2009-07-23T23:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53944",
    "user": "jhpalmieri"
}
```

Attachment

apply on top of the other patch



---

archive/issue_comments_053945.json:
```json
{
    "body": "Attachment\n\nPositive review.  A few very minor doc fixes added (for the change from `\\LaTeX` to `LaTeX`, it seems that jsMath doesn't know about this command, so it doesn't look good in the notebook with #5653 applied).\n\nApply patches trac_6591_view_viewer_tightpage-nt.patch and trac_6591-doc2.patch.\n\nI think it's fine to leave the description of notebook mode second; it would take actual thought to change it at this point.  When I worked on this docstring a while ago, my feeling was that since most of the options are ignored in notebook mode, command-line mode should come first.",
    "created_at": "2009-07-23T23:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53945",
    "user": "jhpalmieri"
}
```

Attachment

Positive review.  A few very minor doc fixes added (for the change from `\LaTeX` to `LaTeX`, it seems that jsMath doesn't know about this command, so it doesn't look good in the notebook with #5653 applied).

Apply patches trac_6591_view_viewer_tightpage-nt.patch and trac_6591-doc2.patch.

I think it's fine to leave the description of notebook mode second; it would take actual thought to change it at this point.  When I worked on this docstring a while ago, my feeling was that since most of the options are ignored in notebook mode, command-line mode should come first.



---

archive/issue_comments_053946.json:
```json
{
    "body": "Thanks John! That was quick. Time difference is a good thing :-)",
    "created_at": "2009-07-24T07:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53946",
    "user": "nthiery"
}
```

Thanks John! That was quick. Time difference is a good thing :-)



---

archive/issue_comments_053947.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T21:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6591#issuecomment-53947",
    "user": "mvngu"
}
```

Resolution: fixed
