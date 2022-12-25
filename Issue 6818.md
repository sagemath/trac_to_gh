# Issue 6818: [with patch; needs review] maxima interface gets dramatically slower over time

archive/issues_006818.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf you do a few hundred calls to the maxima interface, it gets way way slower.\n\n\n```\nsage: timeit(\"str(maxima.eval('1+2'))\")\n5 loops, best of 3: 758 \u00b5s per loop\nsage: timeit(\"str(maxima.eval('1+2'))\")\n625 loops, best of 3: 1.22 ms per loop\nsage: timeit(\"str(maxima.eval('1+2'))\")\n125 loops, best of 3: 2.98 ms per loop\nsage: timeit(\"str(maxima.eval('1+2'))\")\n125 loops, best of 3: 3.97 ms per loop\n```\n\n\nIt turns out that this is caused by computation of the maxima input prompt number, which uses the following \"clever\" algorithm to compute \"n+1\":\n\n\n```\n(defmfun makelabel (x)\n  (when (and $dskuse (not $nolabels) (> (incf dcount) $filesize))\n    (setq dcount 0)\n    (dsksave))\n  (setq linelable ($concat '|| x $linenum))\n  (unless $nolabels\n    (when (or (null (cdr $labels))\n              (when (member linelable (cddr $labels) :test #'equal)\n                (setf $labels (delete linelable $labels :count 1 :test #'eq)) t)\n              (not (eq linelable (cadr $labels))))\n      (setq $labels (cons (car $labels) (cons linelable (cdr $labels))))))\n  linelable)\n```\n\n\nMore precisely, this code \"checks\nthat the list containing all labels does not contain the new label\nwhich it generates. After you create 2*35150 labels, this takes longer than when maxima starts.\", according to Andrej Vodopivec who tracked this down and told us a simple fix.  Put:\n\n\n```\nnolabels:true;\n```\n\n\nat the beginning of our Maxima session.  This is fine for Sage, since Sage doesn't use the labels in any way.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6818\n\n",
    "created_at": "2009-08-24T14:43:39Z",
    "labels": [
        "component: interfaces",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch; needs review] maxima interface gets dramatically slower over time",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6818",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

If you do a few hundred calls to the maxima interface, it gets way way slower.


```
sage: timeit("str(maxima.eval('1+2'))")
5 loops, best of 3: 758 µs per loop
sage: timeit("str(maxima.eval('1+2'))")
625 loops, best of 3: 1.22 ms per loop
sage: timeit("str(maxima.eval('1+2'))")
125 loops, best of 3: 2.98 ms per loop
sage: timeit("str(maxima.eval('1+2'))")
125 loops, best of 3: 3.97 ms per loop
```


It turns out that this is caused by computation of the maxima input prompt number, which uses the following "clever" algorithm to compute "n+1":


```
(defmfun makelabel (x)
  (when (and $dskuse (not $nolabels) (> (incf dcount) $filesize))
    (setq dcount 0)
    (dsksave))
  (setq linelable ($concat '|| x $linenum))
  (unless $nolabels
    (when (or (null (cdr $labels))
              (when (member linelable (cddr $labels) :test #'equal)
                (setf $labels (delete linelable $labels :count 1 :test #'eq)) t)
              (not (eq linelable (cadr $labels))))
      (setq $labels (cons (car $labels) (cons linelable (cdr $labels))))))
  linelable)
```


More precisely, this code "checks
that the list containing all labels does not contain the new label
which it generates. After you create 2*35150 labels, this takes longer than when maxima starts.", according to Andrej Vodopivec who tracked this down and told us a simple fix.  Put:


```
nolabels:true;
```


at the beginning of our Maxima session.  This is fine for Sage, since Sage doesn't use the labels in any way.

Issue created by migration from https://trac.sagemath.org/ticket/6818





---

archive/issue_comments_056121.json:
```json
{
    "body": "Attachment [trac_6818.patch](tarball://root/attachments/some-uuid/ticket6818/trac_6818.patch) by @williamstein created at 2009-08-24 15:51:26",
    "created_at": "2009-08-24T15:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6818#issuecomment-56121",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6818.patch](tarball://root/attachments/some-uuid/ticket6818/trac_6818.patch) by @williamstein created at 2009-08-24 15:51:26



---

archive/issue_comments_056122.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-08-24T23:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6818#issuecomment-56122",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_056123.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T01:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6818#issuecomment-56123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-25T01:17:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6818",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6818#event-7052"
}
```
