# Industry Chain

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
* Food
* Coal
* Iron
* Steel
* Wood

## Oil Chain

### Oil Wells
* Availability:		1900
* Location:			Country
* Produce: 			Oil
* Receive: 			None

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
* Location:			Country
* Receive (boost):	Chemicals
* Produce: 			Food

## Steel Chain

### Coal Mine
* Availability:		Always
* Commuters: 		Passengers
* Location:			Country
* Produce: 			Coal

### Iron Mine
* Availability		1856-
* Location:			Country
* Commuters: 		Passengers
* Produce: 			Iron

### Steel Mill
* Availability:		1856-
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Iron, Coal
* Produce: 			Steel 

## Factory
* Availability:		1800+
* Location:			Nearby Town
* Commuters:		Passengers
* Receive:			Steel, Wood
* Produce:			Goods

## Power Plant
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Coal, Oil

## Wood Chain

### Forestry
* Availability:		Always
* Produce: 			Wood

### Paper Mill
* Location:			Nearby Town
* Commuters: 		Passengers
* Receive: 			Wood, Chemicals, Recyclables?
* Produce: 			Goods

## Recyclables Chain

Produced by houses

Accepted by power plant (waste to energy)

Recycle Center
* Receive:			Recyclables
* Produce:			
	* Scrap to Steel Mill (metals)
	* Fertilizer to farms (organic waste)
	* Waste paper to paper mill (paper products)
	* Plastic to factories (plastic waste)



Other Sprites:

* Printing Plant
* Gold Mine
* Copper Ore Mine
* Water Tower
