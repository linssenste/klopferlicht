# klopferlicht

### NES Controller
The project uses two classic Nintendo NES controllers.

<img width="1024" height="479" alt="image" src="https://github.com/user-attachments/assets/35fbf07c-81bc-45cd-9575-3915284a8adf" />

#### Controller 1
- GND (black) → GND  
- VCC (white) → 5V  
- Clock (red) → GPIO27 (Pin 13)  
- Latch (orange) → GPIO17 (Pin 11)  
- Data (yellow) → GPIO22 (Pin 15)  

#### Controller 2
- GND (black) → GND  
- VCC (white) → 5V  
- Clock (red) → GPIO6 (Pin 31)  
- Latch (orange) → GPIO5 (Pin 29)  
- Data (yellow) → GPIO13 (Pin 33)  


### Rotary Encoder (EC11)
The project also uses one EC11 rotary encoder with push button.

#### Encoder Wiring
- CLK → GPIO25 (Pin 22)  
- DT → GPIO23 (Pin 16)  
- SW → GPIO16 (Pin 36)  
- GND → GND  

Note: the encoder uses the Raspberry Pi internal pull-up resistors


### BMI160 Accelerometer
The BMI160 is connected over I2C.

#### BMI160 Wiring
- VCC → 3.3V  
- GND → GND  
- SDA (green) → GPIO2 / SDA (Pin 3)  
- SCL (blue) → GPIO3 / SCL (Pin 5)  
- CS → 3.3V  
- SDO → GND

  
