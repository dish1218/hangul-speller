# 한글 맞춤법 교정기 (Hangul Speller)

한글 어문 규정(한글 맞춤법, 표준어 규정, 외래어 표기법 등)에 기반한 맞춤법 교정 데스크톱 애플리케이션.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Structure

| Path | Role |
|---|---|
| `main.py` | Entrypoint, PyQt5 GUI |
| `hangul_speller/` | Core engine package |
| `hangul_speller/rules/` | 규칙 모듈 (맞춤법/띄어쓰기/문장부호 등) |
| `data/` | 규정 데이터 사전 |
| `tests/` | 테스트 |
