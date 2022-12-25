# Issue 6010: [with patch, positive review] implement various invariants for genus 2 hyperelliptic curves

archive/issues_006010.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  kohel\n\nKeywords: genus 2 hyperelliptic igusa invariants\n\nPatch says it best -- Igusa and related invariants for hyperelliptic curves of genus 2 (equivalently, quintic/sextic binary forms).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6010\n\n",
    "closed_at": "2009-05-12T06:42:00Z",
    "created_at": "2009-05-08T21:58:26Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, positive review] implement various invariants for genus 2 hyperelliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6010",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  kohel

Keywords: genus 2 hyperelliptic igusa invariants

Patch says it best -- Igusa and related invariants for hyperelliptic curves of genus 2 (equivalently, quintic/sextic binary forms).

Issue created by migration from https://trac.sagemath.org/ticket/6010





---

archive/issue_comments_047735.json:
```json
{
    "body": "Wow, awesome that you did this! Thanks!!",
    "created_at": "2009-05-09T15:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6010#issuecomment-47735",
    "user": "https://github.com/williamstein"
}
```

Wow, awesome that you did this! Thanks!!



---

archive/issue_comments_047736.json:
```json
{
    "body": "Can you rebase this against 3.4.2.  I get:\n\n```\npatching file sage/schemes/hyperelliptic_curves/all.py\nHunk #1 FAILED at 0\n1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/all.py.rej\npatching file sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\nHunk #1 FAILED at 6\nHunk #2 FAILED at 25\n2 out of 3 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py.rej\npatching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py\nHunk #1 FAILED at 62\n1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej\nfile sage/schemes/hyperelliptic_curves/invariants.py already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/invariants.py.rej\nabort: patch failed to apply\n\n```",
    "created_at": "2009-05-12T05:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6010#issuecomment-47736",
    "user": "https://github.com/williamstein"
}
```

Can you rebase this against 3.4.2.  I get:

```
patching file sage/schemes/hyperelliptic_curves/all.py
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/all.py.rej
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py
Hunk #1 FAILED at 6
Hunk #2 FAILED at 25
2 out of 3 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py.rej
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py
Hunk #1 FAILED at 62
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py.rej
file sage/schemes/hyperelliptic_curves/invariants.py already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/invariants.py.rej
abort: patch failed to apply

```



---

archive/issue_comments_047737.json:
```json
{
    "body": "Attachment [trac_6010-genus-2-invariants-2.2.patch](tarball://root/attachments/some-uuid/ticket6010/trac_6010-genus-2-invariants-2.2.patch) by @ncalexan created at 2009-05-12 06:08:01",
    "created_at": "2009-05-12T06:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6010#issuecomment-47737",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6010-genus-2-invariants-2.2.patch](tarball://root/attachments/some-uuid/ticket6010/trac_6010-genus-2-invariants-2.2.patch) by @ncalexan created at 2009-05-12 06:08:01



---

archive/issue_comments_047738.json:
```json
{
    "body": "(apply only trac_6010-genus-2-invariants-2.2.patch )",
    "created_at": "2009-05-12T06:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6010#issuecomment-47738",
    "user": "https://github.com/williamstein"
}
```

(apply only trac_6010-genus-2-invariants-2.2.patch )



---

archive/issue_events_014117.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-12T06:42:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6010#event-14117"
}
```



---

archive/issue_comments_047739.json:
```json
{
    "body": "Merged trac_6010-genus-2-invariants-2.2.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T06:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6010#issuecomment-47739",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_6010-genus-2-invariants-2.2.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_047740.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T06:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6010#issuecomment-47740",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
