# Issue 7018: Looking for trees with search_doc("tree") is a bad idea

archive/issues_007018.json:
```json
{
    "body": "Assignee: tba\n\nCC:  ddrake\n\nI understand the word \"tree\" may be the only way to get this result, the other words being less common or not mathematics-related... Even though :\n\n```\nsage: search_doc(\"tree\")\nhtml/en/installation/source.html:226:tree. This can take close to an hour on some machines. Depending on the\nhtml/en/installation/source.html:246:build tree to <tt class=\"docutils literal\"><span class=\"pre\">/usr/local</span></tt>. You might also copy the <tt class=\"docutils literal\"><span class=\"pre\">sage-*/sage</span>html/en/installation/index.html:59:<li class=\"toctree-l1\"><a class=\"reference external\" href=\"introduction.html\">Introduction</a></li>\nhtml/en/installation/index.html:62:<li class=\"toctree-l1\"><a class=\"reference external\" href=\"binary.html\">Pre-built Binary Install</a><ul>\nhtml/en/installation/index.html:63:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"binary.html#linux-and-os-x\">Linux and OS X</a></li>\nhtml/en/installation/index.html:64:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"binary.html#microsoft-windows\">Microsoft Windows</a></li>\nhtml/en/installation/index.html:69:<li class=\"toctree-l1\"><a class=\"reference external\" href=\"source.html\">Install from Source Code</a><ul>\nhtml/en/installation/index.html:70:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"source.html#steps-to-install-from-source\">Steps to Install from Source</a></li>\nhtml/en/installation/index.html:71:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"source.html#installation-in-a-multiuser-environment\">Installation in a Multiuser Environment</a></li>\nhtml/en/installation/index.html:72:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"source.html#special-notes\">Special Notes</a></li>\nhtml/en/installation/index.html:77:<li class=\"toctree-l1\"><a class=\"reference external\" href=\"icon.html\">Desktop icon</a></li>\nhtml/en/installation/index.html:80:<li class=\"toctree-l1\"><a class=\"reference external\" href=\"documentation.html\">The Documentation</a></li>\nhtml/en/numerical_sage/index.html:72:<li class=\"toctree-l1\"><a class=\"reference external\" href=\"numerical_tools.html\">Numerical Tools</a><ul>\nhtml/en/numerical_sage/index.html:73:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"numpy.html\">NumPy</a></li>\nhtml/en/numerical_sage/index.html:74:<li class=\"toctree-l2\"><a class=\"reference external\" href=\"scipy.html\">SciPy</a></li>\n\n```\n\nand much more below, as class=doctree is in all the lines... ;-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7018\n\n",
    "created_at": "2009-09-26T07:19:47Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Looking for trees with search_doc(\"tree\") is a bad idea",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7018",
    "user": "ncohen"
}
```
Assignee: tba

CC:  ddrake

I understand the word "tree" may be the only way to get this result, the other words being less common or not mathematics-related... Even though :

```
sage: search_doc("tree")
html/en/installation/source.html:226:tree. This can take close to an hour on some machines. Depending on the
html/en/installation/source.html:246:build tree to <tt class="docutils literal"><span class="pre">/usr/local</span></tt>. You might also copy the <tt class="docutils literal"><span class="pre">sage-*/sage</span>html/en/installation/index.html:59:<li class="toctree-l1"><a class="reference external" href="introduction.html">Introduction</a></li>
html/en/installation/index.html:62:<li class="toctree-l1"><a class="reference external" href="binary.html">Pre-built Binary Install</a><ul>
html/en/installation/index.html:63:<li class="toctree-l2"><a class="reference external" href="binary.html#linux-and-os-x">Linux and OS X</a></li>
html/en/installation/index.html:64:<li class="toctree-l2"><a class="reference external" href="binary.html#microsoft-windows">Microsoft Windows</a></li>
html/en/installation/index.html:69:<li class="toctree-l1"><a class="reference external" href="source.html">Install from Source Code</a><ul>
html/en/installation/index.html:70:<li class="toctree-l2"><a class="reference external" href="source.html#steps-to-install-from-source">Steps to Install from Source</a></li>
html/en/installation/index.html:71:<li class="toctree-l2"><a class="reference external" href="source.html#installation-in-a-multiuser-environment">Installation in a Multiuser Environment</a></li>
html/en/installation/index.html:72:<li class="toctree-l2"><a class="reference external" href="source.html#special-notes">Special Notes</a></li>
html/en/installation/index.html:77:<li class="toctree-l1"><a class="reference external" href="icon.html">Desktop icon</a></li>
html/en/installation/index.html:80:<li class="toctree-l1"><a class="reference external" href="documentation.html">The Documentation</a></li>
html/en/numerical_sage/index.html:72:<li class="toctree-l1"><a class="reference external" href="numerical_tools.html">Numerical Tools</a><ul>
html/en/numerical_sage/index.html:73:<li class="toctree-l2"><a class="reference external" href="numpy.html">NumPy</a></li>
html/en/numerical_sage/index.html:74:<li class="toctree-l2"><a class="reference external" href="scipy.html">SciPy</a></li>

```

and much more below, as class=doctree is in all the lines... ;-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7018





---

archive/issue_comments_058099.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T02:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7018#issuecomment-58099",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058100.json:
```json
{
    "body": "Here is a patch.  This implements two new keywords for searching, one of which addresses the issue in this ticket.  These work for `search_src`, `search_doc`, and `search_def`.\n\n- You can now do `search_doc('tree', whole_word=True)`, and it will look for 'tree' as a whole word, not returning matches for 'toctree' or 'trees'.\n\n- You can now do `search_src('TreE', ignore_case=True)`, and it will return matches for 'TREE', 'Tree', 'tree', etc., completely ignoring case.  (By default, all searches continue to be case-sensitive, so `search_src('TreE')` returns no matches.)",
    "created_at": "2010-01-20T02:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7018#issuecomment-58100",
    "user": "jhpalmieri"
}
```

Here is a patch.  This implements two new keywords for searching, one of which addresses the issue in this ticket.  These work for `search_src`, `search_doc`, and `search_def`.

- You can now do `search_doc('tree', whole_word=True)`, and it will look for 'tree' as a whole word, not returning matches for 'toctree' or 'trees'.

- You can now do `search_src('TreE', ignore_case=True)`, and it will return matches for 'TREE', 'Tree', 'tree', etc., completely ignoring case.  (By default, all searches continue to be case-sensitive, so `search_src('TreE')` returns no matches.)



---

archive/issue_comments_058101.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-21T00:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7018#issuecomment-58101",
    "user": "ddrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058102.json:
```json
{
    "body": "Attachment [trac_7018-search.patch](tarball://root/attachments/some-uuid/ticket7018/trac_7018-search.patch) by ddrake created at 2010-01-21 00:09:45\n\nThis looks good, works as advertised, and passes all doctests. Positive review.",
    "created_at": "2010-01-21T00:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7018#issuecomment-58102",
    "user": "ddrake"
}
```

Attachment [trac_7018-search.patch](tarball://root/attachments/some-uuid/ticket7018/trac_7018-search.patch) by ddrake created at 2010-01-21 00:09:45

This looks good, works as advertised, and passes all doctests. Positive review.



---

archive/issue_comments_058103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T15:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7018#issuecomment-58103",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_058104.json:
```json
{
    "body": "See also discussion on sage-combinat-devel: http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/8560fa9a2eda7712",
    "created_at": "2010-04-18T08:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7018#issuecomment-58104",
    "user": "nthiery"
}
```

See also discussion on sage-combinat-devel: http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/8560fa9a2eda7712
