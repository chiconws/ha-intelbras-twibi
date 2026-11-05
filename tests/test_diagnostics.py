"""Diagnostics never leak secrets."""

import json

from custom_components.intelbras_twibi.diagnostics import (
    async_get_config_entry_diagnostics,
)
from homeassistant.core import HomeAssistant


async def test_redacts_secrets(hass: HomeAssistant, loaded) -> None:
    """Test redacts secrets."""
    diag = await async_get_config_entry_diagnostics(hass, loaded)
    text = json.dumps(diag)
    for secret in ("secret", "guestsecret", "TWIBI0000PRIM", "192.168.5.20"):
        assert secret not in text
    assert diag["router"]["node_info"][0]["dut_name"] == "Twibi Fast"
