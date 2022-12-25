# Issue 411: sage_c_lib moved into primary sage tree

archive/issues_000411.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  dmharvey@math.harvard.edu\n\nThe attached mercurial bundle has the c_lib moved into the tree and some other enhancements as well:\n\n1)  Many modifications to .hgignore to make it ignore c_lib junk and keep it from ignore .h files and .c files only under sage/\n2)  setup.py misc improvements\n3)  setup.py checks for recursive dependencies on .pyx files.  So if you have a deep includes -- i.e. a .pxi included from a .pxi, it will now include this in the age comparisons.  Unfortunately, this approximately doubles the time on a no-op build.  I don't know what other people think about this, but I'm rather freakish about knowing that my builds are reliable so I think it is worth it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/411\n\n",
    "created_at": "2007-08-09T02:26:12Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "sage_c_lib moved into primary sage tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/411",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

CC:  dmharvey@math.harvard.edu

The attached mercurial bundle has the c_lib moved into the tree and some other enhancements as well:

1)  Many modifications to .hgignore to make it ignore c_lib junk and keep it from ignore .h files and .c files only under sage/
2)  setup.py misc improvements
3)  setup.py checks for recursive dependencies on .pyx files.  So if you have a deep includes -- i.e. a .pxi included from a .pxi, it will now include this in the age comparisons.  Unfortunately, this approximately doubles the time on a no-op build.  I don't know what other people think about this, but I'm rather freakish about knowing that my builds are reliable so I think it is worth it.



Issue created by migration from https://trac.sagemath.org/ticket/411





---

archive/issue_comments_002015.json:
```json
{
    "body": "Mercurial bundle",
    "created_at": "2007-08-09T02:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2015",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Mercurial bundle



---

archive/issue_comments_002016.json:
```json
{
    "body": "Attachment [c_lib_in_tree_and_setup_enhancements.hg](tarball://root/attachments/some-uuid/ticket411/c_lib_in_tree_and_setup_enhancements.hg) by dmharvey created at 2007-08-28 18:49:39",
    "created_at": "2007-08-28T18:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2016",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [c_lib_in_tree_and_setup_enhancements.hg](tarball://root/attachments/some-uuid/ticket411/c_lib_in_tree_and_setup_enhancements.hg) by dmharvey created at 2007-08-28 18:49:39



---

archive/issue_comments_002017.json:
```json
{
    "body": "Conversion to using SCons and integrated c_lib into tree",
    "created_at": "2007-08-28T18:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2017",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Conversion to using SCons and integrated c_lib into tree



---

archive/issue_comments_002018.json:
```json
{
    "body": "Attachment [c_lib_into_main.patch](tarball://root/attachments/some-uuid/ticket411/c_lib_into_main.patch) by jbmohler created at 2007-08-28 18:52:46\n\nIgnore the attachment c_lib_in_tree_and_setup_enhancements.hg\n\nThe attachment c_lib_into_main.patch lacks some setup_enhancements of the first patch, but it is converted to scons.\n\nThe scons-0.97.spkg from the experimental repository is needed for this patch.",
    "created_at": "2007-08-28T18:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2018",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [c_lib_into_main.patch](tarball://root/attachments/some-uuid/ticket411/c_lib_into_main.patch) by jbmohler created at 2007-08-28 18:52:46

Ignore the attachment c_lib_in_tree_and_setup_enhancements.hg

The attachment c_lib_into_main.patch lacks some setup_enhancements of the first patch, but it is converted to scons.

The scons-0.97.spkg from the experimental repository is needed for this patch.



---

archive/issue_comments_002019.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-08-29T16:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2019",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_002020.json:
```json
{
    "body": "throw on top of c_lib_into_main.patch, fixes mysterious segfault in libsingular related to strdup()",
    "created_at": "2007-08-29T20:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2020",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

throw on top of c_lib_into_main.patch, fixes mysterious segfault in libsingular related to strdup()



---

archive/issue_comments_002021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T00:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2021",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000437.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-08-30T00:58:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/411#event-437"
}
```



---

archive/issue_comments_002022.json:
```json
{
    "body": "Attachment [strdup.patch](tarball://root/attachments/some-uuid/ticket411/strdup.patch) by @williamstein created at 2007-08-30 00:58:04\n\nI incorporated this in.  There were some weird issues with mpz_get_pyintlong not being defined, which I fixed\nby adding back some files to ext.  Fix this correctly in the future.",
    "created_at": "2007-08-30T00:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2022",
    "user": "https://github.com/williamstein"
}
```

Attachment [strdup.patch](tarball://root/attachments/some-uuid/ticket411/strdup.patch) by @williamstein created at 2007-08-30 00:58:04

I incorporated this in.  There were some weird issues with mpz_get_pyintlong not being defined, which I fixed
by adding back some files to ext.  Fix this correctly in the future.
