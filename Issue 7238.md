# Issue 7238: sagenb notebook: insert new cell *above* text cell

archive/issues_007238.json:
```json
{
    "body": "Assignee: boothby\n\nThis is a longstanding annoying GUI issue with the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7238\n\n",
    "created_at": "2009-10-18T06:31:05Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "sagenb notebook: insert new cell *above* text cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7238",
    "user": "@williamstein"
}
```
Assignee: boothby

This is a longstanding annoying GUI issue with the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/7238





---

archive/issue_comments_060041.json:
```json
{
    "body": "Attachment [trac_7238.patch](tarball://root/attachments/some-uuid/ticket7238/trac_7238.patch) by @williamstein created at 2009-10-18 09:22:16\n\npart 1",
    "created_at": "2009-10-18T09:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60041",
    "user": "@williamstein"
}
```

Attachment [trac_7238.patch](tarball://root/attachments/some-uuid/ticket7238/trac_7238.patch) by @williamstein created at 2009-10-18 09:22:16

part 1



---

archive/issue_comments_060042.json:
```json
{
    "body": "first patch works but there is an issue: \nNOTE: there is still one issue, namely that if you insert a new cell above a text cell,\nthen delete it, the cursor jumps to the end of the worksheet.  If you refresh before\ndeleting then everything is fine.",
    "created_at": "2009-10-18T09:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60042",
    "user": "@williamstein"
}
```

first patch works but there is an issue: 
NOTE: there is still one issue, namely that if you insert a new cell above a text cell,
then delete it, the cursor jumps to the end of the worksheet.  If you refresh before
deleting then everything is fine.



---

archive/issue_comments_060043.json:
```json
{
    "body": "Attachment [trac_7238-part2.patch](tarball://root/attachments/some-uuid/ticket7238/trac_7238-part2.patch) by @williamstein created at 2009-10-19 17:35:30\n\nthis fixes moving between cells",
    "created_at": "2009-10-19T17:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60043",
    "user": "@williamstein"
}
```

Attachment [trac_7238-part2.patch](tarball://root/attachments/some-uuid/ticket7238/trac_7238-part2.patch) by @williamstein created at 2009-10-19 17:35:30

this fixes moving between cells



---

archive/issue_comments_060044.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T17:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60044",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060045.json:
```json
{
    "body": "Patch works as advertised. Positive review.",
    "created_at": "2009-10-19T18:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60045",
    "user": "@TimDumol"
}
```

Patch works as advertised. Positive review.



---

archive/issue_comments_060046.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-19T18:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60046",
    "user": "@TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060047.json:
```json
{
    "body": "I think there are a few problems with the patch set:\n\n* [Expected] doctest failures in `cell.py`.\n* Adding a new text cell at the end of a worksheet does not update the `cell_id_list`.\n* In Firebug's console, there are two errors:\n  * `get_cell(id) is null` in `resize_all_cells()` for text cells.\n  * `cell_prev is null` in `join_cell()` when the top cell is a text cell.\n\nI'm working on part 3.",
    "created_at": "2009-10-20T01:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60047",
    "user": "@qed777"
}
```

I think there are a few problems with the patch set:

* [Expected] doctest failures in `cell.py`.
* Adding a new text cell at the end of a worksheet does not update the `cell_id_list`.
* In Firebug's console, there are two errors:
  * `get_cell(id) is null` in `resize_all_cells()` for text cells.
  * `cell_prev is null` in `join_cell()` when the top cell is a text cell.

I'm working on part 3.



---

archive/issue_comments_060048.json:
```json
{
    "body": "Also:  Evaluating all cells, deleting all output, slide mode.\n\nA potential annoyance:  Reopening (or editing) a worksheet fuses consecutive text cells.\nShould we have \"special\" delimiters for text cells?",
    "created_at": "2009-10-20T06:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60048",
    "user": "@qed777"
}
```

Also:  Evaluating all cells, deleting all output, slide mode.

A potential annoyance:  Reopening (or editing) a worksheet fuses consecutive text cells.
Should we have "special" delimiters for text cells?



---

archive/issue_comments_060049.json:
```json
{
    "body": "Part 3.  Various small fixes.  Apply on top of other patches.",
    "created_at": "2009-10-20T06:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60049",
    "user": "@qed777"
}
```

Part 3.  Various small fixes.  Apply on top of other patches.



---

archive/issue_comments_060050.json:
```json
{
    "body": "Attachment [trac_7238-insert_above_text_cell.patch](tarball://root/attachments/some-uuid/ticket7238/trac_7238-insert_above_text_cell.patch) by @williamstein created at 2009-10-20 18:07:25\n\n> A potential annoyance: Reopening (or editing) a worksheet fuses consecutive \n> text cells. Should we have \"special\" delimiters for text cells? \n\nThis has been the case since there first were text cells.  Some people consider it good (a feature), and others find it confusing.",
    "created_at": "2009-10-20T18:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60050",
    "user": "@williamstein"
}
```

Attachment [trac_7238-insert_above_text_cell.patch](tarball://root/attachments/some-uuid/ticket7238/trac_7238-insert_above_text_cell.patch) by @williamstein created at 2009-10-20 18:07:25

> A potential annoyance: Reopening (or editing) a worksheet fuses consecutive 
> text cells. Should we have "special" delimiters for text cells? 

This has been the case since there first were text cells.  Some people consider it good (a feature), and others find it confusing.



---

archive/issue_comments_060051.json:
```json
{
    "body": "Tim Dumol gave this a positive review, then Mitesh Patel found some issues and I read his code and was happy with all those fixes and verified that they fixed the new issues.  So I think it is reasonable to give this a positive review.  It is also now merged in sagenb.",
    "created_at": "2009-10-20T23:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60051",
    "user": "@williamstein"
}
```

Tim Dumol gave this a positive review, then Mitesh Patel found some issues and I read his code and was happy with all those fixes and verified that they fixed the new issues.  So I think it is reasonable to give this a positive review.  It is also now merged in sagenb.



---

archive/issue_comments_060052.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-20T23:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7238#issuecomment-60052",
    "user": "@williamstein"
}
```

Resolution: fixed
