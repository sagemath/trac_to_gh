# Issue 302: Improved error reporting for notebook

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2007-03-01 06:04:32

Assignee: was

If the notebook server gets messed up, the notebook server should display a web page in place of any other pages. 


---

Comment by was created at 2007-03-01 18:07:26

Resolution: invalid


---

Comment by was created at 2007-03-01 18:07:26

This doesn't make sense.  If the notebook server is "messed up", then it can't display anything, since it's messed up.  Messed up, means it crashed.


---

Comment by TimothyClemans created at 2007-03-01 22:27:51

"chmod -w nb.sobj" messes up the notebook.

    self.save_notebook_every_so_often()
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/server/notebook/server.py", line 320, in save_notebook_every_so_often
    notebook.save()
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 750, in save
    SageObject.save(self, F, compress=False)
  File "sage_object.pyx", line 139, in sage_object.SageObject.save
IOError: [Errno 13] Permission denied: '/home/Timothy/sage_notebook/nb.sobj'
----------------------------------------
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET / HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /jsmath/plugins/noImageFonts.js HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /jsmath/jsMath.js HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /sagelogo.png HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:37] "GET /corner.png HTTP/1.1" 200 -
localhost.localdomain - - [01/Mar/2007 14:22:38] "GET /jsmath/jsMath-fallback-unix.js HTTP/1.1" 200 -

 The notebook stops running computations, however it is still serving web pages. It should stop serving those pages and show an error.


---

Comment by TimothyClemans created at 2007-03-01 22:27:51

Resolution changed from invalid to 


---

Comment by TimothyClemans created at 2007-03-01 22:27:51

Changing status from closed to reopened.


---

Comment by TimothyClemans created at 2007-03-26 03:33:44

Changing type from defect to enhancement.


---

Comment by TimothyClemans created at 2007-03-26 03:33:44

Changing priority from critical to minor.


---

Comment by TimothyClemans created at 2008-07-04 18:02:14

Please close this ticket as invalid.


---

Comment by mabshoff created at 2008-07-04 20:19:02

Timothy,

could you give a reason for the record why this should be invalid?

Cheers,

Michael


---

Comment by TimothyClemans created at 2008-07-04 21:03:53

I think it should be marked as invalid because we don't have a good list of the errors that could pop up. When we do then this will become more necessary. 

For example on the TRAC server for Knoboo I've seen it report that the server is having database trouble. If we discover that a Sage Notebook can become unusable then this sort of error reporting would become necessary.


---

Comment by mabshoff created at 2008-07-04 21:40:22

Resolution: invalid


---

Comment by mabshoff created at 2008-07-04 21:40:22

Sounds reasonable to me. Invalidated.
