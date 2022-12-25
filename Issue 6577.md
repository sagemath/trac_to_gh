# Issue 6577: [with patch, positive review] Reference manual build errors in 4.1.1.alpha0

archive/issues_006577.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: reference manual\n\nThis is in 4.1.1.alpha0: \n\n```\nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.get:8: (WARNING/2) Inline literal start-string without end-string.                                              \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.ramified_at:11: (WARNING/2) Inline literal start-string without end-string.                                     \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.unramified_outside:13: (WARNING/2) Inline literal start-string without end-string.                              \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:3: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.                                                                                 \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:4: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```        \n\nIssue created by migration from https://trac.sagemath.org/ticket/6577\n\n",
    "closed_at": "2009-07-23T01:58:29Z",
    "created_at": "2009-07-21T09:56:01Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] Reference manual build errors in 4.1.1.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6577",
    "user": "https://github.com/loefflerd"
}
```
Assignee: tba

Keywords: reference manual

This is in 4.1.1.alpha0: 

```
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.get:8: (WARNING/2) Inline literal start-string without end-string.                                              
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.ramified_at:11: (WARNING/2) Inline literal start-string without end-string.                                     
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.unramified_outside:13: (WARNING/2) Inline literal start-string without end-string.                              
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:3: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.                                                                                 
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:4: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```        

Issue created by migration from https://trac.sagemath.org/ticket/6577





---

archive/issue_comments_053592.json:
```json
{
    "body": "Attachment [trac_6577-refmanual_warnings_4_1_1_alpha0.patch](tarball://root/attachments/some-uuid/ticket6577/trac_6577-refmanual_warnings_4_1_1_alpha0.patch) by @loefflerd created at 2009-07-21 11:21:40",
    "created_at": "2009-07-21T11:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53592",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6577-refmanual_warnings_4_1_1_alpha0.patch](tarball://root/attachments/some-uuid/ticket6577/trac_6577-refmanual_warnings_4_1_1_alpha0.patch) by @loefflerd created at 2009-07-21 11:21:40



---

archive/issue_comments_053593.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-07-21T11:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53593",
    "user": "https://github.com/loefflerd"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_053594.json:
```json
{
    "body": "Changing keywords from \"\" to \"reference manual\".",
    "created_at": "2009-07-21T11:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53594",
    "user": "https://github.com/loefflerd"
}
```

Changing keywords from "" to "reference manual".



---

archive/issue_comments_053595.json:
```json
{
    "body": "Begone are the warnings :-)",
    "created_at": "2009-07-21T14:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53595",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Begone are the warnings :-)



---

archive/issue_events_015517.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T01:58:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6577#event-15517"
}
```



---

archive/issue_comments_053596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T01:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53596",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
