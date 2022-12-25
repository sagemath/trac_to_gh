# Issue 3752: gap.eval -- oddity in parsing multiline input and comments

archive/issues_003752.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nOn Thu, Jul 31, 2008 at 11:20 AM, Peter <> wrote:\n>\n> Hi,\n>\n> I'm trying to use some GAP code in the Sage notebook, and the code has\n> many one-line comments in it (starting with #). I switched the\n> notebook to gap mode (using the dropdown menu) and then noticed that\n> in each cell only commands that appear before the first comment are\n> processed by GAP. The same happens in cells that start with %gap.\n>\n> Can someone perhaps verify this behaviour and/or suggest a fix? (I'm\n> using Sage 3.0.5, and the same behaviour seems to occur on\n> Sagenb.org.)\n\nYes, here's an example of this in the sage notebook text form (I made the triple {'s into double for this ticket): \n\n{{{\nUntitled\nsystem:gap\n\n\n{{id=112|\nPrint(2 + 2); # add numbers\nPrint(3 + 3); # add more numbers\n///\n\n4\n}}\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/3752\n\n",
    "created_at": "2008-08-01T01:13:39Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "gap.eval -- oddity in parsing multiline input and comments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3752",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
On Thu, Jul 31, 2008 at 11:20 AM, Peter <> wrote:
>
> Hi,
>
> I'm trying to use some GAP code in the Sage notebook, and the code has
> many one-line comments in it (starting with #). I switched the
> notebook to gap mode (using the dropdown menu) and then noticed that
> in each cell only commands that appear before the first comment are
> processed by GAP. The same happens in cells that start with %gap.
>
> Can someone perhaps verify this behaviour and/or suggest a fix? (I'm
> using Sage 3.0.5, and the same behaviour seems to occur on
> Sagenb.org.)

Yes, here's an example of this in the sage notebook text form (I made the triple {'s into double for this ticket): 

{{{
Untitled
system:gap


{{id=112|
Print(2 + 2); # add numbers
Print(3 + 3); # add more numbers
///

4
}}
}}}

Issue created by migration from https://trac.sagemath.org/ticket/3752





---

archive/issue_comments_026603.json:
```json
{
    "body": "This problem can be fixed by adding the following lines at the start of the \neval method in the file interfaces/gap.py:\n\n```\n        # remove comments, replace newlines by space\n        x = \"\".join([(r[:r.find('#')] if r.find('#')!=-1 else r)+' ' \\\n                     for r in x.split('\\n')])\n```\n\n(This still needs to be tested on a variety of GAP input lines.)\n\nI also noticed that if the length of the string processed by GAP is more than ~103 characters, then no output is produced (although the GAP code seems to be evaluated correctly and any functions defined in the code works in subsequent notebook cells).\n\nHere is an example:\n\n```\n{{id=112|\n%gap\ntest := function()\nreturn \"make a long input string  (delete 1 char to see the output)\";\nend;\ntest();\n///\n}}\n```",
    "created_at": "2008-08-07T23:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26603",
    "user": "https://trac.sagemath.org/admin/accounts/users/jipsen"
}
```

This problem can be fixed by adding the following lines at the start of the 
eval method in the file interfaces/gap.py:

```
        # remove comments, replace newlines by space
        x = "".join([(r[:r.find('#')] if r.find('#')!=-1 else r)+' ' \
                     for r in x.split('\n')])
```

(This still needs to be tested on a variety of GAP input lines.)

I also noticed that if the length of the string processed by GAP is more than ~103 characters, then no output is produced (although the GAP code seems to be evaluated correctly and any functions defined in the code works in subsequent notebook cells).

Here is an example:

```
{{id=112|
%gap
test := function()
return "make a long input string  (delete 1 char to see the output)";
end;
test();
///
}}
```



---

archive/issue_comments_026604.json:
```json
{
    "body": "Attachment [trac_3752.patch](tarball://root/attachments/some-uuid/ticket3752/trac_3752.patch) by @mwhansen created at 2009-01-23 10:31:30",
    "created_at": "2009-01-23T10:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26604",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3752.patch](tarball://root/attachments/some-uuid/ticket3752/trac_3752.patch) by @mwhansen created at 2009-01-23 10:31:30



---

archive/issue_comments_026605.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T10:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26605",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026606.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-01-23T10:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26606",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_026607.json:
```json
{
    "body": "I have a performance concern, but this is #5086 now.",
    "created_at": "2009-01-24T07:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26607",
    "user": "https://github.com/malb"
}
```

I have a performance concern, but this is #5086 now.



---

archive/issue_events_008601.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T19:31:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3752#event-8601"
}
```



---

archive/issue_events_008602.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T19:31:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3752#event-8602"
}
```



---

archive/issue_comments_026608.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_026609.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3752#issuecomment-26609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
