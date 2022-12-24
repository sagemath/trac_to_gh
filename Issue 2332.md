# Issue 2332: notebook -- the evaluate link doesn't

archive/issues_002332.json:
```json
{
    "body": "Assignee: boothby\n\nProblems with the evaluate link that appears in the active notebook cell have\nbeen reported by several people on the Sage mailing lists.  Here's the latest\nbug report, which has some interesting ideas about possible solutions. \n\n\n```\n\nOn Tue, Feb 26, 2008 at 8:24 AM, Francis Clarke <> wrote:\n> \n>  The \"evaluate\" links for the notebook introduced in SAGE 2.9.2 have\n>  never worked for me (Mac OS X 10.4.11, SAGE 2.9.2 -- 2.10.2 + either\n>  Safari or Firefox).  The links appears when they should and seem to be\n>  correct, e.g., (reformatted):\n>  \n>     <a href  = \"javascript:evaluate_cell(115,0)\"\n>        class = \"eval_button\"\n>        id    = \"eval_button115\"\n>        alt   = \"Click here or press shift-return to evaluate\">\n>     evaluate\n>     </a>\n>  \n>  but clicking on the link has no effect.  This is a pity, as it's a\n>  (potentially) very nice feature.  The cells evaluate perfectly well\n>  with shift-return.\n\nI just want to point out that the evaluate link *does* work for me\nand most people in Firefox.   It does not work for me in Safari.\nI don't understand why it doesn't work, but all your hints in this\nemail will help.  Thanks!  We're tracking this issue at \n \n\n>  \n>  Looking at this link, and cell.py line 575, where it's created, I fail\n>  to see what is wrong.  Perhaps the javascript function evaluate_cell\n>  (defined in js.py) can't be found in this context?\n>  \n>  One thing I did notice is the attribute\n>     alt=\"Click here or press shift-return to evaluate\"\n>  There is no alt attribute for the A element in HTML 4.01, so it has no\n>  effect here.  Probably 'alt' should be replaced by 'title'.  Though,\n>  of course, this isn't the cause of my main problem.\n>  \n>  \n>  A couple of other details from cell.py noticed in passing:\n>  \n>  line  64: math_parse is defined in html.py not cell.py\n>  \n>  line 577: has no effect.  Presumably it should have been commented out\n>  along with lines 579--584.\n>  \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2332\n\n",
    "created_at": "2008-02-27T12:50:54Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- the evaluate link doesn't",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2332",
    "user": "was"
}
```
Assignee: boothby

Problems with the evaluate link that appears in the active notebook cell have
been reported by several people on the Sage mailing lists.  Here's the latest
bug report, which has some interesting ideas about possible solutions. 


```

On Tue, Feb 26, 2008 at 8:24 AM, Francis Clarke <> wrote:
> 
>  The "evaluate" links for the notebook introduced in SAGE 2.9.2 have
>  never worked for me (Mac OS X 10.4.11, SAGE 2.9.2 -- 2.10.2 + either
>  Safari or Firefox).  The links appears when they should and seem to be
>  correct, e.g., (reformatted):
>  
>     <a href  = "javascript:evaluate_cell(115,0)"
>        class = "eval_button"
>        id    = "eval_button115"
>        alt   = "Click here or press shift-return to evaluate">
>     evaluate
>     </a>
>  
>  but clicking on the link has no effect.  This is a pity, as it's a
>  (potentially) very nice feature.  The cells evaluate perfectly well
>  with shift-return.

I just want to point out that the evaluate link *does* work for me
and most people in Firefox.   It does not work for me in Safari.
I don't understand why it doesn't work, but all your hints in this
email will help.  Thanks!  We're tracking this issue at 
 

>  
>  Looking at this link, and cell.py line 575, where it's created, I fail
>  to see what is wrong.  Perhaps the javascript function evaluate_cell
>  (defined in js.py) can't be found in this context?
>  
>  One thing I did notice is the attribute
>     alt="Click here or press shift-return to evaluate"
>  There is no alt attribute for the A element in HTML 4.01, so it has no
>  effect here.  Probably 'alt' should be replaced by 'title'.  Though,
>  of course, this isn't the cause of my main problem.
>  
>  
>  A couple of other details from cell.py noticed in passing:
>  
>  line  64: math_parse is defined in html.py not cell.py
>  
>  line 577: has no effect.  Presumably it should have been commented out
>  along with lines 579--584.
>  

```


Issue created by migration from https://trac.sagemath.org/ticket/2332





---

archive/issue_comments_015599.json:
```json
{
    "body": "Replying to [ticket:2332 was]:\n> Problems with the evaluate link that appears in the active notebook cell have\n> been reported by several people on the Sage mailing lists.  Here's the latest\n> bug report, which has some interesting ideas about possible solutions. \n> \n> {{{\n> \n> On Tue, Feb 26, 2008 at 8:24 AM, Francis Clarke <> wrote:\n> > \n> >  The \"evaluate\" links for the notebook introduced in SAGE 2.9.2 have\n> >  never worked for me (Mac OS X 10.4.11, SAGE 2.9.2 -- 2.10.2 + either\n> >  Safari or Firefox).  The links appears when they should and seem to be\n> >  correct, e.g., (reformatted):\n> >  \n> >     <a href  = \"javascript:evaluate_cell(115,0)\"\n> >        class = \"eval_button\"\n> >        id    = \"eval_button115\"\n> >        alt   = \"Click here or press shift-return to evaluate\">\n> >     evaluate\n> >     </a>\n> >  \n> >  but clicking on the link has no effect.  This is a pity, as it's a\n> >  (potentially) very nice feature.  The cells evaluate perfectly well\n> >  with shift-return.\n> \n> I just want to point out that the evaluate link *does* work for me\n> and most people in Firefox.   It does not work for me in Safari.\n> I don't understand why it doesn't work, but all your hints in this\n> email will help.  Thanks!  We're tracking this issue at \n>  \n> \n> >  \n> >  Looking at this link, and cell.py line 575, where it's created, I fail\n> >  to see what is wrong.  Perhaps the javascript function evaluate_cell\n> >  (defined in js.py) can't be found in this context?\n> >  \n> >  One thing I did notice is the attribute\n> >     alt=\"Click here or press shift-return to evaluate\"\n> >  There is no alt attribute for the A element in HTML 4.01, so it has no\n> >  effect here.  Probably 'alt' should be replaced by 'title'.  Though,\n> >  of course, this isn't the cause of my main problem.\n> >  \n> >  \n> >  A couple of other details from cell.py noticed in passing:\n> >  \n> >  line  64: math_parse is defined in html.py not cell.py\n> >  \n> >  line 577: has no effect.  Presumably it should have been commented out\n> >  along with lines 579--584.\n> >  \n> \n> }}}\nI found Justin's suggested mod: extend the timeout in cell_blur, to be effective.\nMaybe Williams machines are faster than my little laptop. Tried 200ms but that was\nunreliable, 250ms seems to work OK.\n\nI await Justin's proposed mods....\n\nBill",
    "created_at": "2008-03-12T14:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2332#issuecomment-15599",
    "user": "bill.p"
}
```

Replying to [ticket:2332 was]:
> Problems with the evaluate link that appears in the active notebook cell have
> been reported by several people on the Sage mailing lists.  Here's the latest
> bug report, which has some interesting ideas about possible solutions. 
> 
> {{{
> 
> On Tue, Feb 26, 2008 at 8:24 AM, Francis Clarke <> wrote:
> > 
> >  The "evaluate" links for the notebook introduced in SAGE 2.9.2 have
> >  never worked for me (Mac OS X 10.4.11, SAGE 2.9.2 -- 2.10.2 + either
> >  Safari or Firefox).  The links appears when they should and seem to be
> >  correct, e.g., (reformatted):
> >  
> >     <a href  = "javascript:evaluate_cell(115,0)"
> >        class = "eval_button"
> >        id    = "eval_button115"
> >        alt   = "Click here or press shift-return to evaluate">
> >     evaluate
> >     </a>
> >  
> >  but clicking on the link has no effect.  This is a pity, as it's a
> >  (potentially) very nice feature.  The cells evaluate perfectly well
> >  with shift-return.
> 
> I just want to point out that the evaluate link *does* work for me
> and most people in Firefox.   It does not work for me in Safari.
> I don't understand why it doesn't work, but all your hints in this
> email will help.  Thanks!  We're tracking this issue at 
>  
> 
> >  
> >  Looking at this link, and cell.py line 575, where it's created, I fail
> >  to see what is wrong.  Perhaps the javascript function evaluate_cell
> >  (defined in js.py) can't be found in this context?
> >  
> >  One thing I did notice is the attribute
> >     alt="Click here or press shift-return to evaluate"
> >  There is no alt attribute for the A element in HTML 4.01, so it has no
> >  effect here.  Probably 'alt' should be replaced by 'title'.  Though,
> >  of course, this isn't the cause of my main problem.
> >  
> >  
> >  A couple of other details from cell.py noticed in passing:
> >  
> >  line  64: math_parse is defined in html.py not cell.py
> >  
> >  line 577: has no effect.  Presumably it should have been commented out
> >  along with lines 579--584.
> >  
> 
> }}}
I found Justin's suggested mod: extend the timeout in cell_blur, to be effective.
Maybe Williams machines are faster than my little laptop. Tried 200ms but that was
unreliable, 250ms seems to work OK.

I await Justin's proposed mods....

Bill



---

archive/issue_comments_015600.json:
```json
{
    "body": "Attachment [2332-evaluate-button.patch](tarball://root/attachments/some-uuid/ticket2332/2332-evaluate-button.patch) by boothby created at 2008-03-14 00:06:38",
    "created_at": "2008-03-14T00:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2332#issuecomment-15600",
    "user": "boothby"
}
```

Attachment [2332-evaluate-button.patch](tarball://root/attachments/some-uuid/ticket2332/2332-evaluate-button.patch) by boothby created at 2008-03-14 00:06:38



---

archive/issue_comments_015601.json:
```json
{
    "body": "Rock solid (for me and my superfast laptop)!",
    "created_at": "2008-03-17T04:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2332#issuecomment-15601",
    "user": "was"
}
```

Rock solid (for me and my superfast laptop)!



---

archive/issue_comments_015602.json:
```json
{
    "body": "Merged in Sage 2.10.4.final",
    "created_at": "2008-03-17T04:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2332#issuecomment-15602",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.final



---

archive/issue_comments_015603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-17T04:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2332#issuecomment-15603",
    "user": "mabshoff"
}
```

Resolution: fixed
