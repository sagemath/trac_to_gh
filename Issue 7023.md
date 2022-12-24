# Issue 7023: Upgrade to Cython 0.11.3

archive/issues_007023.json:
```json
{
    "body": "Assignee: mabshoff\n\nJust released Cyton 0.11.3. \n\nhttp://groups.google.com/group/cython-users/browse_thread/thread/a63639d3246bcf48 \n\nIt would be good to have this in Sage. As well as bugfixes and better error reporting, the really nice improvement is the ability to profile Cython code with cProfile and friends. (It's not on by default yet, use the cython.profile directive to enable it for a given module/function). \n\nAll doctests pass after applying the patch, which merely fixes some previously uncaught bugs (useless dead code). \n\nIssue created by migration from https://trac.sagemath.org/ticket/7023\n\n",
    "created_at": "2009-09-27T07:27:57Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Upgrade to Cython 0.11.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7023",
    "user": "robertwb"
}
```
Assignee: mabshoff

Just released Cyton 0.11.3. 

http://groups.google.com/group/cython-users/browse_thread/thread/a63639d3246bcf48 

It would be good to have this in Sage. As well as bugfixes and better error reporting, the really nice improvement is the ability to profile Cython code with cProfile and friends. (It's not on by default yet, use the cython.profile directive to enable it for a given module/function). 

All doctests pass after applying the patch, which merely fixes some previously uncaught bugs (useless dead code). 

Issue created by migration from https://trac.sagemath.org/ticket/7023





---

archive/issue_comments_058162.json:
```json
{
    "body": "Attachment [7023-cython-0.11.3.patch](tarball://root/attachments/some-uuid/ticket7023/7023-cython-0.11.3.patch) by robertwb created at 2009-09-27 07:53:53\n\nSpkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.3.spkg",
    "created_at": "2009-09-27T07:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7023#issuecomment-58162",
    "user": "robertwb"
}
```

Attachment [7023-cython-0.11.3.patch](tarball://root/attachments/some-uuid/ticket7023/7023-cython-0.11.3.patch) by robertwb created at 2009-09-27 07:53:53

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.3.spkg



---

archive/issue_comments_058163.json:
```json
{
    "body": "Note the upgrade to 0.12 is being tracked at #7272.  That upgrade depends on this patch too.",
    "created_at": "2009-10-28T09:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7023#issuecomment-58163",
    "user": "jason"
}
```

Note the upgrade to 0.12 is being tracked at #7272.  That upgrade depends on this patch too.



---

archive/issue_comments_058164.json:
```json
{
    "body": "Looks good to me.  I've merged the patch in 4.3.alpha0, but used the spkg from #7272 (along with its patch).",
    "created_at": "2009-11-17T11:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7023#issuecomment-58164",
    "user": "mhansen"
}
```

Looks good to me.  I've merged the patch in 4.3.alpha0, but used the spkg from #7272 (along with its patch).



---

archive/issue_comments_058165.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T11:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7023#issuecomment-58165",
    "user": "mhansen"
}
```

Resolution: fixed
