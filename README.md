# Orb Descentralizada (Raspberry Pi)

Sistema open-source para prototipar uma **Orb** de verificação local usando Raspberry Pi (cam + IA local),
com foco em **privacidade**, **multilíngue** (pt-BR/en/es) e **modularidade**.

## Objetivos
- Captura de imagem local (sem upload automático).
- Processamento em borda: detecção/qualidade da imagem e checagens simples.
- API local (HTTP) para integrar com dapps, dashboards e outros serviços.
- Modo *kiosk* para fluxo de uso assistido.

## Hardware sugerido
- Raspberry Pi 5 (ou 4) + câmera oficial (ou USB UVC).
- Módulo de IA opcional (Hailo/Coral USB) – plug-and-play.
- Tela pequena HDMI (5–7") para *kiosk*.
- Botão físico (GPIO) para iniciar fluxo.

## Estrutura
```text
src/
  app/
    __init__.py
    server.py        # API FastAPI local
    camera.py        # wrapper de câmera
    pipeline.py      # orquestra o fluxo
  models/
    README.md
docs/
  arquitetura.md
  api.md
examples/
  curl_check.sh
```

## Como rodar
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.app.server:app --host 0.0.0.0 --port 8080 --reload
```

## Segurança & Privacidade
- Processamento local por padrão.
- Logs mínimos e anonimizados.
- Sem datas antigas exibidas em UI.

## Licença
MIT
