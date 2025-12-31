import mitsuba as mi

mi.set_variant('cuda_ad_spectral_polarized')
scene = mi.load_file("scene.xml")
img = mi.render(scene)
