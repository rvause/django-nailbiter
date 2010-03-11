"""
Defaults for nailbiter app.
"""

# Defines image processors.
PROCESSORS = (
    'nailbiter.processors.colorspace',
    'nailbiter.processors.autocrop',
    'nailbiter.processors.scale_and_crop',
    'nailbiter.processors.filters',
)
