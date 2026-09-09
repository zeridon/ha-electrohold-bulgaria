"""Config flow for Electrohold Bulgaria."""

from __future__ import annotations

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class ElectroholdConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle the Electrohold config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> ConfigFlowResult:
        """Handle the setup flow."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title="Electrohold Bulgaria",
            data={},
        )
