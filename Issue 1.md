# Issue 1: SAGE Notebook leaves dead processes on OS X

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-11 03:58:42

Assignee: somebody

The sage notebook restart often leaves "dead Python" process running.
This is especially bad on OS X, where there is a 100 process limit by
default (at least on my laptop). 


---

Comment by was created at 2006-09-14 08:21:51

I finally decided to fix that bug under OS X where the SAGE notebook
spawns > 100 processes, which OS X doesn't like (i.e., when you hit
restart a lot).  It took me 2 minutes to fix, so I wish I had done
it earlier. 

I just inserted this line

            self.__sage._expect = None

in worksheet.py as line 661, so now its:
        alarm(2)
        try:
            self.__sage._expect = None
            del self.__sage
        except AttributeError, msg:
            print "WARNING: %s"%msg
        except Exception, msg:
            print msg
            print "WARNING: Error deleting SAGE object!"
        cancel_alarm()


I checked this into the standard darcs repository.


---

Comment by was created at 2006-09-14 08:21:51

Resolution: fixed
