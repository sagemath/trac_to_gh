# Issue 4809: the installation guide and constructions guide should be CC licensed

archive/issues_004809.json:
```json
{
    "body": "Assignee: tba\n\nOur documentation should be clearly licensed.\n\n\n```\n15:09 < hampton|home> what is the license of the sage documentation?\n15:09 < hampton|home> is it a type of creative commons?\n15:11 < ddrake> hrm, I dunno. It should be, I think.\n15:13 < ddrake> yep: by-sa\n15:13 < ddrake> http://sagemath.org/doc/tut/node1.html\n15:14 < hampton|home> that's the tutorial - are they are under that?\n15:14 < hampton|home> the others don't have a notice I think\n15:14 < ddrake> the installation guide and constructions don't have a notice\n15:15 < ddrake> ref manual is attribution-sharealike\n15:15 < ddrake> programming guide too\n15:15 < hampton|home> cool, thanks\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4809\n\n",
    "created_at": "2008-12-16T06:22:54Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "the installation guide and constructions guide should be CC licensed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4809",
    "user": "@dandrake"
}
```
Assignee: tba

Our documentation should be clearly licensed.


```
15:09 < hampton|home> what is the license of the sage documentation?
15:09 < hampton|home> is it a type of creative commons?
15:11 < ddrake> hrm, I dunno. It should be, I think.
15:13 < ddrake> yep: by-sa
15:13 < ddrake> http://sagemath.org/doc/tut/node1.html
15:14 < hampton|home> that's the tutorial - are they are under that?
15:14 < hampton|home> the others don't have a notice I think
15:14 < ddrake> the installation guide and constructions don't have a notice
15:15 < ddrake> ref manual is attribution-sharealike
15:15 < ddrake> programming guide too
15:15 < hampton|home> cool, thanks
```


Issue created by migration from https://trac.sagemath.org/ticket/4809





---

archive/issue_comments_036456.json:
```json
{
    "body": "The attached patches license the constructions guide and installation guide as CC Attribution-Sharealike, which is the same as the other Sage documentation. Since David Joyner is listed as the/an author of both documents, I suppose he should approve or sign off on these patches.",
    "created_at": "2008-12-16T06:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36456",
    "user": "@dandrake"
}
```

The attached patches license the constructions guide and installation guide as CC Attribution-Sharealike, which is the same as the other Sage documentation. Since David Joyner is listed as the/an author of both documents, I suppose he should approve or sign off on these patches.



---

archive/issue_comments_036457.json:
```json
{
    "body": "Actually, href will not work for a few reasons. \n\n(1)  The href (or whatever it's called) package is commented out, so it won't compile. \n\n(2) But I think the href latex package somehow conflicts with the Python doc latex package (?), and uncommenting it doesn't work either. (After moving to rest/sphinyx is this an issue?)\n\nThe solution is easy though - use \\url{...} instead. It is used in other places in const.tex and inst.tex as well. If you just swap href with url it compiles fine and I'll give this a positive review.",
    "created_at": "2008-12-17T03:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36457",
    "user": "@wdjoyner"
}
```

Actually, href will not work for a few reasons. 

(1)  The href (or whatever it's called) package is commented out, so it won't compile. 

(2) But I think the href latex package somehow conflicts with the Python doc latex package (?), and uncommenting it doesn't work either. (After moving to rest/sphinyx is this an issue?)

The solution is easy though - use \url{...} instead. It is used in other places in const.tex and inst.tex as well. If you just swap href with url it compiles fine and I'll give this a positive review.



---

archive/issue_comments_036458.json:
```json
{
    "body": "Attachment [trac_4809_constructions.patch](tarball://root/attachments/some-uuid/ticket4809/trac_4809_constructions.patch) by @dandrake created at 2009-04-14 01:28:40",
    "created_at": "2009-04-14T01:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36458",
    "user": "@dandrake"
}
```

Attachment [trac_4809_constructions.patch](tarball://root/attachments/some-uuid/ticket4809/trac_4809_constructions.patch) by @dandrake created at 2009-04-14 01:28:40



---

archive/issue_comments_036459.json:
```json
{
    "body": "Attachment [trac_4809_installation.patch](tarball://root/attachments/some-uuid/ticket4809/trac_4809_installation.patch) by @dandrake created at 2009-04-14 01:31:19",
    "created_at": "2009-04-14T01:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36459",
    "user": "@dandrake"
}
```

Attachment [trac_4809_installation.patch](tarball://root/attachments/some-uuid/ticket4809/trac_4809_installation.patch) by @dandrake created at 2009-04-14 01:31:19



---

archive/issue_comments_036460.json:
```json
{
    "body": "Updated versions of the patches for the spinx-ified documentation.",
    "created_at": "2009-04-14T01:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36460",
    "user": "@dandrake"
}
```

Updated versions of the patches for the spinx-ified documentation.



---

archive/issue_comments_036461.json:
```json
{
    "body": "trac_4809_constructions.patch and trac_4809_installation.patch are ready to go: positive review.  Meanwhile, I can't find any license information for the tutorial, reference manual, or developer's guide.  Did they disappear in the Sphinx conversion?  Here's a new patch which adds them.  It also removes the line \"Contents:\" from various index.rst files -- if you produce a PDF from the docs, the table of contents is printed first, then whatever is in index.rst, so you would end up with an introduction followed by \"Contents:\", and then the rest of the page was blank.",
    "created_at": "2009-04-21T17:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36461",
    "user": "@jhpalmieri"
}
```

trac_4809_constructions.patch and trac_4809_installation.patch are ready to go: positive review.  Meanwhile, I can't find any license information for the tutorial, reference manual, or developer's guide.  Did they disappear in the Sphinx conversion?  Here's a new patch which adds them.  It also removes the line "Contents:" from various index.rst files -- if you produce a PDF from the docs, the table of contents is printed first, then whatever is in index.rst, so you would end up with an introduction followed by "Contents:", and then the rest of the page was blank.



---

archive/issue_comments_036462.json:
```json
{
    "body": "Attachment [trac_4809_other.patch](tarball://root/attachments/some-uuid/ticket4809/trac_4809_other.patch) by @jhpalmieri created at 2009-04-21 17:56:29",
    "created_at": "2009-04-21T17:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36462",
    "user": "@jhpalmieri"
}
```

Attachment [trac_4809_other.patch](tarball://root/attachments/some-uuid/ticket4809/trac_4809_other.patch) by @jhpalmieri created at 2009-04-21 17:56:29



---

archive/issue_comments_036463.json:
```json
{
    "body": "Changing assignee from tba to @dandrake.",
    "created_at": "2009-04-22T04:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36463",
    "user": "@dandrake"
}
```

Changing assignee from tba to @dandrake.



---

archive/issue_comments_036464.json:
```json
{
    "body": "We should definitely license the rest of the documentation, too. Positive review to trac_4809_other.patch.\n\nI'll also open a French version of this ticket. I'm sure I could cut and paste something into the French tutorial, but I'll let one of our Francophone developers handle that.\n\nI'm changing the milestone to 3.4.2 since these are not big or invasive patches, and should get in as soon as possible.",
    "created_at": "2009-04-22T04:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36464",
    "user": "@dandrake"
}
```

We should definitely license the rest of the documentation, too. Positive review to trac_4809_other.patch.

I'll also open a French version of this ticket. I'm sure I could cut and paste something into the French tutorial, but I'll let one of our Francophone developers handle that.

I'm changing the milestone to 3.4.2 since these are not big or invasive patches, and should get in as soon as possible.



---

archive/issue_comments_036465.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-22T04:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36465",
    "user": "@dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036466.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T04:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36466",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036467.json:
```json
{
    "body": "Merged all three patches in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T04:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4809#issuecomment-36467",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.4.2.alpha0.

Cheers,

Michael
