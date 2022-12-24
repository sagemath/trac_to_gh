# Issue 6518: [with patch, needs review] doctest script uses deprecated signature for showwarning

archive/issues_006518.json:
```json
{
    "body": "Assignee: tbd\n\nI got this while doctesting a patch with 4.1:\n\n\n```\nsage -t  \"devel/sage-s/sage/symbolic/expression_conversions.py\"\n/home/burcin/sage/sage-4.1/local/lib/python/site-packages/sage/misc/misc.py:1901: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument\n  warn(message, DeprecationWarning, stacklevel=3)\n```\n\n\nApparently showwarning got a new argument in Python 2.6, as stated here:\n\nhttp://docs.python.org/library/warnings.html#showwarning/show\n\nAttached patch fixes the `sage-doctest` script to use the new call signature. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6518\n\n",
    "created_at": "2009-07-12T12:18:31Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] doctest script uses deprecated signature for showwarning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6518",
    "user": "burcin"
}
```
Assignee: tbd

I got this while doctesting a patch with 4.1:


```
sage -t  "devel/sage-s/sage/symbolic/expression_conversions.py"
/home/burcin/sage/sage-4.1/local/lib/python/site-packages/sage/misc/misc.py:1901: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument
  warn(message, DeprecationWarning, stacklevel=3)
```


Apparently showwarning got a new argument in Python 2.6, as stated here:

http://docs.python.org/library/warnings.html#showwarning/show

Attached patch fixes the `sage-doctest` script to use the new call signature. 

Issue created by migration from https://trac.sagemath.org/ticket/6518





---

archive/issue_comments_053131.json:
```json
{
    "body": "Attachment [trac_6518-doctest_warning.patch](tarball://root/attachments/some-uuid/ticket6518/trac_6518-doctest_warning.patch) by burcin created at 2009-07-12 12:20:52\n\npatch for the scripts repository",
    "created_at": "2009-07-12T12:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6518#issuecomment-53131",
    "user": "burcin"
}
```

Attachment [trac_6518-doctest_warning.patch](tarball://root/attachments/some-uuid/ticket6518/trac_6518-doctest_warning.patch) by burcin created at 2009-07-12 12:20:52

patch for the scripts repository



---

archive/issue_comments_053132.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-07-13T20:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6518#issuecomment-53132",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_053133.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-17T09:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6518#issuecomment-53133",
    "user": "mvngu"
}
```

Resolution: fixed
