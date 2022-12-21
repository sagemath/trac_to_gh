# Issue 4162: Upgrade trac to 0.11

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-09-21 02:26:42

Assignee: was

Trac 0.11.1 is the newest stable release of trac.  Upgrading to trac 0.11 will allow us to make the ticket review process an actual process (with discrete stages and a workflow that we can send tickets through), instead of the current adhoc keyword-based method.  I'm sure there are other things that are good too.

One thing that may need to be done is to make sure that Robert's extension to display bundles works.

See the suggestions in http://groups.google.com/group/sage-devel/browse_thread/thread/d794dcc6f98c17fe/cd75d577420d1764?lnk=gst&q=needs+review+needs+more+info#cd75d577420d1764 to see if we can implement these better with the new trac.


---

Comment by jason created at 2008-09-21 02:28:23

For reference, here is a list from the above mailing list discussion:


```
# Desirable Trac Features #

* more statistics
* a default CC to a google group sage-trac, this requires that a
  google group is created [done] and that somebody with admin
  access to sagemath.org enables smtp for trac [not done yet]
* mercurial bundle browsing: This is currently not support by
  the mercurial plugin for trac, but Robert Bradshaw might end up
  doing some trac hacking as part of his TA appointment at UW so
  he could perhaps look into this.
* IRC logs: A trac extension to log IRC channels exists. We should
  consider using it, but make it clear in #sage-devel that the
  discussion is logged. We should also consider adding #sage-support
  so that the signal/noise ratio for development stays high on
  #sage-devel, but sage newbies could ask questions about Sage use.
  This would also potentially be a way for people to move up in
  the food chain from sage newbie to experienced user to eventually
  sage developer.
* loads more interesting bits at http://trac-hacks.org/ - but we
  should not merge in too many extensions because it makes
  maintainability more difficult once we upgrade to newer trac
  releases. I maintain several phpBB installations and not
  adding a wild bunch of mods proved to be a smart choice.
* Jason Grout has suggested new "states" of tickets to make
  the system more finely grained:

      active
      active (needs more info)
      patch (code needs work)
      patch (code needs review)
      patch (code needs to be committed)
      fixed
      duplicate
      invalid
      worksforme
      wontfix
      bydesign

   The names have been modeled after Drupal's ticket tracking system 
```



---

Comment by jason created at 2008-09-21 02:28:57

(some of those things have already been done in the current trac, like Robert's bundle browsing extension.)


---

Comment by jason created at 2008-09-21 02:35:34

Also, we ought to see if an upgrade would provide a solution for #1768.


---

Comment by mabshoff created at 2008-09-21 05:24:06

As mhansen pointed out in trac:

 * we have a test version of the Sage trac running off-site
 * I am reluctant to first upgrade the Sage trac, but I want to got with the mpir and then cython trac since the smaller install are likely to flush out problems.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 08:38:18

Resolution: fixed


---

Comment by mabshoff created at 2009-02-21 08:38:18

Fixed by William during the modular.math -> VMWare transition.

Any follow up, i.e workflow updates, should go to new tickets.

Cheers,

Michael
