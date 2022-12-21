# Issue 5161: [with patch, needs review] Remove outdated SHAREDFLAGS and Solaris specific injected flags from sage-env

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-02 19:59:15

Assignee: mabshoff

sage-env sets a bunch of environment variables like SHAREFLAGS that cause trouble on Cygwin and Solaris and are also pretty outdated. Setting global flags should be handled in a cleaner matter in case they are required, so for now remove the code from sage-env. It does break previously working setups and has cost me considerable time to work around before I discovered that the problem was introduced by sage-env.

Cheers,

Michael


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2009-02-03 01:03:42

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 01:03:42

Resolution: fixed
