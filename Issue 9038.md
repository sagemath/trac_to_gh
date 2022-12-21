# Issue 9038: Typeset: Wrong charset for Greek characters

Issue created by migration from Trac.

Original creator: jan

Original creation time: 2010-05-24 19:42:07

Assignee: jason, was

Client: Ubuntu Karmic 9.10 with jsmath 3.5.9, jsmath-fonts 1.3-2, ttf-jsmath, and Firefox 3.5.9.

Server: Either http://www.sagebn.org or Debian Lenny with Sage 4.4.2 compiled from source

When displaying a formula containing "pi" with "Typeset" checked, the character Ú (capital U with accent) is displayed instead of the pi character.


---

Comment by jason created at 2010-05-25 19:51:10

This is most likely a problem with the ttf-jsmath package.  See http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html

"Linux users with Firefox 3.5 should use the last archive in the list, as the Linux version of Firefoex 3.5 can not process the non-standard encoding used in the other archives."

Can you install the linux firefox 3.5 fonts listed in the website above and see if that fixes the problem?


---

Comment by jason created at 2010-05-25 19:51:10

Changing status from new to needs_info.


---

Comment by jan created at 2010-05-28 22:47:24

Resolution: wontfix


---

Comment by jan created at 2010-05-28 22:47:24

Replying to [comment:2 jason]:
> This is most likely a problem with the ttf-jsmath package.  See http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html
> Can you install the linux firefox 3.5 fonts listed in the website above and see if that fixes the problem?

You were right. After removing ttf-jsmath and installing the downloaded fonts it works. Thank you.
