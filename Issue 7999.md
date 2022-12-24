# Issue 7999: SyntaxError when loading Sage 4.3.1.rc1 due to non-ASCII character

archive/issues_007999.json:
```json
{
    "body": "Assignee: tbd\n\nI built Sage 4.3.1.rc1 from source and then produced a sage.math binary. Loading the binary resulted in the following SyntaxError:\n\n```\nSyntaxError: Non-ASCII character '\\xc3' in file /dev/shm/mvngu/sage-4.3.1.rc1-dev/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py on line 5448, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (ell_rational_field.py, line 5447)\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nThe guilty line is line 5447:\n\n```\n           modular forms. Ast\u00e9risque, (295):ix, 117-290, 2004.                  \n```\n\nof `sage/schemes/elliptic_curves/ell_rational_field.py`, which doesn't have the following preamble to indicate that the file has non-ASCII characters:\n\n```\n# -*- coding: utf-8 -*-\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7999\n\n",
    "created_at": "2010-01-19T15:29:25Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "SyntaxError when loading Sage 4.3.1.rc1 due to non-ASCII character",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7999",
    "user": "mvngu"
}
```
Assignee: tbd

I built Sage 4.3.1.rc1 from source and then produced a sage.math binary. Loading the binary resulted in the following SyntaxError:

```
SyntaxError: Non-ASCII character '\xc3' in file /dev/shm/mvngu/sage-4.3.1.rc1-dev/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py on line 5448, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (ell_rational_field.py, line 5447)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

The guilty line is line 5447:

```
           modular forms. Astérisque, (295):ix, 117-290, 2004.                  
```

of `sage/schemes/elliptic_curves/ell_rational_field.py`, which doesn't have the following preamble to indicate that the file has non-ASCII characters:

```
# -*- coding: utf-8 -*-
```


Issue created by migration from https://trac.sagemath.org/ticket/7999





---

archive/issue_comments_069898.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T15:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7999#issuecomment-69898",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069899.json:
```json
{
    "body": "based on Sage 4.3.1.rc1",
    "created_at": "2010-01-19T16:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7999#issuecomment-69899",
    "user": "mvngu"
}
```

based on Sage 4.3.1.rc1



---

archive/issue_comments_069900.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T19:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7999#issuecomment-69900",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069901.json:
```json
{
    "body": "Attachment [trac_7999-encoding.patch](tarball://root/attachments/some-uuid/ticket7999/trac_7999-encoding.patch) by @qed777 created at 2010-01-19 19:42:03",
    "created_at": "2010-01-19T19:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7999#issuecomment-69901",
    "user": "@qed777"
}
```

Attachment [trac_7999-encoding.patch](tarball://root/attachments/some-uuid/ticket7999/trac_7999-encoding.patch) by @qed777 created at 2010-01-19 19:42:03



---

archive/issue_comments_069902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T20:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7999#issuecomment-69902",
    "user": "@rlmill"
}
```

Resolution: fixed
