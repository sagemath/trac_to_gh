# Issue 7308: cliquer's spkg-install does not work on cygwin

Issue created by migration from https://trac.sagemath.org/ticket/7308

Original creator: mhansen

Original creation time: 2009-10-26 09:23:36

Assignee: tbd

CC:  dkirkby was

Keywords: cliquer

The section where SAGESOFLAGS are set assumes that the operating system is Linux, OS X, or Solaris.  The spkg-install script exists even if SAGE_PORT is set to yes.


I'll post a patch and a new SPKG here shortly.


---

Comment by mhansen created at 2009-10-26 09:30:01

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2009-10-30 14:41:22

I'm not in a position to test this, but if you need to make any changes, I would suggest the following would be helpful. Some are I admit code I introduced, which is probaby not necessary. None are particularly important. 

 * There is no longer any need to have 


```
if [ -n "$SAGE_FORTRAN_LIB" ] && [ ! -e "$SAGE_FORTRAN_LIB" ]; then
    echo "SAGE_FORTRAN_LIB is defined as $SAGE_FORTRAN_LIB, but does not exist"
    exit 1
fi
}}} 
since code in the recent ''prereq-0.4'' (#7021) script checks this, so the above code is redundant. 

 * There is no need to have the following line

` if [ "x$SAGE64" = "xyes" ] || [ "x$SAGE64" = "x1" ]; then `

It should instead be replaced by

   ` if [ "x$SAGE64" = "xyes" ]; then `

since some earlier code in the ''prereq-0.3'' script written by William only allows SAGE64 to be unset, or set to ''yes'' or ''no''. It is not possible to set it to ''1'', so there is no point testing if it is ''1''. The same behaviour is followed in my recent updated to prereq-0.4 (#7021) and also to prereq-0.5 which I have awaiting review (#7352)

 * There is no need to have 
  {{{
    # We exit here, since we are possibly on an unsupported platform.
    if [ -n "${SAGE_PORT:-x}" ]; then
        echo "Cannot determine your platform or it is not supported... exiting"
        exit 1
    else
   }}}
since the recent ''prereq-0.4'' update will exit for '''all''' unsupported platforms unless SAGE_PORT is set to 'yes'.


---

Comment by was created at 2010-02-07 05:52:56

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-02-07 05:52:56

The actual patch looks fine to me.    Kirkby's comments are all fine, but of course shouldn't be part of this ticket.  There is no point in confusing things by doing too much at once.


---

Comment by mpatel created at 2010-02-10 16:53:06

I think the existing package is called `cliquer-1.2.p3`.  Should we make the new one `p4`?


---

Comment by mpatel created at 2010-02-10 23:45:02

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-02-13 06:41:20

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-02-13 06:42:00

I rebased Mike's patch, refereed it, and posted a new spkg with the rebased patch here:

   http://wstein.org/home/wstein/ports/cygwin/cliquer-1.2.p4.spkg


---

Comment by was created at 2010-02-13 06:42:00

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-16 04:26:12

Feel free to open another ticket to address the issues that drkirkby raised.


---

Comment by mvngu created at 2010-02-16 04:26:12

Resolution: fixed
