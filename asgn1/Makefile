all:
	cp src/lexerP1.py bin/lexer.py	
	cp src/parser.py bin/parser.py
	cp src/scalalex.py bin/scalalex.py
	python -m py_compile bin/lexer.py
	python -m py_compile bin/parser.py
	mv bin/lexer.pyc bin/lexer
	mv bin/parser.pyc bin/parser
	chmod -R 777 bin/
clean:
	rm -rf bin/*
	rm test1.dot
