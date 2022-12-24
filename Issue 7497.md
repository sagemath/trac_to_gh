# Issue 7497: notebook -- bug in viewing/editing attached files

archive/issues_007497.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook, click \"Data --> Upload or create file...\", then edit the file to contain\n\n```\nHi </textarea> foo bar \n```\n\n\nSave it and re-open it.  The foo bar is *outside* the text area!  This is because this is rendered using the data/sage/html/notebook/download_or_delete_datafile.html template with this line in it:\n\n```\n    <textarea class=\"edit\" name=\"textfield\" rows=17 cols=70 id=\"textfield\">{{ text_file_content }}</textarea>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7497\n\n",
    "created_at": "2009-11-20T05:37:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- bug in viewing/editing attached files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7497",
    "user": "was"
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

archive/issue_comments_063384.json:
```json
{
    "body": "I think it's sufficient to replace `{{ text_file_content }}` with `{{ text_file_content|e }}` (cf. [this](http://jinja.pocoo.org/2/documentation/templates#html-escaping)).",
    "created_at": "2009-12-14T17:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63384",
    "user": "mpatel"
}
```

I think it's sufficient to replace `{{ text_file_content }}` with `{{ text_file_content|e }}` (cf. [this](http://jinja.pocoo.org/2/documentation/templates#html-escaping)).



---

archive/issue_comments_063385.json:
```json
{
    "body": "Escape data file content placed in view/edit window.  sagenb repo.",
    "created_at": "2010-01-02T01:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63385",
    "user": "mpatel"
}
```

Escape data file content placed in view/edit window.  sagenb repo.



---

archive/issue_comments_063386.json:
```json
{
    "body": "Attachment [trac_7497-escape_view_edit_attached.patch](tarball://root/attachments/some-uuid/ticket7497/trac_7497-escape_view_edit_attached.patch) by mpatel created at 2010-01-02 01:08:54",
    "created_at": "2010-01-02T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63386",
    "user": "mpatel"
}
```

Attachment [trac_7497-escape_view_edit_attached.patch](tarball://root/attachments/some-uuid/ticket7497/trac_7497-escape_view_edit_attached.patch) by mpatel created at 2010-01-02 01:08:54



---

archive/issue_comments_063387.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T01:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63387",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063388.json:
```json
{
    "body": "#7786's v8 should subsume this.  If/when that ticket merges, please close this ticket.",
    "created_at": "2010-01-07T03:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63388",
    "user": "mpatel"
}
```

#7786's v8 should subsume this.  If/when that ticket merges, please close this ticket.



---

archive/issue_comments_063389.json:
```json
{
    "body": "Works with sagenb-0.6.",
    "created_at": "2010-01-19T03:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63389",
    "user": "timdumol"
}
```

Works with sagenb-0.6.



---

archive/issue_comments_063390.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7497#issuecomment-63390",
    "user": "timdumol"
}
```

Resolution: duplicate
