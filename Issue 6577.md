# Issue 6577: Reference manual build errors in 4.1.1.alpha0

archive/issues_006577.json:
```json
{
    "body": "Assignee: tba\n\nThis is in 4.1.1.alpha0: \n\n```\nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.get:8: (WARNING/2) Inline literal start-string without end-string.                                              \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.ramified_at:11: (WARNING/2) Inline literal start-string without end-string.                                     \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.unramified_outside:13: (WARNING/2) Inline literal start-string without end-string.                              \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:3: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.                                                                                 \nWARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:4: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n        \n\nIssue created by migration from https://trac.sagemath.org/ticket/6577\n\n",
    "created_at": "2009-07-21T09:56:01Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Reference manual build errors in 4.1.1.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6577",
    "user": "davidloeffler"
}
```
Assignee: tba

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

archive/issue_comments_053693.json:
```json
{
    "body": "Attachment [trac_6577-refmanual_warnings_4_1_1_alpha0.patch](tarball://root/attachments/some-uuid/ticket6577/trac_6577-refmanual_warnings_4_1_1_alpha0.patch) by davidloeffler created at 2009-07-21 11:21:40",
    "created_at": "2009-07-21T11:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53693",
    "user": "davidloeffler"
}
```

Attachment [trac_6577-refmanual_warnings_4_1_1_alpha0.patch](tarball://root/attachments/some-uuid/ticket6577/trac_6577-refmanual_warnings_4_1_1_alpha0.patch) by davidloeffler created at 2009-07-21 11:21:40



---

archive/issue_comments_053694.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-07-21T11:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53694",
    "user": "davidloeffler"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_053695.json:
```json
{
    "body": "Changing keywords from \"\" to \"reference manual\".",
    "created_at": "2009-07-21T11:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53695",
    "user": "davidloeffler"
}
```

Changing keywords from "" to "reference manual".



---

archive/issue_comments_053696.json:
```json
{
    "body": "Begone are the warnings :-)",
    "created_at": "2009-07-21T14:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53696",
    "user": "mvngu"
}
```

Begone are the warnings :-)



---

archive/issue_comments_053697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T01:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6577#issuecomment-53697",
    "user": "mvngu"
}
```

Resolution: fixed
