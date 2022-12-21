# Issue 7139: flint always building 32-bit on Solaris even when SAGE64="yes"

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-06 01:23:31

Assignee: tbd

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/lib, we can see the flint  library is 32-bit, even though SAGE64 was set to "yes", so flint is ignoring the setting of SAGE64. It should also be notes that flint ignores CC and CXX too - see #7024


This is far from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too.

    * zlib #7128
    * libgpg_error #7129
    * libpng #7130
    * libcliquer #7131
    * pari #7133
    * ntl #7134
    * python #7135
    * gp #7136 
    * ratpoints #7137
    * freetype #7138

mpir currently mixes 32 and 64-bit objects, so does not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform. This is not a very difficult task really. Whilst any changes to the source that might be necessary for a port would take a lot of time, finding the right flags to build with should be quite easy. 


---

Comment by drkirkby created at 2010-01-02 06:52:51

Resolution: duplicate


---

Comment by drkirkby created at 2010-01-02 06:52:51

Like an idiot, I created another ticket for this same problem. I'm closing this one, as the other one has the patch and is more upto date.
