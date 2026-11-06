# Intelbras Twibi

[![Marketplace][badge-marketplace]][link-marketplace]
[![GitHub Release][badge-release]][link-release]
[![Home Assistant][badge-ha]][link-ha]
[![GitHub Commit Activity][badge-commit-activity]][link-commits]
[![HACS Validation][badge-hacs-validation]][link-hacs-validation]
[![Hassfest][badge-hassfest]][link-hassfest]
[![Tests][badge-tests]][link-tests]
[![License][badge-license]][link-license]

Integração local do Home Assistant para a rede mesh **Intelbras Twibi**: presença dos dispositivos, velocidade da internet, LEDs, Wi-Fi de visitantes e reinício, sem nuvem.

## Recursos

- Um dispositivo por unidade Twibi, com a unidade principal e as secundárias
- `device_tracker` para os clientes da rede (todos ou só os escolhidos)
- Velocidade de download e upload da internet, clientes conectados e IP da WAN
- LED de status de cada unidade, Wi-Fi de visitantes, UPnP e reinício da rede
- Tudo local: a integração fala direto com o roteador, sem conta nem nuvem

## Requisitos

- Home Assistant 2026.9 ou mais recente
- Rede Twibi (Fast, Giga ou Force) acessível pelo Home Assistant
- A senha de administração do Twibi

## Instalação

### Marketplace (recomendado)

[![Abrir este repositório no Marketplace da sua instância do Home Assistant.][badge-my-marketplace]][link-my-marketplace]

1. Clique no botão acima. Se o Home Assistant pedir, confirme a adição do repositório.
2. Baixe **Intelbras Twibi** em **Configurações → Marketplace**.
3. Reinicie o Home Assistant.

No Home Assistant 2026.10 ou anterior, instale o [HACS](https://hacs.xyz/) antes e use:
[![Abrir este repositório no HACS da sua instância do Home Assistant.][badge-my-hacs]][link-my-hacs]
Depois baixe **Intelbras Twibi** no HACS e reinicie o Home Assistant.

### Manual

1. Baixe a [versão mais recente][link-release].
2. Copie `custom_components/intelbras_twibi` para a pasta `custom_components` da sua
   configuração do Home Assistant.
3. Reinicie o Home Assistant.

### Atualizando da v1.x

A v0.1.0 é uma reescrita: o domínio mudou de `intelbras_twibi_router` para
`intelbras_twibi` e a numeração recomeçou, então o Marketplace/HACS não oferece a
atualização sozinho. O Home Assistant não move uma entrada entre domínios:

1. Exclua a entrada antiga **Intelbras Twibi** em **Configurações → Dispositivos e
   serviços** e remova a versão antiga no Marketplace/HACS.
2. Apague a pasta `custom_components/intelbras_twibi_router`, se ainda existir.
3. Instale a versão atual, reinicie o Home Assistant e adicione a integração de novo.

## Configuração

[![Configurar Intelbras Twibi na sua instância do Home Assistant.][badge-my-config]][link-my-config]

1. Vá em **Configurações → Dispositivos e serviços → Adicionar integração**.
2. Procure por **Intelbras Twibi** e siga os passos.

| Campo | Descrição |
| --- | --- |
| Endereço | IP do Twibi principal (padrão `192.168.5.1`) |
| Senha | A mesma senha do app ou da página do Twibi |

Endereço e senha podem ser alterados depois pelo menu **Reconfigurar**. Em **Configurar**, escolha
quais dispositivos rastrear (vazio = todos) e se cabos devem ser ignorados.

## Entidades

| Entidade | Plataforma | Descrição |
| --- | --- | --- |
| Internet | `binary_sensor` | Conexão da WAN no Twibi principal |
| Velocidade de download / upload | `sensor` | Tráfego atual da WAN, em kbit/s |
| Clientes conectados | `sensor` | Quantidade de dispositivos na rede |
| Endereço IP da WAN | `sensor` | IP recebido do provedor (diagnóstico) |
| Última inicialização | `sensor` | Quando cada unidade ligou (diagnóstico) |
| Qualidade do link mesh | `sensor` | Sinal Wi-Fi entre a unidade secundária e a principal, em dBm (desconhecido quando ligadas por cabo) |
| LED de status | `light` | LED da frente de cada unidade |
| Wi-Fi de visitantes / UPnP | `switch` | Liga e desliga, mantendo nome e senha da rede de visitantes |
| Reiniciar rede mesh | `button` | Reinicia todas as unidades |
| Cliente | `device_tracker` | Em casa enquanto aparece na lista do roteador |

## Solução de problemas

- **Diagnóstico:** Configurações → Dispositivos e serviços → Intelbras Twibi → ⋮ →
  **Baixar diagnóstico** (credenciais são ocultadas). Anexe o arquivo ao abrir um bug.
- **Logs de depuração:**

```yaml
logger:
  logs:
    custom_components.intelbras_twibi: debug
```

## Limitações conhecidas

- O Twibi não informa o nome de todos os clientes; sem nome, o tracker usa o MAC.
- Rastreadores de dispositivos que o Home Assistant ainda não conhece entram desativados
  (comportamento padrão do HA); escolha-os em **Configurar** para ativá-los.
- Firmwares diferentes respondem de formas diferentes; se algo faltar, abra uma issue com o diagnóstico.

## Remoção

1. Vá em **Configurações → Dispositivos e serviços → Intelbras Twibi**, abra ⋮ e selecione **Excluir**.
2. Remova em **Configurações → Marketplace** (ou no HACS), ou apague
   `custom_components/intelbras_twibi` se instalou manualmente.
3. Reinicie o Home Assistant.

## Desenvolvimento

Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para configurar o ambiente, rodar as verificações e os testes, e o [AGENTS.md](AGENTS.md) para a estrutura do código.

## Licença

MIT, veja [LICENSE](LICENSE).

[badge-marketplace]: https://img.shields.io/badge/Marketplace-Custom-41BDF5.svg
[badge-release]: https://img.shields.io/github/v/release/chiconws/ha-intelbras-twibi
[badge-ha]: https://img.shields.io/badge/Home%20Assistant-2026.9%2B-41BDF5?logo=home-assistant
[badge-commit-activity]: https://img.shields.io/github/commit-activity/m/chiconws/ha-intelbras-twibi
[badge-hacs-validation]: https://github.com/chiconws/ha-intelbras-twibi/actions/workflows/hacs.yaml/badge.svg
[badge-hassfest]: https://github.com/chiconws/ha-intelbras-twibi/actions/workflows/hassfest.yaml/badge.svg
[badge-tests]: https://github.com/chiconws/ha-intelbras-twibi/actions/workflows/tests.yaml/badge.svg
[badge-license]: https://img.shields.io/github/license/chiconws/ha-intelbras-twibi
[badge-my-marketplace]: https://my.home-assistant.io/badges/marketplace_repository.svg
[badge-my-hacs]: https://my.home-assistant.io/badges/hacs_repository.svg
[badge-my-config]: https://my.home-assistant.io/badges/config_flow_start.svg

[link-marketplace]: https://www.home-assistant.io/integrations/marketplace/
[link-release]: https://github.com/chiconws/ha-intelbras-twibi/releases/latest
[link-ha]: https://www.home-assistant.io/
[link-commits]: https://github.com/chiconws/ha-intelbras-twibi/commits/main
[link-hacs-validation]: https://github.com/chiconws/ha-intelbras-twibi/actions/workflows/hacs.yaml
[link-hassfest]: https://github.com/chiconws/ha-intelbras-twibi/actions/workflows/hassfest.yaml
[link-tests]: https://github.com/chiconws/ha-intelbras-twibi/actions/workflows/tests.yaml
[link-license]: LICENSE
[link-my-marketplace]: https://my.home-assistant.io/redirect/marketplace_repository/?owner=chiconws&repository=ha-intelbras-twibi&category=integration
[link-my-hacs]: https://my.home-assistant.io/redirect/hacs_repository/?owner=chiconws&repository=ha-intelbras-twibi&category=integration
[link-my-config]: https://my.home-assistant.io/redirect/config_flow_start/?domain=intelbras_twibi
