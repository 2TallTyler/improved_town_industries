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