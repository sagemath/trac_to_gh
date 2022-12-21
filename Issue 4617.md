# Issue 4617: Create a `test-dummy.spkg`

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-11-25 12:55:40

Assignee: mabshoff

Keywords: dummy test package

This is related with ticket #4587

For doc-testing the installation of packages, there should be some `test-dummy.spkg`

The purpose of the package is to do _nothing_. William suggested to mark it `optional -- admin`, I am not sure what that means.

Also, there should be an easy way to get rid of `test-dummy.spkg` after installation.

Idea:
 * `sage -i test-dummy.spkg` should simply result in an entry in the list of installed packages.
 * uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.


---

Comment by SimonKing created at 2008-11-25 20:43:31

Replying to [ticket:4617 SimonKing]:
> William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means "tested by the admin who has write privileges to the sage install]

Thanks! 

>  * uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.

... which probably also requires admin privileges. So, the to-be-created doctests for #4587 will also be optional -- admin, right?


---

Comment by jdemeyer created at 2014-11-06 15:57:48

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-11-06 15:57:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2014-11-06 15:57:59

Obsolete


---

Comment by vbraun created at 2014-11-07 16:49:58

Resolution: wontfix
