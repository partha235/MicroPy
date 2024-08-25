# MCU
In 1970s, microcontroller has been introduced to the world of electronics by two american companies Intel & Texas. The need for microcontroller evolved when there is a need for single compact designed that handel single process unless microprocessor need separate circuit for time control I/O devices and memory unit. They had become backbone for embedded system development. Microcontroller is an small integrated chip which governs the specified task within an embedded system without requiring a complex operating system. It contains processor core, RAM and EEPROM for storing programs and also peripheral devices for communication. MCU are designed for low power consumption, cost-effective and space efficiency. Modern controllers has AD converters and oscillator for time functions.
### Parts
A microcontroller consists of several key parts, each playing a crucial role in its functionality. Here are the primary components:

### 1. Control Processing Unit (CPU)
The CPU is the brain of the microcontroller. It performs the arithmetic and logical operations, executes instructions, and controls the flow of data within the system.

### 2. Memory
Memory in a microcontroller is used for storing data and instructions. It typically includes:
- **RAM (Random Access Memory)**: Used for temporary data storage during operation.
- **ROM (Read-Only Memory)**: Stores the firmware or software code permanently.
- **EEPROM (Electrically Erasable Programmable Read-Only Memory)**: Allows for data storage that can be modified electrically.

### 3. Input/Output Ports (I/O Ports)
I/O ports are used to interface the microcontroller with external devices such as sensors, displays, and other peripherals. They allow the microcontroller to receive and send digital signals.

### 4. Timers/Counters
Timers and counters are used for measuring time intervals, generating delays, and counting events. They are essential for tasks like pulse-width modulation (PWM) and event counting.

### 5. Analog-to-Digital Converter (ADC)
An ADC converts analog signals (such as those from sensors) into digital data that the CPU can process. This is crucial for applications involving analog inputs.

### 6. Digital-to-Analog Converter (DAC)
A DAC converts digital data back into analog signals. This is useful for applications that require analog output, such as audio signal generation.

### 7. Oscillator/Clock
The oscillator provides the clock signal that drives the microcontroller. It determines the speed at which the microcontroller operates and synchronizes its functions.

### 8. Serial Communication Interfaces
These interfaces enable the microcontroller to communicate with other devices using serial protocols. Common serial interfaces include:
- **UART (Universal Asynchronous Receiver/Transmitter)**
- **SPI (Serial Peripheral Interface)**
- **I2C (Inter-Integrated Circuit)**

### 9. Interrupt Controller
The interrupt controller manages the interrupt signals that allow the CPU to respond to asynchronous events, ensuring timely and efficient processing of critical tasks.

### 10. Power Supply
The power supply provides the necessary voltage and current to operate the microcontroller and its components.

In microcontrollers (MCUs), different types of RAM are used to serve various purposes. Here are the main types of RAM typically found in MCUs:

## Ram Types

### 1. **Static RAM (SRAM)**
- **Characteristics**: SRAM stores data in flip-flop circuits, providing fast access and high reliability. It does not need to be periodically refreshed, unlike DRAM.
- **Usage**: Commonly used for general-purpose data storage and working memory within MCUs due to its speed and simplicity.
- **Advantages**: Fast access time, no refresh needed.
- **Disadvantages**: More expensive and consumes more power compared to DRAM.

### 2. **Dynamic RAM (DRAM)**
- **Characteristics**: DRAM stores data in capacitors, which require periodic refreshing to maintain the data.
- **Usage**: Less common in MCUs due to the need for refresh circuitry and more complex control. Sometimes used in applications where a larger amount of RAM is needed and cost is a concern.
- **Advantages**: Higher density and lower cost per bit compared to SRAM.
- **Disadvantages**: Slower access time, needs refresh cycles, more complex control logic.

### 3. **Non-Volatile RAM (NVRAM)**
- **Characteristics**: NVRAM retains data even when power is turned off. Types of NVRAM include Ferroelectric RAM (FRAM) and Magnetoresistive RAM (MRAM).
- **Usage**: Used in applications where data retention is crucial without constant power, such as in configuration settings and logging data.
- **Advantages**: Retains data without power, fast access time.
- **Disadvantages**: Typically more expensive than SRAM and DRAM.

### 4. **Pseudo-Static RAM (PSRAM)**
- **Characteristics**: PSRAM combines features of both SRAM and DRAM. It uses a DRAM core with a built-in refresh circuit, making it behave like SRAM.
- **Usage**: Used in applications that require larger RAM sizes with SRAM-like interface and performance.
- **Advantages**: Higher density and lower cost than pure SRAM, simple interface.
- **Disadvantages**: Slower than pure SRAM, but typically faster than DRAM.

### 5. **Embedded DRAM (eDRAM)**
- **Characteristics**: eDRAM is integrated into the microcontroller chip itself, providing high-speed access to larger amounts of RAM.
- **Usage**: Used in advanced MCUs requiring higher performance and larger RAM capacities, such as those used in graphics and high-speed computing applications.
- **Advantages**: Higher density, lower power consumption compared to off-chip DRAM.
- **Disadvantages**: Complexity in manufacturing and design, typically found in more advanced and expensive MCUs.

These types of RAM are used in different microcontrollers based on the specific requirements of the application, balancing factors such as speed, power consumption, cost, and data retention needs.

## Communication Interfaces 
Microcontrollers (MCUs) support various communication interfaces to connect with other devices, peripherals, and networks. These interfaces enable data exchange in embedded systems, each with its own protocol, advantages, and typical use cases. Here are the main types of communication interfaces found in MCUs:

### 1. **Serial Communication Interfaces**

#### **Universal Asynchronous Receiver/Transmitter (UART)**
- **Characteristics**: Asynchronous communication, uses start and stop bits to frame data.
- **Usage**: Commonly used for serial communication between microcontrollers and PCs, GPS modules, Bluetooth modules, etc.
- **Advantages**: Simple, widely supported.
- **Disadvantages**: Slower compared to some other serial protocols, requires precise timing.

#### **Serial Peripheral Interface (SPI)**
- **Characteristics**: Synchronous communication, uses separate lines for data in, data out, clock, and chip select.
- **Usage**: Connecting microcontrollers to sensors, SD cards, and other peripherals.
- **Advantages**: High speed, full-duplex communication, simple protocol.
- **Disadvantages**: Requires more pins compared to I2C, limited to short distances.

#### **Inter-Integrated Circuit (I2C)**
- **Characteristics**: Synchronous communication, uses two lines (data and clock) for communication between multiple devices.
- **Usage**: Connecting multiple peripherals like EEPROMs, sensors, and RTCs to a microcontroller.
- **Advantages**: Supports multiple devices on the same bus, relatively simple wiring.
- **Disadvantages**: Slower than SPI, more complex protocol.

### 2. **Parallel Communication Interfaces**

#### **General-Purpose Input/Output (GPIO)**
- **Characteristics**: Basic interface for digital input and output, configurable as input or output pins.
- **Usage**: Interfacing with switches, LEDs, sensors, and other simple peripherals.
- **Advantages**: Simple to use, versatile.
- **Disadvantages**: Limited speed and distance, not suitable for complex communication.

#### **Parallel Data Bus**
- **Characteristics**: Transfers multiple bits of data simultaneously over multiple lines.
- **Usage**: Used in older systems for connecting peripherals like printers and displays.
- **Advantages**: High-speed data transfer.
- **Disadvantages**: Requires many pins, more complex wiring.

### 3. **Wireless Communication Interfaces**

#### **Bluetooth**
- **Characteristics**: Wireless communication over short distances, operates in the 2.4 GHz ISM band.
- **Usage**: Wireless connectivity for devices like smartphones, wireless sensors, and peripherals.
- **Advantages**: Widely supported, convenient for short-range communication.
- **Disadvantages**: Limited range and data rate compared to Wi-Fi.

#### **Wi-Fi**
- **Characteristics**: Wireless communication over longer distances, operates in the 2.4 GHz and 5 GHz bands.
- **Usage**: Connecting microcontrollers to the internet or local networks.
- **Advantages**: High data rates, wide coverage.
- **Disadvantages**: Higher power consumption, more complex protocol.

#### **Zigbee**
- **Characteristics**: Low-power, low-data-rate wireless communication, operates in the 2.4 GHz ISM band.
- **Usage**: Home automation, industrial control, and other low-power applications.
- **Advantages**: Low power consumption, supports mesh networking.
- **Disadvantages**: Lower data rates and shorter range compared to Wi-Fi.

### 4. **Specialized Communication Interfaces**

#### **Controller Area Network (CAN)**
- **Characteristics**: Robust vehicle bus standard, supports real-time data exchange between microcontrollers and devices.
- **Usage**: Automotive applications, industrial automation.
- **Advantages**: High reliability, real-time performance, fault-tolerant.
- **Disadvantages**: More complex protocol, requires CAN transceiver.

#### **Universal Serial Bus (USB)**
- **Characteristics**: Standard for connecting peripherals to a host computer.
- **Usage**: Connecting keyboards, mice, storage devices, and more to microcontrollers.
- **Advantages**: High data rates, supports power delivery.
- **Disadvantages**: More complex protocol, higher power consumption.

These communication interfaces provide flexibility for connecting microcontrollers with a wide range of peripherals and networks, enabling the creation of diverse and complex embedded systems.

## Register
Registers are small, fast storage locations within a microcontroller's CPU. They are used to store and manipulate data during the execution of instructions. Registers play a critical role in the operation of a microcontroller, as they provide the CPU with quick access to data that is actively being processed. Here’s an overview of different types of registers commonly found in microcontrollers:

### 1. **General-Purpose Registers**
- **Purpose**: Used to temporarily hold data and operands for arithmetic and logic operations.
- **Usage**: These registers can be used by the programmer to store intermediate results, variables, or any data that needs to be accessed quickly.
- **Example**: In an 8-bit microcontroller, general-purpose registers might be named R0, R1, R2, etc.

### 2. **Special Function Registers (SFRs)**
- **Purpose**: Control and monitor specific functions of the microcontroller, such as I/O ports, timers, interrupts, and more.
- **Usage**: Each SFR is assigned to a specific function within the microcontroller. For example, a register might control the configuration of an I/O port, or another might hold the status of an interrupt flag.
- **Example**: Registers like `PORTA`, `TMR0`, and `STATUS` in PIC microcontrollers.

### 3. **Program Counter (PC)**
- **Purpose**: Holds the address of the next instruction to be executed by the CPU.
- **Usage**: The program counter is automatically updated as the CPU fetches and executes instructions. It allows the CPU to keep track of the sequence of program execution.
- **Example**: In many microcontrollers, the PC increments by one after each instruction fetch, unless a jump or branch instruction alters its value.

### 4. **Stack Pointer (SP)**
- **Purpose**: Points to the top of the stack, a special area in memory used for temporary storage during function calls and interrupt handling.
- **Usage**: The stack pointer is modified when data is pushed onto or popped from the stack, enabling nested function calls and return addresses to be stored and retrieved.
- **Example**: In many microcontrollers, the SP is automatically adjusted when the CPU executes `PUSH`, `POP`, `CALL`, or `RET` instructions.

### 5. **Status Register / Flag Register**
- **Purpose**: Holds flags that indicate the results of operations, such as zero, carry, overflow, and negative flags.
- **Usage**: These flags are used by the CPU to make decisions during program execution, such as determining whether to branch based on the outcome of a comparison.
- **Example**: Common flags include the Zero (Z) flag, Carry (C) flag, and Negative (N) flag.

### 6. **Accumulator**
- **Purpose**: A special-purpose register used to store the results of arithmetic and logic operations.
- **Usage**: The accumulator is central to most operations in a microcontroller, as it often holds one of the operands and stores the result of an operation.
- **Example**: In an 8-bit microcontroller, the accumulator might be referred to as register A or ACC.

### 7. **Instruction Register (IR)**
- **Purpose**: Holds the current instruction that is being decoded and executed by the CPU.
- **Usage**: After an instruction is fetched from memory, it is loaded into the IR, where it is then decoded to determine the operation to be performed.
- **Example**: The IR is internal to the CPU and is typically not directly accessible by the programmer.

### 8. **Data Pointer/Index Register**
- **Purpose**: Used to point to data in memory, often in conjunction with indirect addressing modes.
- **Usage**: Index registers are used to iterate over arrays or access memory locations dynamically.
- **Example**: Registers like X and Y in 8-bit microcontrollers, or `DPTR` in 8051 microcontrollers.

### 9. **Interrupt Registers**
- **Purpose**: Used to manage and control interrupt functionality, including enabling/disabling interrupts and handling interrupt priorities.
- **Usage**: These registers often include flags that indicate whether an interrupt has occurred, as well as control bits to enable or configure interrupts.
- **Example**: `INTCON` in PIC microcontrollers or `IE` and `IP` registers in 8051 microcontrollers.

### 10. **Configuration Registers**
- **Purpose**: Used to configure various aspects of the microcontroller's operation, such as oscillator settings, power modes, and peripheral configurations.
- **Usage**: These registers are usually set at the beginning of a program to configure the microcontroller's environment.
- **Example**: `CONFIG` registers in many microcontrollers are used to set clock sources, watchdog timers, and other system-wide settings.

Registers are essential to the efficient operation of a microcontroller, providing the CPU with the necessary data and control to execute programs swiftly and accurately.

## Bit Value
The bit value, such as 8-bit, 16-bit, or 32-bit, refers to the width of the data that a microcontroller (or any processor) can process or handle in a single operation. This bit width is directly related to the architecture of the CPU and influences several aspects of the system, including its processing power, memory addressing capability, and the complexity of the operations it can perform. Here’s what these bit values signify:

### 1. **8-Bit Microcontroller**
- **Data Width**: The CPU processes data in chunks of 8 bits (1 byte) at a time. This means that the largest number it can handle directly in one operation is 255 (or 2^8 - 1).
- **Memory Addressing**: An 8-bit microcontroller can typically address up to 64 KB of memory (assuming a 16-bit address bus, since 2^16 = 65,536).
- **Applications**: Often used in simple, low-power applications like small embedded systems, household appliances, and basic control tasks.
- **Examples**: Microcontrollers like the Intel 8051, Atmel AVR (ATmega328), and PIC16 series.

### 2. **16-Bit Microcontroller**
- **Data Width**: The CPU processes data in chunks of 16 bits (2 bytes) at a time. This allows it to handle numbers up to 65,535 (or 2^16 - 1) in a single operation.
- **Memory Addressing**: A 16-bit microcontroller can typically address up to 64 KB of memory, although some architectures use extended addressing to handle more.
- **Applications**: Used in more complex embedded systems, such as automotive control, industrial automation, and more sophisticated appliances.
- **Examples**: Microcontrollers like the Texas Instruments MSP430, Microchip PIC24, and some ARM Cortex-M3 cores.

### 3. **32-Bit Microcontroller**
- **Data Width**: The CPU processes data in chunks of 32 bits (4 bytes) at a time. It can handle numbers up to 4,294,967,295 (or 2^32 - 1).
- **Memory Addressing**: A 32-bit microcontroller can address up to 4 GB of memory (since 2^32 = 4,294,967,296), although many embedded systems have less physical memory.
- **Applications**: Used in advanced embedded systems, including high-performance consumer electronics, networking equipment, and complex control systems.
- **Examples**: Microcontrollers like the ARM Cortex-M4, ARM Cortex-M7, and some models of the ESP32 series.

### 4. **64-Bit Microcontroller**
- **Data Width**: The CPU processes data in chunks of 64 bits (8 bytes) at a time. It can handle extremely large numbers, up to 18,446,744,073,709,551,615 (or 2^64 - 1).
- **Memory Addressing**: A 64-bit microcontroller can theoretically address up to 16 exabytes of memory (2^64 bytes), though practical systems have much less.
- **Applications**: Found in very high-performance applications, such as advanced computing systems, powerful embedded systems, and modern processors in PCs and servers.
- **Examples**: Some advanced ARM cores (like ARM Cortex-A series), and many modern desktop processors.

### Summary of Implications:
- **Processing Power**: A higher bit width generally means the microcontroller can process larger chunks of data more quickly, leading to better performance for certain tasks.
- **Memory Addressing**: The bit width also affects how much memory the microcontroller can directly address, with larger bit widths allowing access to more memory.
- **Complexity and Cost**: Higher bit-width microcontrollers are typically more complex and expensive, but they offer greater capabilities for more demanding applications.

When choosing a microcontroller, the bit value is an important consideration, as it directly impacts the performance and suitability of the microcontroller for a given task.

## ADC
ADC typically refers to a **Analog-to-Digital Converter (ADC)**, which is a crucial component in embedded systems and electronics. An ADC converts an analog signal (a continuous voltage) into a digital representation that a microcontroller or processor can process. Here’s a more detailed overview of ADCs and their key aspects:

### 1. **Basic Concept**
- **Analog Signal**: Continuous signal, such as a voltage or current, that varies over time.
- **Digital Signal**: Discrete signal in binary form (0s and 1s) that can be processed by digital systems.

### 2. **How ADC Works**
1. **Sampling**: The ADC periodically samples the analog signal at specific intervals.
2. **Quantization**: The sampled signal is then quantized into discrete values based on the ADC’s resolution.
3. **Encoding**: The quantized values are converted into a binary number that represents the analog signal.

### 3. **Key Parameters of ADC**
- **Resolution**: The number of bits used to represent the analog signal. For example, an 8-bit ADC can represent 256 different values (2^8), while a 12-bit ADC can represent 4096 values (2^12).
- **Sampling Rate**: How often the ADC samples the analog signal per second, measured in samples per second (SPS) or Hertz (Hz).
- **Reference Voltage**: The maximum voltage that the ADC can measure. The range of the ADC is typically from 0V to the reference voltage.

### 4. **Types of ADC**
- **Successive Approximation Register (SAR) ADC**: Uses a binary search algorithm to approximate the analog input voltage. Commonly used due to its balance of speed and resolution.
- **Delta-Sigma ADC**: Uses oversampling and noise shaping to achieve high resolution and accuracy. Often used in applications requiring high precision.
- **Flash ADC**: Uses a bank of comparators to convert the analog signal to a digital value in a single step. Very fast but typically has lower resolution.
- **Integrating ADC**: Measures the input signal by integrating it over time. Provides high accuracy but is generally slower.

### 5. **Application Examples**
- **Microcontrollers**: Many microcontrollers have built-in ADCs for reading sensor data, such as temperature sensors, light sensors, and potentiometers.
- **Audio Systems**: Converts analog audio signals into digital data for processing and playback.
- **Instrumentation**: Measures physical quantities (e.g., voltage, current) and converts them into digital form for analysis and display.

### Example in Microcontrollers
Here’s a simple example of how you might use an ADC in a microcontroller (e.g., Arduino) to read an analog voltage:

```cpp
int analogPin = A0;  // Pin where the analog sensor is connected
int sensorValue = 0; // Variable to store the ADC result

void setup() {
    Serial.begin(9600); // Start serial communication
}

void loop() {
    sensorValue = analogRead(analogPin); // Read the analog input
    Serial.println(sensorValue);         // Print the result to the Serial Monitor
    delay(1000); // Wait for 1 second before the next read
}
```

## DAC
A **Digital-to-Analog Converter (DAC)** is a crucial component in electronics and embedded systems, serving the opposite function of an Analog-to-Digital Converter (ADC). A DAC converts digital data (usually binary) into an analog signal, such as a continuous voltage or current.

### 1. **Basic Concept**
- **Digital Input**: The input to a DAC is a digital value, typically represented in binary form (e.g., 8-bit, 16-bit, etc.).
- **Analog Output**: The output is an analog signal, which can vary continuously over a range of values, such as a voltage between 0V and a reference voltage.

### 2. **How DAC Works**
1. **Digital Input**: The DAC receives a binary value as input. For example, an 8-bit DAC might receive a value between 0 (00000000) and 255 (11111111).
2. **Conversion Process**: The DAC converts this digital value into a corresponding analog voltage or current. The conversion process involves switching circuits, resistors, and capacitors to produce the analog output.
3. **Analog Output**: The analog output is a continuous signal, which can be used to control other devices, generate sound, or represent data in an analog form.

### 3. **Key Parameters of DAC**
- **Resolution**: The number of bits in the digital input determines the DAC's resolution. A higher resolution means the DAC can produce more precise analog output values. For example, a 12-bit DAC can produce 4096 distinct output levels.
- **Reference Voltage**: The maximum output voltage the DAC can generate. The output range is typically from 0V to the reference voltage.
- **Sampling Rate**: The speed at which the DAC can convert digital values to analog signals, usually measured in samples per second (SPS) or Hertz (Hz).
- **Settling Time**: The time it takes for the DAC output to stabilize after a change in the digital input.

### 4. **Types of DAC**
- **Binary Weighted Resistor DAC**: Uses resistors with binary-weighted values to convert the digital input to an analog output. Simple but can be impractical for high-bit resolutions due to resistor accuracy requirements.
- **R-2R Ladder DAC**: Utilizes a network of resistors with only two values, making it easier to implement with high precision.
- **Delta-Sigma DAC**: Uses oversampling and noise shaping to produce high-resolution outputs. Often used in high-fidelity audio applications.
- **Pulse Width Modulation (PWM) DAC**: Converts a digital signal to an analog signal using pulse width modulation, often followed by filtering to smooth the output.

### 5. **Application Examples**
- **Audio Output**: DACs are widely used in audio devices to convert digital audio signals into analog sound waves that can be amplified and played through speakers.
- **Signal Generation**: In function generators or arbitrary waveform generators, DACs are used to produce precise analog signals from digital inputs.
- **Control Systems**: DACs are used to convert digital control signals into analog signals to drive actuators, motors, or other analog devices.
- **Video Output**: In video equipment, DACs convert digital video signals into analog signals that can be displayed on monitors or TVs.

### Example in Embedded Systems
In a microcontroller, you might use a DAC to generate an analog voltage corresponding to a digital value:

```cpp
int digitalValue = 128;  // Example 8-bit digital value
analogWrite(pin, digitalValue);  // Output analog signal on the specified pin
```

### Summary
A DAC is essential for converting digital data into an analog form that can interact with the physical world. It’s a key component in audio, video, and control systems, enabling digital devices to produce analog signals that can drive speakers, displays, motors, and other analog hardware.

## I2S
**I2S (Inter-IC Sound)** is a standard serial bus interface used to connect digital audio devices. It is specifically designed for the transmission of digital audio data between components such as microcontrollers, digital signal processors (DSPs), digital-to-analog converters (DACs), analog-to-digital converters (ADCs), and other audio-related ICs.

### 1. **Basic Overview**
- **Purpose**: I2S is used to transfer audio data in a digital format, reducing the noise and degradation associated with analog signals.
- **Data Types**: It handles pulse-code modulated (PCM) audio data, typically used in applications such as audio playback and recording.

### 2. **I2S Bus Components**
- **Master Device**: Controls the clock signals and the data flow. Often, a microcontroller or DSP acts as the master.
- **Slave Devices**: Receives clock signals from the master and sends or receives audio data accordingly. Common slave devices include DACs, ADCs, or audio codecs.

### 3. **I2S Signal Lines**
- **SD (Serial Data)**: This line carries the actual audio data. It can be unidirectional or bidirectional, depending on whether the device is sending or receiving data.
- **SCK (Serial Clock)**: The clock signal that synchronizes the data transfer. It’s generated by the master device and used to shift the data bits in and out.
- **WS (Word Select)**: Also known as LRCK (Left/Right Clock), this signal indicates which audio channel (left or right) is being transmitted. The signal changes state at the beginning of each audio sample.
  - `WS = 0` (Low): Left channel data is being transmitted.
  - `WS = 1` (High): Right channel data is being transmitted.
- **MCLK (Master Clock)**: Often used in more complex systems, MCLK is a higher frequency clock that serves as a reference clock for generating the serial clock (SCK) and word select (WS) signals. Not all I2S systems use MCLK.

### 4. **I2S Audio Data Format**
- **Word Length**: The number of bits used to represent each audio sample, typically 16, 24, or 32 bits.
- **Data Format**: PCM audio data, with separate channels for left and right audio.
- **Bit Clock Rate**: The frequency of the serial clock (SCK) determines the rate at which data bits are transmitted. It is a multiple of the sample rate, depending on the word length and the number of channels.

### 5. **Typical Use Cases**
- **Digital Audio Players**: To connect a microcontroller or DSP to a DAC for high-quality audio output.
- **Microphones**: To transmit digital audio data from a digital microphone to a processor or microcontroller.
- **Bluetooth Audio Modules**: Often use I2S to interface with audio codecs for wireless audio transmission.
- **Sound Cards**: In computers, I2S is used internally to connect various audio components.

### Example of I2S in a Microcontroller (Arduino or ESP32)
Here's a conceptual example of how you might set up I2S communication in an ESP32 to output audio data:

```cpp
#include "driver/i2s.h"

void setup() {
  // Configure I2S settings
  i2s_config_t i2s_config = {
      .mode = I2S_MODE_MASTER | I2S_MODE_TX,  // Master mode and transmit data
      .sample_rate = 44100,                   // Sample rate
      .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT, // 16-bit audio
      .channel_format = I2S_CHANNEL_FMT_RIGHT_LEFT, // Stereo
      .communication_format = I2S_COMM_FORMAT_I2S,  // I2S format
      .intr_alloc_flags = 0,  // Interrupt level
      .dma_buf_count = 8,
      .dma_buf_len = 64,
  };

  // Configure I2S pins
  i2s_pin_config_t pin_config = {
      .bck_io_num = 26,   // Bit clock pin
      .ws_io_num = 25,    // Word select pin (LRCK)
      .data_out_num = 22, // Data output pin
      .data_in_num = -1   // Data input pin (not used in this example)
  };

  // Install and start I2S driver
  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL);
  i2s_set_pin(I2S_NUM_0, &pin_config);
}

void loop() {
  // In a real application, you would write audio data to the I2S bus here.
}
```