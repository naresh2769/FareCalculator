# FareCalculator – CityCab Travel Optimizer (Python Project)

## Project Description

FareCalculator is a Python-based command-line application that estimates ride fares for a ride-sharing service called **CityCab**.  
The fare is calculated based on:

- Distance travelled
- Vehicle type selected
- Time of travel (Peak / Non-Peak hours)

The system applies **surge pricing automatically** during peak hours to simulate real-world ride-sharing platforms.

---

## Features

Vehicle-based pricing using dictionary mapping  
Surge pricing logic during peak hours (5 PM – 8 PM)  
Modular function-based structure  
Error handling for invalid inputs  
Supports multiple ride calculations  
Generates formatted ride receipt  

---

## Pricing Structure

| Vehicle Type | Rate per km |
|-------------|-------------|
| Economy     | ₹10         |
| Premium     | ₹18         |
| SUV         | ₹25         |

