# Issue 7762: `conf.py` for Sage documentation hardcodes sagenb path

archive/issues_007762.json:
```json
{
    "body": "Assignee: mvngu\n\njhpalmieri on sage-devel:\n\n```\nAs of 4.3.rc0, it looks like sagenb is perhaps being installed in the\nwrong place, resulting in failures when building the documentation\nwith the \"-j\" option (it can't find some of the relevant javascript):\n\ncopying static files... WARNING: static directory '/Applications/sage/\nlocal/lib/python/site-packages/sagenb/data/jsmath/' does not exist\n\nIn 4.3.alpha1, sagenb was installed in SAGE_ROOT/local/lib/python/site-\npackages/.\n\nIn 4.3.rc0 and 4.3.rc1, sagenb is installed in SAGE_ROOT/local/lib/\npython/site-packages/sagenb-0.4.7-py2.6.egg/\n\n[...]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7762\n\n",
    "created_at": "2009-12-24T17:25:05Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "`conf.py` for Sage documentation hardcodes sagenb path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7762",
    "user": "timdumol"
}
```
Assignee: mvngu

jhpalmieri on sage-devel:

```
As of 4.3.rc0, it looks like sagenb is perhaps being installed in the
wrong place, resulting in failures when building the documentation
with the "-j" option (it can't find some of the relevant javascript):

copying static files... WARNING: static directory '/Applications/sage/
local/lib/python/site-packages/sagenb/data/jsmath/' does not exist

In 4.3.alpha1, sagenb was installed in SAGE_ROOT/local/lib/python/site-
packages/.

In 4.3.rc0 and 4.3.rc1, sagenb is installed in SAGE_ROOT/local/lib/
python/site-packages/sagenb-0.4.7-py2.6.egg/

[...]
```


Issue created by migration from https://trac.sagemath.org/ticket/7762





---

archive/issue_comments_066862.json:
```json
{
    "body": "Attachment [trac_7762-conf-sagenb-path.patch](tarball://root/attachments/some-uuid/ticket7762/trac_7762-conf-sagenb-path.patch) by timdumol created at 2009-12-24 17:26:42\n\nUses `sagenb.misc.misc.DATA` instead.",
    "created_at": "2009-12-24T17:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7762#issuecomment-66862",
    "user": "timdumol"
}
```

Attachment [trac_7762-conf-sagenb-path.patch](tarball://root/attachments/some-uuid/ticket7762/trac_7762-conf-sagenb-path.patch) by timdumol created at 2009-12-24 17:26:42

Uses `sagenb.misc.misc.DATA` instead.



---

archive/issue_comments_066863.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-24T17:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7762#issuecomment-66863",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066864.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-24T18:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7762#issuecomment-66864",
    "user": "timdumol"
}
```

Resolution: duplicate



---

archive/issue_comments_066865.json:
```json
{
    "body": "This is a duplicate of #7755.",
    "created_at": "2009-12-24T18:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7762#issuecomment-66865",
    "user": "timdumol"
}
```

This is a duplicate of #7755.
