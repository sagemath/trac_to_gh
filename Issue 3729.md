# Issue 3729: [with patch; needs review] Only overwrite RHOME environment variable when it is unset

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-07-26 17:28:35

Assignee: mabshoff

When using my Debian Sage package, "import rpy" fails because Sage is overwriting the RHOME environment variable.  I could install a symlink to the right place in $SAGE_LOCAL/lib/R, but I think it's cleaner for Sage to only replace RHOME if it isn't already set (and then the Debian Sage wrapper script would set it correctly).  I've attached a patch to do this.

There are several uncommitted changes in spkg/base/sage-env, so my patch is a normal patch (rather than an hg one).


---

Attachment


---

Comment by mabshoff created at 2008-07-27 01:21:54

Hi Tim,

this patch is problematic and I would prefer if you carried it in a Debian specific patch. We did begin setting RHOME since certain distributions like Gentoo set it when R was installed in the system. Then that R would be run which leads to problems, so setting it conditionally will reintroduce the same issues.

Cheers,

Michael


---

Comment by tabbott created at 2008-07-27 01:27:49

How about we change it to test whether an environment variable with a different name is set, e.g.

if [ -z "$SAGE_USE_SYSTEM_RHOME" ];
     RHOME="SAGE_LOCAL"/local/lib/R && export RHOME
fi

This I think should be pretty unlikely to bring those issues back, but still gives packagers a hook to set RHOME themselves.


---

Comment by mabshoff created at 2008-07-27 11:41:37

Hi Tim,

Replying to [comment:2 tabbott]:
> How about we change it to test whether an environment variable with a different name is set, e.g.
> 
> if [ -z "$SAGE_USE_SYSTEM_RHOME" ];
>      RHOME="SAGE_LOCAL"/local/lib/R && export RHOME
> fi
> 
> This I think should be pretty unlikely to bring those issues back, but still gives packagers a hook to set RHOME themselves.

Well, the problem I see here is that this way we have to set it in Sage somewhere before sourcing sage-env. We could do it in the sage script itself, but that is meant to do only the minimal number of things to get running and then sage-env deals with the environment. What I would prefer is something the other way around, i.e. distributions wishing to use the installed "system" set something in env that sage-env tests for and if SAGE_USE_SYSTEM_RHOME equaled "no" we would not set RHOME.

Thoughts"

Cheers,

Michael


---

Comment by tabbott created at 2008-07-27 17:40:41

I think the code snippet I offered has the semantics you describe (the code will set RHOME if and only if SAGE_USE_SYSTEM_RHOME is not set, and distributions would set it to "yes" to cause Sage to not change RHOME).  Maybe the variable needs a clearer name, like SAGE_DONT_SET_RHOME, but by "system rhome" I meant that Sage should not it, and that's what the code does.


---

Comment by mabshoff created at 2008-07-31 00:13:18

Yes, I was not as awake as I should have been when I reviewed the patch. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 00:53:05

Merged in Sage 3.1.alpha0


---

Comment by mabshoff created at 2008-07-31 00:53:05

Resolution: fixed
