# Issue 1896: Gracefully handle 3d plotting when no java

archive/issues_001896.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOn Jan 23, 2008, at 9:47 AM, Simon King wrote:\n\nDear Michael,\n\nOn Jan 23, 11:22 am, mabshoff <Michael.Absh...@fsmath.mathematik.uni-\ndortmund.de> wrote:\n<snip>\nWhat is a JDK?\n\nI was just running yast and was searching for JDK. It showed me three\npackages: java-1_4_2-caco-devel, ldapjdk and ldapjdk-javadoc. None of\nthem is installed. Should i?\n\nA java development toolkit. We have had some reports about jmol not\nworking where installing the Sun JDK solved the issue.\n\nThank you! It did solve it, jmol works now. The notebook doesn't, but\ni understood this will be solved in another alpha-version.\n\nIn sage-2.10, that i obtained without installing java-1_4_2-caco-\ndevel, ldapjdk and ldapjdk-javadoc, there was no problem with jmol.\nIs the dependency on JDK new?\n\nTo use jmol, all one needs is the Java runtime environment (not the full JDK).\n\nIf so, i think it should be mentioned in\nhttp://modular.math.washington.edu/sage/doc/html/inst/node5.html\n\nFor interactive 3d plots, yes. I think if no viewer is specified, and it detects java is not installed, then it should render in Tachyon (perhaps printing a warning that Java was not found). From the notebook, there is usually a big grey box with a \"must install java plugin to view this content\" warning that should be sufficient.\n\n- Robert\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1896\n\n",
    "created_at": "2008-01-23T18:27:47Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "Gracefully handle 3d plotting when no java",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1896",
    "user": "robertwb"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/1896





---

archive/issue_comments_012000.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-04-04T19:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1896#issuecomment-12000",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_012001.json:
```json
{
    "body": "let us close that one as invalid..",
    "created_at": "2018-04-04T19:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1896#issuecomment-12001",
    "user": "chapoton"
}
```

let us close that one as invalid..



---

archive/issue_comments_012002.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-04-15T11:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1896#issuecomment-12002",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_012003.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1896#issuecomment-12003",
    "user": "vdelecroix"
}
```

Resolution: wontfix



---

archive/issue_comments_012004.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1896#issuecomment-12004",
    "user": "vdelecroix"
}
```

closing positively reviewed duplicates
