# Issue 7855: offline sage notebook

archive/issues_007855.json:
```json
{
    "body": "Assignee: was\n\nCC:  jhpalmieri\n\n\n```\nOn Jan 6, 1:03 am, William Stein <wst...@gmail.com> wrote:\n> Does anybody know how Google Gears or whatever does things like\n> offline gmail?\n\nFirst, skip Gears - that project fades out and will be html5. Chrome,\nFirefox and Safari are afaik nearly capable of providing these\nfeatures, or already do. Gears is just an early example that is\nsimilar to html5.\n\nOne feature is to have a database. Then, you can access tables and\nentries with (probably a bit limited?) SQL.  For the implementation,\nthere could be a table for each worksheet, or one table holding all\ncells and a n:m relationship table for worksheet:cell or something\nlike that.\n\nAnother html5 feature is to define offline resources. These are html\n(or other) files which are stored locally. They will be used for the\nstarting page and the static javascript code. Maybe it's also possible\nfor this feature to save everything as such an offline resource and no\nneed for the database mentioned above.\n\nhttp://www.w3.org/TR/offline-webapps/\nhttp://www.w3.org/TR/2009/WD-webdatabase-20091222/\nhttp://www.w3.org/TR/html5/offline.html\n\nand here i found examples:\nhttp://html5demos.com/\nespecially this file is interesting:\nhttp://html5demos.com/tweets.js\nand\nhttp://html5demos.com/offlineapp\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7855\n\n",
    "created_at": "2010-01-06T14:50:27Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "offline sage notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7855",
    "user": "was"
}
```
Assignee: was

CC:  jhpalmieri


```
On Jan 6, 1:03 am, William Stein <wst...@gmail.com> wrote:
> Does anybody know how Google Gears or whatever does things like
> offline gmail?

First, skip Gears - that project fades out and will be html5. Chrome,
Firefox and Safari are afaik nearly capable of providing these
features, or already do. Gears is just an early example that is
similar to html5.

One feature is to have a database. Then, you can access tables and
entries with (probably a bit limited?) SQL.  For the implementation,
there could be a table for each worksheet, or one table holding all
cells and a n:m relationship table for worksheet:cell or something
like that.

Another html5 feature is to define offline resources. These are html
(or other) files which are stored locally. They will be used for the
starting page and the static javascript code. Maybe it's also possible
for this feature to save everything as such an offline resource and no
need for the database mentioned above.

http://www.w3.org/TR/offline-webapps/
http://www.w3.org/TR/2009/WD-webdatabase-20091222/
http://www.w3.org/TR/html5/offline.html

and here i found examples:
http://html5demos.com/
especially this file is interesting:
http://html5demos.com/tweets.js
and
http://html5demos.com/offlineapp

```


Issue created by migration from https://trac.sagemath.org/ticket/7855





---

archive/issue_comments_068062.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-07-25T07:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7855#issuecomment-68062",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068063.json:
```json
{
    "body": "I think this is very outdated.",
    "created_at": "2017-07-25T07:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7855#issuecomment-68063",
    "user": "chapoton"
}
```

I think this is very outdated.



---

archive/issue_comments_068064.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-07-25T15:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7855#issuecomment-68064",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068065.json:
```json
{
    "body": "Agreed.",
    "created_at": "2017-07-25T15:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7855#issuecomment-68065",
    "user": "jhpalmieri"
}
```

Agreed.



---

archive/issue_comments_068066.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7855#issuecomment-68066",
    "user": "embray"
}
```

Resolution: wontfix
