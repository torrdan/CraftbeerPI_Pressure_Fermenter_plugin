#error message on app.log "2020-01-30 08:09:35,127 - ERROR - Exceptionread_passive_sensor: 'Sensor' object has no attribute 'mode'"

from modules import cbpi
from modules.core.hardware import SensorPassive
from modules.core.step import StepBase
from modules.core.props import Property
from modules.core.props import Property, StepProperty
import Adafruit_ADS1x15


@cbpi.sensor
class PressureSensor(SensorPassive):

    GAIN = 2/3
    voltLow = Property.Number("Voltage low", configurable=True, default_value=0, description="Pressure sensor minimal voltage. Usually 0")
    voltHigh = Property.Number("Voltage high", configurable=True, default_value=5, description="Pressure sensor minimal voltage. Usually 5")
    pressureLow = Property.Number("Pressure low", configurable=True, default_value=0, description="The pressure value at the minimal voltage. value in Bar")
    pressureHigh = Property.Number("Pressure high", configurable=True, default_value=6, description="The pressure value at the maxmimal voltage. value in Bar")
    coefficientA = 0
    coefficientB = 0


    def init(self):
        self.coefficientA = (float(self.pressureHigh - self.pressureLow)) / ((float(self.voltHigh - self.voltLow)))
        self.coefficientB = (float)(self.coefficientA) * self.voltLow - self.pressureLow
        self.adc = Adafruit_ADS1x15.ADS1115()


    def stop(self):
        '''
        Stop the sensor. Is called when the sensor config is updated or the sensor is deleted
        :return:
        '''
        pass


    def get_unit(self):
        '''
       :return: Unit of the sensor as string. Should not be longer than 3 characters
       '''
        return "Bar"
    
    def read(self):
        
        value = [0]
        # Read ADC channel 0
        value[0] = self.adc.read_adc(0, gain=self.GAIN)
        # Ratio of 15 bit value to max volts determines volts
        volt = value[0] / 32767.0 * 6.144
        # Tests shows linear relationship between bar & voltage:
        pressure = self.coefficientA * volt + self.coefficientB
        output = pressure
        self.data_received(output)
    
    @classmethod
    def init_global(cls):
        '''
        Called one at the startup for all sensors
        :return: 
        '''
        



