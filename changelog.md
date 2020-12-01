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
  - A big thanks to **jrook1445** for helping me understand the house production loop and writing clever code, and to **/u/Pop06095** on reddit for playtesting and providing great feedback!
- Add: Chemicals delivered to Farms (as fertilizer) are now converted into Food at a 1:1 rate, as with deliveries to the Paper Mill
- Add: Loading ITI alongside most incompatible industry sets throws a fatal error which disables ITI. The list of incompatible industries is defined manually, so please notify me of new/additional incompatible NewGRFs.
- Codechange: Industries now have defined industry IDs for future update stability

### 1.5.1
September 2, 2020

- Change: Primary industries may generate in (owned by) a city
  - The minimum distance still applies, but if a player starts a game with "Proportion of towns that will become cities" set to 1 in 1, primary industries will now generate
  - Banning primary industries next to cities has not proved necessary
- Fix: Recycling Center obeys "Generate Primary Industries Only" parameter

### 1.6.0
November 8, 2020

- Add: Nuclear Energy chain
  - Uranium Mine
    - Accepts Chemicals
	- Produces Uranium, Passengers
  - Nuclear Fuel Plant
    - Accepts Uranium, Nuclear Waste
	- Produces Nuclear Fuel, Passengers
  - Power Plant (existing industry)
    - Accepts Nuclear Fuel, Oil, Coal, Waste
	- Produces Nuclear Waste, Passengers
- Add: Oil Rigs are back! (identical to Vanilla)
- Add: Sawmill processes Wood into Lumber
- Add: Forest produces Wood (replaces Logging Camp, identical to vanilla Forest)
- Add: Farms accept Waste; feeding it to the pigs generates 1 ton of Food per 4 tons of Waste delivered (Recycled Materials has a 1:1 ratio, incentivizing a change once the Recycling Center is invented in 1945)
- Add: Secondary industry passenger production is scaled to cargo deliveries
  - Each industry employs 1 worker per 4 units of cargo delivered
  -  Symmetric Cargodist should route passengers back to the industry as workers headed to work
  -  Passengers are no longer "Requires" cargos but are still accepted by industry tiles
- Add: Secondary industries now close if cargo is not delivered for 5 years (vanilla behavior, previously disrupted by passenger generation)
- Add: Waste & Recycling now compatible with other house sets which generate Waste
  - Improved Town Layouts
  - OpenGFX Mars Houses - Late Start
- Add: Error messages for incompatible industry NewGRFs now specifies which NewGRF is incompatible
- Fix: Coal and Iron Mines now have a safety valve on their clustering mechanic, preventing a deadlock where the next mine is required to be within 100 tiles of another mine, but no owning town is within range
- Change: Transporting Waste pays slightly more
- Change: Waste & Recycling parameter text and error now requires Improved Town Layouts 1.3.0 (removes year >= 1882 limit for Waste production, now that Farms accept Waste)
- Change: Use base game industry count management instead of handling it within ITI
- Removed: Parameter for Logging Camp to act like Sub-Tropic Lumber Mill

### 1.6.1
November 19, 2020

- Add: German translation by WoelfiVW
- Codechange: Remove unused strings from depreciated parameters

### 1.6.2
November 20, 2020

- Fix: German translation

### 1.6.3
November 21, 2020

- Fix: Sawmills accept passengers

### 1.7.0
TBD

- Add: Processing industries in towns are now grouped into "industrial zones," within 15 tiles of another industry
- Change: Rebalanced industry funding costs
  - Sawmills are the cheapest industry to fund, possible to fund with a standard £300k starting loan in addition to an initial train line (Iron Horse 2)
  - Power Plants are another good starting industry, only slightly more expensive than the Sawmill and accepting either Coal or Oil (or Waste, when enabled).
  - Recycling Centers are relatively inexpensive but are not a good starting industry since small towns won't produce much Waste.
  - The Factory is the standard Goods origin and isn't affordable with the starting loan, but won't be too hard to save up for.
  - The Paper Mill also produces Goods, but unlike the Factory it accepts Wood directly without needing a Sawmill or Steel Mill. This benefit, and the complexity of paper-making, makes it more expensive than the Factory.
  - Steel Mills and Oil Refineries are an impressive industries and an expensive investment.
  - Nuclear Fuel Plants are high-tech and quite pricey.
- Change: Rebalanced cargo payment rates to new industry funding costs
  - Reduced payments for primary and secondary bulk cargos (Wood, Oil, Uranium, Lumber, Steel, Waste) to incentivize completing further steps of the industry chain
  - Increased payment for Chemicals
  - Reduced payment for Goods
- Change: Coal, Iron, and Uranium mines may build near towns
- Change: Removed industry clustering mechanic, which wasn't noticable and was causing problems
- Fix: When Generating Primary Industries Only, removed incorrect errors created by Sawmills and Nuclear Fuel Plants