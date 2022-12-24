# Issue 6859: Add more graph generators

archive/issues_006859.json:
```json
{
    "body": "Assignee: rlm\n\nThis patch add graph generators for the hyper star, (n,k)-star, n-star, and bubble sort graph.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6859\n\n",
    "created_at": "2009-09-02T01:42:16Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "Add more graph generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6859",
    "user": "myurko"
}
```
Assignee: rlm

This patch add graph generators for the hyper star, (n,k)-star, n-star, and bubble sort graph.

Issue created by migration from https://trac.sagemath.org/ticket/6859





---

archive/issue_comments_056559.json:
```json
{
    "body": "Attachment [trac_6859.patch](tarball://root/attachments/some-uuid/ticket6859/trac_6859.patch) by myurko created at 2009-09-02 01:42:57",
    "created_at": "2009-09-02T01:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56559",
    "user": "myurko"
}
```

Attachment [trac_6859.patch](tarball://root/attachments/some-uuid/ticket6859/trac_6859.patch) by myurko created at 2009-09-02 01:42:57



---

archive/issue_comments_056560.json:
```json
{
    "body": "Would it be possible to add to the docstrings the definition of what these graphs should be ?\n\nNathann",
    "created_at": "2009-09-06T09:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56560",
    "user": "ncohen"
}
```

Would it be possible to add to the docstrings the definition of what these graphs should be ?

Nathann



---

archive/issue_comments_056561.json:
```json
{
    "body": "Sure. I'll add definitions.",
    "created_at": "2009-09-06T13:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56561",
    "user": "myurko"
}
```

Sure. I'll add definitions.



---

archive/issue_comments_056562.json:
```json
{
    "body": "I do not know if you are aware of it ( I was not until very recently ) but the docstrings are used to generate a very complete documentation accessible through there :\n\nhttp://www.sagemath.org/doc/reference/graphs.html\n\nThis also means that you can use LaTeX in your description if you deem it necessary, and that the formula will be automatically translated into beautiful equations on this page ;-)\n\nNathann",
    "created_at": "2009-09-06T14:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56562",
    "user": "ncohen"
}
```

I do not know if you are aware of it ( I was not until very recently ) but the docstrings are used to generate a very complete documentation accessible through there :

http://www.sagemath.org/doc/reference/graphs.html

This also means that you can use LaTeX in your description if you deem it necessary, and that the formula will be automatically translated into beautiful equations on this page ;-)

Nathann



---

archive/issue_comments_056563.json:
```json
{
    "body": "Well, I knew that you can use Latex in docstrings, but I tried not to use it since it is hard to read when introspecting.",
    "created_at": "2009-09-06T14:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56563",
    "user": "myurko"
}
```

Well, I knew that you can use Latex in docstrings, but I tried not to use it since it is hard to read when introspecting.



---

archive/issue_comments_056564.json:
```json
{
    "body": "Attachment [trac_6859_definitions.patch](tarball://root/attachments/some-uuid/ticket6859/trac_6859_definitions.patch) by myurko created at 2009-09-06 15:20:29\n\nAdds definitions of graphs to docstrings",
    "created_at": "2009-09-06T15:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56564",
    "user": "myurko"
}
```

Attachment [trac_6859_definitions.patch](tarball://root/attachments/some-uuid/ticket6859/trac_6859_definitions.patch) by myurko created at 2009-09-06 15:20:29

Adds definitions of graphs to docstrings



---

archive/issue_comments_056565.json:
```json
{
    "body": "Very nice.\n\nI'm attaching a patch which optimizes some of the code to use more python things (like swapping), plus fixes a few typos.  I think someone needs to review my patch.",
    "created_at": "2009-09-22T16:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56565",
    "user": "jason"
}
```

Very nice.

I'm attaching a patch which optimizes some of the code to use more python things (like swapping), plus fixes a few typos.  I think someone needs to review my patch.



---

archive/issue_comments_056566.json:
```json
{
    "body": "Attachment [trac-6859-optimize.patch](tarball://root/attachments/some-uuid/ticket6859/trac-6859-optimize.patch) by jason created at 2009-09-22 16:46:11\n\napply on top of previous patches",
    "created_at": "2009-09-22T16:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56566",
    "user": "jason"
}
```

Attachment [trac-6859-optimize.patch](tarball://root/attachments/some-uuid/ticket6859/trac-6859-optimize.patch) by jason created at 2009-09-22 16:46:11

apply on top of previous patches



---

archive/issue_comments_056567.json:
```json
{
    "body": "I obviously can't review the patch, but the swapping certainly looks better. Coding too long in java has made forget some of the nice python idioms.",
    "created_at": "2009-09-22T17:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56567",
    "user": "myurko"
}
```

I obviously can't review the patch, but the swapping certainly looks better. Coding too long in java has made forget some of the nice python idioms.



---

archive/issue_comments_056568.json:
```json
{
    "body": "Okay, positive review for your patch.\n\nYou can review my changes (just make sure that you still get the same graphs).  If you okay my changes, change this ticket to \"positive review\".",
    "created_at": "2009-09-22T19:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56568",
    "user": "jason"
}
```

Okay, positive review for your patch.

You can review my changes (just make sure that you still get the same graphs).  If you okay my changes, change this ticket to "positive review".



---

archive/issue_comments_056569.json:
```json
{
    "body": "All the graphs except the n,k star graph worked still. However, it was just a one line fix to keep the v[0] = tmp_bit line inside the for loop (otherwise all the vertices become looped). I've uploaded a one line patch to fix it.",
    "created_at": "2009-09-22T21:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56569",
    "user": "myurko"
}
```

All the graphs except the n,k star graph worked still. However, it was just a one line fix to keep the v[0] = tmp_bit line inside the for loop (otherwise all the vertices become looped). I've uploaded a one line patch to fix it.



---

archive/issue_comments_056570.json:
```json
{
    "body": "Attachment [trac-6859-optimize-fix.patch](tarball://root/attachments/some-uuid/ticket6859/trac-6859-optimize-fix.patch) by myurko created at 2009-09-22 21:38:05",
    "created_at": "2009-09-22T21:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56570",
    "user": "myurko"
}
```

Attachment [trac-6859-optimize-fix.patch](tarball://root/attachments/some-uuid/ticket6859/trac-6859-optimize-fix.patch) by myurko created at 2009-09-22 21:38:05



---

archive/issue_comments_056571.json:
```json
{
    "body": "ah, right.  Okay, then, positive review.",
    "created_at": "2009-09-22T22:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56571",
    "user": "jason"
}
```

ah, right.  Okay, then, positive review.



---

archive/issue_comments_056572.json:
```json
{
    "body": "The patch `trac_6859-ascii-chars.patch` uses only ASCII characters for quotation marks and long dashes. Without it, merging `trac_6859.patch` and building the reference manual would result in the following error:\n\n```\nreading sources... sage/graphs/graph_generators /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/Sphinx-0.5.1-py2.6.egg/sphinx/environment.py:543: DeprecationWarning: BaseException.message has been deprecated as of Python 2.6\n  raise SphinxError(err.message)\nSphinx error:\n```\n",
    "created_at": "2009-09-24T10:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56572",
    "user": "mvngu"
}
```

The patch `trac_6859-ascii-chars.patch` uses only ASCII characters for quotation marks and long dashes. Without it, merging `trac_6859.patch` and building the reference manual would result in the following error:

```
reading sources... sage/graphs/graph_generators /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/Sphinx-0.5.1-py2.6.egg/sphinx/environment.py:543: DeprecationWarning: BaseException.message has been deprecated as of Python 2.6
  raise SphinxError(err.message)
Sphinx error:
```




---

archive/issue_comments_056573.json:
```json
{
    "body": "use ASCII characters for quotation marks and long dashes",
    "created_at": "2009-09-24T10:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56573",
    "user": "mvngu"
}
```

use ASCII characters for quotation marks and long dashes



---

archive/issue_comments_056574.json:
```json
{
    "body": "Attachment [trac_6859-formatting-issues.patch](tarball://root/attachments/some-uuid/ticket6859/trac_6859-formatting-issues.patch) by mvngu created at 2009-09-24 10:24:47\n\nproper formatting of lists",
    "created_at": "2009-09-24T10:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56574",
    "user": "mvngu"
}
```

Attachment [trac_6859-formatting-issues.patch](tarball://root/attachments/some-uuid/ticket6859/trac_6859-formatting-issues.patch) by mvngu created at 2009-09-24 10:24:47

proper formatting of lists



---

archive/issue_comments_056575.json:
```json
{
    "body": "The patch `trac_6859-formatting-issues.patch` fixes formatting of lists. Without it, I get the following warnings when building the reference manual:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.HyperStarGraph:22: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.NKStarGraph:25: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.NStarGraph:19: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n```\n",
    "created_at": "2009-09-24T10:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56575",
    "user": "mvngu"
}
```

The patch `trac_6859-formatting-issues.patch` fixes formatting of lists. Without it, I get the following warnings when building the reference manual:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.HyperStarGraph:22: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.NKStarGraph:25: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python2.6/site-packages/sage/graphs/graph_generators.py:docstring of sage.graphs.graph_generators.GraphGenerators.NStarGraph:19: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```




---

archive/issue_comments_056576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T10:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56576",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056577.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6859.patch`\n2. `trac_6859-ascii-chars.patch`\n3. `trac_6859_definitions.patch`\n4. `trac-6859-optimize.patch`\n5. `trac-6859-optimize-fix.patch`\n6. `trac_6859-formatting-issues.patch`",
    "created_at": "2009-09-24T10:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56577",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6859.patch`
2. `trac_6859-ascii-chars.patch`
3. `trac_6859_definitions.patch`
4. `trac-6859-optimize.patch`
5. `trac-6859-optimize-fix.patch`
6. `trac_6859-formatting-issues.patch`



---

archive/issue_comments_056578.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6859#issuecomment-56578",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
