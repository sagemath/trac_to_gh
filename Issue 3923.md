# Issue 3923: [with patch, not ready for review] notebook -- convert existing templates to Jinja templates

Issue created by migration from https://trac.sagemath.org/ticket/3923

Original creator: TimothyClemans

Original creation time: 2008-08-22 00:11:17

Assignee: boothby

Requires the Jinja Template Engine http://jinja.pocoo.org/2/


---

Attachment


---

Attachment


---

Attachment


---

Attachment

removes old files


---

Attachment


---

Comment by malb created at 2008-09-24 11:04:20

I think that this is not ready for review until Jinja is in Sage, if it ever gets into Sage.


---

Comment by mabshoff created at 2008-09-24 11:09:39

Replying to [comment:2 malb]:
> I think that this is not ready for review until Jinja is in Sage, if it ever gets into Sage.

Jinja is required for the ReST transition of the documentation, so I am very bullish that it will get in. In total the ReST tool chain in 4 spkg weights in at 2MB compressed total and since it is a large improvement over the current situation with latex2html I think it will happen soon. Mike Hansen is pretty much ready to go here and it seems likely that those changes will be in 3.2.x if not 3.2 (assuming the spkgs get voted in obviously :))

Cheers,

Michael


---

Comment by malb created at 2008-09-24 11:24:18

Replying to [comment:3 mabshoff]:
> Jinja is required for the ReST transition of the documentation, so I am very bullish that it will get in. In total the ReST tool chain in 4 spkg weights in at 2MB compressed total and since it is a large improvement over the current situation with latex2html I think it will happen soon. Mike Hansen is pretty much ready to go here and it seems likely that those changes will be in 3.2.x if not 3.2 (assuming the spkgs get voted in obviously :))

Don't get me wrong, I'm all in favor of Jinja getting in, but this still needs formal verification. Also, IIRC there is the issue of Jinja v1 (ReST) vs. v2 (this patch)?


---

Comment by mabshoff created at 2008-09-24 11:29:36

Replying to [comment:4 malb]:

> Don't get me wrong, I'm all in favor of Jinja getting in, but this still needs formal verification. Also, IIRC there is the issue of Jinja v1 (ReST) vs. v2 (this patch)?

Sure, I agree. Mike has figured out IIRC that both Jinja and ReST and this code plays well together with Jinja v2. Timothy should have actually checked with [sage-devel] formally before going off into the sunset and code up loads of features that the code in question would actually be merged. But this story is likely to have a happy end :). Hopefully everyone involved here will learn a lesson from this.

Cheers,

Michael


---

Comment by mhansen created at 2008-10-23 23:15:22

Changing assignee from boothby to mhansen.


---

Attachment

I rebased the patches against 3.2.alpha0, moved the templates from extcode to sage/server/notebook/templates/, and changed the imports to use Jinja1 instead of Jinja2.

Apply only trac_3923.patch.


---

Comment by mhansen created at 2008-10-23 23:15:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-25 22:55:09

Merged trac_3923.patch in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-25 22:55:09

Resolution: fixed
