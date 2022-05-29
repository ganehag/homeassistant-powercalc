"""Aliases for manufacturers and model IDs."""

MANUFACTURER_ALIASES = {
    "Philips": "Signify Netherlands B.V.",
    "IKEA": "IKEA of Sweden",
    "Xiaomi": "Aqara",
    "LUMI": "Aqara",
    "ADEO": "Lexman",
}

MANUFACTURER_DIRECTORY_MAPPING = {
    "IKEA of Sweden": "ikea",
    "Feibit Inc co.  ": "jiawen",
    "LEDVANCE": "ledvance",
    "MLI": "mueller-licht",
    "OSRAM": "osram",
    "Signify Netherlands B.V.": "signify",
    "Aqara": "aqara",
    "Lexman": "lexman",
    "Yeelight": "yeelight",
}

MODEL_DIRECTORY_MAPPING = {
    "IKEA of Sweden": {
        "FLOALT panel WS 30x30": "L1527",
        "FLOALT panel WS 60x60": "L1529",
        "TRADFRI bulb E14 WS opal 400lm": "LED1536G5",
        "TRADFRI bulb GU10 WS 400lm": "LED1537R6",
        "TRADFRI bulb E27 WS opal 980lm": "LED1545G12",
        "TRADFRI bulb E27 WS clear 950lm": "LED1546G12",
        "TRADFRI bulb E27 opal 1000lm": "LED1623G12",
        "TRADFRI bulb E27 W opal 1000lm": "LED1623G12",
        "TRADFRI bulb E14 CWS opal 600lm": "LED1624G9",
        "TRADFRI bulb E26 CWS opal 600lm": "LED1624G9",
        "TRADFRI bulb E27 CWS opal 600lm": "LED1624G9",
        "TRADFRI bulb E14 W op/ch 400lm": "LED1649C5",
        "TRADFRI bulb GU10 W 400lm": "LED1650R5",
        "TRADFRI bulb E27 WS opal 1000lm": "LED1732G11",
        "TRADFRI bulb E14 WS opal 600lm": "LED1733G7",
        "TRADFRI bulb E27 WS clear 806lm": "LED1736G9",
        "TRADFRI bulb E14 WS opal 600lm": "LED1738G7",
        "TRADFRI bulb E14 WS 470lm": "LED1835C6",
        "TRADFRI bulb E27 WW 806lm": "LED1836G9",
        "TRADFRI bulb E27 WW clear 250lm": "LED1842G3",
        "TRADFRI bulb GU10 WW 400lm": "LED1837R5",
        "TRADFRI bulb GU10 CWS 345lm": "LED1923R5",
        "TRADFRI bulb E27 CWS 806lm": "LED1924G9",
        "TRADFRI bulb E14 CWS 470lm": "LED1925G6",
        "TRADFRIbulbE14WScandleopal470lm": "LED1949C5",
        "TRADFRIbulbE14WSglobeopal470lm": "LED2002G5",
        "TRADFRIbulbE27WSglobeopal1055lm": "LED2003G10",
        "TTRADFRIbulbGU10WS345lm": "LED2005R5",
        "TRADFRI bulb GU10 WW 345lm": "LED2005R5",
        "LEPTITER Recessed spot light": "T1820",
    },
    "Signify Netherlands B.V.": {
        "9290022166": "LCA001",
        "929003053401": "LCA001",
        "929001953101": "LCG002",
        "1741430P7": "LCS001",
        "1741530P7": "LCS001",
        "9290012573A": "LCT015",
        "440400982841": "LCT024",
        "7602031P7": "LCT026",
        "9290022169": "LTA001",
        "9290024719": "LTA011",
        "3261030P6": "LTC001",
        "3261031P6": "LTC001",
        "3261048P6": "LTC001",
        "3418931P6": "LTC012",
        "3417711P6": "LTW017",
        "8718699673147": "LWA001",
        "433714": "LWB004",
        "8718696449691": "LWB010",
        "9290024406": "LWU001",
        "9290011370B": "LWF001",
        "8719514328242": "LTA004",
        "8718699703424": "LCL001",
        "8718699671211": "LWE002",
        "9290020399": "LWE002",
        # US Versions. Alias to EU versions
        "LWA003": "LWA001",
        "9290022268": "LWA001",
        "LWV002": "LWV001",
        "046677551780": "LWV001",
        "LWO002": "LWO001",
        "9290022415": "LWO001",
        "LWA008": "LWA009",
        "9290023351": "LWA009",
        "LCA007": "LCA006",
        "9290024687": "LCA006",
        "LCA005": "LCA001",
        "9290022266A": "LCA001",
    },
    "Yeelight": {
        "color2": "YLDP06YL",
    },
}