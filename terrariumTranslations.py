# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from terrariumWeather import terrariumWeather
from terrariumSensor import terrariumSensor
from terrariumSwitch import terrariumSwitch
from terrariumDoor import terrariumDoor
from terrariumWebcam import terrariumWebcam

class terrariumTranslations():

  def __init__(self):
    logger.info('Initialize TerariumPI translations')
    self.translations = {}
    self.__load()

  def __load(self):
    logger.debug('Loading TerariumPI translations')
    # Weather
    self.translations['weather_field_location'] = _('Holds the external source URL. Supported sources are: <strong>%s</strong>.' %
                                                     ('</strong>, <strong>'.join(terrariumWeather.valid_sources.keys())))
    self.translations['weather_field_wind_speed'] = _('Choose the wind speed indicator. The software will recalculate to the chosen indicator.')
    self.translations['weather_field_temperature'] = _('Choose the temperature indicator. The software will recalculate to the chosen indicator.')
    # End weather

    # Sensors
    self.translations['sensor_field_hardware'] = _('Holds the sensor hardware type. Supported hardware types are: <strong>%s</strong>.' %
                                                    ('</strong>, <strong>'.join(terrariumSensor.valid_hardware_types)))
    self.translations['sensor_field_address'] = _('Holds the sensor address. Depending on hardware type, it is either a read only hex number or GPIO pin')
    self.translations['sensor_field_type'] = _('Holds the sensor type. Supported sensor types are: <strong>%s</strong>.' %
                                               ('</strong>, <strong>'.join(terrariumSensor.valid_sensor_types)))
    self.translations['sensor_field_name'] = _('Holds the name of the sensor.')
    self.translations['sensor_field_alarm_min'] = _('Holds the sensor lower alarm value of the sensor. When below this value, alarms can be triggered.')
    self.translations['sensor_field_alarm_max'] = _('Holds the sensor maximum alarm value of the sensor. When above this value, alarms can be triggered.')
    self.translations['sensor_field_limit_min'] = _('Holds the sensor lowest value that should be used in the graphs.')
    self.translations['sensor_field_limit_max'] = _('Holds the sensor maximum value that should be used in the graphs.')
    self.translations['sensor_field_current'] = _('Shows the sensor current value in temperature or humidity (read only).')
    # End sensors

    # Switches
    self.translations['switch_field_hardware'] = _('Holds the switch hardware type. Supported hardware types are: <strong>%s</strong>.' %
                                                    ('</strong>, <strong>'.join(terrariumSwitch.valid_hardware_types)))
    self.translations['switch_field_address'] = _('Holds the switch address. Depending on hardware type, it is either a number or GPIO pin')
    self.translations['switch_field_name'] = _('Holds the switch name.')
    self.translations['switch_field_power_wattage'] = _('Holds the switch power usage in Watt when switched on.')
    self.translations['switch_field_water_flow'] = _('Holds the switch water flow in liters per minute when switched on')
    # End switches

    # Doors
    self.translations['door_field_hardware'] = _('Holds the door hardware type. Supported hardware types are: <strong>%s</strong>.' %
                                                    ('</strong>, <strong>'.join(terrariumDoor.valid_hardware_types)))
    self.translations['door_field_address'] = _('Holds the door address.')
    self.translations['door_field_name'] = _('Holds the door name.')
    # End doors

    # Webcam
    self.translations['webcam_field_location'] = _('Holds the webcam location source. Supported sources are: <strong>RPICam</strong>, <strong>V4L device</strong>, <strong>Remote URL</strong>')
    self.translations['webcam_field_name'] = _('Holds the webcam name.')
    self.translations['webcam_field_rotation'] = _('Holds the webcam rotation of the image.')
    self.translations['webcam_field_preview'] = _('Shows the webcam preview image.')
    # End webcam

    # System
    self.translations['environment_field_lights_enable'] = _('Enable or disable the light system. When enabled, you can make changes below. By disabling it will not loose the current settings. It will temporary stop the lighting system.')
    self.translations['environment_field_lights_modus'] = _('Select the modus on which the lights will be put on and off. Select weather to use the sun rise and sun set at your location. This will make the amount of lighting variable to the actual amount of daylight. When selecting clock, the light will put on and off at sellected times.')
    self.translations['environment_field_lights_on'] = _('Enter the time when the light should be put on. Only available when running in \'%s\' modus.' % _('Timer'))
    self.translations['environment_field_lights_off'] = _('Enter the time when the lights should be put off. Only available when running in \'%s\' modus.' % _('Timer'))
    self.translations['environment_field_lights_max_hours'] = _('Enter the maximum amount of lights time in hours. When the time between on and off is more then this maximum, the on and off time will be shifted more to each other.')
    self.translations['environment_field_lights_min_hours'] = _('Enter the minimal amount of lights time in hours. When the time between on and off is less then this amount of hours, the on and off time will be widenend untill the minimum amount of hours entered here.')
    self.translations['environment_field_lights_hour_shift'] = _('Enter the amount of hours that the lights should shift. Is only needed when running in the \'%s\' modus. Enter a positive number for adding hours to the start time. Use negative numbers for subtracking from the start time.' % _('Weather'))
    self.translations['environment_field_lights_power_switches'] = _('Select the power switches that should be toggled on the selected times above. Normally these are the switches connected to the lights. Select all needed switches below.')


    self.translations['environment_field_sprayer_enable'] = _('Enable or disable the sprayer system. When enabled, you can make changes below. By disabling it will not loose the current settings. It will temporary stop the sprayer system.')
    self.translations['environment_field_sprayer_enable_during_night'] = _('Enable spraying when the lights are off. This can cause water flow when there is not enough heat to vaporize the water.')
    self.translations['environment_field_sprayer_modus'] = _('Select the operating modus. For now only sensor modus is available.')
    self.translations['environment_field_sprayer_delay'] = _('How much time must there be between two spray actions and after startup. Enter the amount of seconds in which the humidity can settle.')
    self.translations['environment_field_sprayer_duration'] = _('How long is the system spraying. Enter the amount of seconds that the system is on when the humidity is to low.')
    self.translations['environment_field_sprayer_power_switches'] = _('Select the power switches that should be toggled on the selected times above. Normally these are the switches connected to the sprayer. Select all needed switches below.')
    self.translations['environment_field_sprayer_humidity_sensors'] = _('Select the humidity sensors that are used to controll the humidity. When selecting multiple sensors, the average is calculated to determen the final humidity.')


    self.translations['environment_field_heater_enable'] = _('Enable or disable the heater system. When enabled, you can make changes below. By disabling it will not loose the current settings. It will temporary stop the heater system.')
    self.translations['environment_field_heater_enable_during_day'] = _('Enable heating when the lights are on. This can cause overheating when the lights are on.')
    self.translations['environment_field_heater_modus'] = _('Select the operating modus. Use \'%s\' modus to select the time period in which the heating is running. Select \'%s\' modus to use the sun rise and sun set as on and off times. When the sun rises the heating system will stop. Use \'%s\' modus to have the heating running when the lights are off.' % (_('Timer'),_('Weather'),_('Sensor')))
    self.translations['environment_field_heater_on'] = _('Enter the time when the heater should be put on. Only available when running in \'%s\' modus.' % _('Timer'))
    self.translations['environment_field_heater_off'] = _('Enter the time when the heater should be put off. Only available when running in \'%s\' modus.' % _('Timer'))
    self.translations['environment_field_heater_power_switches'] = _('Select the power switches that should be toggled on the selected times above. Normally these are the switches connected to the heater. Select all needed switches below.')
    self.translations['environment_field_heater_temperature_sensors'] = _('Select the temperature sensors that are used to controll the temperature. When selecting multiple sensors, the average is calculated to determen the final temperature.')


    self.translations['environment_field_cooler_enable'] = _('Enable or disable the cooler system. When enabled, you can make changes below. By disabling it will not loose the current settings. It will temporary stop the cooler system.')
    self.translations['environment_field_cooler_enable_during_night'] = _('Enable cooling when the lights are off. This can cause a very low temperature when the lights are off.')
    self.translations['environment_field_cooler_modus'] = _('Select the operating modus. Use \'%s\' modus to select the time period in which the heating is running. Select \'%s\' modus to use the sun rise and sun set as on and off times. When the sun rises the heating system will stop. Use \'%s\' modus to have the heating running when the lights are off.' % (_('Timer'),_('Weather'),_('Sensor')))
    self.translations['environment_field_cooler_on'] = _('Enter the time when the cooler should be put on. Only available when running in \'%s\' modus.' % _('Timer'))
    self.translations['environment_field_cooler_off'] = _('Enter the time when the cooler should be put off. Only available when running in \'%s\' modus.' % _('Timer'))
    self.translations['environment_field_cooler_power_switches'] = _('Select the power switches that should be toggled on the selected times above. Normally these are the switches connected to the cooler. Select all needed switches below.')
    self.translations['environment_field_cooler_temperature_sensors'] = _('Select the temperature sensors that are used to controll the temperature. When selecting multiple sensors, the average is calculated to determen the final temperature.')


    # End system

    logger.info('Loaded TerrariumPI translations')

  def get_translation(self,translation):
    if translation in self.translations:
      return self.translations[translation]

    logger.warning('No translation available for \'%s\'' % (translation,))
    return 'No translation available for \'%s\'' % (translation,)

  def reload(self):
    logger.info('Reloading TerrariumPI translations')
    self.__load()
