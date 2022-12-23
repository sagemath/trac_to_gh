# Issue 4029: sage-env kills the shell when called from "wrong" directory

Issue created by migration from https://trac.sagemath.org/ticket/4029

Original creator: dphilp

Original creation time: 2008-09-01 04:03:55

Assignee: mabshoff

CC:  iandrus

Keywords: sage-env source

Sourcing sage-env from any directory other than SAGE_ROOT or SAGE_LOCAL/bin kills the shell.  This is considerably disconcerting behaviour.  An explanatory message would be nice (if not a proper fix).


---

Comment by mabshoff created at 2008-09-17 11:55:02

Oops, no milestone


---

Comment by mabshoff created at 2009-01-24 12:52:56

There is a typo in the commit message, but otherwise this is the correct fix. I initially also wanted to do the indenting, but this is a much cleaner and better solution.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 13:59:42

The patch does not apply to my merged tree. I believe #22 collides with this, but it should be easy to rebase post 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 07:18:59

The rebase needs to make sure that the changes from #22 don't get lost :)

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-10-05 07:19:06

I've attached a new patch which implements a cleaner solution using "$(exit 1)".  See http://fvue.nl/wiki/Bash:_Return_or_exit%3F


---

Comment by was created at 2009-10-05 13:22:32

merged in sage-4.1.2.rc1....


---

Comment by was created at 2009-10-05 13:31:45

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

Attachment

I used the very hacky (but effective)

```
return 1 2>/dev/null || exit 1
```

instead of `return` or `exit`.


---

Comment by iandrus created at 2010-12-29 20:31:59

Changing status from needs_work to needs_review.


---

Comment by iandrus created at 2011-03-24 00:08:44

Will be obsolete with #10469.


---

Comment by jhpalmieri created at 2011-03-24 21:00:47

I don't think this will be obsolete with #10469: after applying that patch, if I open up a new shell and source sage-env, the shell closes.  Isn't the issue using "exit" instead of "return", since the script is being sourced?  I'm not a shell script expert, but can we just replace "exit 1" with "return 1" everywhere?  Failing that, can you explain your hack

```
return 1 2>/dev/null || exit 1
```

This seems to work for me.


---

Comment by iandrus created at 2011-03-24 23:31:55

Changing status from needs_review to needs_work.


---

Comment by iandrus created at 2011-03-24 23:31:55

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

Comment by jhpalmieri created at 2011-03-24 23:44:01

See #9960; that changes every "exit" to "return" in sage-env.  Perhaps that one will obsolete this one.  If you wanted to give it one more review, that would be great.


---

Comment by iandrus created at 2011-03-25 00:09:13

That would definitely obsolete this one, though we still need to change the `start-sage.sh` in the Mac app.  I think that's fairly low priority though, and since I'm the one who maintains that, it should be easy.


---

Comment by jhpalmieri created at 2011-03-25 14:46:30

Changing status from needs_work to positive_review.


---

Comment by jhpalmieri created at 2011-03-25 14:46:30

I'm marking this "positive review" so the release manager can close it once #9960 is merged.


---

Comment by jdemeyer created at 2011-05-13 06:12:45

See #9960.


---

Comment by jdemeyer created at 2011-05-13 06:12:45

Resolution: duplicate
