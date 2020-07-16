# Improved Town Industries

## Overview

- Simple cargos accepted by multiple industries, designed for asymmetric Cargodist
- Processing industries spawn near towns
- Most industries accept and create passengers as workers
- Industries have realistic invention dates for gameplay as early as 1700
- Includes Object tiles for visually expanding industries
- Designed for Temperate climate only
- Uses only base game sprites, so visually compatible with any base graphics set including original TTD, OpenGFX, aBase, zBase, and NightGFX.
- Requires OpenTTD version 1.10.0, JGR version 0.34, or better.
- Requires NewGRF vehicles which support additional cargos

## Features

### Expanded industry and cargo chains

- Added cargos to Temperate industries and added some industries and behaviors from Sub-arctic and Sub-tropical
- Cargos are generic and have multiple destinations, designed for asymmetric Cargodist gameplay.
  - For example, the Oil Refinery processes Oil into Chemicals, which can be delivered to the Paper Mill or the Factory.
- The additional cargos require NewGRF vehicles which support additional cargos.
- Food can be delivered directly to towns when a NewGRF house set accepts Food (recommended: Improved Town Layouts) or converted to Goods by the Factory

### Processing industries spawn near towns

- Processing industries only build near towns and require 300 population per industry
- Primary industries (Coal Mine, Oil Wells, Farm, etc.) far outnumber processing industries (Factory, Steel Mill, etc.)
- Funded industries can be built without any restrictions

### Industries accept passengers

- Most industries accept and create passengers as workers
  - Exceptions: workers at Farms and Logging Camps live on-site and don't commute
- Delivering passengers does not influence industry production
  - Like town buildings, industries produce passengers without checking if passengers were delivered to them
  - Tying industry passenger creation to delivered passengers isn't possible because imperfect station ratings and symmetric Cargodist would produce a negative feedback loop, eliminating all demand for passenger traffic to industries

### Industries are invented at realistic dates in history

- Always: Farm, Coal Mine, Logging Camp
- 1800: Factory
- 1856: Iron Mine and Steel Mill
- 1882: Power Plant
- 1885: Paper Mill
- 1900: Oil Wells and Oil Refinery

Please set your desired industry density in both the OpenTTD map generation screen and the NewGRF parameters. This is necessary to control industry probability and reserve slots for industries invented after the game starts.

### Includes eyecandy objects

- Nearly all tiles included as objects for expanding industrial areas

## Limitations / Not in Scope

- Since all sprites come from the base graphics set, there are no snow sprites. 
- I don't plan to add compatibility for other climates in this set, but the code is GPL-licensed if you would like to make your own industry set with new graphics.