# Issue 297: polymake -- create a build package for the optional SAGE package polymake-2.3

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-26 22:13:14

Assignee: was

CC:  sage-combinat jpflori

It seems much has changed since polymake v 2.2, so this might be difficult.
Also, they have interactive scripts, which one has to deal with.  Yuck.

I did try just building from scratch and it seemed to work without any funny
business with GMP, etc. 

If you work on this, email wstein`@`gmail.com



---

Comment by mabshoff created at 2007-08-23 07:23:38

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-08-23 07:23:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-23 10:24:05

Replying to [ticket:297 was]:
> It seems much has changed since polymake v 2.2, so this might be difficult.
> Also, they have interactive scripts, which one has to deal with.  Yuck.
> 
> I did try just building from scratch and it seemed to work without any funny
> business with GMP, etc. 
> 
> If you work on this, email wstein`@`gmail.com

Ok, I did some investigation. We need to modify support/configure.pl:

Around line 273:

```
$InstallTop ||= $multi ? "/usr/local/share/polymake" : "/usr/local/polymake";
if (!$silent) {
   print "\nWhere should ", ($multi ? "the architecture-independent part of " : ""), "polymake be installed? ";
   answer_path($InstallTop);
}
```

Instead of answer_path($InstallTop) we just should assign $InstallTop=getenv($SAGE_LOCAL) (or something alike, my perl is slightly rusty).

We also need to add Sage's gmp to $Libs around line 614 somewhere.

Cheers,

Michael


---

Comment by burcin created at 2011-05-31 14:22:18

I created packages for a prerelease version of polymake before this workshop:

http://polymake.org/doku.php/workshop0311

The package and its dependencies are here:

http://sage.math.washington.edu/home/burcin/polymake/

These packages were just for convenience. They are not ready for review. :)

I also started writing a python wrapper to libPolymake. It's not useful for anything yet, but I could make it useful and release it if there is interest.


---

Comment by kcrisman created at 2013-01-29 20:59:03

There has definitely been interest in this from various people I've spoken to over the years.  Also, it would be good to have it be an optional spkg for this.  Note the current version is now 2.12 (Burcin's was 2.9).


---

Comment by kcrisman created at 2014-11-20 14:06:52

This is, in the aggregate, a dup of #5488, #13768, and #14116.  Take your pick :)  In particular, Burcin extended his work and it was integrated into Sage in the latter two tickets, which have _much_ more information.


---

Comment by kcrisman created at 2014-11-20 14:06:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-11-20 14:07:06

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-28 20:58:27

Resolution: duplicate
