# Issue 7933: update copyright years to span 2006--2010

archive/issues_007933.json:
```json
{
    "body": "Assignee: mvngu\n\nIt's that time of the year again when the copyright years for Sage need to be updated to reflect the new year. The copyright years should now span 2006--2010. The [Sage wiki](http://wiki.sagemath.org/devel/UpdateCopyright) contains a page that lists file you need to edit in order to update the copyright years.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7933\n\n",
    "created_at": "2010-01-15T03:58:23Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "update copyright years to span 2006--2010",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7933",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

It's that time of the year again when the copyright years for Sage need to be updated to reflect the new year. The copyright years should now span 2006--2010. The [Sage wiki](http://wiki.sagemath.org/devel/UpdateCopyright) contains a page that lists file you need to edit in order to update the copyright years.

Issue created by migration from https://trac.sagemath.org/ticket/7933





---

archive/issue_comments_069010.json:
```json
{
    "body": "Attachment [README.txt](tarball://root/attachments/some-uuid/ticket7933/README.txt) by mvngu created at 2010-01-15 10:57:21\n\nREADME.txt with updated copyright years; based on Sage 4.3.1.alpha2",
    "created_at": "2010-01-15T10:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [README.txt](tarball://root/attachments/some-uuid/ticket7933/README.txt) by mvngu created at 2010-01-15 10:57:21

README.txt with updated copyright years; based on Sage 4.3.1.alpha2



---

archive/issue_comments_069011.json:
```json
{
    "body": "differences between the above updated README.txt and the current one in Sage 4.3.1.alpha2",
    "created_at": "2010-01-15T10:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

differences between the above updated README.txt and the current one in Sage 4.3.1.alpha2



---

archive/issue_comments_069012.json:
```json
{
    "body": "Attachment [README.patch](tarball://root/attachments/some-uuid/ticket7933/README.patch) by mvngu created at 2010-01-15 11:01:07",
    "created_at": "2010-01-15T11:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69012",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [README.patch](tarball://root/attachments/some-uuid/ticket7933/README.patch) by mvngu created at 2010-01-15 11:01:07



---

archive/issue_comments_069013.json:
```json
{
    "body": "Attachment [trac_7933-mac-app.patch](tarball://root/attachments/some-uuid/ticket7933/trac_7933-mac-app.patch) by mvngu created at 2010-01-15 11:03:22\n\nupdated copyright years for the Mac app",
    "created_at": "2010-01-15T11:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69013",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7933-mac-app.patch](tarball://root/attachments/some-uuid/ticket7933/trac_7933-mac-app.patch) by mvngu created at 2010-01-15 11:03:22

updated copyright years for the Mac app



---

archive/issue_comments_069014.json:
```json
{
    "body": "Attachment [trac_7933-doc-builder.patch](tarball://root/attachments/some-uuid/ticket7933/trac_7933-doc-builder.patch) by mvngu created at 2010-01-16 07:41:00\n\napply to sage-main; based on Sage 4.3.1.alpha2",
    "created_at": "2010-01-16T07:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69014",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7933-doc-builder.patch](tarball://root/attachments/some-uuid/ticket7933/trac_7933-doc-builder.patch) by mvngu created at 2010-01-16 07:41:00

apply to sage-main; based on Sage 4.3.1.alpha2



---

archive/issue_comments_069015.json:
```json
{
    "body": "I think the above patches should take care of updating the copyright years. Here's a description of these patches and where to apply them:\n\n1. The file [README.txt](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/README.txt) should be placed under `SAGE_ROOT/`. That file is not under revision control, so the release manager needs to replace the current `README.txt` with the attached updated `README.txt`. To show the differences between the current `README.txt` in Sage 4.3.1.alpha2 and the updated `README.txt`, see the patch file [README.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/README.patch). Note that this patch is only for showing differences; don't apply it.\n2. The patch [trac_7933-mac-app.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/trac_7933-mac-app.patch) should be applied to the `data/` repository under `SAGE_ROOT/data/extcode`. Before applying that patch, the release manager needs to remove a junk file under that directory:\n {{{\n[mvngu`@`mod extcode]$ pwd\n/dev/shm/mvngu/sage-4.3.1.alpha2/data/extcode\n[mvngu`@`mod extcode]$ hg st\n? sage/ext/.DS_Store.rej\n[mvngu`@`mod extcode]$ rm sage/ext/.DS_Store.rej \n[mvngu`@`mod extcode]$ hg st\n<no-output>\n }}}\n After removing the junk file, then apply the patch.\n1. Finally, apply the patch [trac_7933-doc-builder.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/trac_7933-doc-builder.patch) to the repository `sage-main`. This patch affects the configuration file `doc/common/conf.py`, so the file's corresponding Python byte code file should be removed:\n {{{\n[mvngu`@`mod common]$ pwd\n/dev/shm/mvngu/sage-4.3.1.alpha2/devel/sage-main/doc/common\n[mvngu`@`mod common]$ rm conf.pyc\n }}}\n This ensures that, after the patch is applied, generating the documentation with \"./sage -docbuild ...\" would first generate a byte code version of the patched `doc/common/conf.py` file. If the previous byte code file of `doc/common/conf.py` is not removed, then it's likely that the generated documentation (especially the HTML version) would still use the current copyright years \"2005--2009\".",
    "created_at": "2010-01-16T07:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69015",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I think the above patches should take care of updating the copyright years. Here's a description of these patches and where to apply them:

1. The file [README.txt](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/README.txt) should be placed under `SAGE_ROOT/`. That file is not under revision control, so the release manager needs to replace the current `README.txt` with the attached updated `README.txt`. To show the differences between the current `README.txt` in Sage 4.3.1.alpha2 and the updated `README.txt`, see the patch file [README.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/README.patch). Note that this patch is only for showing differences; don't apply it.
2. The patch [trac_7933-mac-app.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/trac_7933-mac-app.patch) should be applied to the `data/` repository under `SAGE_ROOT/data/extcode`. Before applying that patch, the release manager needs to remove a junk file under that directory:
 {{{
[mvngu`@`mod extcode]$ pwd
/dev/shm/mvngu/sage-4.3.1.alpha2/data/extcode
[mvngu`@`mod extcode]$ hg st
? sage/ext/.DS_Store.rej
[mvngu`@`mod extcode]$ rm sage/ext/.DS_Store.rej 
[mvngu`@`mod extcode]$ hg st
<no-output>
 }}}
 After removing the junk file, then apply the patch.
1. Finally, apply the patch [trac_7933-doc-builder.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/trac_7933-doc-builder.patch) to the repository `sage-main`. This patch affects the configuration file `doc/common/conf.py`, so the file's corresponding Python byte code file should be removed:
 {{{
[mvngu`@`mod common]$ pwd
/dev/shm/mvngu/sage-4.3.1.alpha2/devel/sage-main/doc/common
[mvngu`@`mod common]$ rm conf.pyc
 }}}
 This ensures that, after the patch is applied, generating the documentation with "./sage -docbuild ..." would first generate a byte code version of the patched `doc/common/conf.py` file. If the previous byte code file of `doc/common/conf.py` is not removed, then it's likely that the generated documentation (especially the HTML version) would still use the current copyright years "2005--2009".



---

archive/issue_comments_069016.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T07:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069017.json:
```json
{
    "body": "All three patches apply cleanly.\u00a0 In particular, they're in line with [UpdateCopyright](http://wiki.sagemath.org/devel/UpdateCopyright).\n\nNote: I don't have access to a Mac, so I can't test the changes in the extcode patch (if they're testable).\n\nIn case someone hasn't already mentioned it: a current copyright year also hints that a project is actively developed.",
    "created_at": "2010-01-31T00:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69017",
    "user": "https://github.com/qed777"
}
```

All three patches apply cleanly.  In particular, they're in line with [UpdateCopyright](http://wiki.sagemath.org/devel/UpdateCopyright).

Note: I don't have access to a Mac, so I can't test the changes in the extcode patch (if they're testable).

In case someone hasn't already mentioned it: a current copyright year also hints that a project is actively developed.



---

archive/issue_comments_069018.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T00:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69018",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018995.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-02T05:17:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7933#event-18995"
}
```



---

archive/issue_comments_069019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T05:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_069020.json:
```json
{
    "body": "Merged as per the above instructions.",
    "created_at": "2010-02-02T05:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7933#issuecomment-69020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged as per the above instructions.
