# Improved Town Industries

## Changelog

### 1.0.0
July 15, 2020

- Release

### 1.0.1
July 16, 2020

- Add: Parameter to enable elevation requirements for Coal Mine, Farm, and Oil Wells (fixes #1)
- Change: Use Default TTD strings for industry names where possible to utilize base game translations. Exceptions:
  - Nearby station names must use literal strings
  - Power Plant and Logging Camp strings don't exist in OpenTTD (they are called "Power Station" and "Lumber Mill")
- Fix: Industries can be funded as intended (fixes #3)
- Fix: Remove industry limit when using funding "Many random industries" in Scenario Editor (fixes #3)
- Fix: Secondary industries can be funded when "Generate primary only" parameter is enabled (fixes #4)
- Fix: Oil Refinery no longer needs to be near water when funding "Many random industries" in Scenario Editor

### 1.0.2
July 16, 2020

- ~~Add: Parameter to require oil refineries to generate near water~~ Removed in 1.1.0

### 1.1.0
July 18, 2020

- Add: Farms accept Chemicals as fertilizer
- Add: Loading ITI on a map smaller than 256x256 now gives a fatal error rather than breaking without notice, since industries won't generate below this size
- Change: Factory always accepts Food
- Change: Rewrite parameter description for elevation requirement
- Fix: Disable all default cargos and define from scratch
- Remove: Parameter to change Factory acceptance of Food. Factory now always accepts Food.
- Remove: Parameter to disable extractive industry clustering
  - Map size check already handles this well; no need for confusion
- Remove: Parameter to require oil refineries to generate near water
  - Simplification of an unneccesary parameter. This requirement is already disabled in Scenario Editor and funded industries, so its only use is for industries created during world generation or during a game.

### 1.2.0
July 19, 2020

- Fix: Override special flags for Oil Wells to allow production increases and build past 1950
- Fix: Redefine cargo IDs for proper ordering in the Cargo Flow Legend
- Fix: Map too small error triggers properly on rectangular maps

### 1.2.1
July 22, 2020

- Fix: Houses now produce Mail properly, instead of Goods

### 1.2.2
July 25, 2020

- Change: Population requirement for Factory reduced to 100 if Improved Town Layouts is loaded with the Reduced Early House Population parameter active 
- Fix: Map too small error actually requires 256x256, not 256x512

### 1.3.2
July 31, 2020

- Fix: Cargo labels reorganized (again) to fix Goods and Food acceptance by base game houses (#7)
- Change: Rewritten NewGRF description mentions the need for NewGRF vehicles (#8)

### 1.4.0
August 11, 2020

- Add: Parameter to disable automatic field generation
- Add: Decorative objects for each type of farm field, with terrain awareness
- Add: Additional industry tile layouts for Coal Mine, Logging Camp, Oil Refinery, Paper Mill, and Factory
  - Thanks to YaoAngelsin for designing many of these
- Add/Change: Added parameter to make Logging Camp behave like the vanilla Forest. This is the new default, but players can still choose the previous sub-tropic Lumber Mill behavior.

### 1.5.0
August 29, 2020

- Add: Waste & Recycling (see Readme)
- Add: Chemicals delivered to Farms (as fertilizer) are now converted into Food at a 1:1 rate, as with deliveries to the Paper Mill
- Add: Loading ITI alongside most incompatible industry sets throws a fatal error which disables ITI. The list of incompatible industries is defined manually, so please notify me of new/additional incompatible NewGRFs.
- Codechange: Industries now have defined industry IDs for future update stability