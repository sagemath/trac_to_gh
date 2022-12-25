# Issue 5470: Update Cython entry in Developer's Guide

archive/issues_005470.json:
```json
{
    "body": "Assignee: @cswiercz\n\nCC:  @cswiercz\n\nKeywords: documentation, cython\n\nThe current description for adding a new Cython module is outdated:\n\nhttp://www.sagemath.org/doc/prog/node29.html\n\n```\n3. Create a .pyx file in the Sage library and add a listing for it to the variable\next_modules in the file SAGE_ROOT/devel/sage/setup.py. For example, the file \nSAGE_ROOT/devel/sage/sage/graphs/chrompoly.pyx has lines\n\n    Extension('sage.graphs.chrompoly',\n              ['sage/graphs/chrompoly.pyx']\n              ), \\\n\nin setup.py. Also, the module - in this example sage.graphs.chrompoly - needs to be \nadded to the packages list in setup.py . Then type sage -b to build Sage with the new \ncode.\n```\n\n\nThis documentation needs to account for the separate `module_list.py` file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5470\n\n",
    "created_at": "2009-03-10T19:54:07Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Update Cython entry in Developer's Guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5470",
    "user": "https://github.com/cswiercz"
}
```
Assignee: @cswiercz

CC:  @cswiercz

Keywords: documentation, cython

The current description for adding a new Cython module is outdated:

http://www.sagemath.org/doc/prog/node29.html

```
3. Create a .pyx file in the Sage library and add a listing for it to the variable
ext_modules in the file SAGE_ROOT/devel/sage/setup.py. For example, the file 
SAGE_ROOT/devel/sage/sage/graphs/chrompoly.pyx has lines

    Extension('sage.graphs.chrompoly',
              ['sage/graphs/chrompoly.pyx']
              ), \

in setup.py. Also, the module - in this example sage.graphs.chrompoly - needs to be 
added to the packages list in setup.py . Then type sage -b to build Sage with the new 
code.
```


This documentation needs to account for the separate `module_list.py` file.

Issue created by migration from https://trac.sagemath.org/ticket/5470





---

archive/issue_comments_042367.json:
```json
{
    "body": "Yes, it is under version control:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.rc2/devel/sage$ hg log doc/en/developer/coding_in_other.rst\nchangeset:   11689:d83194742483\nuser:        Mike Hansen <mhansen@gmail.com>\ndate:        Tue Feb 24 09:13:12 2009 -0800\nsummary:     Added the documentation to the main repository.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T20:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42367",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, it is under version control:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.rc2/devel/sage$ hg log doc/en/developer/coding_in_other.rst
changeset:   11689:d83194742483
user:        Mike Hansen <mhansen@gmail.com>
date:        Tue Feb 24 09:13:12 2009 -0800
summary:     Added the documentation to the main repository.
```


Cheers,

Michael



---

archive/issue_comments_042368.json:
```json
{
    "body": "Attachment [sage-5470.patch](tarball://root/attachments/some-uuid/ticket5470/sage-5470.patch) by @cswiercz created at 2009-03-10 21:39:11",
    "created_at": "2009-03-10T21:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42368",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-5470.patch](tarball://root/attachments/some-uuid/ticket5470/sage-5470.patch) by @cswiercz created at 2009-03-10 21:39:11



---

archive/issue_comments_042369.json:
```json
{
    "body": "D'oh! I must have been looking at another screen or something.\n\nThe patch is attached an is ready for review.",
    "created_at": "2009-03-10T21:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42369",
    "user": "https://github.com/cswiercz"
}
```

D'oh! I must have been looking at another screen or something.

The patch is attached an is ready for review.



---

archive/issue_comments_042370.json:
```json
{
    "body": "Mostly looks good. The only complaint I have is about step (2)\n\n\n```\n   #. Then, add the module name to the ``packages`` list in the file\n      ``SAGE_ROOT/devel/sage/setup.py``.\n```\n\n\none only does this if one is making an new package (directory).",
    "created_at": "2009-03-17T00:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42370",
    "user": "https://github.com/robertwb"
}
```

Mostly looks good. The only complaint I have is about step (2)


```
   #. Then, add the module name to the ``packages`` list in the file
      ``SAGE_ROOT/devel/sage/setup.py``.
```


one only does this if one is making an new package (directory).



---

archive/issue_comments_042371.json:
```json
{
    "body": "Attachment [sage-5470-part2.patch](tarball://root/attachments/some-uuid/ticket5470/sage-5470-part2.patch) by @cswiercz created at 2009-03-30 21:29:50\n\nApply in the following order:\n\n`sage-5470.patch`\n\n`sage-5470-part2.patch`",
    "created_at": "2009-03-30T21:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42371",
    "user": "https://github.com/cswiercz"
}
```

Attachment [sage-5470-part2.patch](tarball://root/attachments/some-uuid/ticket5470/sage-5470-part2.patch) by @cswiercz created at 2009-03-30 21:29:50

Apply in the following order:

`sage-5470.patch`

`sage-5470-part2.patch`



---

archive/issue_comments_042372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T01:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42372",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042373.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T01:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5470#issuecomment-42373",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_events_005724.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-01T01:15:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5470",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5470#event-5724"
}
```
