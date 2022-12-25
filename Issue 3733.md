# Issue 3733: notebook -- add something to reference manual about user-customizable css (easy ticket)

archive/issues_003733.json:
```json
{
    "body": "Assignee: boothby\n\n```\nI am working on a project this summer that uses SAGE to assemble some\ninteractive Calculus lessons, and I was hoping to do something like\nthis. So thank you very much!\n\nWill this be placed in the manual or the Wiki?\n\nregards\njohn perry\n\nOn May 27, 9:57 am, \"William Stein\" <wst...@gmail.com> wrote:\n> Hi,\n>\n> I've always wondered why nobody creates nice stylized \"skins\", etc.\n> for the notebook.\n> It just occurred to me that though I made it trivial to change the\n> notebook css on the\n> fly, nobody knows how.  If you would like to make your Sage notebook\n> look totally\n> different, here's a quick tutorial (assumes you are not using the\n> vmware version of\n> the notebook):\n>\n> 1. See attached screenshot.\n>\n> 2. Start your *own* notebook server running locally on your computer.\n>\n> 3. Make a new file $HOME/.sage/notebook.css with these contents:\n>\n> textarea.cell_input {\n>   color:#003300;\n>   border: 0px;\n>   font-family: monaco;\n>\n> }\n>\n> div.cell_not_evaluated {\n>     border-left: 3px solid #ff8888;\n>\n> }\n>\n> td.cell_number_running {\n>    border-left:20px solid orange;\n>\n> }\n>\n> 4. Press refresh in your web browser and observe that the above css takes\n> effect thus changing the style of your notebook.\n>\n> 5. You can change a lot.  To get a feel for the options seehttp://localhost:8000/css/main.css\n> where 8000 is replaced by whatever port your notebook runs on.\n>\n> This feature has been in Sage for two years, but I don't think anybody\n> has ever used it.\n>\n>  -- William\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3733\n\n",
    "created_at": "2008-07-28T05:41:36Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook -- add something to reference manual about user-customizable css (easy ticket)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3733",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

```
I am working on a project this summer that uses SAGE to assemble some
interactive Calculus lessons, and I was hoping to do something like
this. So thank you very much!

Will this be placed in the manual or the Wiki?

regards
john perry

On May 27, 9:57 am, "William Stein" <wst...@gmail.com> wrote:
> Hi,
>
> I've always wondered why nobody creates nice stylized "skins", etc.
> for the notebook.
> It just occurred to me that though I made it trivial to change the
> notebook css on the
> fly, nobody knows how.  If you would like to make your Sage notebook
> look totally
> different, here's a quick tutorial (assumes you are not using the
> vmware version of
> the notebook):
>
> 1. See attached screenshot.
>
> 2. Start your *own* notebook server running locally on your computer.
>
> 3. Make a new file $HOME/.sage/notebook.css with these contents:
>
> textarea.cell_input {
>   color:#003300;
>   border: 0px;
>   font-family: monaco;
>
> }
>
> div.cell_not_evaluated {
>     border-left: 3px solid #ff8888;
>
> }
>
> td.cell_number_running {
>    border-left:20px solid orange;
>
> }
>
> 4. Press refresh in your web browser and observe that the above css takes
> effect thus changing the style of your notebook.
>
> 5. You can change a lot.  To get a feel for the options seehttp://localhost:8000/css/main.css
> where 8000 is replaced by whatever port your notebook runs on.
>
> This feature has been in Sage for two years, but I don't think anybody
> has ever used it.
>
>  -- William
```

Issue created by migration from https://trac.sagemath.org/ticket/3733





---

archive/issue_comments_026447.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-19T23:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3733#issuecomment-26447",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026448.json:
```json
{
    "body": "Attachment [sagenb-3733.patch](tarball://root/attachments/some-uuid/ticket3733/sagenb-3733.patch) by @williamstein created at 2009-11-19 23:26:47\n\nNote only does this add the remark to the manual, but also sphinxifies the ``notebook?`` docstring.",
    "created_at": "2009-11-19T23:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3733#issuecomment-26448",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb-3733.patch](tarball://root/attachments/some-uuid/ticket3733/sagenb-3733.patch) by @williamstein created at 2009-11-19 23:26:47

Note only does this add the remark to the manual, but also sphinxifies the ``notebook?`` docstring.



---

archive/issue_comments_026449.json:
```json
{
    "body": "I didn't know this existed until now. Positive review. I've added a few more improvements to the ReST docstring at #7611.",
    "created_at": "2009-12-06T07:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3733#issuecomment-26449",
    "user": "https://github.com/TimDumol"
}
```

I didn't know this existed until now. Positive review. I've added a few more improvements to the ReST docstring at #7611.



---

archive/issue_comments_026450.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T19:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3733#issuecomment-26450",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008552.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-08T19:59:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3733#event-8552"
}
```



---

archive/issue_comments_026451.json:
```json
{
    "body": "merged into sagenb-0.4.6.",
    "created_at": "2009-12-08T19:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3733#issuecomment-26451",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.4.6.
