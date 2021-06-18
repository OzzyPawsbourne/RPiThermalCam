# RPiThermalCam
Using a FLIR Lepton w/ breakout board on a Raspberry Pi, get the temperature at a point and change the colormap.

# Requirements
pylepton from [lepton3-dev](https://github.com/groupgets/pylepton/tree/lepton3-dev) or [lepton3](https://github.com/groupgets/pylepton/tree/lepton3) branch

# Usage
def rpi_temp(data,point,palette_switch=True,circle_flag=True,text_flag=True):

    Parameters:
    
    data
    
        raw data input coming from the FLIR Lepton
        
    point
    
        (0-159,0-119) the point to get the temperature
    
    palette_switch
    
        True : Ironblack
        
        False : Rainbow
        
    circle_flag
    
        enable to put an indicating circle on the output image
        
    text_flag
    
        enable to put the temperature reading on the output image

# References
[Colormap](https://github.com/groupgets/GetThermal/blob/bb467924750a686cc3930f7e3a253818b755a2c0/src/dataformatter.cpp#L6)

Wiring Connections from the official [Lepton website](https://lepton.flir.com/getting-started/lepton-quick-start-raspberry-pi/#settingUpBreadboard)
