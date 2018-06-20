main:
	python3 src/$@.py

cliff_walking:
	python3 src/$@.py

maze:
	python3 src/$@.py

setup-linux:
	rm src/MalmoPython.so
	ln -s ../lib/x86-64_linux/MalmoPython.so src/MalmoPython.so

setup-macos:
	rm src/MalmoPython.so
	ln -s ../lib/x86-64_macos/MalmoPython.so src/MalmoPython.so
