# Issue 5990: [with patch, needs review] developer's guide: more on .spkg files

archive/issues_005990.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThis is an amalgamation of information from the patch at #4857 and the wiki page [http://wiki.sagemath.org/SPKG_Audit](http://wiki.sagemath.org/SPKG_Audit).  Therefore Georg Weber should get credit for the parts coming from #4857, while Michael Abshoff and Dan Drake should get credit for the parts coming from the wiki page.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5990\n\n",
    "created_at": "2009-05-05T18:23:20Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] developer's guide: more on .spkg files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5990",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

This is an amalgamation of information from the patch at #4857 and the wiki page [http://wiki.sagemath.org/SPKG_Audit](http://wiki.sagemath.org/SPKG_Audit).  Therefore Georg Weber should get credit for the parts coming from #4857, while Michael Abshoff and Dan Drake should get credit for the parts coming from the wiki page.


Issue created by migration from https://trac.sagemath.org/ticket/5990





---

archive/issue_comments_047598.json:
```json
{
    "body": "\"Positive Review\" because I just read the patch online on trac and it is definitely an enhancement over the old documentation.\n\n\"Minus epsilon\" because I actually didn't download and test the patch (whether it applies to Sage-3.4.2, whether the documentation still builds, and such).\n\nThere is still room for improvement, e.g. display sample contents of the \".hgignore\" file --- this file has to contain necessarily \"src\" as an exception.",
    "created_at": "2009-05-05T20:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47598",
    "user": "GeorgSWeber"
}
```

"Positive Review" because I just read the patch online on trac and it is definitely an enhancement over the old documentation.

"Minus epsilon" because I actually didn't download and test the patch (whether it applies to Sage-3.4.2, whether the documentation still builds, and such).

There is still room for improvement, e.g. display sample contents of the ".hgignore" file --- this file has to contain necessarily "src" as an exception.



---

archive/issue_comments_047599.json:
```json
{
    "body": "Here's a new version with a sample .hgignore file.",
    "created_at": "2009-05-05T22:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47599",
    "user": "jhpalmieri"
}
```

Here's a new version with a sample .hgignore file.



---

archive/issue_comments_047600.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-05T22:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47600",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_047601.json:
```json
{
    "body": "I'm changing this from \"positive review minus epsilon\" to \"needs review\" so that it still appears in the list of tickets needing review.  If someone is willing to confirm that the patch applies and that the documentation builds correctly (with `sage -docbuild developer FORMAT`, with FORMAT being \"html\", \"pdf\", etc.) then I think it can get a full positive review.",
    "created_at": "2009-05-31T22:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47601",
    "user": "jhpalmieri"
}
```

I'm changing this from "positive review minus epsilon" to "needs review" so that it still appears in the list of tickets needing review.  If someone is willing to confirm that the patch applies and that the documentation builds correctly (with `sage -docbuild developer FORMAT`, with FORMAT being "html", "pdf", etc.) then I think it can get a full positive review.



---

archive/issue_comments_047602.json:
```json
{
    "body": "The patch applies to 4.0.rc2 and sage -docbuild developer html works on a mac OS 10.4. I don't have pdflatex installed yet, so the pdf option fails.",
    "created_at": "2009-06-01T00:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47602",
    "user": "wdj"
}
```

The patch applies to 4.0.rc2 and sage -docbuild developer html works on a mac OS 10.4. I don't have pdflatex installed yet, so the pdf option fails.



---

archive/issue_comments_047603.json:
```json
{
    "body": "Both work in ubuntu 9.04, with the pdf placed in devel/sage/doc/output/pdf/en/developer and the html in\n/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/doc/output/html/en/developer. According to the comment above by  jhpalmieri, I am therefore changing this to a positive review.",
    "created_at": "2009-06-01T00:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47603",
    "user": "wdj"
}
```

Both work in ubuntu 9.04, with the pdf placed in devel/sage/doc/output/pdf/en/developer and the html in
/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/doc/output/html/en/developer. According to the comment above by  jhpalmieri, I am therefore changing this to a positive review.



---

archive/issue_comments_047604.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T05:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47604",
    "user": "mhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_047605.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T05:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5990#issuecomment-47605",
    "user": "mhansen"
}
```

Resolution: fixed
