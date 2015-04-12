all:
	cp src/lexerP1.py bin/lexer.py	
	cp src/parser.py bin/irgen.py
	cp src/scalalex.py bin/scalalex.py
	python -m py_compile bin/lexer.py
	python -m py_compile bin/irgen.py
	mv bin/lexer.pyc bin/lexer
	mv bin/irgen.pyc bin/irgen
	chmod -R 777 bin/
clean:
	rm -rf bin/*
	rm test1.dot
