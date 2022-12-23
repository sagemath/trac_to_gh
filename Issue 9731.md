# Issue 9731: Export/Import of GML/Graphml/Yaml files through NetworkX

Issue created by migration from https://trac.sagemath.org/ticket/9731

Original creator: ncohen

Original creation time: 2010-08-12 03:48:58

Assignee: jason, ncohen, rlm

CC:  bedwards

Thanks to Ben's update of NetworkX, these methods can now be used through Sage... This patch updates the constructor method for Graph, and adds write_* methods to export graphs.

This patch requires #9567

Nathann


---

Comment by ncohen created at 2010-08-12 03:50:55

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2010-11-26 17:11:55

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-11-26 17:11:55


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

Comment by rlm created at 2010-11-26 17:12:28

By the way, those showed up with sage-4.6.1.alpha2 plus the patches here, if that is relevant.


---

Comment by ncohen created at 2010-11-29 19:15:49

Not only that, but once the yaml export is removed the graphml docstring does not pass because of stupid edge labels set by default (if you write a file without any edge label, the one you get has its endpoints as labels) with weird 'u' before the vertices' name... O_o

Nathann
