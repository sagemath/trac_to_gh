# Issue 2098: [with patch; needs review] rudimentary debian package build support

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-02-08 03:51:37

Assignee: tabbott

Add spkg-build-debian, and hook it in to sage-spkg.


---

Attachment


---

Attachment


---

Attachment


---

Comment by tabbott created at 2008-02-10 03:20:23

sage-build-debian will probably eventually want to look something like this.  I'm not applying it as a patch because it'll break the previous patchset:

DEBIAN_REPO would be set to point to a temporary Debian repository that is in the approx sources.list for SAGE, so that each package has its dependencies uploaded to the test repo when it comes time to build it for Debian.

#!/bin/sh -x
echo "Starting Debian build"
[ -d dist/debian ] || exit 0 # exit cleanly for packages we're using the Debian versions of
mv dist/debian src/
sage-dasource src/
sage-sbuildhack "$DEBIAN_RELEASE" *.dsc || exit 1
mkdir -p $SAGE_ROOT/deb
DEBIAN_ARCH=$(echo lenny-amd64 | cut -f 2 -d-)
reprepro -b $DEBIAN_REPO --ignore=wrongdistribution include *_${DEBIAN_ARCH}.changes
mv *.dsc *.changes *.build *.deb *.tar.gz *.diff.gz /deb
echo "Debian Build complete"


---

Comment by tabbott created at 2008-02-10 03:21:22

The 5th patch is to the sage spkg, not sage_scripts.


---

Attachment


---

Comment by mabshoff created at 2008-02-14 13:07:16

Patches look good to me. I sat next to Tim as he wrote most of the code, so maybe somebody else wants to take another look. In the end we might need to generalize the code a little more for other packaging systems.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 15:18:02

Resolution: fixed


---

Comment by mabshoff created at 2008-02-14 15:18:02

Merged debian1.patch-debian5.patch in Sage 2.10.2.alpha0


---

Attachment

This patch is needed to make the non-Debianized build work again
