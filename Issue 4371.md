# Issue 4371: Add support for lazy attributes via a decorator

archive/issues_004371.json:
```json
{
    "body": "Assignee: cwitty\n\nThe lazy-attribute-...-nt patch on the sage-combinat patch servers is a first implementation of lazy attributes (see the doc in the patch).\nComments and alternative implementations welcome! See the current caveats in the doc\n\nCheers,\n\t\t\t\t\t\t\t\tNicolas\n\nIssue created by migration from https://trac.sagemath.org/ticket/4371\n\n",
    "created_at": "2008-10-26T13:30:55Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "Add support for lazy attributes via a decorator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4371",
    "user": "nthiery"
}
```
Assignee: cwitty

The lazy-attribute-...-nt patch on the sage-combinat patch servers is a first implementation of lazy attributes (see the doc in the patch).
Comments and alternative implementations welcome! See the current caveats in the doc

Cheers,
								Nicolas

Issue created by migration from https://trac.sagemath.org/ticket/4371





---

archive/issue_comments_032128.json:
```json
{
    "body": "Patch",
    "created_at": "2008-10-26T13:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32128",
    "user": "nthiery"
}
```

Patch



---

archive/issue_comments_032129.json:
```json
{
    "body": "Attachment [lazy_attributes-4371-nt.patch](tarball://root/attachments/some-uuid/ticket4371/lazy_attributes-4371-nt.patch) by nthiery created at 2008-10-26 13:35:59\n\nIn case I did not make myself clear: this patch is *not* ready for insertion in sage.\nIt's more of a request for comments!",
    "created_at": "2008-10-26T13:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32129",
    "user": "nthiery"
}
```

Attachment [lazy_attributes-4371-nt.patch](tarball://root/attachments/some-uuid/ticket4371/lazy_attributes-4371-nt.patch) by nthiery created at 2008-10-26 13:35:59

In case I did not make myself clear: this patch is *not* ready for insertion in sage.
It's more of a request for comments!



---

archive/issue_comments_032130.json:
```json
{
    "body": "Replying to [comment:1 nthiery]:\n> In case I did not make myself clear: this patch is *not* ready for insertion in sage.\n> It's more of a request for comments!\n\n\nHere are some possible fixes for improving the documentation of the patch **lazy_attributes-4371-nt.patch**:\n\n\n\n1.\n\n```\n-easilly override a given attribute; you don't need to call the\n+easily override a given attribute; you don't need to call the\n```\n\n\n\n\n2.\n\n```\n-the internal dictionnary of the object:\n+the internal dictionary of the object:\n```\n\n\n\nOtherwise, the doc looks OK to me.",
    "created_at": "2008-10-26T23:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32130",
    "user": "mvngu"
}
```

Replying to [comment:1 nthiery]:
> In case I did not make myself clear: this patch is *not* ready for insertion in sage.
> It's more of a request for comments!


Here are some possible fixes for improving the documentation of the patch **lazy_attributes-4371-nt.patch**:



1.

```
-easilly override a given attribute; you don't need to call the
+easily override a given attribute; you don't need to call the
```




2.

```
-the internal dictionnary of the object:
+the internal dictionary of the object:
```



Otherwise, the doc looks OK to me.



---

archive/issue_comments_032131.json:
```json
{
    "body": "Fixes applied. Thanks. Lazy attributes now work well with new style classes:\n\nhttp://sage.math.washington.edu:2144/file/03b4130fb25d/lazy_attributes-4371-nt.patch",
    "created_at": "2008-10-27T10:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32131",
    "user": "nthiery"
}
```

Fixes applied. Thanks. Lazy attributes now work well with new style classes:

http://sage.math.washington.edu:2144/file/03b4130fb25d/lazy_attributes-4371-nt.patch



---

archive/issue_comments_032132.json:
```json
{
    "body": "Replying to [comment:3 nthiery]:\n> Fixes applied. Thanks. Lazy attributes now work well with new style classes:\n> \n> http://sage.math.washington.edu:2144/file/03b4130fb25d/lazy_attributes-4371-nt.patch\n\n\nFor your new patch at the above URL, here's a fix to improve your documentation:\n\n```\n-Invoking Descriptors in the python reference manual).\n+Invoking Descriptors in the Python reference manual).\n```\n",
    "created_at": "2008-10-27T11:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32132",
    "user": "mvngu"
}
```

Replying to [comment:3 nthiery]:
> Fixes applied. Thanks. Lazy attributes now work well with new style classes:
> 
> http://sage.math.washington.edu:2144/file/03b4130fb25d/lazy_attributes-4371-nt.patch


For your new patch at the above URL, here's a fix to improve your documentation:

```
-Invoking Descriptors in the python reference manual).
+Invoking Descriptors in the Python reference manual).
```




---

archive/issue_comments_032133.json:
```json
{
    "body": "Nicolas,\n\nshould this patch be reviewed?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T17:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32133",
    "user": "mabshoff"
}
```

Nicolas,

should this patch be reviewed?

Cheers,

Michael



---

archive/issue_comments_032134.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-09T21:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32134",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032135.json:
```json
{
    "body": "Changing assignee from cwitty to nthiery.",
    "created_at": "2008-11-09T21:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32135",
    "user": "nthiery"
}
```

Changing assignee from cwitty to nthiery.



---

archive/issue_comments_032136.json:
```json
{
    "body": "Comments on it are more than welcome (in particular for the hasattr feature).\nNo need to waste time on a complete final review though.\n\nThanks,\n\t\t\tNicolas",
    "created_at": "2008-11-09T21:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32136",
    "user": "nthiery"
}
```

Comments on it are more than welcome (in particular for the hasattr feature).
No need to waste time on a complete final review though.

Thanks,
			Nicolas



---

archive/issue_comments_032137.json:
```json
{
    "body": "Ready for review.\nNot all desired features are implemented, but we need the bulk for upcoming patches.",
    "created_at": "2009-02-13T16:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32137",
    "user": "nthiery"
}
```

Ready for review.
Not all desired features are implemented, but we need the bulk for upcoming patches.



---

archive/issue_comments_032138.json:
```json
{
    "body": "Attachment [lazy_attributes-4371-nt.2.patch](tarball://root/attachments/some-uuid/ticket4371/lazy_attributes-4371-nt.2.patch) by nthiery created at 2009-02-13 16:12:26",
    "created_at": "2009-02-13T16:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32138",
    "user": "nthiery"
}
```

Attachment [lazy_attributes-4371-nt.2.patch](tarball://root/attachments/some-uuid/ticket4371/lazy_attributes-4371-nt.2.patch) by nthiery created at 2009-02-13 16:12:26



---

archive/issue_comments_032139.json:
```json
{
    "body": "Apply `lazy_attributes-4371-nt.2.patch` only.",
    "created_at": "2009-02-14T00:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32139",
    "user": "rlm"
}
```

Apply `lazy_attributes-4371-nt.2.patch` only.



---

archive/issue_comments_032140.json:
```json
{
    "body": "For the record note that \n\n* `__init___`\n* `__get__`\n\ndo not have doctests, but this will not stop the merge in this case :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32140",
    "user": "mabshoff"
}
```

For the record note that 

* `__init___`
* `__get__`

do not have doctests, but this will not stop the merge in this case :)

Cheers,

Michael



---

archive/issue_comments_032141.json:
```json
{
    "body": "Merged lazy_attributes-4371-nt.2.patch in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32141",
    "user": "mabshoff"
}
```

Merged lazy_attributes-4371-nt.2.patch in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_032142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T02:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32142",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032143.json:
```json
{
    "body": "Thanks Michael and Robert.\n\nMichael: could you please fold the patch into sage-3.3 on the sage-combinat patch server?\n\nThanks!",
    "created_at": "2009-02-14T18:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4371#issuecomment-32143",
    "user": "nthiery"
}
```

Thanks Michael and Robert.

Michael: could you please fold the patch into sage-3.3 on the sage-combinat patch server?

Thanks!
