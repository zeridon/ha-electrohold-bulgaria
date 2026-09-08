"""Constants for the Electrohold integration."""

from datetime import timedelta

DOMAIN = "electrohold"

NAME = "Electrohold Bulgaria Regulated Prices)"

SOURCE_URL = (
    "https://electrohold.bg/bg/sales/domakinstva/snabdyavane-po-regulirani-ceni/"
)

UPDATE_INTERVAL = timedelta(hours=24)

VAT_RATE = 0.20

CONF_URL = "url"

ATTR_SOURCE = "source"
ATTR_LAST_UPDATE = "last_update"
ATTR_VAT_RATE = "vat_rate"
ATTR_DAY_PRICE = "day_price"
ATTR_NIGHT_PRICE = "night_price"
ATTR_EXCL_VAT = "price_excl_vat"
ATTR_INCL_VAT = "price_incl_vat"

TARIFF_DAY = "Дневна"
TARIFF_NIGHT = "Нощна"

