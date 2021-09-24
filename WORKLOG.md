#### Team: 
Jinghong Hu, Yu-hsuan Shih, Chia-hao Wu, Xinyao Zhang

#### Acknowledgements: 
- In pa1, our four team members implment each one's implemention of the parser and the lexer. Then, we held a meeting to do the code review to evaluate these implementations to choose which implementation we're going to use.
- Jinghong Hu: implemented parser/lexer, improved/fixed the adopted version, write the `good.py` file.
- Yu-hsuan Shih: implemented parser/lexer (adopted), provdied 2 extra tests.
- Chia-hao Wu: organized weekly meetings, implemented parser/lexer, improved/fixed the adopted version, provide 40 extra tests, write the `bad.py` file
- Xinyao Zhang: implemented parser/lexer, improved/fixed the adopted version.

#### Indentation:

For indentation, we handle it by introducing state `INDENTSTATE`. There are two situation that the lexer will go in to the states:
1. Every time a `NEWLINE` token is seen (`line: 135, 136`)
2. An indentation happens in the first line of the program (`line: 238`)

After entering the INDENTSTATE state, the first thing we do is calculating the indentation level (called `col` in the code). The indentation can contain either (1) whitespaces or (2) tabs, where we replace it by whitespaces such that the up-until-now indentation level is a multiple of 8. (`line: 243-255`)


Next, we decide whether to output an `INDENT` or `DEDENT` token or do nothing basing on the current line’s indentation level (`col`). This is done by comparing `col` with variables that we used to store the indentation information in the program (`line: 95, 96`):
- `this.indent`: an integer storing current indent level, start from 0.
- `this.indents`: an object of Java integer stack class storing indent levels that have been seen so far (exclude the latest one which is stored in "indent").

We wrote two auxiliary functions to do the comparison (`line: 97-112`):
- `boolean addIndent(int col)`: if an indentation should happen (i.e. col is greater this.indent), returns TRUE and updates the variable this.indent with col and push this.indent to the this.indents stack.
- `boolean rmIndent(int col)`: if a dedentation should happen (i.e. col is less than this.indent), returns TRUE and pop out a value in the stack this.indents and update this.indent with the value.

The action of the lexer is then determined by the return value of the two auxiliary functions, using the following procedure (`line: 256-285`): 

We start by **calling `addIndent`**. If the return value of addIndent is `TRUE`, then an `INDENT` token is returned by the lexer and we return back to the YYINITIAL state. If not, then we **call `rmIndent`**. If the return value of rmIndent is `FALSE`, there is no action needed. We return back to the `YYINITIAL` state; If it is `TRUE`, before outputting the `DEDENT` token, we **check whether the current line’s indentation level (`col`) is valid** (the indentation after DEDENT should be one of the previous indentation lengths). If it is invalid, we return an `UNRECOGNIZED` token instead. Note that since there could be a line that requires more than one dendentations, we **push back the input whitespaces characters whenever the return value of rmIndent is TRUE** so that the described procedure can happen multiple times until the correct number of DEDENT tokens are returned. 

Special case: EOF dedentation (`line: 304-310`)

The parser requires a correct number of (INDENT, DEDENT) pairs to parse the grammar correctly. We therefore output the `DEDENT` tokens at the end of the program to match the number of indentations. This is achieved by modifying the end of file variable `zzAtEOF`, which allows as to reach the states multiple times and output the correct number of DEDENT tokens.

#### Challenges
- *Strings output extra backslashes in the JSON AST output*
The JSON will replace the “\” by “\\” automatically in strings, which causes extra backslashes in our output file, so we do some modifications of our STRING token. We simply go through each character in the string. If we find a substring “\\n”, “\\t”, “\\””, or “\\\\”, we replace them by “\n”, “\t”, “\””, or “\\”. 

- *Overflow integer handling.*
The token matched IntegerLiteral regular expression, which only contains number digits, may be an overflow integer. We try to  convert the token to integer first by the method Integer.parseInt(). If we catch a NumberFormatException, which is caused by overflow in our case, we mark the token as UNRECOGNIZED token.

- *Shift/Reduce Conflict.*
When finished writing up all grammar rules for CUP parser, the compiler complained that multiple shift/reduce conflicts are found so parser generation is aborted. The reason is that two or more grammar rules can be used for parsing the same expression but different results. There is no straightforward solution at first glance since multiple rules are involved and we should choose to rule out the redundant one. We merged some rules in binary_expr (in cup file) to avoid introducing ambiguity and more states to do that.

- In order to convert an if-elif-else statement into a data structure that each elif statement or else statement will be put into the else body of the previous statement. One way to cope with that is using left associativity, finding the innermost IfStmt and plugging the elif or else statements into its else body. The other way is letting the IF, ELIF and ELSE terminals to be right associative and dealing with the right most first. Finally, we choose the second way, setting IF, ELIF and ELSE terminals to be right associative because this way is more straightforward.

#### Improvements

- For error recovery, we implement our parser to be able to recover errors parsing the parameters of a function definition or the arguments of a function call expression or method call expression and continue parsing the rest of the arguments.

- We add more test cases in the /src/tes1/data/pa1/AdditionalTestCase by extracting test scenarios from the ChocoPy language reference to make sure we cover all syntax scenarios.

- We add a new feature to detect a return syntax error, “It is illegal for a return statement to occur at the top level outside a function or method body.”.
