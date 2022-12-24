# Issue 9731: Export/Import of GML/Graphml/Yaml files through NetworkX

archive/issues_009731.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  bedwards\n\nThanks to Ben's update of NetworkX, these methods can now be used through Sage... This patch updates the constructor method for Graph, and adds write_* methods to export graphs.\n\nThis patch requires #9567\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9731\n\n",
    "created_at": "2010-08-12T03:48:58Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Export/Import of GML/Graphml/Yaml files through NetworkX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9731",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  bedwards

Thanks to Ben's update of NetworkX, these methods can now be used through Sage... This patch updates the constructor method for Graph, and adds write_* methods to export graphs.

This patch requires #9567

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9731





---

archive/issue_comments_095110.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-12T03:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9731#issuecomment-95110",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095111.json:
```json
{
    "body": "Attachment [trac_9731.patch](tarball://root/attachments/some-uuid/ticket9731/trac_9731.patch) by ncohen created at 2010-08-12 03:50:55",
    "created_at": "2010-08-12T03:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9731#issuecomment-95111",
    "user": "ncohen"
}
```

Attachment [trac_9731.patch](tarball://root/attachments/some-uuid/ticket9731/trac_9731.patch) by ncohen created at 2010-08-12 03:50:55



---

archive/issue_comments_095112.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-26T17:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9731#issuecomment-95112",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095113.json:
```json
{
    "body": "\n```\nsage -t -long ./sage/graphs/generic_graph.py\n**********************************************************************\nFile \"/home/rlmill/sage-4.6.1.alpha2/devel/sage-main/sage/graphs/generic_graph.py\", line 14430:\n    sage: g.is_isomorphic(h)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/rlmill/sage-4.6.1.alpha2/devel/sage-main/sage/graphs/generic_graph.py\", line 14444:\n    sage: g.write_yaml(SAGE_TMP+\"/g.yml\")\nException raised:\n    Traceback (most recent call last):\n      File \"/home/rlmill/sage-4.6.1.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/rlmill/sage-4.6.1.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/rlmill/sage-4.6.1.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_217[3]>\", line 1, in <module>\n        g.write_yaml(SAGE_TMP+\"/g.yml\")###line 14444:\n    sage: g.write_yaml(SAGE_TMP+\"/g.yml\")\n      File \"/home/rlmill/sage-4.6.1.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 14451, in write_yaml\n        networkx.write_yaml(self.networkx_graph(copy = False), filename)\n      File \"/home/rlmill/sage-4.6.1.alpha2/local/lib/python2.6/networkx/readwrite/nx_yaml.py\", line 40, in write_yaml\n        \"write_yaml() requires PyYAML: http://pyyaml.org/ \"\n    ImportError: write_yaml() requires PyYAML: http://pyyaml.org/\n**********************************************************************\n```\n\n\nThere are more, but...",
    "created_at": "2010-11-26T17:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9731#issuecomment-95113",
    "user": "rlm"
}
```


```
sage -t -long ./sage/graphs/generic_graph.py
**********************************************************************
File "/home/rlmill/sage-4.6.1.alpha2/devel/sage-main/sage/graphs/generic_graph.py", line 14430:
    sage: g.is_isomorphic(h)
Expected:
    True
Got:
    False
**********************************************************************
File "/home/rlmill/sage-4.6.1.alpha2/devel/sage-main/sage/graphs/generic_graph.py", line 14444:
    sage: g.write_yaml(SAGE_TMP+"/g.yml")
Exception raised:
    Traceback (most recent call last):
      File "/home/rlmill/sage-4.6.1.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6.1.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6.1.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_217[3]>", line 1, in <module>
        g.write_yaml(SAGE_TMP+"/g.yml")###line 14444:
    sage: g.write_yaml(SAGE_TMP+"/g.yml")
      File "/home/rlmill/sage-4.6.1.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 14451, in write_yaml
        networkx.write_yaml(self.networkx_graph(copy = False), filename)
      File "/home/rlmill/sage-4.6.1.alpha2/local/lib/python2.6/networkx/readwrite/nx_yaml.py", line 40, in write_yaml
        "write_yaml() requires PyYAML: http://pyyaml.org/ "
    ImportError: write_yaml() requires PyYAML: http://pyyaml.org/
**********************************************************************
```


There are more, but...



---

archive/issue_comments_095114.json:
```json
{
    "body": "By the way, those showed up with sage-4.6.1.alpha2 plus the patches here, if that is relevant.",
    "created_at": "2010-11-26T17:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9731#issuecomment-95114",
    "user": "rlm"
}
```

By the way, those showed up with sage-4.6.1.alpha2 plus the patches here, if that is relevant.



---

archive/issue_comments_095115.json:
```json
{
    "body": "Not only that, but once the yaml export is removed the graphml docstring does not pass because of stupid edge labels set by default (if you write a file without any edge label, the one you get has its endpoints as labels) with weird 'u' before the vertices' name... O_o\n\nNathann",
    "created_at": "2010-11-29T19:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9731#issuecomment-95115",
    "user": "ncohen"
}
```

Not only that, but once the yaml export is removed the graphml docstring does not pass because of stupid edge labels set by default (if you write a file without any edge label, the one you get has its endpoints as labels) with weird 'u' before the vertices' name... O_o

Nathann
