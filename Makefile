venv: requirements.txt
	rm -rf venv
	virtualenv -p python3.6 venv
	venv/bin/pip install -r requirements.txt

.PHONY: test
test: venv
	venv/bin/pytest tests

.PHONY: deploy
deploy: clean
	zip -r deploy.zip spare_the_air/ lambda_function.py
	aws lambda update-function-code --region us-west-2 --function-name spare_the_air --zip-file 'fileb://deploy.zip'

.PHONY: clean
clean:
	rm -rf venv
	rm -f deploy.zip
