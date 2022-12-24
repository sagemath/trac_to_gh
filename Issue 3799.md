# Issue 3799: degree sequence should not be a single integer in graph_database

archive/issues_003799.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm\n\nThis is part of Jason Grout's formatting of his database, but it should be translated to and from a sequence of integers for the user.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3799\n\n",
    "created_at": "2008-08-10T10:04:30Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "degree sequence should not be a single integer in graph_database",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3799",
    "user": "rlm"
}
```
Assignee: rlm

CC:  rlm

This is part of Jason Grout's formatting of his database, but it should be translated to and from a sequence of integers for the user.

Issue created by migration from https://trac.sagemath.org/ticket/3799





---

archive/issue_comments_027009.json:
```json
{
    "body": "this patch inspired a full graph database re-write.  Coming soon!",
    "created_at": "2008-08-14T00:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27009",
    "user": "ekirkman"
}
```

this patch inspired a full graph database re-write.  Coming soon!



---

archive/issue_comments_027010.json:
```json
{
    "body": "Attachment [3799-databases.patch](tarball://root/attachments/some-uuid/ticket3799/3799-databases.patch) by ekirkman created at 2008-09-22 10:39:54",
    "created_at": "2008-09-22T10:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27010",
    "user": "ekirkman"
}
```

Attachment [3799-databases.patch](tarball://root/attachments/some-uuid/ticket3799/3799-databases.patch) by ekirkman created at 2008-09-22 10:39:54



---

archive/issue_comments_027011.json:
```json
{
    "body": "This patch should be stable for review, and it includes some definite improvements.  There will be more database enhancements coming, but they'll deserve their own tickets.  Oops -- one more patch coming with doctest fixes...",
    "created_at": "2008-09-22T11:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27011",
    "user": "ekirkman"
}
```

This patch should be stable for review, and it includes some definite improvements.  There will be more database enhancements coming, but they'll deserve their own tickets.  Oops -- one more patch coming with doctest fixes...



---

archive/issue_comments_027012.json:
```json
{
    "body": "Attachment [3799-doctest.patch](tarball://root/attachments/some-uuid/ticket3799/3799-doctest.patch) by ekirkman created at 2008-09-22 11:28:08",
    "created_at": "2008-09-22T11:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27012",
    "user": "ekirkman"
}
```

Attachment [3799-doctest.patch](tarball://root/attachments/some-uuid/ticket3799/3799-doctest.patch) by ekirkman created at 2008-09-22 11:28:08



---

archive/issue_comments_027013.json:
```json
{
    "body": "Due to the new restrictions on incoming patches, this can't be merged until all of the functions added/modified have doctests. This includes `verify_type, verify_operator, construct_skeleton, _apply_format, _apply_plot,` and maybe others. For discussion, if nothing else, I challenge `No doctest is intentional.` in `database.py`.\n\nPerhaps this could be reworded/more specific (and you don't need to shout, I can hear you ;-) ):\n\n```\n# WORD ON THE STREET IS THAT SQLITE IS RETARDED ABOUT\n# *ALTER TABLE* COMMANDS... SO MEANWHILE WE ACCOMPLISH THIS\n# BY CREATING A TEMPORARY TABLE.  SUGGESTIONS FOR SPEEDUP ARE\n# WELCOME.  (OR JUST SEND A PATCH...)\n```\n\n\nWhy was the copyright statement removed from `graph_database.py`? Remember that these statements protect our code!",
    "created_at": "2008-09-22T15:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27013",
    "user": "rlm"
}
```

Due to the new restrictions on incoming patches, this can't be merged until all of the functions added/modified have doctests. This includes `verify_type, verify_operator, construct_skeleton, _apply_format, _apply_plot,` and maybe others. For discussion, if nothing else, I challenge `No doctest is intentional.` in `database.py`.

Perhaps this could be reworded/more specific (and you don't need to shout, I can hear you ;-) ):

```
# WORD ON THE STREET IS THAT SQLITE IS RETARDED ABOUT
# *ALTER TABLE* COMMANDS... SO MEANWHILE WE ACCOMPLISH THIS
# BY CREATING A TEMPORARY TABLE.  SUGGESTIONS FOR SPEEDUP ARE
# WELCOME.  (OR JUST SEND A PATCH...)
```


Why was the copyright statement removed from `graph_database.py`? Remember that these statements protect our code!



---

archive/issue_comments_027014.json:
```json
{
    "body": "Attachment [3799-coverage.patch](tarball://root/attachments/some-uuid/ticket3799/3799-coverage.patch) by ekirkman created at 2008-09-29 21:50:43\n\nAttached another patch to address the problems mentioned.",
    "created_at": "2008-09-29T21:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27014",
    "user": "ekirkman"
}
```

Attachment [3799-coverage.patch](tarball://root/attachments/some-uuid/ticket3799/3799-coverage.patch) by ekirkman created at 2008-09-29 21:50:43

Attached another patch to address the problems mentioned.



---

archive/issue_comments_027015.json:
```json
{
    "body": "Attachment [3799-oops.patch](tarball://root/attachments/some-uuid/ticket3799/3799-oops.patch) by ekirkman created at 2008-09-29 22:05:14",
    "created_at": "2008-09-29T22:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27015",
    "user": "ekirkman"
}
```

Attachment [3799-oops.patch](tarball://root/attachments/some-uuid/ticket3799/3799-oops.patch) by ekirkman created at 2008-09-29 22:05:14



---

archive/issue_comments_027016.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-29T22:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27016",
    "user": "rlm"
}
```

Looks good to me.



---

archive/issue_comments_027017.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-29T23:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27017",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027018.json:
```json
{
    "body": "Merged all four patches in Sage 3.1.3.alpha2",
    "created_at": "2008-09-29T23:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3799#issuecomment-27018",
    "user": "mabshoff"
}
```

Merged all four patches in Sage 3.1.3.alpha2
