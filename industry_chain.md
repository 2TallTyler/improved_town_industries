# Industry Chain

## Objects
* Create objects of all industry tiles, for expansion as well as mocking up industry sprite kitbashes in different graphics sets

## Parameters
* Generate primary industries only
* Industries need workers (passengers)
* Locate processing industries near towns

## Cargos

* Passengers (workers/commuters)
* Goods
* Oil
* Chemicals
* Grain
* Milk
* Alcohol
* Food
* Coal
* Iron
* Steel
* Wood

## Oil Chain

### Oil Wells
* Availability:		1900
* Produce: 			Oil
* Receive: 			None

### Oil Rig
* Availability:		use default		
* Produce: 			use default

### Oil Refinery
* Availability:		1900
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Oil
* Produce: 			Goods, Chemicals
* Location: 		Nearby Town

## Food Chain

### Farm 
* Availability:		Always
* Receive (boost):	Chemicals
* Produce: 			Food

### Brewery
* Sprite: 			Food Processing Plant
* Availability:		Always		
* Location:			Nearby Town
* Commuters:		Passengers
* Receive: 			Food
* Produce: 			Alcohol

## Steel Chain

### Coal Mine
* Availability:		Always
* Commuters: 		Passengers
* Location:			Nearby Town
* Produce: 			Coal

### Iron Mine
* Availability		1856-
* Location:			Nearby Town
* Commuters: 		Passengers
* Produce: 			Iron

### Steel Mill
* Availability:		1856-
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Iron, Coal
* Produce: 			Steel 

## Factory
* Location:			Nearby Town
* Commuters:		Passengers
* Receive:			Steel, Wood, Recyclables?
* Produce:			Goods

## Power Plant
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Coal

## Wood Chain

### Forestry
* Availability:		Always
* Produce: 			Wood

### Paper Mill
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Wood, Chemicals, Recyclables?
* Produce: 			Goods





Other Sprites:

* Printing Plant
* Gold Mine
* Copper Ore Mine
* Water Tower
