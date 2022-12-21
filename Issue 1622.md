# Issue 1622: update gnutls to 2.2.0

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-29 04:36:21

Assignee: was




---

Comment by mabshoff created at 2007-12-29 04:38:02

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-29 04:38:02

Changing assignee from was to mabshoff.


---

Comment by yi created at 2008-01-11 00:55:59

They just released 2.3.0 so we might as well update to the latest.

http://www.gnu.org/software/gnutls/releases/gnutls-2.3.0.tar.bz2


---

Comment by yi created at 2008-01-11 07:41:29

I just tried to create spkg's for it and everything is dandy except python-gnutls.  There are major changes to the openpgp parts of gnutls which causes the pytho-gnutls not to work. I've contacted the author of python-gnutls to see if he'll update the wrapper.


---

Comment by yi created at 2008-01-11 07:42:10

Also, here is a list of related packages that need to be updated as well:

opencdk
libgcrypt
libgpg-error
python-gnutls


---

Comment by mabshoff created at 2008-01-11 10:08:15

Replying to [comment:4 yi]:
> Also, here is a list of related packages that need to be updated as well:
> 
> opencdk
> libgcrypt
> libgpg-error
> python-gnutls

You are correct that once we update GNUTLS we at least need to update OpenCDK, but I will also update the others in one swoop. I will do this after I switch python to ucs4 though, which is the big goal for alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-19 23:15:01

An updated spkg with 64 bit OSX Mac support is at:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/gnutls-2.2.1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-19 23:15:16

Merged in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-19 23:15:16

Resolution: fixed
