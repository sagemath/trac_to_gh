# Issue 5638: [with patch, needs review] deprecate jsmath from the command line

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-30 01:02:42

Assignee: jhpalmieri

From the command line, jsmath is kind of broken and is also superfluous: `jsmath('blah', mode='inline')` is basically equivalent to `html('$blah$')`, and similarly if mode='display': just use '$$blah$$'.  This patch removes jsmath from import into the global name space at the command line, rewrites the code to make it just call html, and adds a deprecation warning.



---

Attachment

This works, looks good, and also works with #5636.


---

Comment by mabshoff created at 2009-03-31 08:32:07

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 08:32:07

Resolution: fixed
