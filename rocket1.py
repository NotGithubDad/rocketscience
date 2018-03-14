# rocketscience
from ggrocket import Rocket, Planet

earth = Planet(viewscale=0.00005)
rocket = Rocket(earth, altitude=400000, velocity=7725.73, timezoom=1)
earth.run(rocket)
