build:
	BEEMO_CONFIG=config.yml beemo

serve:
	python -m http.server -d www 8000 &