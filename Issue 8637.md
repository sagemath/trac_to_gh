# Issue 8637: typo in sagenb/data/sage/html/worksheet_listing.html, line 117

archive/issues_008637.json:
```json
{
    "body": "Assignee: jason, was\n\nFrom IRC on March 31 2010:\n\n```\n15:24 < uc-paul> OK to report a bug in sagenb in this room?\n15:28 < uc-paul> My public facing Sage notebook server has a log file full of \n                 entries like the following:\n15:28 < uc-paul> *.*.*.* - - [01/Apr/2010:11:04:58 +1300] \"GET \n/pub/?typ=activereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereverserevers\n15:28 < uc-paul> eversereversereversereversereversereversereversereversereverser\neversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereverse&sort=owner&reverse=True HTTP/1.0\" 200 31347\n15:28 < uc-paul> This is due to a typo in \n                 sagenb/data/sage/html/worksheet_listing.html, line 117\n15:31 < uc-paul> Patch at  http://www.math.canterbury.ac.nz/~p.brouwers/sage/worksheet.patch\n```\n\n\nThe patch, in case it gets taken down, is:\n\n```\n--- a/sagenb/data/sage/html/worksheet_listing.html      2010-04-01 10:39:58.000000000 +1300\n+++ b/sagenb/data/sage/html/worksheet_listing.html      2010-04-01 10:47:49.000000000 +1300\n@@ -114,7 +114,7 @@\n             </td>\n\n             <td>\n-                <a class=\"listcontrol\" href=\".?typ={{ typ }}{{ '' if sort != 'last_edited' or reverse else 'reverse&=True' }}\">\n+                <a class=\"listcontrol\" href=\".?typ={{ typ }}{{ '' if sort != 'last_edited' or reverse else '&reverse=True' }}\">\n                     Last Edited\n                 </a>\n             </td>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8637\n\n",
    "created_at": "2010-03-31T23:34:09Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "typo in sagenb/data/sage/html/worksheet_listing.html, line 117",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8637",
    "user": "ddrake"
}
```
Assignee: jason, was

From IRC on March 31 2010:

```
15:24 < uc-paul> OK to report a bug in sagenb in this room?
15:28 < uc-paul> My public facing Sage notebook server has a log file full of 
                 entries like the following:
15:28 < uc-paul> *.*.*.* - - [01/Apr/2010:11:04:58 +1300] "GET 
/pub/?typ=activereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereverserevers
15:28 < uc-paul> eversereversereversereversereversereversereversereversereverser
eversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereverse&sort=owner&reverse=True HTTP/1.0" 200 31347
15:28 < uc-paul> This is due to a typo in 
                 sagenb/data/sage/html/worksheet_listing.html, line 117
15:31 < uc-paul> Patch at  http://www.math.canterbury.ac.nz/~p.brouwers/sage/worksheet.patch
```


The patch, in case it gets taken down, is:

```
--- a/sagenb/data/sage/html/worksheet_listing.html      2010-04-01 10:39:58.000000000 +1300
+++ b/sagenb/data/sage/html/worksheet_listing.html      2010-04-01 10:47:49.000000000 +1300
@@ -114,7 +114,7 @@
             </td>

             <td>
-                <a class="listcontrol" href=".?typ={{ typ }}{{ '' if sort != 'last_edited' or reverse else 'reverse&=True' }}">
+                <a class="listcontrol" href=".?typ={{ typ }}{{ '' if sort != 'last_edited' or reverse else '&reverse=True' }}">
                     Last Edited
                 </a>
             </td>
```


Issue created by migration from https://trac.sagemath.org/ticket/8637





---

archive/issue_comments_078322.json:
```json
{
    "body": "Attachment [trac_8637.patch](tarball://root/attachments/some-uuid/ticket8637/trac_8637.patch) by ddrake created at 2010-03-31 23:47:22\n\nI made Paul's patch into a proper Mercurial patch and credited him for it. Please review!",
    "created_at": "2010-03-31T23:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8637#issuecomment-78322",
    "user": "ddrake"
}
```

Attachment [trac_8637.patch](tarball://root/attachments/some-uuid/ticket8637/trac_8637.patch) by ddrake created at 2010-03-31 23:47:22

I made Paul's patch into a proper Mercurial patch and credited him for it. Please review!



---

archive/issue_comments_078323.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-31T23:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8637#issuecomment-78323",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078324.json:
```json
{
    "body": "Nice catch by Paul. Positive review.",
    "created_at": "2010-04-01T19:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8637#issuecomment-78324",
    "user": "timdumol"
}
```

Nice catch by Paul. Positive review.



---

archive/issue_comments_078325.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-01T19:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8637#issuecomment-78325",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-04T04:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8637#issuecomment-78326",
    "user": "timdumol"
}
```

Resolution: fixed
