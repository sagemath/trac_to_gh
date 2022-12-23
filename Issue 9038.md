# Issue 9038: Typeset: Wrong charset for Greek characters

archive/issues_009038.json:
```json
{
    "body": "Assignee: jason, was\n\nClient: Ubuntu Karmic 9.10 with jsmath 3.5.9, jsmath-fonts 1.3-2, ttf-jsmath, and Firefox 3.5.9.\n\nServer: Either http://www.sagebn.org or Debian Lenny with Sage 4.4.2 compiled from source\n\nWhen displaying a formula containing \"pi\" with \"Typeset\" checked, the character \u00da (capital U with accent) is displayed instead of the pi character.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9038\n\n",
    "created_at": "2010-05-24T19:42:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Typeset: Wrong charset for Greek characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9038",
    "user": "jan"
}
```
Assignee: jason, was

Client: Ubuntu Karmic 9.10 with jsmath 3.5.9, jsmath-fonts 1.3-2, ttf-jsmath, and Firefox 3.5.9.

Server: Either http://www.sagebn.org or Debian Lenny with Sage 4.4.2 compiled from source

When displaying a formula containing "pi" with "Typeset" checked, the character Ú (capital U with accent) is displayed instead of the pi character.

Issue created by migration from https://trac.sagemath.org/ticket/9038





---

archive/issue_comments_083669.json:
```json
{
    "body": "This is most likely a problem with the ttf-jsmath package.  See http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html\n\n\"Linux users with Firefox 3.5 should use the last archive in the list, as the Linux version of Firefoex 3.5 can not process the non-standard encoding used in the other archives.\"\n\nCan you install the linux firefox 3.5 fonts listed in the website above and see if that fixes the problem?",
    "created_at": "2010-05-25T19:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9038#issuecomment-83669",
    "user": "jason"
}
```

This is most likely a problem with the ttf-jsmath package.  See http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html

"Linux users with Firefox 3.5 should use the last archive in the list, as the Linux version of Firefoex 3.5 can not process the non-standard encoding used in the other archives."

Can you install the linux firefox 3.5 fonts listed in the website above and see if that fixes the problem?



---

archive/issue_comments_083670.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-05-25T19:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9038#issuecomment-83670",
    "user": "jason"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_083671.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-05-28T22:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9038#issuecomment-83671",
    "user": "jan"
}
```

Resolution: wontfix



---

archive/issue_comments_083672.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> This is most likely a problem with the ttf-jsmath package.  See http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html\n> Can you install the linux firefox 3.5 fonts listed in the website above and see if that fixes the problem?\n\nYou were right. After removing ttf-jsmath and installing the downloaded fonts it works. Thank you.",
    "created_at": "2010-05-28T22:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9038#issuecomment-83672",
    "user": "jan"
}
```

Replying to [comment:2 jason]:
> This is most likely a problem with the ttf-jsmath package.  See http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html
> Can you install the linux firefox 3.5 fonts listed in the website above and see if that fixes the problem?

You were right. After removing ttf-jsmath and installing the downloaded fonts it works. Thank you.
