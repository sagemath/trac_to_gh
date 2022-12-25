# Issue 8599: Allow size as an argument for point2d

archive/issues_008599.json:
```json
{
    "body": "Assignee: @seblabbe\n\nFor 3d points, one must use the argument `size`  :\n\n```\nsage: point((2,3,4), size=100)\n```\n\nBut for 2d points, one must use the argument `pointsize`  :\n\n```\nsage: point((2,3), size=100)\nverbose 0 (136: primitive.py, options) WARNING: Ignoring option 'size'=100\nverbose 0 (136: primitive.py, options) \nThe allowed options for Point set defined by 1 point(s) are:\n    alpha          How transparent the line is.                                \n    faceted        If True color the edge of the point.                        \n    hue            The color given as a hue.                                   \n    pointsize      How big the point is.                                       \n    rgbcolor       The color as an RGB tuple.                                  \n    zorder         The layer level in which to draw                            \n\n\nsage: point((2,3), pointsize=100)\n```\n\nI think `pointsize` is kind of redundant and `size` would not be ambiguous. At least, if we keep `pointsize` for backward compatibility reasons, I would like\n\n```\nsage: point((2,3), size=100)\n```\n\nto work.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8599\n\n",
    "closed_at": "2010-04-16T18:51:09Z",
    "created_at": "2010-03-24T15:30:11Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Allow size as an argument for point2d",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8599",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

For 3d points, one must use the argument `size`  :

```
sage: point((2,3,4), size=100)
```

But for 2d points, one must use the argument `pointsize`  :

```
sage: point((2,3), size=100)
verbose 0 (136: primitive.py, options) WARNING: Ignoring option 'size'=100
verbose 0 (136: primitive.py, options) 
The allowed options for Point set defined by 1 point(s) are:
    alpha          How transparent the line is.                                
    faceted        If True color the edge of the point.                        
    hue            The color given as a hue.                                   
    pointsize      How big the point is.                                       
    rgbcolor       The color as an RGB tuple.                                  
    zorder         The layer level in which to draw                            


sage: point((2,3), pointsize=100)
```

I think `pointsize` is kind of redundant and `size` would not be ambiguous. At least, if we keep `pointsize` for backward compatibility reasons, I would like

```
sage: point((2,3), size=100)
```

to work.


Issue created by migration from https://trac.sagemath.org/ticket/8599





---

archive/issue_comments_077743.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-24T17:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77743",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077744.json:
```json
{
    "body": "Attachment [trac_8599_pointsize-sl.patch](tarball://root/attachments/some-uuid/ticket8599/trac_8599_pointsize-sl.patch) by @seblabbe created at 2010-03-25 13:38:02",
    "created_at": "2010-03-25T13:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77744",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8599_pointsize-sl.patch](tarball://root/attachments/some-uuid/ticket8599/trac_8599_pointsize-sl.patch) by @seblabbe created at 2010-03-25 13:38:02



---

archive/issue_comments_077745.json:
```json
{
    "body": "I improved a comment about pointsize vs size and just uploaded the patch.",
    "created_at": "2010-03-25T13:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77745",
    "user": "https://github.com/seblabbe"
}
```

I improved a comment about pointsize vs size and just uploaded the patch.



---

archive/issue_comments_077746.json:
```json
{
    "body": "Positive review on slabbe's patch.\n\nI enhanced the documentation for pointsize, added a deprecation functionality for the rename decorator, and then deprecated the pointsize keyword in my patch.  My patch needs to be reviewed now.",
    "created_at": "2010-03-25T16:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77746",
    "user": "https://github.com/jasongrout"
}
```

Positive review on slabbe's patch.

I enhanced the documentation for pointsize, added a deprecation functionality for the rename decorator, and then deprecated the pointsize keyword in my patch.  My patch needs to be reviewed now.



---

archive/issue_comments_077747.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-03-25T19:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77747",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_077748.json:
```json
{
    "body": "Attachment [trac-8599-fix-docs.patch](tarball://root/attachments/some-uuid/ticket8599/trac-8599-fix-docs.patch) by @jasongrout created at 2010-03-25 19:10:39\n\nOkay, I moved the deprecation code over to #8607, since William requested that we don't deprecate the pointsize option (for mma compatibility).  I've instead posted a new patch which just contains a few documentation enhancements and fixes.  Sebastien, can you review my patch?  If it's a positive review, then set this to positive review.",
    "created_at": "2010-03-25T19:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77748",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8599-fix-docs.patch](tarball://root/attachments/some-uuid/ticket8599/trac-8599-fix-docs.patch) by @jasongrout created at 2010-03-25 19:10:39

Okay, I moved the deprecation code over to #8607, since William requested that we don't deprecate the pointsize option (for mma compatibility).  I've instead posted a new patch which just contains a few documentation enhancements and fixes.  Sebastien, can you review my patch?  If it's a positive review, then set this to positive review.



---

archive/issue_comments_077749.json:
```json
{
    "body": "Positive review for Jason's doc fixes.\n\n#8607 = great!",
    "created_at": "2010-03-26T13:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77749",
    "user": "https://github.com/seblabbe"
}
```

Positive review for Jason's doc fixes.

#8607 = great!



---

archive/issue_comments_077750.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-26T13:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77750",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077751.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8599_pointsize-sl.patch\n- trac-8599-fix-docs.patch",
    "created_at": "2010-04-16T18:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77751",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8599_pointsize-sl.patch
- trac-8599-fix-docs.patch



---

archive/issue_comments_077752.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8599#issuecomment-77752",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020785.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:51:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8599",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8599#event-20785"
}
```
