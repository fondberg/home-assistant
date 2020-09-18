"""Test the Easee EV Charger config flow."""
<<<<<<< HEAD
from homeassistant import config_entries, setup
from homeassistant.components.easee.config_flow import CannotConnect, InvalidAuth
=======
from easee import AuthorizationFailedException

from homeassistant import config_entries, setup
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
from homeassistant.components.easee.const import DOMAIN

from tests.async_mock import patch


async def test_form(hass):
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}

<<<<<<< HEAD
    with patch(
        "homeassistant.components.easee.config_flow.PlaceholderHub.authenticate",
        return_value=True,
    ), patch(
=======
    with patch("easee.Easee.connect", return_value=True,), patch(
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
        "homeassistant.components.easee.async_setup", return_value=True
    ) as mock_setup, patch(
        "homeassistant.components.easee.async_setup_entry",
        return_value=True,
    ) as mock_setup_entry:
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
<<<<<<< HEAD
                "host": "1.1.1.1",
=======
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
                "username": "test-username",
                "password": "test-password",
            },
        )

    assert result2["type"] == "create_entry"
<<<<<<< HEAD
    assert result2["title"] == "Name of the device"
    assert result2["data"] == {
        "host": "1.1.1.1",
=======

    assert result2["data"] == {
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
        "username": "test-username",
        "password": "test-password",
    }
    await hass.async_block_till_done()
    assert len(mock_setup.mock_calls) == 1
    assert len(mock_setup_entry.mock_calls) == 1


<<<<<<< HEAD
async def test_form_invalid_auth(hass):
    """Test we handle invalid auth."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with patch(
        "homeassistant.components.easee.config_flow.PlaceholderHub.authenticate",
        side_effect=InvalidAuth,
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
                "host": "1.1.1.1",
                "username": "test-username",
                "password": "test-password",
            },
        )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "invalid_auth"}


=======
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
async def test_form_cannot_connect(hass):
    """Test we handle cannot connect error."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    with patch(
<<<<<<< HEAD
        "homeassistant.components.easee.config_flow.PlaceholderHub.authenticate",
        side_effect=CannotConnect,
=======
        "easee.Easee.connect",
        side_effect=AuthorizationFailedException,
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {
<<<<<<< HEAD
                "host": "1.1.1.1",
=======
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
                "username": "test-username",
                "password": "test-password",
            },
        )

    assert result2["type"] == "form"
<<<<<<< HEAD
    assert result2["errors"] == {"base": "cannot_connect"}
=======
    assert result2["errors"] == {"base": "connection_failure"}
>>>>>>> 2db7db7e07bc31a695a3152b65cd67b241fc3480
