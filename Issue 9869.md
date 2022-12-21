# Issue 9869: Clean up Cliquer's Makefile and spkg-install

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-07 21:20:38

Assignee: GeorgSWeber

CC:  ncohen mvngu

The `Makefile` and `spkg-install` for Cliquer could do with a lot of cleaning up. Some examples of the problems are:

 * There are flags set for the C++ and Fortran compilers, though the code is only C. 
 * There's code to check for a mix of Sun and GNU compilers, when better tests now exists as `$SAGE_LOCAL/bin/testcc.sh`
 * Lots of unnecessary environment variables are set. 
 * Many, many other problems. 

*None of these issues are currently causing any problems, but should be resolved at some point*


---

Comment by leif created at 2010-09-09 02:24:26

Changing assignee from GeorgSWeber to leif.


---

Comment by leif created at 2010-09-09 02:24:26

To tranquilize Dave :-)

I've made several comments at tickets related to Cliquer, e.g. #9833 and #9871.

I think this should then be a follow-up of #9871, despite the numbers.


---

Comment by drkirkby created at 2010-09-15 09:54:40

Changing component from build to linear programming.


---

Comment by ncohen created at 2010-09-15 11:11:16

Hello !

> There is one technical question you can however answer. Do we need the binary file "cl" so it can be executed from the command line, or is the library libcliquer.so sufficient?

No, the cl file is not used, and this is precisely what the Sage code included in cliquer is useful for : directly calling the library's functions with a Graph object using the Graph structure it expects to find, without having to create an ugly temporary file to call the executable on it `:-)`

Nathann


---

Comment by drkirkby created at 2010-11-07 00:19:06

Leif, you were keen to take ownership of this. Has anything happened with it? 

Dave


---

Comment by drkirkby created at 2011-03-23 15:09:25

I ask once again. Any chance of you sorting this out Leif, since you wanted to take ownership of it. 

Dave


---

Comment by jdemeyer created at 2011-04-25 17:15:43

See #11227 for another issue with cliquer, unrelated to this ticket.


---

Comment by jdemeyer created at 2014-01-16 13:34:00

Changing component from linear programming to packages: standard.


---

Comment by jdemeyer created at 2014-01-16 13:34:00

I'll tackle this.


---

Comment by jdemeyer created at 2014-01-16 14:41:59

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-01-16 14:41:59

New commits:


---

Comment by jpflori created at 2014-02-20 16:13:33

Don't know why trac was not able to merge the branch as I encountered no conflicts when merging it.

I've made a few changes to make the script more like the "new" scripts as described in the dev guide, you may not be happy with them and are very welcome to change them back.
Otherwise let's positively review this ticket.

Anyway, I'm going to autotoolify cliquer, post it in a follow-up ticket and suggest it upstream.
The Makefile is just too awful right now.
----
New commits:


---

Comment by jpflori created at 2014-02-20 16:28:38

I've sent an email upstream about the possibility of releasing an official version including some of the Debian's patches (http://anonscm.debian.org/gitweb/?p=debian-science/packages/cliquer.git;a=tree;f=debian/patches;hb=HEAD) and an autotoolified build system.


---

Comment by jdemeyer created at 2014-02-21 06:03:04

I think `set -e` is a good thing and should be used more. So I reverted that change.


---

Comment by jdemeyer created at 2014-02-21 06:03:04

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-22 06:45:28

Resolution: fixed


---

Comment by jpflori created at 2014-02-24 13:30:44

FYI, upstream has nicely answered my questions.
They don't really mind cliquer being distributed in different forms in various places and don't plan on releasing any new upstream version "in the next ten years or so (or ever?)".
