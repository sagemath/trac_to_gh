# Issue 9294: wrong usage of except

archive/issues_009294.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @hemmecke\n\nsagenb-0.8.p2/src/sagenb/sagenb/notebook/js.py\n\nsays\n\ntry:\n    from sage.misc.misc import SAGE_ROOT\n    from pkg_resources import Requirement, working_set\n    sagenb_path = working_set.find(Requirement.parse('sagenb')).location\n    debug_mode = SAGE_ROOT not in os.path.realpath(sagenb_path)\nexcept AttributeError, ImportError:\n    debug_mode = False\n\nBut according to what I cite below, it should rather be\n\nexcept (AttributeError, ImportError):\n\nhttp://docs.python.org/tutorial/errors.html\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9294\n\n",
    "created_at": "2010-06-21T09:36:28Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "wrong usage of except",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9294",
    "user": "@hemmecke"
}
```
Assignee: jason, was

CC:  @hemmecke

sagenb-0.8.p2/src/sagenb/sagenb/notebook/js.py

says

try:
    from sage.misc.misc import SAGE_ROOT
    from pkg_resources import Requirement, working_set
    sagenb_path = working_set.find(Requirement.parse('sagenb')).location
    debug_mode = SAGE_ROOT not in os.path.realpath(sagenb_path)
except AttributeError, ImportError:
    debug_mode = False

But according to what I cite below, it should rather be

except (AttributeError, ImportError):

http://docs.python.org/tutorial/errors.html


Issue created by migration from https://trac.sagemath.org/ticket/9294





---

archive/issue_comments_087518.json:
```json
{
    "body": "Attachment [js-except-fix.diff](tarball://root/attachments/some-uuid/ticket9294/js-except-fix.diff) by @hemmecke created at 2010-06-21 09:36:54",
    "created_at": "2010-06-21T09:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87518",
    "user": "@hemmecke"
}
```

Attachment [js-except-fix.diff](tarball://root/attachments/some-uuid/ticket9294/js-except-fix.diff) by @hemmecke created at 2010-06-21 09:36:54



---

archive/issue_comments_087519.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-21T09:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87519",
    "user": "@hemmecke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087520.json:
```json
{
    "body": "Nice catch! Positive review.",
    "created_at": "2010-07-05T10:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87520",
    "user": "@TimDumol"
}
```

Nice catch! Positive review.



---

archive/issue_comments_087521.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-05T10:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87521",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087522.json:
```json
{
    "body": "See also\n\nhttp://groups.google.com/group/sage-notebook/msg/e74a7366f9f50f3c\n\nThe bug seems to be fixed already.",
    "created_at": "2010-07-05T11:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87522",
    "user": "@hemmecke"
}
```

See also

http://groups.google.com/group/sage-notebook/msg/e74a7366f9f50f3c

The bug seems to be fixed already.



---

archive/issue_comments_087523.json:
```json
{
    "body": "Didn't seem to be the case when I applied the patch. The boxen.math url is just giving me a 500 error.",
    "created_at": "2010-07-05T11:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87523",
    "user": "@TimDumol"
}
```

Didn't seem to be the case when I applied the patch. The boxen.math url is just giving me a 500 error.



---

archive/issue_comments_087524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T05:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9294#issuecomment-87524",
    "user": "@TimDumol"
}
```

Resolution: fixed
