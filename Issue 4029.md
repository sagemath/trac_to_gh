# Issue 4029: sage-env kills the shell when called from "wrong" directory

archive/issues_004029.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @gvol\n\nKeywords: sage-env source\n\nSourcing sage-env from any directory other than SAGE_ROOT or SAGE_LOCAL/bin kills the shell.  This is considerably disconcerting behaviour.  An explanatory message would be nice (if not a proper fix).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4029\n\n",
    "created_at": "2008-09-01T04:03:55Z",
    "labels": [
        "distribution",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-env kills the shell when called from \"wrong\" directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4029",
    "user": "dphilp"
}
```
Assignee: mabshoff

CC:  @gvol

Keywords: sage-env source

Sourcing sage-env from any directory other than SAGE_ROOT or SAGE_LOCAL/bin kills the shell.  This is considerably disconcerting behaviour.  An explanatory message would be nice (if not a proper fix).

Issue created by migration from https://trac.sagemath.org/ticket/4029





---

archive/issue_comments_029052.json:
```json
{
    "body": "Oops, no milestone",
    "created_at": "2008-09-17T11:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29052",
    "user": "mabshoff"
}
```

Oops, no milestone



---

archive/issue_comments_029053.json:
```json
{
    "body": "There is a typo in the commit message, but otherwise this is the correct fix. I initially also wanted to do the indenting, but this is a much cleaner and better solution.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T12:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29053",
    "user": "mabshoff"
}
```

There is a typo in the commit message, but otherwise this is the correct fix. I initially also wanted to do the indenting, but this is a much cleaner and better solution.

Cheers,

Michael



---

archive/issue_comments_029054.json:
```json
{
    "body": "The patch does not apply to my merged tree. I believe #22 collides with this, but it should be easy to rebase post 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T13:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29054",
    "user": "mabshoff"
}
```

The patch does not apply to my merged tree. I believe #22 collides with this, but it should be easy to rebase post 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_029055.json:
```json
{
    "body": "The rebase needs to make sure that the changes from #22 don't get lost :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29055",
    "user": "mabshoff"
}
```

The rebase needs to make sure that the changes from #22 don't get lost :)

Cheers,

Michael



---

archive/issue_comments_029056.json:
```json
{
    "body": "Attachment [trac_4029.patch](tarball://root/attachments/some-uuid/ticket4029/trac_4029.patch) by @mwhansen created at 2009-10-05 07:18:06",
    "created_at": "2009-10-05T07:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29056",
    "user": "@mwhansen"
}
```

Attachment [trac_4029.patch](tarball://root/attachments/some-uuid/ticket4029/trac_4029.patch) by @mwhansen created at 2009-10-05 07:18:06



---

archive/issue_comments_029057.json:
```json
{
    "body": "I've attached a new patch which implements a cleaner solution using \"$(exit 1)\".  See http://fvue.nl/wiki/Bash:_Return_or_exit%3F",
    "created_at": "2009-10-05T07:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29057",
    "user": "@mwhansen"
}
```

I've attached a new patch which implements a cleaner solution using "$(exit 1)".  See http://fvue.nl/wiki/Bash:_Return_or_exit%3F



---

archive/issue_comments_029058.json:
```json
{
    "body": "merged in sage-4.1.2.rc1....",
    "created_at": "2009-10-05T13:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29058",
    "user": "@williamstein"
}
```

merged in sage-4.1.2.rc1....



---

archive/issue_comments_029059.json:
```json
{
    "body": "Reopened because wjp pointed out a serious issue -- the rest of the script gets executed. \n\nSome irc discussion about this:\n\n```\nwilliamstein: Regarding sage-env, I redid a patch of yours at #4029.\n[06:15am] williamstein:\nWow, what does \"$(exit 1)\" mean?\n[06:15am] williamstein:\nah, you give a reference.\n[06:16am] williamstein:\nI still don't understand it.\n[06:18am] williamstein:\nMike could you change the patch itself to include a comment about what $(exit 1) means?  Or maybe just a link to that page in\n[06:18am] williamstein:\na\n[06:18am] williamstein:\ncomment?\n[06:18am] williamstein:\nBecause googling for \"$(exit 1)\" would be tricky.\n[06:18am] williamstein:\n$(exit 1)\n[06:18am] williamstein:\nactually, it is easy to google for.\n[06:18am] williamstein:\nNo, it isn't.\n[06:20am] williamstein:\nwell if it works, it works, I guess.\n[06:21am] mhansen:\nYeah, I don't quite understand it myself.\n[06:22am] williamstein:\nWell, it works perfecty.\n[06:22am] williamstein:\nso positive review.\n[06:23am] williamstein:\nAnd the current behavior in Sage (without the patch) is indeed \"disconcerting\".\n[06:24am] mhansen:\nI'm surprised that one page was the only page that I could find something about it.\n[06:24am] williamstein:\nIndeed.\n[06:25am] williamstein:\nIt's hard to google though.\n[06:27am] wjp:\nisn't this trick only for passing a return status? I don't think it actually stops the script that's being sourced, right?\n[06:28am] williamstein:\nI don't know.  But if you try it, for some reason it works.\n[06:28am] wjp:\nhm, strange. Did you also test the remainder of sage-env doesn't get executed?\n[06:28am] williamstein:\nwjp -- you seam like the type to pull open the bash source code, read it, and completely understand what $(exit 1) does :-)\n[06:29am] wjp:\nI thought $(...) was the same as `...`\n[06:29am] wjp:\n(yes, I am kind of that type :-) )\n[06:29am] williamstein:\ncrap, in fact, the remainder does get executed.\n[06:30am] williamstein:\nhey mhansen -- what did my original patch do?\n[06:30am] williamstein:\nsince I think you deleted it.\n[06:30am] mhansen:\nRipped the bottom half of sage-env out and put it in a different file.\n[06:30am] mhansen:\nBy bottom half, I meant the part below that line.\n[06:31am] williamstein:\noh, now I remember doing that.\n[06:31am] williamstein:\n\"When in doubt, refactor it out!\"\n```\n",
    "created_at": "2009-10-05T13:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29059",
    "user": "@williamstein"
}
```

Reopened because wjp pointed out a serious issue -- the rest of the script gets executed. 

Some irc discussion about this:

```
williamstein: Regarding sage-env, I redid a patch of yours at #4029.
[06:15am] williamstein:
Wow, what does "$(exit 1)" mean?
[06:15am] williamstein:
ah, you give a reference.
[06:16am] williamstein:
I still don't understand it.
[06:18am] williamstein:
Mike could you change the patch itself to include a comment about what $(exit 1) means?  Or maybe just a link to that page in
[06:18am] williamstein:
a
[06:18am] williamstein:
comment?
[06:18am] williamstein:
Because googling for "$(exit 1)" would be tricky.
[06:18am] williamstein:
$(exit 1)
[06:18am] williamstein:
actually, it is easy to google for.
[06:18am] williamstein:
No, it isn't.
[06:20am] williamstein:
well if it works, it works, I guess.
[06:21am] mhansen:
Yeah, I don't quite understand it myself.
[06:22am] williamstein:
Well, it works perfecty.
[06:22am] williamstein:
so positive review.
[06:23am] williamstein:
And the current behavior in Sage (without the patch) is indeed "disconcerting".
[06:24am] mhansen:
I'm surprised that one page was the only page that I could find something about it.
[06:24am] williamstein:
Indeed.
[06:25am] williamstein:
It's hard to google though.
[06:27am] wjp:
isn't this trick only for passing a return status? I don't think it actually stops the script that's being sourced, right?
[06:28am] williamstein:
I don't know.  But if you try it, for some reason it works.
[06:28am] wjp:
hm, strange. Did you also test the remainder of sage-env doesn't get executed?
[06:28am] williamstein:
wjp -- you seam like the type to pull open the bash source code, read it, and completely understand what $(exit 1) does :-)
[06:29am] wjp:
I thought $(...) was the same as `...`
[06:29am] wjp:
(yes, I am kind of that type :-) )
[06:29am] williamstein:
crap, in fact, the remainder does get executed.
[06:30am] williamstein:
hey mhansen -- what did my original patch do?
[06:30am] williamstein:
since I think you deleted it.
[06:30am] mhansen:
Ripped the bottom half of sage-env out and put it in a different file.
[06:30am] mhansen:
By bottom half, I meant the part below that line.
[06:31am] williamstein:
oh, now I remember doing that.
[06:31am] williamstein:
"When in doubt, refactor it out!"
```




---

archive/issue_comments_029060.json:
```json
{
    "body": "Attachment [trac_4029.2.patch](tarball://root/attachments/some-uuid/ticket4029/trac_4029.2.patch) by @gvol created at 2010-12-29 20:31:59\n\nI used the very hacky (but effective)\n\n```\nreturn 1 2>/dev/null || exit 1\n```\n\ninstead of `return` or `exit`.",
    "created_at": "2010-12-29T20:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29060",
    "user": "@gvol"
}
```

Attachment [trac_4029.2.patch](tarball://root/attachments/some-uuid/ticket4029/trac_4029.2.patch) by @gvol created at 2010-12-29 20:31:59

I used the very hacky (but effective)

```
return 1 2>/dev/null || exit 1
```

instead of `return` or `exit`.



---

archive/issue_comments_029061.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-29T20:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29061",
    "user": "@gvol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_029062.json:
```json
{
    "body": "Will be obsolete with #10469.",
    "created_at": "2011-03-24T00:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29062",
    "user": "@gvol"
}
```

Will be obsolete with #10469.



---

archive/issue_comments_029063.json:
```json
{
    "body": "I don't think this will be obsolete with #10469: after applying that patch, if I open up a new shell and source sage-env, the shell closes.  Isn't the issue using \"exit\" instead of \"return\", since the script is being sourced?  I'm not a shell script expert, but can we just replace \"exit 1\" with \"return 1\" everywhere?  Failing that, can you explain your hack\n\n```\nreturn 1 2>/dev/null || exit 1\n```\n\nThis seems to work for me.",
    "created_at": "2011-03-24T21:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29063",
    "user": "@jhpalmieri"
}
```

I don't think this will be obsolete with #10469: after applying that patch, if I open up a new shell and source sage-env, the shell closes.  Isn't the issue using "exit" instead of "return", since the script is being sourced?  I'm not a shell script expert, but can we just replace "exit 1" with "return 1" everywhere?  Failing that, can you explain your hack

```
return 1 2>/dev/null || exit 1
```

This seems to work for me.



---

archive/issue_comments_029064.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-24T23:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29064",
    "user": "@gvol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_029065.json:
```json
{
    "body": "You're right this won't be obsoleted by 10469, I was misremembering this ticket.  However, I am a little confused about what is actually wanted--because of the `$(exit)` link I thought we wanted to be able to execute `sage-env`.  I think the correct thing to do is change all of the exit's to return's since `sage-env` is meant to be sourced.  This means that any script which sources sage-env will have to check return status and exit rather than relying on `sage-env` to exit for it.\n\nI could only find `sage-sage`, `Makefile`, `sage-spkg`, and a `start-sage.sh` in the Mac app which source `sage-env` so we will have to change them to check the exit status, and `sage-sage` and `Makefile` already do.  I talked with William and he said he doesn't know why it uses exit rather than having the calling script check the exit status.\n\nIf we want/need to keep the current behavior of exiting, we could use a hack like\n\n```\n# Exit if not called interactively.  For some reason scripts sourcing\n# sage-env expect errors to exit them.  However this is evil for\n# interactive shells.\ncase $- in\n    *i*)    # interactive shell should return\n        die=return;;\n    *)      # non-interactive shell\n        die=exit;;\nesac\n\n# ...\n# some error\n$die 1\n```\n\nto not exit the shell unless it's interactive.  Unfortunately I'm not sure how portable it is--I checked bash and zsh.\n\n---\n\nWhat my previous hack does is try to return and if that fails (because it was executed instead of sourced) then it calls exit.  If it's only ever sourced (per #10469) then it would be better to change them all to return, since that's what my hack would do.",
    "created_at": "2011-03-24T23:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29065",
    "user": "@gvol"
}
```

You're right this won't be obsoleted by 10469, I was misremembering this ticket.  However, I am a little confused about what is actually wanted--because of the `$(exit)` link I thought we wanted to be able to execute `sage-env`.  I think the correct thing to do is change all of the exit's to return's since `sage-env` is meant to be sourced.  This means that any script which sources sage-env will have to check return status and exit rather than relying on `sage-env` to exit for it.

I could only find `sage-sage`, `Makefile`, `sage-spkg`, and a `start-sage.sh` in the Mac app which source `sage-env` so we will have to change them to check the exit status, and `sage-sage` and `Makefile` already do.  I talked with William and he said he doesn't know why it uses exit rather than having the calling script check the exit status.

If we want/need to keep the current behavior of exiting, we could use a hack like

```
# Exit if not called interactively.  For some reason scripts sourcing
# sage-env expect errors to exit them.  However this is evil for
# interactive shells.
case $- in
    *i*)    # interactive shell should return
        die=return;;
    *)      # non-interactive shell
        die=exit;;
esac

# ...
# some error
$die 1
```

to not exit the shell unless it's interactive.  Unfortunately I'm not sure how portable it is--I checked bash and zsh.

---

What my previous hack does is try to return and if that fails (because it was executed instead of sourced) then it calls exit.  If it's only ever sourced (per #10469) then it would be better to change them all to return, since that's what my hack would do.



---

archive/issue_comments_029066.json:
```json
{
    "body": "See #9960; that changes every \"exit\" to \"return\" in sage-env.  Perhaps that one will obsolete this one.  If you wanted to give it one more review, that would be great.",
    "created_at": "2011-03-24T23:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29066",
    "user": "@jhpalmieri"
}
```

See #9960; that changes every "exit" to "return" in sage-env.  Perhaps that one will obsolete this one.  If you wanted to give it one more review, that would be great.



---

archive/issue_comments_029067.json:
```json
{
    "body": "That would definitely obsolete this one, though we still need to change the `start-sage.sh` in the Mac app.  I think that's fairly low priority though, and since I'm the one who maintains that, it should be easy.",
    "created_at": "2011-03-25T00:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29067",
    "user": "@gvol"
}
```

That would definitely obsolete this one, though we still need to change the `start-sage.sh` in the Mac app.  I think that's fairly low priority though, and since I'm the one who maintains that, it should be easy.



---

archive/issue_comments_029068.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-03-25T14:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29068",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_029069.json:
```json
{
    "body": "I'm marking this \"positive review\" so the release manager can close it once #9960 is merged.",
    "created_at": "2011-03-25T14:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29069",
    "user": "@jhpalmieri"
}
```

I'm marking this "positive review" so the release manager can close it once #9960 is merged.



---

archive/issue_comments_029070.json:
```json
{
    "body": "See #9960.",
    "created_at": "2011-05-13T06:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29070",
    "user": "@jdemeyer"
}
```

See #9960.



---

archive/issue_comments_029071.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-13T06:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4029#issuecomment-29071",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
