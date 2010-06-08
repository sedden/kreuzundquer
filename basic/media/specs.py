from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeThumb(processors.Resize):
    width = 136
    height = 102
    crop = True

class ResizeRegular(processors.Resize):
    width = 296
    height = 296
    crop = False

class ResizeDisplay(processors.Resize):
    width = 800
    height = 600
    crop = False

class EnchanceThumb(processors.Adjustment):
    sharpness = 1.5
    color = 0.0

class EnchanceThumbHover(processors.Adjustment):
    sharpness = 1.5
    color = 1.5

class Thumbnail(ImageSpec):
    pre_cache = True
    processors = [processors.Transpose, ResizeThumb, EnchanceThumb]

class Thumbnail_Hover(ImageSpec):
    pre_cache = True
    processors = [processors.Transpose, ResizeThumb, EnchanceThumbHover]

class Regular(ImageSpec):
    pre_cache = True
    processors = [processors.Transpose, ResizeRegular]

class Display(ImageSpec):
    processors = [processors.Transpose, ResizeDisplay]
