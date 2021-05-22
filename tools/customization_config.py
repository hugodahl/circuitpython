config = {
    "replacement_values": {
      "manufacturer": {
        "name_short": "Adafruit",
        "name_long": "Adafruit Industries"
      },
      "product": {
        "name_short": "CircuitPython",
        "download_url": "https://circuitpython.org/download",
	"issue_reporting_url": "https://github.com/adafruit/circuitpython/issues"
      },
      "resources": {
        "base_site_url": "https://learn.adafruit.com",
        "learn_site_url": "/category/circuitpython"
      },
    },
    "fileset": [  # Supports globbing
      "/conf.py",
      "/py/*.c",
      "/py/makeversionhdr.py",
      "/frozen/adafruit*/**/*.py"
    ]
}
