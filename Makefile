# Makefile para PCVitalBoost

.PHONY: help install test clean run build-windows build-linux build-macos build-android build-ios

help:
	@echo "Comandos disponíveis:"
	@echo "  make install        - Instala dependências"
	@echo "  make test          - Executa testes"
	@echo "  make run           - Executa o aplicativo"
	@echo "  make clean         - Remove arquivos temporários"
	@echo "  make build-windows - Cria executável para Windows"
	@echo "  make build-linux   - Cria executável para Linux"
	@echo "  make build-macos   - Cria executável para macOS"
	@echo "  make build-android - Cria APK para Android"

install:
	pip install -r requirements.txt

test:
	python -m unittest discover tests -v

run:
	python src/main.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
	rm -rf build/ dist/ *.egg-info .pytest_cache/ .buildozer/ bin/

build-windows:
	pip install pyinstaller
	pyinstaller PCVitalBoost.spec

build-linux:
	pip install pyinstaller
	pyinstaller PCVitalBoost.spec

build-macos:
	pip install pyinstaller
	pyinstaller PCVitalBoost.spec

build-android:
	pip install buildozer
	buildozer android debug

build-ios:
	@echo "Build para iOS requer macOS com Xcode"
	@echo "Execute: buildozer ios debug"
