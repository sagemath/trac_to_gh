# Issue 9606: local/bin/sage-sage assumes 'sh' is bash

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-07-26 23:42:53

Assignee: pjeremy

CC:  stephen

"sage -sh" is intended to start a subshell of the user's preference (as per $SHELL) with the local Sage environment configured in it.

In order to prevent the environment being altered by the user's shell RC scripts, local/bin/sage-sage passes an argument to $SHELL which is intended to disable RC processing.  Unfortunately, it assumes that 'sh' is 'bash' and passes '--norc' - which is not legal for POSIX shells.

Whilst this appears to be ignored by Solaris /bin/sh and /usr/xpg4/bin/sh (which is at variance to the man page), it is rejected by FreeBSD /bin/sh - which reports "Illegal option --".

The fix is not clear because Cygwin, Linux and OpenSolaris (at least) all install bash as /bin/sh - though experiments show that at least bash-4.1.7 will not run any RC script when invoked as sh.


---

Comment by leif created at 2012-04-19 21:06:33

Changing status from new to needs_info.


---

Comment by leif created at 2012-04-19 21:06:33

Is this still an issue?

(The script btw. has meanwhile been renamed / moved to `$SAGE_ROOT/spkg/bin/sage`.)


---

Comment by jhpalmieri created at 2012-04-19 23:03:53

The relevant part of the script says

```sh
        sh)
            # We don't really know which shell "sh" is (it could be
            # bash, but this is not guaranteed), so we don't set
            # SHELL_OPTS.
            if [ "$color_prompt" = yes ] ; then
                PS1="$(tput rev)(sage-sh)$(tput sgr0) $USER`@``hostname -s`:\${PWD##*/}$ "
            else
                PS1="(sage-sh) $USER`@``hostname -s`:\${PWD}$ "
            fi
            export PS1
            ;;
```

So it doesn't look like this ticket is relevant any more.


---

Comment by kcrisman created at 2013-01-16 01:21:38

`@`Stephen M-S:  If you have time, can you check that `./sage -sh` works from `SAGE_ROOT`?   That would confirm what John and Leif point out here - but it would be nice to have it actually tested, since stranger things have happened.


---

Comment by kcrisman created at 2013-01-16 01:21:38

Changing status from needs_info to needs_review.


---

Comment by stephen created at 2013-01-16 02:48:43

I can confirm that ./sage -sh works from SAGE_ROOT, even when SHELL=/bin/sh.


---

Comment by kcrisman created at 2013-01-16 02:58:36

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-01-16 02:58:36

Great, thank you!


---

Comment by jdemeyer created at 2013-01-17 10:03:30

Resolution: worksforme
