TEST_COMMIT_FILE = test_commit.txt


create_commit_file:
	echo "this is a long string to use as a test commit message. \
	This should be broken up into multiple lines with a gap after \
	the first. Unless you have reall long first line settings \
	that is..." > $(TEST_COMMIT_FILE)

run:
	python3 prepare-commit-msg.py $(TEST_COMMIT_FILE)

test:
	make create_commit_file
	make run
