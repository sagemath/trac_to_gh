# Issue 4060: Polyhedra don't handle real coordinates properly

archive/issues_004060.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: polyhedra\n\nDear All,\n\nI have a question related to the polyhedra module.\nWhen I define a polyhedron using float rather than integer\ncoordinates, I get a weird behavior from the vert_to_ieq function.\nFor example, if I type something like this:\n\np = [[1.1, 2.2], [3.3, 4.4]]\nvert_to_ieq(p, cdd_type=\"real\") \n\nIssue created by migration from https://trac.sagemath.org/ticket/4060\n\n",
    "created_at": "2008-09-04T13:44:12Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Polyhedra don't handle real coordinates properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4060",
    "user": "mhampton"
}
```
Assignee: mhampton

Keywords: polyhedra

Dear All,

I have a question related to the polyhedra module.
When I define a polyhedron using float rather than integer
coordinates, I get a weird behavior from the vert_to_ieq function.
For example, if I type something like this:

p = [[1.1, 2.2], [3.3, 4.4]]
vert_to_ieq(p, cdd_type="real") 

Issue created by migration from https://trac.sagemath.org/ticket/4060





---

archive/issue_comments_029284.json:
```json
{
    "body": "Attachment [trac-4060-patch1.patch](tarball://root/attachments/some-uuid/ticket4060/trac-4060-patch1.patch) by mhampton created at 2008-09-04 20:36:38",
    "created_at": "2008-09-04T20:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4060#issuecomment-29284",
    "user": "mhampton"
}
```

Attachment [trac-4060-patch1.patch](tarball://root/attachments/some-uuid/ticket4060/trac-4060-patch1.patch) by mhampton created at 2008-09-04 20:36:38



---

archive/issue_comments_029285.json:
```json
{
    "body": "Changing assignee from mhampton to somebody.",
    "created_at": "2008-09-04T20:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4060#issuecomment-29285",
    "user": "mhampton"
}
```

Changing assignee from mhampton to somebody.



---

archive/issue_comments_029286.json:
```json
{
    "body": "OK, I think I have resolved this problem.  I added a doctest to the Polyhedron class to test this.",
    "created_at": "2008-09-04T20:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4060#issuecomment-29286",
    "user": "mhampton"
}
```

OK, I think I have resolved this problem.  I added a doctest to the Polyhedron class to test this.



---

archive/issue_comments_029287.json:
```json
{
    "body": "This looks good to me.",
    "created_at": "2008-09-19T00:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4060#issuecomment-29287",
    "user": "@mwhansen"
}
```

This looks good to me.



---

archive/issue_comments_029288.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T03:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4060#issuecomment-29288",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029289.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T03:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4060#issuecomment-29289",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha0
