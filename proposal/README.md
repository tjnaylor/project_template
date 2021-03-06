

# IDS6145(SimTech 2018) - Research Plan

> * Group Name: Denominators
> * Group participants names: Jared Clark, Kamryx Davis & Jacob "TJ" Naylor
> * Project Title: Model Emergency Replenishment Supply Chain to the Port Saint Lucie, Florida Nuclear Power Station

##Abstract:

Natural disasters such as earthquakes, tsunami’s and hurricanes cause extensive damage to the affected areas and require substantial resources to rebuild the communities. Emergency managers at all levels must diligently allocate resources and supply replenishments. It is a process that involves a great deal of planning and preparation prior to an incident (NRC, 2017, pg. 1). In 2011, Port Saint Lucie nuclear power plant had 1,271,947 people living within 50 miles. The large population near the Port Saint Lucie nuclear power station, requires significant logistics resources to replenish the power plant and the local community following a natural disaster. This study uses Anylogic to model the emergency replenishment supply chain to the Port Saint Lucie, FL Nuclear Power Station after a natural disaster damages both primary and auxiliary power. The resupplying of the nuclear plant provides vital supplies to the plant to prevent a nuclear reactor accident as well as humanitarian aid to the local community. This study supports disaster relief efforts to a local community and provides solutions to emergency response leaders on how to logistically provide aid to the area in the event of a natural disaster and a possible reactor accident.


![**Saint Lucie Nuclear Power Station**](images/SLNPS.png)


## General Introduction

Natural disasters cause significant damage and require substantial resources to support the affected area. Allocating emergency resources is a critical requirement for emergency managers at all levels and requires a great deal of planning and preparation prior to an incident (NRC, 2017, pg. 1). More recently, the hurricane damage in 2017 to Key West, Florida and Puerto Rico are prime examples of how difficult and extensive hurricane damage can be.  Additionally, the Haiti earthquake in 2010 is another example of severe consequences of a natural disaster, however, the relief efforts for those examples would have been exacerbated if the incident affected a nuclear facility. Considering disasters such as Fukushima Daiichi, it is imperative that nuclear facilities practice procedures to handle natural disasters and mitigate further damage to the affected area. Locally, the Port Saint Lucie, Florida Nuclear Power Station requires significant support should a natural disaster affect the area. In 2011, MSNBC using 2010 Census data conducted a study on populations within 5,10, 20 and 50 miles of nuclear power plants in the United States (Dedman, 2011). The Port Saint Lucie power plant was one of the sixty-five locations studied out of the 104 commercial nuclear power reactors in the United States. The population within 10 miles of Port Saint Lucie was 206,595 and 1,271,947 within 50 miles. The population increase from the 2000 Census was 49.7 percent and 37 percent respectively (Dedman, 2011). Given the large population within 50 miles of the Port Saint Lucie nuclear power station, logistics support to the power plant and the local community following a natural disaster is critical. 

Currently, the Nuclear Regulatory Commission (NRC) along with federal and local agencies conduct biennial training for emergency preparedness of nuclear facilities across the United States (NRC, 2017, pg. 1). The emergency preparedness training primarily focuses on the response to and mitigation of radiation exposure to the public. Given the scope of the NRCs training with the nuclear facilities, there is little emphasis on logistics planning outside of the immediate containment and mitigation of nuclear radiation which leaves a preparedness gap for humanitarian support to the local community. This study uses Anylogic to model the emergency replenishment supply chain to the Port Saint Lucie, FL Nuclear Power Station after a natural disaster damages both primary and auxiliary power to prevent a nuclear reactor accident similar to Fukushima Daiichi. The purpose of this research is to determine how to replenish the nuclear power station and supply the local populace in a degraded environment after a major hurricane. Due to the significant damage from the hurricane, we hypothesize that the nuclear power station will require limited replenishment, approximately 176,515 personnel will remain in the Port Saint Lucie area and require logistics support and that aerial and ground transportation is the most successful transportation combination to replenish the nuclear power station and supply the local populace. Refinement of emergency response plans will save lives due to decreased response times and also reduce risk to critical infrastructure. This project makes the following contributions:

1. Provides logistics solutions to replenish the Port Saint Lucie nuclear power station.

2. Provides logistics solutions to support disaster relief efforts to the Port Saint Lucie community.

3. Offers M&S solutions to improve emergency response planning. 

![**Hurricane Scale**](images/HurricaneScale.png)

## The Model

The logistics support to the Port Saint Lucie nuclear power station following a natural disaster is substantial and complex. Given the severity of the situation, supplies may be delivered by land, air, or sea. The structural and behavioral diagrams included below capture the most relevant logistic aspects required during an emergency event to the Port Saint Lucie nuclear power plant and community. The model simulates the logistics flow to the Port Saint Lucie nuclear power plant and community. Specific airframes, ground transportation vehicles and vessels are identified in the model to give a realistic depiction of the supply chain.



![**Object Diagram**](images/StructuralDiagram.png)

![**Behavioral Diagram**](images/Emergency_Resp_Act_Diagram.png)


## Fundamental Questions

1. How can we safely replenish the nuclear power station?

2. How do we provide humanitarian aid to the local populace?

3. What are the resources required to accomplish the above questions?

4.  Based on the disaster and conditions, which mode of transportation (ground,air, and/or sea) would be the most efficient mode to deliver supplies and aid?

## Literature Review

Davis and Proctor (2016) discussed the concern for a nuclear plant Spent Fuel Pool (SFP) cooling and water replenishment during emergencies and natural disasters. They compared worst-case water loss rates to the published water throughput volumes several alternative water replenishment response methods useful in hypothetical disaster, response and mitigation scenarios. As discussed, this research focused on replenishing the water for the power station and therefore did not discuss the supply chain required to replenish the power station as a whole or the surrounding community. It helped inform our disaster relief concerns as they pertain to the quantity of water required for replenishment of the Port Saint Lucie Nuclear power station SPF. 
 
Dedman (2011) discussed the growing population in and around nuclear power plant locations across the country. He identified 65 locations of the 104-nuclear power plants across the U.S where the most population growth occurred. Of those, Port Saint Lucie was identified as one of the areas with a large population influx topping over one million people within a 50-mile radius of the power station. Dedman’s research documented the large population in and around the Port Saint Lucie power station but it does not address how those people would be support logistically during an emergency response incident. His research on population growth of the Port Saint Lucie area helped inform our population and logistics estimates for disaster response operations.
 
Sweeney (2017) discussed the probability of Floridians evacuating the area when the governor gives an evacuation order to residents. He identified that approximately 42% of Floridians will likely remain with the home and pets during a natural disaster. His research on the evacuation tendencies of Floridians during a natural disaster helped inform our population estimates and logistics requirements for Port Saint Lucie area during a disaster response.


## Expected Results
Due to the complex nature of emergency management operations the answer to the problem will be multifaceted and dynamic as conditions change. We predict that the most efficient mode to transport relief materials will be a combination of air and sea based assets until road conditions can be cleared. We also predict that stationing critical nodes for supplies will be crucial to providing assistance to both the NPS and surrounding area. The nodes will be dedicated to either providing NPS replenishment or humanitarian aid because of their unique needs. We predict that 42% of the population will remain in the local area however, the number of resources required will be dependent on the severity of the conditions.

## Research Methods
We will be using AnyLogic. A mixture of discrete event based simulation and agent based simulation. Discrete event based simulation will be used because the supply replenishment is triggered by the natural disaster to the power plant. Agent based simulation will be used because based on the conditions agents will distribute and replenish the supplies to agents at the nuclear plant and agents in the civilian population. We will be using imported data from various sources.

This research uses the Federal Emergency Management Agency (FEMA) National Response Framework, focusing on response, (figure 1) as well as a FEMA  inspired  [**Scenario**](![**Scenario**](proposal/HurricaneScenariov1.docx) to address the disaster response situation. This research does not require the use of human subjects; however, a scenario was developed to scope response efforts and guide our simulation research. As stated previously, Anylogic will be used to simulate the supply chain for replenishment and disaster relief efforts. Three simulation iterations will be executed to help identify the most effective combination of transportation (land, sea, air) methods to provide support to the distressed populace and nuclear power station. The supply chain will be limited to no more than three locations on a given supply route and travel no further than 60 miles and all vehicles will undergo routine maintenance during the time of use. Timestamps of each transportation combination will be taken to distinguish the most successful resupply operations. Lastly,  we will use GIS and SPF consumption  datasets to plan disaster repsonse operations for the Port Saint Lucie nuclear power station.

![**FEMA NRF**](images/FEMANRF.png)

Figure 1: Mission Integration within the National Preparedness System (FEMA 2015)

Downloaded from americansecuritytoday.com on 2/22/2018 at 10:00 am by tj.naylor@knights.ucf.edu.







