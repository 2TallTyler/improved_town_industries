# Improved Town Industries

![Trucks drop off Waste at a recycling center while passenger trains bring employees to work](/docs/recycling_center.PNG)

## Overview

- Simple cargos accepted by multiple industries, designed for asymmetric Cargodist
- Processing industries spawn near towns
- Most industries accept and create passengers as workers
- Industries have realistic invention dates for gameplay as early as 1700
- When used with Improved Town Layouts or another compatible house set, adds Waste & Recycling chain
- Includes object tiles for visually expanding industries
- Designed for Temperate climate only
- Uses only base game sprites, so visually compatible with any base graphics set including original TTD, OpenGFX, aBase, zBase, and NightGFX
- Incompatible with other industry sets
- Requires OpenTTD version 1.10.0, JGR version 0.34, or better
- Requires NewGRF vehicles which support additional cargos

## Features

### Expanded industry and cargo chains

- Added cargos to Temperate industries and added some industries and behaviors from Sub-arctic and Sub-tropical
- Cargos are generic and have multiple destinations, designed for asymmetric Cargodist gameplay
  - For example, the Oil Refinery processes Oil into Chemicals, which can be delivered to the Farm as fertilizer, the Factory as plastics, or the Paper Mill as the industrial chemicals used to break down wood pulp.
- The additional cargos require NewGRF vehicles which support additional cargos
- Food can be delivered directly to towns when a NewGRF house set accepts Food (recommended: Improved Town Layouts) or converted to Goods by the Factory

### Processing industries spawn near towns

- Processing industries only build near towns and require 300 population per industry
- Primary industries (Coal Mine, Oil Wells, Farm, etc.) far outnumber processing industries (Factory, Steel Mill, etc.)
- Funded industries can be built without any restrictions

### Industries accept passengers

- Mines have an automatic production level for passengers
- Secondary industries produce 1 passenger per 4 units of cargo delivered
- Many industries accept passengers. This has no effect on cargo production.

### Towns generate Waste 
**(requires Improved Town Layouts)**
- Improved Town Layouts houses produce Waste, which can be transported to the Farm to be fed to the pigs (returns 1/4 ton of Food per ton of Waste) or to the Recycling Center (from 1945) for conversion to Recycled Materials.
- Recycled Materials are accepted at:
  - Steel Mill (scrap metal)
  - Paper Mill (paper and cardboard)
  - Factory (plastics)
  - Farm (organic waste/compost)
- These industries turn Recycled Materials into their usual production (Steel, Goods, or Food), at a 1:1 rate, giving you more secondary products to transport

### Industries are invented at realistic dates in history

- Always: Farm, Coal Mine, Forest
- 1800: Factory, Sawmill
- 1856: Iron Mine and Steel Mill
- 1882: Power Plant
- 1885: Paper Mill
- 1900: Oil Wells and Oil Refinery
- 1945: Recycling Center
- 1956: Uranium Mine, Nuclear Fuel Plant
- 1960: Oil Rig

### Expand your industries with eyecandy objects

- Nearly all tiles included as objects for expanding industrial areas

## Compatibility
- Not compatible with industry replacement sets which add new cargos (FIRS, ECS vectors, XIS, OpenGFX+ Industries, etc.)
  - Attempting to load any of these NewGRFs in addition to Improved Town Industries will create an error which disables ITI
  - Please let me know of any industry incompatibilities which I've missed in my error message list
- Compatible with some small industry sets which use existing cargos (Beach as Industry, Housing as Industry, etc.)
- NewGRF vehicle sets are **required** to transport new and modified cargos. If you want to keep base game trains, OpenGFX+ Trains keeps the vanilla graphics while adding compatibility for NewGRF cargos.

## Parameters
 
- Generate Primary Industries Only
  - Disable automatic generation of Factories, Steel Mills, Paper Mills, Oil Refineries, Power Plants, and Recycling Centers (if enabled)
  - Does not affect funded industries

- Industry elevation requirements
  - Enable elevation checks for industries. Sea level is level 0.
    - Coal Mines must be elevation 4 or higher
	- Farm and Oil Wells must be elevation 2 or less
  - Do not enable with Very Flat terrain type, as Coal Mine will not generate
  
- Farms build fields
  - Choose if Farms construct fields, as in vanilla OpenTTD
  - Field tiles are available as decorative objects, to construct your own fields

- Enable Oil Rigs
  - Choose whether Oil Rigs appear after 1960 (identical to vanilla industry).

- Enable Nuclear Energy chain
  - Enables Uranium Mine and Nuclear Fuel Plant, from 1956. Power Plant accepts Nuclear Fuel and produces Nuclear Waste.

- Enable Waste & Recycling chain
  - Enables Recycling Center to sort Waste from town buildings into Recycled Materials for transport to industries
  - See section above in README
  - **Requires Improved Town Layouts version 1.3.0 or better**

## Limitations / Not in Scope

- Since all sprites come from the base graphics set, there are no snow sprites. 
- I don't plan to add compatibility for other climates in this set, but the code is GPL-licensed if you would like to make your own industry set with new graphics.
