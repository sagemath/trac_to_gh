# Issue 411: sage_c_lib moved into primary sage tree

archive/issues_000411.json:
```json
{
    "body": "Assignee: was\n\nCC:  dmharvey@math.harvard.edu\n\nThe attached mercurial bundle has the c_lib moved into the tree and some other enhancements as well:\n\n1)  Many modifications to .hgignore to make it ignore c_lib junk and keep it from ignore .h files and .c files only under sage/\n2)  setup.py misc improvements\n3)  setup.py checks for recursive dependencies on .pyx files.  So if you have a deep includes -- i.e. a .pxi included from a .pxi, it will now include this in the age comparisons.  Unfortunately, this approximately doubles the time on a no-op build.  I don't know what other people think about this, but I'm rather freakish about knowing that my builds are reliable so I think it is worth it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/411\n\n",
    "created_at": "2007-08-09T02:26:12Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "sage_c_lib moved into primary sage tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/411",
    "user": "jbmohler"
}
```
Assignee: was

CC:  dmharvey@math.harvard.edu

The attached mercurial bundle has the c_lib moved into the tree and some other enhancements as well:

1)  Many modifications to .hgignore to make it ignore c_lib junk and keep it from ignore .h files and .c files only under sage/
2)  setup.py misc improvements
3)  setup.py checks for recursive dependencies on .pyx files.  So if you have a deep includes -- i.e. a .pxi included from a .pxi, it will now include this in the age comparisons.  Unfortunately, this approximately doubles the time on a no-op build.  I don't know what other people think about this, but I'm rather freakish about knowing that my builds are reliable so I think it is worth it.



Issue created by migration from https://trac.sagemath.org/ticket/411





---

archive/issue_comments_002024.json:
```json
{
    "body": "Mercurial bundle",
    "created_at": "2007-08-09T02:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2024",
    "user": "jbmohler"
}
```

Mercurial bundle



---

archive/issue_comments_002025.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-08-28T18:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2025",
    "user": "dmharvey"
}
```

Attachment



---

archive/issue_comments_002026.json:
```json
{
    "body": "Conversion to using SCons and integrated c_lib into tree",
    "created_at": "2007-08-28T18:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2026",
    "user": "jbmohler"
}
```

Conversion to using SCons and integrated c_lib into tree



---

archive/issue_comments_002027.json:
```json
{
    "body": "Attachment\n\nIgnore the attachment c_lib_in_tree_and_setup_enhancements.hg\n\nThe attachment c_lib_into_main.patch lacks some setup_enhancements of the first patch, but it is converted to scons.\n\nThe scons-0.97.spkg from the experimental repository is needed for this patch.",
    "created_at": "2007-08-28T18:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2027",
    "user": "jbmohler"
}
```

Attachment

Ignore the attachment c_lib_in_tree_and_setup_enhancements.hg

The attachment c_lib_into_main.patch lacks some setup_enhancements of the first patch, but it is converted to scons.

The scons-0.97.spkg from the experimental repository is needed for this patch.



---

archive/issue_comments_002028.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-08-29T16:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2028",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_002029.json:
```json
{
    "body": "throw on top of c_lib_into_main.patch, fixes mysterious segfault in libsingular related to strdup()",
    "created_at": "2007-08-29T20:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2029",
    "user": "dmharvey"
}
```

throw on top of c_lib_into_main.patch, fixes mysterious segfault in libsingular related to strdup()



---

archive/issue_comments_002030.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T00:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2030",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002031.json:
```json
{
    "body": "Attachment\n\nI incorporated this in.  There were some weird issues with mpz_get_pyintlong not being defined, which I fixed\nby adding back some files to ext.  Fix this correctly in the future.",
    "created_at": "2007-08-30T00:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/411#issuecomment-2031",
    "user": "was"
}
```

Attachment

I incorporated this in.  There were some weird issues with mpz_get_pyintlong not being defined, which I fixed
by adding back some files to ext.  Fix this correctly in the future.
