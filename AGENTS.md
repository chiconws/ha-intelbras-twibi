# Agent Notes: Intelbras Twibi

Language: README in **pt-BR**; code, logs and `strings.json` in English; translations en + pt-BR.

## Overview

Local polling (`iot_class: local_polling`) integration for Intelbras Twibi mesh routers. It talks
to the primary unit's undocumented `/goform` HTTP API with the admin password. One config entry
per mesh (`single_config_entry`), unique ID = primary unit serial.

## Code structure

All code in `custom_components/intelbras_twibi/`.

- `api.py`: `TwibiClient` and the dataclasses `RouterData`, `Node`, `Client`, `GuestNetwork`. No HA imports.
- `coordinator.py`: `TwibiCoordinator` polls every 30 s; maps `TwibiAuthError` to reauth, other errors to `UpdateFailed`. `TwibiConfigEntry` type.
- `entity.py`: `TwibiEntity` base, one HA device per mesh node; `_async_command` wraps router commands.
- `config_flow.py`: user, reauth, reconfigure; options pick tracked clients and the Wi-Fi-only filter.
- Platforms: `binary_sensor` (WAN), `sensor`, `light` (node LED), `switch` (guest Wi-Fi, UPnP), `button` (reboot), `device_tracker`.
- `diagnostics.py`: raw router reply with passwords, serials and client IPs redacted.

## Key concepts

- Login: POST `/goform/set` `{"login": {"pwd": md5(password), "timestamp": ms}}`; `errcode "1"` = wrong password.
- Reads: GET `/goform/get?module_id=a,b`. Core modules in one request, optional ones (`wan_info`, `guest_info`, `upnp_info`) one per request, skipped on error.
- Session: an HTML reply means the session expired → log in again once. Firmware 1.1.11+ (or a `MESH_user` cookie) needs the cookie sent as an explicit header, because HA's shared session drops cookies from IP hosts.
- Commands: POST `/goform/set` `{name: {..., "timestamp": "ms"}}`; non-zero `errcode` → `TwibiError` → `HomeAssistantError`.
- Trackers: options list wins; empty list = every client seen (plus ones registered earlier). HA disables trackers for unknown MACs by default; chosen ones are enabled.

## Local validation (before push)

`.venv/bin/prek install` once per clone; the git hook then runs ruff (lint + format), codespell, yamllint, prettier, zizmor, markdownlint, mypy and Pyright. By hand:

```bash
SKIP=no-commit-to-branch .venv/bin/prek run --all-files --hook-stage manual
.venv/bin/coverage run -m pytest -q && .venv/bin/coverage report
```

Contributor setup: `CONTRIBUTING.md`.

## Deviations from standard

None.
