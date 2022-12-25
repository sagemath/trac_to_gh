# Issue 3079: [with patch, needs work] quaddouble configuration and spkg-install cleaning

archive/issues_003079.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: editor_mabshoff\n\nThe current spkg-install keep the strange default of the qd \npackage. The proposed patch enable ieee error compliant addition\nand disable sloppy division and multiplication.\nFurther spkg-install currently comes with the following strange\nsettings:\n CXXFLAGS='-fPIC -O3 -Dx86'\n-fpic, beside being platform specific, is useless in this case\nas no shared object is produced. Flags like -Dx86 are best left\nto the configure script, fortunately this should be without effect,\nthe correct parameter being \"X86\". Both flags should be removed as well. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3079\n\n",
    "closed_at": "2008-08-11T05:25:57Z",
    "created_at": "2008-05-02T11:34:25Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs work] quaddouble configuration and spkg-install cleaning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3079",
    "user": "https://github.com/kiwifb"
}
```
Assignee: mabshoff

Keywords: editor_mabshoff

The current spkg-install keep the strange default of the qd 
package. The proposed patch enable ieee error compliant addition
and disable sloppy division and multiplication.
Further spkg-install currently comes with the following strange
settings:
 CXXFLAGS='-fPIC -O3 -Dx86'
-fpic, beside being platform specific, is useless in this case
as no shared object is produced. Flags like -Dx86 are best left
to the configure script, fortunately this should be without effect,
the correct parameter being "X86". Both flags should be removed as well. 

Issue created by migration from https://trac.sagemath.org/ticket/3079





---

archive/issue_comments_021193.json:
```json
{
    "body": "Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3079/spkg-install.patch) by mabshoff created at 2008-05-02 11:59:25",
    "created_at": "2008-05-02T11:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3079#issuecomment-21193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3079/spkg-install.patch) by mabshoff created at 2008-05-02 11:59:25



---

archive/issue_events_006955.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-02T11:59:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "milestone": "sage-3.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3079#event-6955"
}
```



---

archive/issue_comments_021194.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T21:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3079#issuecomment-21194",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_021195.json:
```json
{
    "body": "Since we are dumping quaddouble this ticket is wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-11T05:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3079#issuecomment-21195",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since we are dumping quaddouble this ticket is wontfix.

Cheers,

Michael



---

archive/issue_comments_021196.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-08-11T05:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3079#issuecomment-21196",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_events_006956.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T05:25:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3079#event-6956"
}
```



---

archive/issue_events_006957.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T05:25:57Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3079",
    "milestone": "sage-3.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3079#event-6957"
}
```
