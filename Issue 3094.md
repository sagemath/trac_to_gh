# Issue 3094: [with patch; needs review] Update to SAGE Debian packaging

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-05-03 08:28:33

Assignee: tabbott

The attached patch updates the SAGE dist/debian/ from the extcode repository to work with polybori and zn_poly as separate packages, include a missing cddlib dependency, set SAGE_TESTDIR in the wrapper script, and various other minor fixes.


---

Attachment


---

Comment by tabbott created at 2008-05-03 08:32:52

I added a second patch that makes it so SAGE can find the cdd tests.


---

Attachment


---

Comment by mabshoff created at 2008-05-03 14:58:12

I skimmed sage-debian-package-3.0.1.patch and it looks correct, but I am no expert there. sage-cdd-bin.patch looks good to me. Since this patch only potentially breaks the Debian build and Tim will fix it himself positive review. It would be great if we could get more people from the Debian community to increase the bus factor on the Debian packaging.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 14:58:24

Merged in Sage 3.0.1.final


---

Comment by mabshoff created at 2008-05-03 14:58:24

Resolution: fixed
