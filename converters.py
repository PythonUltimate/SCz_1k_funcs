# Converters


def celsius_to_fahrenheit(degrees):
    return 9 / 5 * degrees + 32


def celsius_to_kelvin(degrees):
    return degrees + 273.15


def fahrenheit_to_kelvin(degrees):
    return 5 / 9 * (degrees - 32) + 273.15


def fahrenheit_to_celsius(degrees):
    return 5 / 9 * (degrees - 32)


def celsius_to_rankine(degrees):
    return 9 / 5 * degrees + 491.67


def celsius_to_reaumur(degrees):
    return degrees * 0.8


def meter_to_angstroms(length):
    return length * 10000000000


def meter_to_feet(length):
    return length * 3.28084


def cmpermin_to_mpers(speed):
    return speed * 0.0001667


def footperh_to_mpers(speed):
    return speed * 8.46667e-05


def footpermin_to_mpers(speed):
    return speed * 0.00508


def footpers_to_mpers(speed):
    return speed * 0.3048


def inchpermin_to_mpers(speed):
    return speed * 0.000423333


def inchpers_to_mpers(speed):
    return speed * 0.0254


def kmperh_to_mpers(speed):
    return speed * 0.2777778


def kmpers_to_mpers(speed):
    return speed * 1000


def knots_to_mpers(speed):
    return speed * 0.5144444


def mperh_to_mpers(speed):
    return speed * 0.0002777778


def mpermin_to_mpers(speed):
    return speed * 0.01667


def mileperh_to_mpers(speed):
    return speed * 0.44704


def mileperm_to_mpers(speed):
    return speed * 26.8224


def milepers_to_mpers(speed):
    return speed * 1609.344


def speedoflight_to_mpers(speed):
    return speed * 299792458


def yardperh_to_mpers(speed):
    return speed * 0.000254


def yardperm_to_mpers(speed):
    return speed * 0.01524


def yardpers_to_mpers(speed):
    return speed * 0.9144


def squareinch_to_squarem(area):
    return area * 0.00064516


def squarefoot_to_squarem(area):
    return area * 0.09290304


def squareyard_to_squarem(area):
    return area * 0.83612736


def squaremile_to_squarem(area):
    return area * 2589988.11


def acre_to_squarem(area):
    return area * 4046.856


def hectare_to_squarem(area):
    return area * 10000


def squaremm_to_squarem(area):
    return area * 0.000001


def squarecm_to_squarem(area):
    return area * 0.0001


def squarekm_to_squarem(area):
    return area * 1000000


def atm_to_pascal(pressure):
    return pressure * 101325


def bar_to_pascal(pressure):
    return pressure * 100000


def barye_to_pascal(pressure):
    return pressure * 0.1


def cmhg_to_pascal(pressure):
    return pressure * 1333.33


def cmh2o_to_pascal(pressure):
    return pressure * 98.0638


def ftHg_to_pascal(pressure):
    return pressure * 40636.66


def fth2o_to_pascal(pressure):
    return pressure * 2988.98


def kgfmm2_to_pascal(pressure):
    return pressure * 9806650


def mmHg_to_pascal(pressure):
    return pressure * 133.3224


def lbft2_to_pascal(pressure):
    return pressure * 47.88


def psi_to_pascal(pressure):
    return pressure * 6894.757


def torr_to_pascal(pressure):
    return pressure * 133.3224


def barrel_to_m3(volume):
    return volume * 0.158987295


def bushel_to_m3(volume):
    return volume * 0.0366872


def cord_to_m3(volume):
    return volume * 3.624556364


def ft3_to_m3(volume):
    return volume * 0.028316847


def in3_to_m3(volume):
    return volume * 1.63871e-05


def yd3_to_m3(volume):
    return volume * 0.764554858


def cup_to_m3(volume):
    return volume * 0.000236588


def ounce_to_m3(volume):
    return volume * 2.95735e-05


def gallon_to_m3(volume):
    return volume * 0.00454609


def gill_to_m3(volume):
    return volume * 0.000118294


def hogshead_to_m3(volume):
    return volume * 0.238480942


def ml_to_m3(volume):
    return volume * 0.000001


def peck_to_m3(volume):
    return volume * 0.00909218


def pint_to_m3(volume):
    return volume * 0.000568261


def quart_to_m3(volume):
    return volume * 0.001101221


def tablespoon_to_m3(volume):
    return volume * 1.77582e-05


def teaspoon_to_m3(volume):
    return volume * 5.91939e-06


def kg_to_lb(weight):
    return weight * 2.205


def lb_to_kg(weight):
    return weight * 0.4536


def ounce_to_gram(weight):
    return weight * 28.3495


def pound_to_gram(weight):
    return weight * 453.59237


def kgforce_to_newton(force):
    return force * 9.80665


def ounceforce_to_newton(force):
    return force * 0.2780139


def tonforce_to_newton(force):
    return force * 8896.443


def btuh_to_watt(power):
    return power * 0.2930711


def calh_to_watt(power):
    return power * 4.1868 / 60 / 60


def hp_to_watt(power):
    return power * 745.7


def jouleh_to_watt(power):
    return power * 1 / 60 / 60


def min_to_sec(time):
    return time * 60


def hour_to_sec(time):
    return time * 3600


def day_to_sec(time):
    return time * 86400


def week_to_sec(time):
    return time * 604800


def month_to_sec(time):
    return time * 2628000


def year_to_sec(time):
    return time * 31636000


def inch_to_meter(length):
    return length * 0.0254


def foot_to_meter(length):
    return length * 0.3048


def yward_to_meter(length):
    return length * 0.9144


def rod_to_meter(length):
    return length * 5.0292


def angstrom_to_meter(length):
    return length * 1e-10


def lightyear_to_meter(length):
    return length * 9460730472580800


def lightday_to_meter(lenth):
    return lenth * 25902068371200


def lighthour_to_meter(length):
    return length * 1079252848800


def lightmin_to_meter(length):
    return length * 17987547480


def lightsec_to_meter(length):
    return length * 299792458


def ozin3_to_kgm3(density):
    return density * 1729.994


def lbin3_to_kgm3(density):
    return density * 27679.904


def ozgal_to_kgm3(density):
    return density * 6.236


def lbgal_to_kgm3(density):
    return density * 99.776


def tonyd3_to_kgm3(density):
    return density * 1328.939

def neper_to_bel(sound):
    return sound * 0.8686




def hours_to_minutes(time):
    hours = time // 60
    minutes = time % 60
    return f'{hours}:{minutes}'


def minutes_to_hours(time):
    return f'{time / 60}h'


def bits_to_bytes(units):
    return units * 0.125


def lux_to_phot(unit):
    return unit * 0.0001


def lux_to_wattcm2(unit):
    return unit * 1.4641288e-7


def pln_to_goldoz(amount):
    return amount * 1/8398.83




def pln_to_eur(amount):
    return amount * 1/47146


def pln_to_usd(amount):
    return amount * 1/4.7328

def pln_to_chf(amount):
    return amount * 1/4,7905

def pln_to_gbp(amount):
    return amount * 5.3795

def pln_to_czk(amount):
    return amount * 1/0.1935

def pln_to_sek(amount):
    return amount * 1/0.4333

def pln_to_uah(amount):
    return amount * 1/0.1258

def pln_to_cny(amount):
    return amount * 1/0.6528

def pln_to_jpy(amount):
    return amount * 1/0.032323

def pln_to_btc(amount):
    return amount * 1/74439.53

def pln_to_eth(amount):
    return amount * 1/6099.99

def pln_to_sasin(amount):
    return amount * 1/70000000

def tuzin_to_unit(amount):
    return amount * 12

def mendel_to_unit(amount):
    return amount * 15

def kopa_to_units(amount):
    return amount * 60

def gros_to_unit(amount):
    return amount * 144

