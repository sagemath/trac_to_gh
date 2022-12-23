# Issue 4449: sage-combinat install script doesn't work with 3.2.alpha2

Issue created by migration from https://trac.sagemath.org/ticket/4449

Original creator: saliola

Original creation time: 2008-11-05 22:23:44

Assignee: saliola

CC:  sage-combinat

Keywords: sage-combinat

'sage -combinat install' on sage-3.2.alpha2 fails (and not on 'hg qpush -a').


---

Attachment


---

Comment by saliola created at 2008-11-05 22:30:13

The script fails because the following re.search in get_sage_version

    return re.search('(\d+\.\d+\.\d+)',sage_version).group()

doesn't match anything for "3.2.alpha0". One way to get around this is to use a try-except statement (see the attached patch sage-combinat_4449.patch).

Now for 3.2.alpha2, the version number returned is '3.2.0' and for '3.2.1.alpha2' it is '3.2.1'. I think this should be okay since the version number is used to determine the guards (and the guards don't change much between alpha releases).

Now the script runs, and fails at the end during the 'hg qpush -a' (which is acceptable).


---

Comment by mabshoff created at 2008-11-05 22:32:20

Notice that there is also #4415, so hopefully this will not collide.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-05 22:34:21

Looks good to me. It won't catch all odd version numbers and nothing like x.y.z.w, but we don't use those any more.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-05 22:34:43

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-05 22:34:43

Resolution: fixed
