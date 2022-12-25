# Issue 8552: replace os.system calls in latex.py with appropriate replacements

archive/issues_008552.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri\n\nThis is a followup to #8486, which uses `os.system('which xelatex')` to see if XeLaTeX is available. With #8474 now merged, we should use `have_program` to do that, and also replace other uses of `os.system` with appropriate `subprocess` replacements, since we are [supposed to use subprocess, and not os.system](http://docs.python.org/library/os.html#os.system)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8552\n\n",
    "created_at": "2010-03-17T08:35:51Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "replace os.system calls in latex.py with appropriate replacements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8552",
    "user": "https://github.com/dandrake"
}
```
Assignee: tbd

CC:  @jhpalmieri

This is a followup to #8486, which uses `os.system('which xelatex')` to see if XeLaTeX is available. With #8474 now merged, we should use `have_program` to do that, and also replace other uses of `os.system` with appropriate `subprocess` replacements, since we are [supposed to use subprocess, and not os.system](http://docs.python.org/library/os.html#os.system)

Issue created by migration from https://trac.sagemath.org/ticket/8552





---

archive/issue_comments_077215.json:
```json
{
    "body": "Attachment [trac_8552_whitespace.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552_whitespace.patch) by @dandrake created at 2010-03-23 13:54:54\n\nclean up unnecessary whitespace in latex.py",
    "created_at": "2010-03-23T13:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77215",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_8552_whitespace.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552_whitespace.patch) by @dandrake created at 2010-03-23 13:54:54

clean up unnecessary whitespace in latex.py



---

archive/issue_comments_077216.json:
```json
{
    "body": "replace os.system with subprocess.call; apply on top of whitespace patch",
    "created_at": "2010-03-23T13:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77216",
    "user": "https://github.com/dandrake"
}
```

replace os.system with subprocess.call; apply on top of whitespace patch



---

archive/issue_comments_077217.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T14:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77217",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077218.json:
```json
{
    "body": "Attachment [trac_8552.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552.patch) by @dandrake created at 2010-03-23 14:12:20\n\nThese patches depend on the \"v2\" patch at #8486.\n         \nPlease look this patch over. I think I've tested all the execution paths and have everything working, but I only tested it on one system, so it needs some review and testing.\n\nA design decision that needs to be addressed: it's easiest to just do `subprocess.call()`, which waits for the command to finish; there are a few places where the `os.system` call ended with `&` to put the command in the background. I can reproduce that behavior with the subprocess module, but it's not as convenient, since I have to spawn the process and poll and so on. I can't detect much of a pattern or necessity to those places that possibly put the command in the background; is it okay if we just eliminate that option?\n\nAnother issue: the viewer commands from `misc.viewer` on Linux all return strings with a space in them: `'sage-native-execute xdg-open'`, which does not play nicely with subprocess; when you put that string into its call list, it tries to execute a single command with a space in it, named \"sage-native-execute xdg-open\" and this does not work well. It's easy enough to snag the \"xdg-open\" part, but if we eventually are using subprocess everywhere, we should switch the viewer commands to returning lists of strings.",
    "created_at": "2010-03-23T14:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77218",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_8552.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552.patch) by @dandrake created at 2010-03-23 14:12:20

These patches depend on the "v2" patch at #8486.
         
Please look this patch over. I think I've tested all the execution paths and have everything working, but I only tested it on one system, so it needs some review and testing.

A design decision that needs to be addressed: it's easiest to just do `subprocess.call()`, which waits for the command to finish; there are a few places where the `os.system` call ended with `&` to put the command in the background. I can reproduce that behavior with the subprocess module, but it's not as convenient, since I have to spawn the process and poll and so on. I can't detect much of a pattern or necessity to those places that possibly put the command in the background; is it okay if we just eliminate that option?

Another issue: the viewer commands from `misc.viewer` on Linux all return strings with a space in them: `'sage-native-execute xdg-open'`, which does not play nicely with subprocess; when you put that string into its call list, it tries to execute a single command with a space in it, named "sage-native-execute xdg-open" and this does not work well. It's easy enough to snag the "xdg-open" part, but if we eventually are using subprocess everywhere, we should switch the viewer commands to returning lists of strings.



---

archive/issue_comments_077219.json:
```json
{
    "body": "Overall, it looks good.\n\nI think line 615, `debug=True` should be deleted.  I also think that before line 1793\n\n```\nprint 'viewer: \"{0}\"'.format(viewer)\n```\n\nwe should have `if debug:`\n\nI notice that you don't seem to be using \"base\" in the switch from \n\n```\nlt = 'cd \"%s\"&& sage-native-execute %s \\\\\\\\nonstopmode \\\\\\\\input{%s.tex} %s'%(base, command, filename, redirect)\n```\n\nto\n\n```\nlt = ['sage-native-execute', command, r'\\nonstopmode', r'\\input{' + filename + '.tex}'] \n```\n\nBut it seems to work with your patch, so I guess it's okay.\n\n> is it okay if we just eliminate that [background] option?\n\nI think so.  If you think it's worth asking around, you could post on sage-devel.  Anyway, I think we can eliminate it, but we should probably keep the argument there for backwards compatibility, but have it do nothing -- this is what your patch does, right?  We (meaning you) just need to document that the option no longer does anything.\n\n> Another issue: the viewer commands from misc.viewer on Linux all return strings with a space in them\n\nIf \"s\" is the output of one of these commands, can we do s.split() to turn it into a list, split at spaces (if there are any)?  Oh, I guess that's what you're doing.\n\n----------\n\nSummary: fix the debugging issues (the print statement), and document the fact that \"do_in_background\" now has no effect, and I think this is ready to go.",
    "created_at": "2010-06-23T20:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77219",
    "user": "https://github.com/jhpalmieri"
}
```

Overall, it looks good.

I think line 615, `debug=True` should be deleted.  I also think that before line 1793

```
print 'viewer: "{0}"'.format(viewer)
```

we should have `if debug:`

I notice that you don't seem to be using "base" in the switch from 

```
lt = 'cd "%s"&& sage-native-execute %s \\\\nonstopmode \\\\input{%s.tex} %s'%(base, command, filename, redirect)
```

to

```
lt = ['sage-native-execute', command, r'\nonstopmode', r'\input{' + filename + '.tex}'] 
```

But it seems to work with your patch, so I guess it's okay.

> is it okay if we just eliminate that [background] option?

I think so.  If you think it's worth asking around, you could post on sage-devel.  Anyway, I think we can eliminate it, but we should probably keep the argument there for backwards compatibility, but have it do nothing -- this is what your patch does, right?  We (meaning you) just need to document that the option no longer does anything.

> Another issue: the viewer commands from misc.viewer on Linux all return strings with a space in them

If "s" is the output of one of these commands, can we do s.split() to turn it into a list, split at spaces (if there are any)?  Oh, I guess that's what you're doing.

----------

Summary: fix the debugging issues (the print statement), and document the fact that "do_in_background" now has no effect, and I think this is ready to go.



---

archive/issue_comments_077220.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-23T20:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77220",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077221.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-25T19:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77221",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077222.json:
```json
{
    "body": "I'm attaching two new patches here.  One is a referee patch, present for review only: do not apply it.  The other combines all of the patches into one.  Dan, if you're happy with my changes, please give this a positive review.",
    "created_at": "2011-03-25T19:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77222",
    "user": "https://github.com/jhpalmieri"
}
```

I'm attaching two new patches here.  One is a referee patch, present for review only: do not apply it.  The other combines all of the patches into one.  Dan, if you're happy with my changes, please give this a positive review.



---

archive/issue_comments_077223.json:
```json
{
    "body": "Attachment [trac_8552-ref.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552-ref.patch) by @jhpalmieri created at 2011-03-25 19:37:45\n\nfor review only, do not apply (diff between Dan's two patches and the all-in-one patch)",
    "created_at": "2011-03-25T19:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77223",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8552-ref.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552-ref.patch) by @jhpalmieri created at 2011-03-25 19:37:45

for review only, do not apply (diff between Dan's two patches and the all-in-one patch)



---

archive/issue_comments_077224.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2011-03-25T19:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77224",
    "user": "https://github.com/jhpalmieri"
}
```

apply only this patch



---

archive/issue_comments_077225.json:
```json
{
    "body": "Attachment [trac_8552-all-in-one.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552-all-in-one.patch) by @dandrake created at 2011-03-26 07:55:07\n\nThanks for finishing this, John. Sorry I left it unfinished. Your changes look good.",
    "created_at": "2011-03-26T07:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77225",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_8552-all-in-one.patch](tarball://root/attachments/some-uuid/ticket8552/trac_8552-all-in-one.patch) by @dandrake created at 2011-03-26 07:55:07

Thanks for finishing this, John. Sorry I left it unfinished. Your changes look good.



---

archive/issue_comments_077226.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-26T07:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77226",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T08:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8552#issuecomment-77227",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_008735.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-07T08:38:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8552",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8552#event-8735"
}
```
