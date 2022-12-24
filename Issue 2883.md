# Issue 2883: notebook -- typing in safari is sluggish!

archive/issues_002883.json:
```json
{
    "body": "Assignee: boothby\n\nTyping in the current version of the notebook in Safari is significantly slower than typing on an Apple IIe running Windows Vista.  Fix it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/2883\n\n",
    "created_at": "2008-04-11T23:30:44Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "notebook -- typing in safari is sluggish!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2883",
    "user": "boothby"
}
```
Assignee: boothby

Typing in the current version of the notebook in Safari is significantly slower than typing on an Apple IIe running Windows Vista.  Fix it!

Issue created by migration from https://trac.sagemath.org/ticket/2883





---

archive/issue_comments_019830.json:
```json
{
    "body": "Attachment [2883-resize-flood.patch](tarball://root/attachments/some-uuid/ticket2883/2883-resize-flood.patch) by boothby created at 2008-04-11 23:55:15",
    "created_at": "2008-04-11T23:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19830",
    "user": "boothby"
}
```

Attachment [2883-resize-flood.patch](tarball://root/attachments/some-uuid/ticket2883/2883-resize-flood.patch) by boothby created at 2008-04-11 23:55:15



---

archive/issue_comments_019831.json:
```json
{
    "body": "This patch is impossible to apply.  It has this line in it\n\n```\n@@ -790,6 +794,29 @@ function resize_all_cells() {\n```\n\nwhich is the only mention of the resize_all_cells function.  So it\ndepends on some other patch you didn't provide.",
    "created_at": "2008-04-12T04:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19831",
    "user": "was"
}
```

This patch is impossible to apply.  It has this line in it

```
@@ -790,6 +794,29 @@ function resize_all_cells() {
```

which is the only mention of the resize_all_cells function.  So it
depends on some other patch you didn't provide.



---

archive/issue_comments_019832.json:
```json
{
    "body": "Sorry, this depends on #2882",
    "created_at": "2008-04-12T06:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19832",
    "user": "boothby"
}
```

Sorry, this depends on #2882



---

archive/issue_comments_019833.json:
```json
{
    "body": "I am getting rejects against my merge tree:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha4/devel/sage$ patch -p1 --dry-run < trac_2883-resize-flood.patch\npatching file sage/server/notebook/cell.py\nHunk #1 FAILED at 646.\n1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/cell.py.rej\npatching file sage/server/notebook/js.py\n```\n\nPlease rebase against my merge tree alpah4 in the usual place.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T00:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19833",
    "user": "mabshoff"
}
```

I am getting rejects against my merge tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha4/devel/sage$ patch -p1 --dry-run < trac_2883-resize-flood.patch
patching file sage/server/notebook/cell.py
Hunk #1 FAILED at 646.
1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/cell.py.rej
patching file sage/server/notebook/js.py
```

Please rebase against my merge tree alpah4 in the usual place.

Cheers,

Michael



---

archive/issue_comments_019834.json:
```json
{
    "body": "\n```\n[03:19] <mabshoff> wstein-2901: the reject for #2883 is the following:\n[03:20] <mabshoff> it is: onKeyUp    = 'return cell_input_resize(this);'\n[03:20] <mabshoff> the patch expects: onKeyUp    = 'return cell_input_resize(%s);' \n[03:20] <mabshoff> And it want to replace it with: onKeyUp    = 'return input_keyup(%s, event);' \n[03:20] <wstein-2901> mabshoff -- it should be this.\n[03:20] <wstein-2901> \"this\"\n[03:20] <wstein-2901> Oh, I see.\n[03:20] <wstein-2901> hmm.\n[03:21] <wstein-2901> It should be: onKeyUp    = 'return input_keyup(%s, event);'\n[03:21] <mabshoff> ok.\n[03:21] <mabshoff> wstein-2901: merging it like that then\n```\n",
    "created_at": "2008-04-13T02:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19834",
    "user": "mabshoff"
}
```


```
[03:19] <mabshoff> wstein-2901: the reject for #2883 is the following:
[03:20] <mabshoff> it is: onKeyUp    = 'return cell_input_resize(this);'
[03:20] <mabshoff> the patch expects: onKeyUp    = 'return cell_input_resize(%s);' 
[03:20] <mabshoff> And it want to replace it with: onKeyUp    = 'return input_keyup(%s, event);' 
[03:20] <wstein-2901> mabshoff -- it should be this.
[03:20] <wstein-2901> "this"
[03:20] <wstein-2901> Oh, I see.
[03:20] <wstein-2901> hmm.
[03:21] <wstein-2901> It should be: onKeyUp    = 'return input_keyup(%s, event);'
[03:21] <mabshoff> ok.
[03:21] <mabshoff> wstein-2901: merging it like that then
```




---

archive/issue_comments_019835.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-13T02:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19835",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019836.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T02:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2883#issuecomment-19836",
    "user": "mabshoff"
}
```

Resolution: fixed
