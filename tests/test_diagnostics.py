"""Diagnostics never leak secrets."""

import json

from custom_components.intelbras_twibi.const import CONF_TRACKED_DEVICES
from custom_components.intelbras_twibi.diagnostics import (
    async_get_config_entry_diagnostics,
)
from homeassistant.core import HomeAssistant


async def test_redacts_secrets(hass: HomeAssistant, loaded) -> None:
    """Test redacts secrets."""
    diag = await async_get_config_entry_diagnostics(hass, loaded)
    text = json.dumps(diag)
    for secret in (
        "secret",
        "guestsecret",
        "TWIBI0000PRIM",
        "192.168.5.20",
        "11:22:33:44:55:01",
    ):
        assert secret not in text
    assert diag["router"]["node_info"][0]["dut_name"] == "Twibi Fast"


async def test_redacts_tracked_devices(hass: HomeAssistant, loaded) -> None:
    """Selected client MACs in the options are redacted."""
    hass.config_entries.async_update_entry(
        loaded, options={CONF_TRACKED_DEVICES: ["11:22:33:44:55:01"]}
    )
    await hass.async_block_till_done()
    diag = await async_get_config_entry_diagnostics(hass, loaded)
    assert "11:22:33:44:55:01" not in json.dumps(diag["options"])
