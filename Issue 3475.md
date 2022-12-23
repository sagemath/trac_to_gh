# Issue 3475: [with patch, needs review] setup.py was missing jquery.form.js, upgrade to latest version of jquery (1.2.6) and jquery.form

Issue created by migration from https://trac.sagemath.org/ticket/3475

Original creator: yi

Original creation time: 2008-06-19 21:47:07

Assignee: was

jquery.form.js somehow got dropped from setup.py, which is needed for the web interface, it does *NOT* function correctly without the proper jquery plugin. 

This patch also upgrades jquery, jquery.form to the latest version. 


---

Attachment

renamed patch file to include bug #


---

Comment by craigcitro created at 2008-06-20 04:35:48

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-02 20:05:33

Yi,

can you split off the "missing jquery.form.js from setup.py" part from the jquery update? The copy part of the patch is trivial to review and will get into 3.0.4, I am not so sure about the jquery update since that should be done by somebody who works on the notebook and withb `@`interact for example.

Cheers,

Michael


---

Comment by yi created at 2008-07-02 21:56:27

Michael,

The jquery update is a non issue since AFAIK the notebook does not use the jquery version dsage uses. 

It uses the one found here:

iapetus:~/Software/sage-3.0.3.rc0/data/extcode/notebook/javascript/jquery > 

Maybe in the future we can simply provide one version, but that is another issue. Let me know if this resolves your complaint.


---

Comment by mabshoff created at 2008-07-03 05:02:25

I agree that there are two copies of jquery and we can upgrade DSage's copy without having any repercussions on the notebook one. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-03 05:03:30

Resolution: fixed


---

Comment by mabshoff created at 2008-07-03 05:03:30

Merged in Sage 3.0.4.alpha2
