# Issue 7497: notebook -- bug in viewing/editing attached files

archive/issues_007497.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook, click \"Data --> Upload or create file...\", then edit the file to contain\n\n```\nHi </textarea> foo bar \n```\n\n\nSave it and re-open it.  The foo bar is *outside* the text area!  This is because this is rendered using the data/sage/html/notebook/download_or_delete_datafile.html template with this line in it:\n\n```\n    <textarea class=\"edit\" name=\"textfield\" rows=17 cols=70 id=\"textfield\">{{ text_file_content }}</textarea>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7497\n\n",
    "created_at": "2009-11-20T05:37:45Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- bug in viewing/editing attached files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7497",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

In the notebook, click "Data --> Upload or create file...", then edit the file to contain

```
Hi </textarea> foo bar 
```


Save it and re-open it.  The foo bar is *outside* the text area!  This is because this is rendered using the data/sage/html/notebook/download_or_delete_datafile.html template with this line in it:

```
    <textarea class="edit" name="textfield" rows=17 cols=70 id="textfield">{{ text_file_content }}</textarea>
```


Issue created by migration from https://trac.sagemath.org/ticket/7497





---

archive/issue_comments_063269.json:
```json
{
    "body": "I think it's sufficient to replace `{{ text_file_content }}` with `{{ text_file_content|e }}` (cf. [this](http://jinja.pocoo.org/2/documentation/templates#html-escaping)).",
    "created_at": "2009-12-14T17:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63269",
    "user": "https://github.com/qed777"
}
```

I think it's sufficient to replace `{{ text_file_content }}` with `{{ text_file_content|e }}` (cf. [this](http://jinja.pocoo.org/2/documentation/templates#html-escaping)).



---

archive/issue_comments_063270.json:
```json
{
    "body": "Escape data file content placed in view/edit window.  sagenb repo.",
    "created_at": "2010-01-02T01:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63270",
    "user": "https://github.com/qed777"
}
```

Escape data file content placed in view/edit window.  sagenb repo.



---

archive/issue_comments_063271.json:
```json
{
    "body": "Attachment [trac_7497-escape_view_edit_attached.patch](tarball://root/attachments/some-uuid/ticket7497/trac_7497-escape_view_edit_attached.patch) by @qed777 created at 2010-01-02 01:08:54",
    "created_at": "2010-01-02T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63271",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7497-escape_view_edit_attached.patch](tarball://root/attachments/some-uuid/ticket7497/trac_7497-escape_view_edit_attached.patch) by @qed777 created at 2010-01-02 01:08:54



---

archive/issue_comments_063272.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63272",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063273.json:
```json
{
    "body": "#7786's v8 should subsume this.  If/when that ticket merges, please close this ticket.",
    "created_at": "2010-01-07T03:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63273",
    "user": "https://github.com/qed777"
}
```

#7786's v8 should subsume this.  If/when that ticket merges, please close this ticket.



---

archive/issue_events_007726.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:15:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7497#event-7726"
}
```



---

archive/issue_comments_063274.json:
```json
{
    "body": "Works with sagenb-0.6.",
    "created_at": "2010-01-19T03:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63274",
    "user": "https://github.com/TimDumol"
}
```

Works with sagenb-0.6.



---

archive/issue_comments_063275.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63275",
    "user": "https://github.com/TimDumol"
}
```

Resolution: duplicate
