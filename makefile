codegen:
	cp src/* bin/
	python -m py_compile bin/*.py
	mv bin/codegen.py bin/codegen
	chmod +x bin/codegen
	bin/codegen test/assignment.py   2>/dev/null > /dev/null # to create parsetable once
	rm -f parser.out
	mv parsetab.py bin/parsetab.py
	
clean:
	rm -f -rf bin/*
	rm -f parse*
	rm -f dump
