# Issue 2037: out-of-date tutorial section on errors and exceptions

archive/issues_002037.json:
```json
{
    "body": "Assignee: tba\n\nSection 3.5 \"Errors and Exceptions\" in the tutorial appears to be out of date.  The error messages that come up have changed since the section was written, and the debugger is/looks different (ipdb versus Pdb).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2037\n\n",
    "created_at": "2008-02-03T19:36:03Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "out-of-date tutorial section on errors and exceptions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2037",
    "user": "AlexGhitza"
}
```
Assignee: tba

Section 3.5 "Errors and Exceptions" in the tutorial appears to be out of date.  The error messages that come up have changed since the section was written, and the debugger is/looks different (ipdb versus Pdb).


Issue created by migration from https://trac.sagemath.org/ticket/2037





---

archive/issue_comments_013178.json:
```json
{
    "body": "I just tried to create a patch for this. I also added a section for 3d plotting, copying a few jmol examples from the reference manual. The problem is that sage -t failed horribly, though apparently not due to anything I added. Most seemed to be line return issues. I'm I'm to ignore these then i can proceed to try to create a patch...",
    "created_at": "2008-02-22T16:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13178",
    "user": "wdj"
}
```

I just tried to create a patch for this. I also added a section for 3d plotting, copying a few jmol examples from the reference manual. The problem is that sage -t failed horribly, though apparently not due to anything I added. Most seemed to be line return issues. I'm I'm to ignore these then i can proceed to try to create a patch...



---

archive/issue_comments_013179.json:
```json
{
    "body": "That last sentence should read: \"If I'm supposed to ignore\nthese failures then I can proceed to try to create a patch...\" I guess my\nquestion is: has the format to sage -t changed in such a way that one\nis to ignore such failures? Or, maybe I'm using sage -t incorrectly.",
    "created_at": "2008-02-22T16:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13179",
    "user": "wdj"
}
```

That last sentence should read: "If I'm supposed to ignore
these failures then I can proceed to try to create a patch..." I guess my
question is: has the format to sage -t changed in such a way that one
is to ignore such failures? Or, maybe I'm using sage -t incorrectly.



---

archive/issue_comments_013180.json:
```json
{
    "body": "Sage 2.10.2.alphaX has a broken tut.tex. Take Sage 2.10.2.rc0 or later as a base for a patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-22T17:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13180",
    "user": "mabshoff"
}
```

Sage 2.10.2.alphaX has a broken tut.tex. Take Sage 2.10.2.rc0 or later as a base for a patch.

Cheers,

Michael



---

archive/issue_comments_013181.json:
```json
{
    "body": "I compiled 2.10.2.rc0 from source (4h5m) and had exactly the same problem. The bundle is attached. The export command would not work to create a patch (sorry, Micheal).",
    "created_at": "2008-02-23T00:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13181",
    "user": "wdj"
}
```

I compiled 2.10.2.rc0 from source (4h5m) and had exactly the same problem. The bundle is attached. The export command would not work to create a patch (sorry, Micheal).



---

archive/issue_comments_013182.json:
```json
{
    "body": "Attachment [tut2008-22-02.hg](tarball://root/attachments/some-uuid/ticket2037/tut2008-22-02.hg) by mabshoff created at 2008-02-23 00:07:32\n\nSorry, this made it too late for 2.10.2. It will hopefully go right into 2.10.3.alpha0 :(\n\nCheers,\n\nMichael",
    "created_at": "2008-02-23T00:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13182",
    "user": "mabshoff"
}
```

Attachment [tut2008-22-02.hg](tarball://root/attachments/some-uuid/ticket2037/tut2008-22-02.hg) by mabshoff created at 2008-02-23 00:07:32

Sorry, this made it too late for 2.10.2. It will hopefully go right into 2.10.3.alpha0 :(

Cheers,

Michael



---

archive/issue_comments_013183.json:
```json
{
    "body": "I've taken David's bundle and manually applied it against 2.10.2.rc0, making a few small fixes in the process (fixed a few long lines, added a citation for Jmol, etc.)  The result is in the attached patch, which (if positively reviewed) should be applied instead of the bundle.\n\nI ran sage -t tut.tex and it succeeded, and ./build_pdf and looked at the resulting pdf file.",
    "created_at": "2008-02-23T03:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13183",
    "user": "AlexGhitza"
}
```

I've taken David's bundle and manually applied it against 2.10.2.rc0, making a few small fixes in the process (fixed a few long lines, added a citation for Jmol, etc.)  The result is in the attached patch, which (if positively reviewed) should be applied instead of the bundle.

I ran sage -t tut.tex and it succeeded, and ./build_pdf and looked at the resulting pdf file.



---

archive/issue_comments_013184.json:
```json
{
    "body": "Attachment [2037-tut-fixes.patch](tarball://root/attachments/some-uuid/ticket2037/2037-tut-fixes.patch) by AlexGhitza created at 2008-02-23 03:00:46",
    "created_at": "2008-02-23T03:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13184",
    "user": "AlexGhitza"
}
```

Attachment [2037-tut-fixes.patch](tarball://root/attachments/some-uuid/ticket2037/2037-tut-fixes.patch) by AlexGhitza created at 2008-02-23 03:00:46



---

archive/issue_comments_013185.json:
```json
{
    "body": "Attachment [2037.patch](tarball://root/attachments/some-uuid/ticket2037/2037.patch) by mhansen created at 2008-02-27 23:49:31\n\nThe last patch ( 2037.patch ) applies cleanly after #2323.",
    "created_at": "2008-02-27T23:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13185",
    "user": "mhansen"
}
```

Attachment [2037.patch](tarball://root/attachments/some-uuid/ticket2037/2037.patch) by mhansen created at 2008-02-27 23:49:31

The last patch ( 2037.patch ) applies cleanly after #2323.



---

archive/issue_comments_013186.json:
```json
{
    "body": "Merged 2037.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13186",
    "user": "mabshoff"
}
```

Merged 2037.patch in Sage 2.10.3.rc0



---

archive/issue_comments_013187.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2037#issuecomment-13187",
    "user": "mabshoff"
}
```

Resolution: fixed
