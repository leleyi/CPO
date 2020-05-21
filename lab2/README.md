## Computer Process Organization
### lab2 - Interpreter

#### basic info

* **laboratory work number** : PLMM 5 
* **variant description** :  Regular expression
* **list of group members** : Liu Jun ; Wang Xin Yue

#### contribution

* contribution summary for each group member (should be checkable by git log and git blame);
  * Liu Jun's main contribution is in the grammatical analysis and the establishment of NFA, 
  * Wang Xin Yue's main contribution is in the lexical analysis and testing
  * Together to  Complete readme.md

#### explanation 

Regular expression.

1. Support special characters: \, ^, ., $, *, +, [ ], [ ^  ], { }. 
2. Support functions: match, sub.
3. Visualization as a ﬁnite state machine (state diagram or table).

We use the NFA way to write our regular expression state machine, first perform the lexical analysis of the expression, then use the bottom-up method for grammatical analysis, and then establish NFA, and finally used to match the string.

#### work demonstration 

- work demonstration (how to use developed software, how to test it), should be repeatable by an instructor by given command-line
  examples;

  - output

  ![output](https://github.com/leleyi/CPO/blob/master/lab2/fig/1.png)

  - visualization using GraphViz

  ![visualization](https://github.com/leleyi/CPO/blob/master/lab2/fig/2.jpg)

#### conclusion

The regular expression can be executed by constructing an equivalent NFA and then executing NFA to match the input string.

- NFA means Nondeterministic Finite Automaton

  The working process of the finite state machine is the process of automatically performing state transition from the starting state according to different inputs.

- From regular expression to NFA

  We use the Thompson algorithm to convert regular expressions to NFA. It is not the most efficient algorithm, but it is practical and easy to understand.