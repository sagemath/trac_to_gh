# Issue 989: [with patch] Stripping $ from documentation

archive/issues_000989.json:
```json
{
    "body": "Assignee: tba\n\n```\nsage: edit?\n```\npresently yields\n\n```\n ...\n          sage: import sage.misc.edit_module as m\n          sage: m.set_edit_template(\"vi -c {line} {file}\")\n ...\n```\nwhereas the last line should read\n\n```\n         sage: m.set_edit_template(\"vi -c ${line} ${file}\")\n```\ni.e., $ gets stripped from EXAMPLE text where it should not.\n\nIssue created by migration from https://trac.sagemath.org/ticket/989\n\n",
    "closed_at": "2007-11-06T21:35:27Z",
    "created_at": "2007-10-25T01:14:24Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "[with patch] Stripping $ from documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/989",
    "user": "https://github.com/nbruin"
}
```
Assignee: tba

```
sage: edit?
```
presently yields

```
 ...
          sage: import sage.misc.edit_module as m
          sage: m.set_edit_template("vi -c {line} {file}")
 ...
```
whereas the last line should read

```
         sage: m.set_edit_template("vi -c ${line} ${file}")
```
i.e., $ gets stripped from EXAMPLE text where it should not.

Issue created by migration from https://trac.sagemath.org/ticket/989





---

archive/issue_comments_006016.json:
```json
{
    "body": "$ signs are stripped from docstrings in sage/misc/sagedoc.py, as part of an effort to convert LaTeX math markup to plain text.\n\nPerhaps the right fix is to notice doctests, and disable these modifications for that part of the docstring.",
    "created_at": "2007-10-27T18:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/989#issuecomment-6016",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

$ signs are stripped from docstrings in sage/misc/sagedoc.py, as part of an effort to convert LaTeX math markup to plain text.

Perhaps the right fix is to notice doctests, and disable these modifications for that part of the docstring.



---

archive/issue_events_002731.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-03T15:09:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/989",
    "milestone": "sage-2.8.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/989#event-2731"
}
```



---

archive/issue_comments_006017.json:
```json
{
    "body": "Attachment [683-989-ncalexan-1.patch](tarball://root/attachments/some-uuid/ticket989/683-989-ncalexan-1.patch) by @ncalexan created at 2007-11-04 07:32:28\n\nChangelog for the patch:\n\n683,989: add 'nodetex' directive to docstrings: doesn't strip (la)tex code from docstrings.\n\nThe first line of a docstring is parsed as a comma-separated list of\ndirectives (no whitespace in directives!).  For example:\n\n```\nr\"\"\"nodetex,notyetimplemented\n...\n\"\"\"\n```\n\nIf 'nodetex' is one of the directives, then no (la)tex code is stripped from\nthe docstring.  The model was the 'nodoctest' directive already found at the\ntop of a file.",
    "created_at": "2007-11-04T07:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/989#issuecomment-6017",
    "user": "https://github.com/ncalexan"
}
```

Attachment [683-989-ncalexan-1.patch](tarball://root/attachments/some-uuid/ticket989/683-989-ncalexan-1.patch) by @ncalexan created at 2007-11-04 07:32:28

Changelog for the patch:

683,989: add 'nodetex' directive to docstrings: doesn't strip (la)tex code from docstrings.

The first line of a docstring is parsed as a comma-separated list of
directives (no whitespace in directives!).  For example:

```
r"""nodetex,notyetimplemented
...
"""
```

If 'nodetex' is one of the directives, then no (la)tex code is stripped from
the docstring.  The model was the 'nodoctest' directive already found at the
top of a file.



---

archive/issue_comments_006018.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T21:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/989#issuecomment-6018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_events_002732.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T21:35:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/989",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/989#event-2732"
}
```



---

archive/issue_comments_006019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T21:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/989#issuecomment-6019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
