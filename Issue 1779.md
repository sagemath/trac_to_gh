# Issue 1779: setup.py computes the cache of some irrelevent files

archive/issues_001779.json:
```json
{
    "body": "Assignee: cwitty\n\nI discovered this:\n\nInstalling c_lib\nscons: `install' is up to date.\nTraceback (most recent call last):\n  File \"setup.py\", line 1079, in <module>\n    H = str(hash_of_cython_file_timestamps())\n  File \"setup.py\", line 1076, in hash_of_cython_file_timestamps\n    return hash_of_dir('sage')\n  File \"setup.py\", line 1072, in hash_of_dir\n    h += hash_of_dir(z)\n  File \"setup.py\", line 1072, in hash_of_dir\n    h += hash_of_dir(z)\n  File \"setup.py\", line 1074, in hash_of_dir\n    h += hash(os.path.getmtime(z))\n  File \"/home/bob/sage/local/lib/python2.5/posixpath.py\", line 143, in getmtime\n    return os.stat(filename).st_mtime\nOSError: [Errno 2] No such file or directory: 'sage/rings/polynomial/.#polynomial_element.pyx'\nsage: There was an error installing modified sage library code.\n\nEmacs must have made a temp file .#polynomial_element.pyx. Python screws up on hashing this; the string should be sanitized in some way, I suppose; however, we do not need to be hashing the timestamp on hidden .pyx files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1779\n\n",
    "created_at": "2008-01-14T23:12:39Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "setup.py computes the cache of some irrelevent files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1779",
    "user": "moretti"
}
```
Assignee: cwitty

I discovered this:

Installing c_lib
scons: `install' is up to date.
Traceback (most recent call last):
  File "setup.py", line 1079, in <module>
    H = str(hash_of_cython_file_timestamps())
  File "setup.py", line 1076, in hash_of_cython_file_timestamps
    return hash_of_dir('sage')
  File "setup.py", line 1072, in hash_of_dir
    h += hash_of_dir(z)
  File "setup.py", line 1072, in hash_of_dir
    h += hash_of_dir(z)
  File "setup.py", line 1074, in hash_of_dir
    h += hash(os.path.getmtime(z))
  File "/home/bob/sage/local/lib/python2.5/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: 'sage/rings/polynomial/.#polynomial_element.pyx'
sage: There was an error installing modified sage library code.

Emacs must have made a temp file .#polynomial_element.pyx. Python screws up on hashing this; the string should be sanitized in some way, I suppose; however, we do not need to be hashing the timestamp on hidden .pyx files.

Issue created by migration from https://trac.sagemath.org/ticket/1779





---

archive/issue_comments_011265.json:
```json
{
    "body": "The attached patch should fix the build issues",
    "created_at": "2008-01-14T23:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1779#issuecomment-11265",
    "user": "moretti"
}
```

The attached patch should fix the build issues



---

archive/issue_comments_011266.json:
```json
{
    "body": "Attachment [hash_fix.patch](tarball://root/attachments/some-uuid/ticket1779/hash_fix.patch) by moretti created at 2008-01-14 23:31:29",
    "created_at": "2008-01-14T23:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1779#issuecomment-11266",
    "user": "moretti"
}
```

Attachment [hash_fix.patch](tarball://root/attachments/some-uuid/ticket1779/hash_fix.patch) by moretti created at 2008-01-14 23:31:29



---

archive/issue_comments_011267.json:
```json
{
    "body": "Patch looks good to me. It seems unlikely that anybody would add legitimate Cython files that start with a dot.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T02:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1779#issuecomment-11267",
    "user": "mabshoff"
}
```

Patch looks good to me. It seems unlikely that anybody would add legitimate Cython files that start with a dot.

Cheers,

Michael



---

archive/issue_comments_011268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T02:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1779#issuecomment-11268",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011269.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3",
    "created_at": "2008-01-15T02:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1779#issuecomment-11269",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha3
