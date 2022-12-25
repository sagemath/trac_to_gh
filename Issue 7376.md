# Issue 7376: searching published worksheets does not work to just search for username

archive/issues_007376.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein\n\nIt would be really nice if the \"Search\" function in the upper left of the published worksheet listing also searched for the username (e.g., I could search for \"jason3\" and get all of my published worksheets).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7376\n\n",
    "created_at": "2009-11-02T17:59:56Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "searching published worksheets does not work to just search for username",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7376",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @williamstein

It would be really nice if the "Search" function in the upper left of the published worksheet listing also searched for the username (e.g., I could search for "jason3" and get all of my published worksheets).

Issue created by migration from https://trac.sagemath.org/ticket/7376





---

archive/issue_comments_061693.json:
```json
{
    "body": "We should also consider supporting more complex queries, e.g., on an \"Advanced Search\" page.  By the way, according to [codenode-devel](http://groups.google.com/group/codenode-devel/browse_thread/thread/d3ffefa3b09937b6/98bdf00f65441934?#98bdf00f65441934), Codenode uses [Whoosh](http://whoosh.ca/) for full-text search.",
    "created_at": "2009-11-04T05:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61693",
    "user": "https://github.com/qed777"
}
```

We should also consider supporting more complex queries, e.g., on an "Advanced Search" page.  By the way, according to [codenode-devel](http://groups.google.com/group/codenode-devel/browse_thread/thread/d3ffefa3b09937b6/98bdf00f65441934?#98bdf00f65441934), Codenode uses [Whoosh](http://whoosh.ca/) for full-text search.



---

archive/issue_comments_061694.json:
```json
{
    "body": "It seems this will work: \n\n```diff\ndiff --git a/sagenb/notebook/worksheet.py b/sagenb/notebook/worksheet.py\n--- a/sagenb/notebook/worksheet.py\n+++ b/sagenb/notebook/worksheet.py\n@@ -1973,7 +1973,7 @@ class Worksheet(object):\n         \"\"\"\n         # Load the worksheet data file from disk.\n         filename = self.worksheet_html_filename()\n-        r = (self.owner().lower() + ' ' + self.name().lower() + ' '\n+        r = (self.publisher().lower() + ' ' + self.name().lower() + ' '\n              + open(filename).read().lower())\n         # Check that every single word is in the file from disk.\n         for W in split_search_string_into_keywords(search):\n```\n",
    "created_at": "2009-11-12T15:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61694",
    "user": "https://github.com/qed777"
}
```

It seems this will work: 

```diff
diff --git a/sagenb/notebook/worksheet.py b/sagenb/notebook/worksheet.py
--- a/sagenb/notebook/worksheet.py
+++ b/sagenb/notebook/worksheet.py
@@ -1973,7 +1973,7 @@ class Worksheet(object):
         """
         # Load the worksheet data file from disk.
         filename = self.worksheet_html_filename()
-        r = (self.owner().lower() + ' ' + self.name().lower() + ' '
+        r = (self.publisher().lower() + ' ' + self.name().lower() + ' '
              + open(filename).read().lower())
         # Check that every single word is in the file from disk.
         for W in split_search_string_into_keywords(search):
```




---

archive/issue_comments_061695.json:
```json
{
    "body": "But:\n\n```python\nsage: from sagenb.notebook.worksheet import split_search_string_into_keywords as ss\nsage: ss('hello there')\n['hello', 'there']\nsage: ss(\" foo bar  'modular form' hello there\")\n['modular form', \"'\", 'hello', 'there']\n```\n\n\n[Pyparsing](http://pyparsing.wikispaces.com/) is another alternative.  There's a [search query parser](http://pyparsing.wikispaces.com/file/view/searchparser.py) among the [examples](http://pyparsing.wikispaces.com/Examples).  The license appears to be a modified-BSD license.\n\nShould we add modifiers?  For example, the search phrase `\"Fourier user:joe` would restrict the search to worksheets published by Joe.  Other possible modifiers: `title`, `text_cell`, `compute_cell`, `dates`, `input`, `output`, `collaborators`, `rating`.",
    "created_at": "2009-11-12T15:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61695",
    "user": "https://github.com/qed777"
}
```

But:

```python
sage: from sagenb.notebook.worksheet import split_search_string_into_keywords as ss
sage: ss('hello there')
['hello', 'there']
sage: ss(" foo bar  'modular form' hello there")
['modular form', "'", 'hello', 'there']
```


[Pyparsing](http://pyparsing.wikispaces.com/) is another alternative.  There's a [search query parser](http://pyparsing.wikispaces.com/file/view/searchparser.py) among the [examples](http://pyparsing.wikispaces.com/Examples).  The license appears to be a modified-BSD license.

Should we add modifiers?  For example, the search phrase `"Fourier user:joe` would restrict the search to worksheets published by Joe.  Other possible modifiers: `title`, `text_cell`, `compute_cell`, `dates`, `input`, `output`, `collaborators`, `rating`.



---

archive/issue_comments_061696.json:
```json
{
    "body": "Search by publisher. Apply to sagenb repo.",
    "created_at": "2009-11-12T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61696",
    "user": "https://github.com/qed777"
}
```

Search by publisher. Apply to sagenb repo.



---

archive/issue_comments_061697.json:
```json
{
    "body": "Attachment [trac_7376-search_by_username.patch](tarball://root/attachments/some-uuid/ticket7376/trac_7376-search_by_username.patch) by @qed777 created at 2009-11-12 15:49:44\n\nAlternate version: Search by owner and publisher.  Apply only this patch to sagenb repo.",
    "created_at": "2009-11-12T15:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61697",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7376-search_by_username.patch](tarball://root/attachments/some-uuid/ticket7376/trac_7376-search_by_username.patch) by @qed777 created at 2009-11-12 15:49:44

Alternate version: Search by owner and publisher.  Apply only this patch to sagenb repo.



---

archive/issue_comments_061698.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-12T15:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61698",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061699.json:
```json
{
    "body": "Attachment [trac_7376-search_by_username_v2.patch](tarball://root/attachments/some-uuid/ticket7376/trac_7376-search_by_username_v2.patch) by @qed777 created at 2009-11-12 15:50:54\n\nShould we do more with this ticket?",
    "created_at": "2009-11-12T15:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61699",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7376-search_by_username_v2.patch](tarball://root/attachments/some-uuid/ticket7376/trac_7376-search_by_username_v2.patch) by @qed777 created at 2009-11-12 15:50:54

Should we do more with this ticket?



---

archive/issue_comments_061700.json:
```json
{
    "body": "Nice; this works as advertised.\n\nI like all the discussion above about even more sophisticated searching systems, but of course they shouldn't hold up this ticket getting a... positive review!",
    "created_at": "2009-12-09T00:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61700",
    "user": "https://github.com/williamstein"
}
```

Nice; this works as advertised.

I like all the discussion above about even more sophisticated searching systems, but of course they shouldn't hold up this ticket getting a... positive review!



---

archive/issue_comments_061701.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T00:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61701",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007598.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-12-09T01:12:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7376#event-7598"
}
```



---

archive/issue_comments_061702.json:
```json
{
    "body": "I merged this patch into sagenb-0.4.6.",
    "created_at": "2009-12-09T01:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61702",
    "user": "https://github.com/williamstein"
}
```

I merged this patch into sagenb-0.4.6.



---

archive/issue_comments_061703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T01:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7376#issuecomment-61703",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
