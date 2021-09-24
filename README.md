# NYU Compiler Construction CSCI-GA.2130/Spring 2021: Programming Assignment 1

This assignment is adapted from https://github.com/cs164berkeley/pa1-chocopy-parser/ with the authors' permission.

See the PA1 document on Piazza for a detailed specification.

## Quickstart

Run the following commands to generate and compile your parser and run the tests:
```
mvn clean package
java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
  --pass=s --test --dir src/test/data/pa1/sample/
```

`--pass=s` uses your parser (`s` for `student`), and with the starter code, only one test should pass.
`--pass=r` uses the reference parser (`r` for `reference`), which should pass all tests.

In addition to running in test mode with `--test`, you can also observe the actual output
of your (or reference) parser with:
```
java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
  --pass=s src/test/data/pa1/sample/expr_plus.py
```
