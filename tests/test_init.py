"""Setup, unload and polling failures."""

from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.intelbras_twibi.api import TwibiAuthError, TwibiConnectionError
from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant


async def test_setup_and_unload(hass: HomeAssistant, loaded) -> None:
    """Test setup and unload."""
    assert loaded.state is ConfigEntryState.LOADED
    assert await hass.config_entries.async_unload(loaded.entry_id)
    assert loaded.state is ConfigEntryState.NOT_LOADED


async def test_router_down_retries_setup(
    hass: HomeAssistant, entry: MockConfigEntry, client
) -> None:
    """Test router down retries setup."""
    client.async_get_data.side_effect = TwibiConnectionError("down")
    await hass.config_entries.async_setup(entry.entry_id)
    assert entry.state is ConfigEntryState.SETUP_RETRY


async def test_wrong_password_starts_reauth(
    hass: HomeAssistant, entry: MockConfigEntry, client
) -> None:
    """Test wrong password starts reauth."""
    client.async_get_data.side_effect = TwibiAuthError
    await hass.config_entries.async_setup(entry.entry_id)
    assert entry.state is ConfigEntryState.SETUP_ERROR
    flows = hass.config_entries.flow.async_progress()
    assert [f["context"]["source"] for f in flows] == ["reauth"]
