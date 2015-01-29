This is the repository for
Scala Compiler, the Scala to MIPS compiler hosted at [IITK](https://git.cse.iitk.ac.in/smanocha/compilersproject)  and [Github](https://github.com/sid17/CompilersProject)

## Contributors
* [Siddhant Manocha](http://home.iitk.ac.in/~smanocha)
* [Satvik Gupta](http://home.iitk.ac.in/~satvikg)
* [Saurav Shekhar](http://home.iitk.ac.in/~sshekh)

## Credits

This project is done as a part of CS335 course at IIT Kanpur under the guidance of 
[Dr.Subhajit Roy](http://web.cse.iitk.ac.in/users/subhajit/).

## Description

### LEXER

The src folder consists of the file named lexer.py which consists of the lexer code. It includes the files : tokensDefination.py , regexDefination.py , printLexerOutput.py defined under include folder.

* tokensDefination.py : Contains the defination of various tokens used in scala 
* regexDefination.py : Defines the regex for various tokens and literals
* printLexerOutput.py : parses the output from the lexer and prints them to the standard output

## Compilation Instructions

The test folder consists of various files namely HelloWorld.scala, etc. The given files can be run for output as 

python src/lexer.py test/HelloWorld.scala

To print the output to a file in output folder, run

 python src/lexer.py test/HelloWorld.scala > output/parsed.scala

 This sends the output to the file parsed.scala under the output folder

