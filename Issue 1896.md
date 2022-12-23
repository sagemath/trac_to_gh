# Issue 1896: Gracefully handle 3d plotting when no java

Issue created by migration from https://trac.sagemath.org/ticket/1896

Original creator: robertwb

Original creation time: 2008-01-23 18:27:47

Assignee: was


```
On Jan 23, 2008, at 9:47 AM, Simon King wrote:

Dear Michael,

On Jan 23, 11:22 am, mabshoff <Michael.Absh...@fsmath.mathematik.uni-
dortmund.de> wrote:
<snip>
What is a JDK?

I was just running yast and was searching for JDK. It showed me three
packages: java-1_4_2-caco-devel, ldapjdk and ldapjdk-javadoc. None of
them is installed. Should i?

A java development toolkit. We have had some reports about jmol not
working where installing the Sun JDK solved the issue.

Thank you! It did solve it, jmol works now. The notebook doesn't, but
i understood this will be solved in another alpha-version.

In sage-2.10, that i obtained without installing java-1_4_2-caco-
devel, ldapjdk and ldapjdk-javadoc, there was no problem with jmol.
Is the dependency on JDK new?

To use jmol, all one needs is the Java runtime environment (not the full JDK).

If so, i think it should be mentioned in
http://modular.math.washington.edu/sage/doc/html/inst/node5.html

For interactive 3d plots, yes. I think if no viewer is specified, and it detects java is not installed, then it should render in Tachyon (perhaps printing a warning that Java was not found). From the notebook, there is usually a big grey box with a "must install java plugin to view this content" warning that should be sufficient.

- Robert

```



---

Comment by chapoton created at 2018-04-04 19:18:37

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-04-04 19:18:37

let us close that one as invalid..


---

Comment by chapoton created at 2018-04-15 11:42:32

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
