# Issue 2663: dpkg-shlibdeps errors for various Debian packages

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-03-25 05:14:47

Assignee: tabbott

When I build eclib and singular for Debian, I get a bunch of errors from dpkg-shlibdeps.  When I build the sagemath package, I get countless pages of scrolling of this sort of error.  I should track down what's going on here.

dpkg-shlibdeps: warning: debian/libec0/usr/lib/libcurvesntl.so shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libcurvesntl.so shouldn't be linked with libgmp.so.3 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libcurvesntl.so shouldn't be linked with libpari-gmp.so.2 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libcurvesntl.so shouldn't be linked with libjcntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libjcntl.so shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libjcntl.so shouldn't be linked with libgmp.so.3 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/librankntl.so shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/librankntl.so shouldn't be linked with libgmp.so.3 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/librankntl.so shouldn't be linked with libpari-gmp.so.2 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/librankntl.so shouldn't be linked with libcurvesntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/librankntl.so shouldn't be linked with libjcntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libg0nntl.so shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libg0nntl.so shouldn't be linked with libgmp.so.3 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libg0nntl.so shouldn't be linked with libpari-gmp.so.2 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libg0nntl.so shouldn't be linked with libcurvesntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/libec0/usr/lib/libg0nntl.so shouldn't be linked with libjcntl.so (it uses none of its symbols).

dpkg-shlibdeps: warning: debian/singular/usr/bin/libparse shouldn't be linked with libgcc_s.so.1 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/Singular shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/Singular shouldn't be linked with libncurses.so.5 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/ESingular shouldn't be linked with libdl.so.2 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/ESingular shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/ESingular shouldn't be linked with libgmp.so.3 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/ESingular shouldn't be linked with libreadline.so.5 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/ESingular shouldn't be linked with libncurses.so.5 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/ESingular shouldn't be linked with libgcc_s.so.1 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/Singular-3-0-4 shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/Singular-3-0-4 shouldn't be linked with libncurses.so.5 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/LLL shouldn't be linked with libgcc_s.so.1 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/TSingular shouldn't be linked with libdl.so.2 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/TSingular shouldn't be linked with libntl.so (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/TSingular shouldn't be linked with libgmp.so.3 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/TSingular shouldn't be linked with libreadline.so.5 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/TSingular shouldn't be linked with libncurses.so.5 (it uses none of its symbols).
dpkg-shlibdeps: warning: debian/singular/usr/bin/TSingular shouldn't be linked with libgcc_s.so.1 (it uses none of its symbols).


---

Comment by tabbott created at 2008-05-27 03:22:14

Resolution: fixed


---

Comment by tabbott created at 2008-05-27 03:22:14

These messages are intended to indicate unecessary -lblah flags, i.e. where we have a -lntl or whatever when linking the shared library, but the shared library doesn't directly use any of the symbols of ntl.  In newer dpkg the messages look like:

dpkg-shlibdeps: warning: dependency on libgmpxx.so.4 could be avoided if "debian/liblinbox0/usr/lib/liblinbox.so.0.0.0" were not uselessly linked against it (they use none of its symbols).
dpkg-shlibdeps: warning: dependency on libblas.so.3gf could be avoided if "debian/liblinbox0/usr/lib/liblinbox.so.0.0.0" were not uselessly linked against it (they use none of its symbols).


Since it seems that on other platforms one does need to link against all one's dependencies, not just one's direct dependencies (at least, I'm guessing this is what's going on; when we followed similar indications on genus2reduction it ended up breaking things on OS X), I'm not sure there's anything one should do about these.  Thus, I'm closing the ticket.
