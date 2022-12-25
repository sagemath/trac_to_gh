# Issue 7464: Remove '-v' option from 'cp' command (GNUism) in database_cremona_ellcurve

archive/issues_007464.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @williamstein drkirkby\n\nKeywords: optional GNUism\n\nThe use of a non-POSIX option '-v' to the 'cp' command prevents this package installing on Solaris. The option, which can also be written as --verbose, is only to show what is actually being copied, so removing it should have no impact. \nTherefore\n\n```\ncp -rv cremona $SAGE_DATA/\n```\nwas changed to \n\n```\ncp -r cremona $SAGE_DATA/\n```\nin spkg-install. \n\nI also renamed 'SAGE.txt' to SPKG.txt, and added a slightly better description, and upstream contact information, to make it more consistent with other packages. \n\nThis is an optional Sage package. \n\nIt is unusual in that the .spkg file, was a tar file, and not a compressed tar file as they usually are. \n\nThe updated files can be found at: \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/database_cremona_ellcurve/\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7464\n\n",
    "closed_at": "2009-11-29T05:39:06Z",
    "created_at": "2009-11-14T20:33:48Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Remove '-v' option from 'cp' command (GNUism) in database_cremona_ellcurve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7464",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @williamstein drkirkby

Keywords: optional GNUism

The use of a non-POSIX option '-v' to the 'cp' command prevents this package installing on Solaris. The option, which can also be written as --verbose, is only to show what is actually being copied, so removing it should have no impact. 
Therefore

```
cp -rv cremona $SAGE_DATA/
```
was changed to 

```
cp -r cremona $SAGE_DATA/
```
in spkg-install. 

I also renamed 'SAGE.txt' to SPKG.txt, and added a slightly better description, and upstream contact information, to make it more consistent with other packages. 

This is an optional Sage package. 

It is unusual in that the .spkg file, was a tar file, and not a compressed tar file as they usually are. 

The updated files can be found at: 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/database_cremona_ellcurve/



Issue created by migration from https://trac.sagemath.org/ticket/7464





---

archive/issue_comments_062750.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-14T20:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62750",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062751.json:
```json
{
    "body": "> It is unusual in that the .spkg file, was a tar file, and \n> not a compressed tar file as they usually are. \n\n\nThis is the case for all databases of compressed files.  One makes a non-compressed spkg by doing\n\n```\n   sage -pkg_nc directory_name\n```",
    "created_at": "2009-11-17T06:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62751",
    "user": "https://github.com/williamstein"
}
```

> It is unusual in that the .spkg file, was a tar file, and 
> not a compressed tar file as they usually are. 


This is the case for all databases of compressed files.  One makes a non-compressed spkg by doing

```
   sage -pkg_nc directory_name
```



---

archive/issue_comments_062752.json:
```json
{
    "body": "Thank you for the information. I used 'tar' to create it, rather than Sage with any option. It seems to work for me. Perhaps you can test it and review it.",
    "created_at": "2009-11-17T23:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62752",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you for the information. I used 'tar' to create it, rather than Sage with any option. It seems to work for me. Perhaps you can test it and review it.



---

archive/issue_comments_062753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-22T12:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62753",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062754.json:
```json
{
    "body": "This looks fine to me. I read the changed files and also successfully installed it onto 4.2.1.  I am happy to be the upstream contact (and would expect to be contacted if anyone found an error in the database).  I should probably volunteer to be the spkg maintainer, but (embarrassingly) I do not even know the format of the main data file \"cremona\" in there!  So in practice William is the maintainer.  I will ask him to give me instructions....",
    "created_at": "2009-11-22T12:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62754",
    "user": "https://github.com/JohnCremona"
}
```

This looks fine to me. I read the changed files and also successfully installed it onto 4.2.1.  I am happy to be the upstream contact (and would expect to be contacted if anyone found an error in the database).  I should probably volunteer to be the spkg maintainer, but (embarrassingly) I do not even know the format of the main data file "cremona" in there!  So in practice William is the maintainer.  I will ask him to give me instructions....



---

archive/issue_comments_062755.json:
```json
{
    "body": ">  I do not even know the format of the main data file \"cremona\" in there! \n\n> So in practice William is the maintainer. I will ask him to give me instructions.... \n\nIt's just a Python pickle.\n\nWilliam",
    "created_at": "2009-11-22T21:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62755",
    "user": "https://github.com/williamstein"
}
```

>  I do not even know the format of the main data file "cremona" in there! 

> So in practice William is the maintainer. I will ask him to give me instructions.... 

It's just a Python pickle.

William



---

archive/issue_events_017694.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-29T05:39:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7464#event-17694"
}
```



---

archive/issue_comments_062756.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62756",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_062757.json:
```json
{
    "body": "Copied into optional packages.",
    "created_at": "2009-11-29T05:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7464#issuecomment-62757",
    "user": "https://github.com/mwhansen"
}
```

Copied into optional packages.
