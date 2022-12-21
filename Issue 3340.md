# Issue 3340: update givaro to 3.2.10 release

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-30 17:40:22

Assignee: mabshoff

We're currently using the givaro 3.2.10rc3 release candidate; we should update to the actual release.  

The differences are somewhat substantial:

[tabbott`@`debuild tmp$] diff -ur givaro-3.2.10/ ../givaro-3.2.10~rc3/ | diffstat
<SNIP>
 123 files changed, 883 insertions(+), 1413 deletions(-)



---

Comment by mabshoff created at 2008-06-26 03:25:50

Clement Pernet's latest Givaro.spkg is at

http://sage.math.washington.edu/home/pernet/givaro-3.2.11.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 03:42:16

The spkg builds fine on OSX and x86-64 Linux and doctests fine. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 03:42:33

Resolution: fixed


---

Comment by mabshoff created at 2008-06-26 03:42:33

Merged in Sage 3.0.4.alpha1
