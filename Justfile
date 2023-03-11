package: clean
	zip -r AWFS3.alfredworkflow . --exclude=.git/** 

deps:
	python3 -m pip install boto3 -t lib
	brew install pngpaste

clean:
	rm -f AWFS3.alfredworkflow
	rm -rf lib