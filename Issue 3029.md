# Issue 3029: [with patch; needs review] Move DEB_AUTO_UPDATE_DEBIAN_CONTROL out of Debian packages

Issue created by migration from https://trac.sagemath.org/ticket/3029

Original creator: tabbott

Original creation time: 2008-04-26 04:13:21

Assignee: tabbott

Debian doesn't allow you to upload packages that use DEB_AUTO_UPDATE_DEBIAN_CONTROL because it causes confusion with Non-Maintainer Uploads.  Since I'd like to get the packages so that they can be uploaded to Debian, we should remove it from our rules files.  Since it's fine for our purposes, I've modified sage-debsource to set DEB_AUTO_UPDATE_DEBIAN_CONTROL so that it always gets used when we are building packages.  I think it's probably easier for Michael to just make the changes than to merge N patches, so the following code will do the relevant update when the relevant spkgs are unpacked.

perl -i -0pe 's/^DEB_AUTO_UPDATE_DEBIAN_CONTROL = 1\n//m' */dist/debian/*/rules */dist/debian/rules

(if the patches are easier to deal with, let me know and I'll generate them)
The complete list of spkgs that require this treatment is as follows:

cddlib
eclib
extcode
flint
flintqs
gap
genus2reduction
gfan
givaro
iml
jmol
lcalc
libfplll
libm4ri
linbox
ntl
palp
polybori
rubiks
scipy_sandbox
singular
symmetrica
sympow
tachyon
zn_poly


---

Attachment


---

Comment by mabshoff created at 2008-04-26 04:28:18

Hi Tim,

do I still need to run the perl script if I apply the patches? I would prefer to import 25 patches since then I do have a record. Since I will likely touch a lot of the spkgs in the next two days for cleanups I think it will be fine if you post those 25 patches and I just merge them as I go.

Cheers,

Michael


---

Comment by tabbott created at 2008-04-26 04:49:55

No, the perl script is what generates the patches that need to be done (there's also a single patch not done by the perl script that I've already uploaded).  I'll go ahead and post the 25 patches, then.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-04-27 07:19:25

The patches look good to me. Most of them are really trivial, the two, three others are fine, too. I put them into the spkgs without bumping the patch level to avoid massive recompile on update.

Please, no more massive 25 spkg patch orgies ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-27 07:19:49

Merged in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-27 07:19:49

Resolution: fixed
