# Smash-Tournament-Simulation

Tien Huynh

Jesse Yu

MatthewS


# Introduction  {#introduction}


### What is a Smash tournament? {#what-is-a-smash-tournament}

A smash tournament is a tournament in which people compete against each other in the video game Super Smash Brothers on the Nintendo Switch. Specifically we will be looking at the most common type of smash tournaments, which are run as double-elimination brackets in a 1 vs 1 format with a standardized ruleset. Competitive smash brothers tournaments are hosted in person because unlike most games, the low latency of playing in person is essential to fighting games. Many competitors claim that playing with higher latency compromises the games competitive integrity, and makes it less engaging.  Weekly smash tournaments are hosted throughout Washington, in specific we’ll be simulating a tournament that is run weekly out of the UW Seattle Campus. This tournament is called Washington Gaming Association Colosseum, but for the remainder of this development plan we will be referring to it as WGAC. 


### What is needed to run a tournament? {#what-is-needed-to-run-a-tournament}

To run events in person so regularly requires quite a bit of resources that need to be managed carefully. Every event needs consoles to play on. The more consoles a tournament has the quicker it will run. In the case of WGAC the tournament organizers rent out a part of a computer gaming lounge and set up consoles in their in order to run the event. This costs the tournament organizers a certain amount of money per monitor that they choose to reserve for every hour that they choose to reserve it. The amount of money needed to rent equipment for a tournament and the venue  is a key concern. Each entrant is charged a certain amount of money to attend the event, which the organizer uses to rent the equipment. Ideally the tournament organizer should always receive enough entrants to be able to pay for the costs of running the event. Additionally tournaments are restricted by time because tournaments being able to run faster attracts more entrants, and also helps to keep the cost of renting equipment down. Last to run a tournament you need staff members to manage the event. Typically for smaller events of below 30 people there is only one staff member running the event and additional staff is only added when there are more people than the single person can handle. 


### Why would we want to model a Smash tournament? {#why-would-we-want-to-model-a-smash-tournament}

Modeling a smash tournament would be beneficial for the tournament organizers to be able to understand techniques they can use to improve the tournaments they run without having to experiment with it in person and risk ruining the tournament experience for competitors. Especially for this tournament running overtime, is problematic because the building closes at a certain hour. That means if the tournament runs overtime, it just has to end without completion, it cannot be extended. By modeling the tournament series we hope to find ways in which we can lower the costs of running tournaments, improve the amount of time in which tournaments run in, and determine when it’s important to increase the number of staff members a tournament has. Creating such a model will involve modeling the environment of a tournament and simulating the amount of time it will take to run the tournament under different conditions. Examples of such conditions could be the configurations of the consoles in the console room, the number of monitors rented, the number of entrants of the tournament, or the number of staff members and where they are located. 


### What is the basic flow of a Smash tournament? {#what-is-the-basic-flow-of-a-smash-tournament}

In a typical smash tournament all of the players arrive in advance, and then when the tournament starts, the staff members will direct competitors in pairs of 2 to play their matches based on the double elimination bracket. In those pairs of 2 competitors will go to their assigned stations and begin playing their matches. A match consists of setting up controls, and playing games with a time limit of 7 minutes until one player has won either 2 matches (best of 3), or 3 matches (best of 3) depending on how far into the tournament is. For example it’s tradition for tournaments to play the last set of the tournament as a best of 5 instead of as a best of 3. After their match is completed players will pack up their controllers and head to the nearest staff member to report the matches score. The staff member then enters this score into the online bracket and calls the next pair of competitors to play should there be one available in the bracket. Keep in mind because this is a bracket format, matches further on in the tournament depend on earlier matches to be played. This process of calling and reporting matches repeats until everyone in the tournament has lost 2 sets except for one person. This person wins the entire tournament. 

Other factors to consider when running a tournament, are that moving players between the reporting desk and their console stations takes more time based on the number of people at the event, and whether or not they have to walk slowly to pass other competitors. At the discretion of the tournament organizer, some of the console setups could be converted to practice setups for spectators and no longer be used for progressing the tournament. Lastly people can leave throughout the night before the tournament ends, resulting in a less crowded venue. 


# Model Description {#model-description}


### Choice of model {#choice-of-model}

To model a smash tournament we will be using an agent based model with a grid system. This is the best way to model this scenario, because it allows us to more easily assign somewhat unique behavior to each player. Furthermore the grid system will allow us to easily represent space between different objects in our simulation. Having a clear representation of space will be important for calculating accurate time measurements for things such as walking from the reporting station to the console station, and for preventing different types of agents from colliding with one another. 


### What our model can be used for {#what-our-model-can-be-used-for}

This model can be used to better understand the amount of time, money, and staff required to run a tournament under different conditions such as the locations of the console, the number of consoles used, the number of entrants to the event, the number of reporting stations, which round matches become best of 5 and the amount that we charge for the tournament. Performing such a simulation will help us determine the optimal room configuration for a tournament with respect to improving profitability, the speed at which tournaments are run and the number of staff members needed to run the event. 


### Things to keep track of throughout the entire model {#things-to-keep-track-of-throughout-the-entire-model}

To perform our analysis we will have to keep track of a couple key elements, which we will consider as the results of each simulation. Each simulation should return the amount of time the tournament took, the number of players that attended the tournament, the net money of the tournament, and the number of staff members needed to run the event. 


### Describing the Environment  {#describing-the-environment}

Our environment will be split up into two main areas. One area is the waiting areas, where players will be when they are not playing a match. The other area will be the console room, where competitors will be playing their tournament sets. Staff members and reporting stations can be located in either the waiting room or the player room. We will experiment with different numbers of reporting stations to see if the change would make a significant difference.

The environment will keep track of the location of all agents to guarantee that agents do not collide with each other or occupy the same space. In separate 2d arrays of the dimensions of each of the rooms the environment will also keep track of the locations of players, the location of reporting stations, and the location of the consoles, and areas occupied by objects such as tables where other agents are not allowed to walk through. 

	

The environment will keep track of the percentage of each room that is currently occupied by things on the grid. Using this percentage the walking speed of the competitors in the room will be determined by the following equation 4.4 ft/s(average walking speed) - some constant * percentage of room occupied.  


### Configuring the Console layout  {#configuring-the-console-layout}

Across multiple simulations we will have to experiment with the number of consoles that we simulate, the positions of the consoles, and the positions of the reporting station. The placement of all of these things is what we will refer to as the room configuration. Consoles are considered occupied if they have two players sitting in front of them, and considered not occupied if they do not have players sitting in front of them. Consoles are assigned an id number so that they can be identified by the tournament organizer, and are given a location within the console room to occupy. 


### Double Elimination Bracket  {#double-elimination-bracket}

The bracket class will be used by the tournament organizer to determine if there is a match that they can run to further progress the tournament. At the beginning of the simulation all of the players will be added to the bracket based on their id number with random seeding. In tournaments seeding is used to rank the skill level of players, for the sake of this simulation we will assume seeding does not influence the amount of time it takes to run a tournament. The bracket will be filled with pairings between players which are staggered in rounds. For example the winners of two of the matches in the first round, will play in the second round. This means that this second match cannot be run until the first two are complete. 

The bracket is structured by matches which are pairings between two players. Each match also belongs to a round which is a phase of the tournament. For every round there is a winners and losers bracket. At the beginning of the tournament all players start off in round 1 of the winners bracket. When a player wins a match they are moved to the next round of winners bracket. If a player loses a match they are moved down to the same round in the losers bracket. Players are considered eliminated from the tournament if they lose 2 matches, one in the winners bracket and one in the losers bracket. The format of a typical double elimination bracket can be seen in figure 2, which is an example from a WGAC run on challonge.com. 

The bracket will have two primary functions, the first is to get the next possible pairing between players if there is any. The second is to update the scores of matches after they are reported to a staff member. In this simulation we will assume that the order in which matches are run are prioritized first by their round number, and then by their index within that round. 

Figure 1: An example Double Elimination Bracket from Challonge.com   

[https://challonge.com/wgacs7](https://challonge.com/wgacs7)  


### Behavior of Matches  {#behavior-of-matches}

Matches involve 2 players and have multiple phases. At initialization matches are determined to be either first to 2 or first to 3 depending on the choice of the tournament organizer. A match starts when two players sit down at a console together, and the most important thing from the match is the amount of time that it takes to complete. The first phase of the match is players setting up their personal in game controls. There is a 50% chance that the players controls are already on the console that they are playing at, so for each player there is a 50% chance setting up controls will only take 20 seconds(the amount of time to see that their controls are there) or 60 seconds(the amount of time it takes for them to setup their controls). Phase 2 of the match involves playing games until one player has won 2 or 3 games depending on the format of the tournament. Each individual game will take a random amount of time, which will be determined by a binomial distribution with a minimum 2 minutes and maximum 7 minutes. (we will revise these times after collecting more data). The last phase of the match involves the players packing up their controllers and getting up from their station which should take about 30 seconds. After the match completes, the players should head to the reporting station to update the tournament organizer on their score. When the match is over, the match should return the amount of time that it took to complete. 


### Representing the Staff Member / Reporting Station  {#representing-the-staff-member-reporting-station}

To report matches some number of agents representing a staff member will be stationed somewhere within the grid. The reporting station is important because it will deal with the assignment of competitors to their console stations, and reporting the scores of the bracket. We assume that for a match to start, competitors must first be assigned that match by a staff member who gets that pairing from the bracket. Additionally matches in the bracket are only updated after the competitors have told the reporting station the result of their match. This process continues until there are no matches left in the simulation. 

Receiving scores from players takes time, and so does assigning players to their next match. After having a score reported to them the tournament organizer at the reporting station cannot do any other tasks for 30 seconds, to simulate the staff member inputting the scores into the bracket management website. Additionally, calling and assigning players to a station also takes 30 seconds per pair of players.  


### Representing the Player  {#representing-the-player}

Players are assigned numbers at the beginning of the tournament which they will be called by. Each Player occupies a  1ft^2 space, which is a single cell on the grid. The player class deals with the behavior of their own movement. Player movement  is triggered by being given instructions from other agents in the model for example the reporting desk, or the match class. 


### Player movement  {#player-movement}


We will use the grid based model to model the environment. For simplicity, the player follows Von Neuman directions: north, south, west, and east. The player movement follows the following rules:



*   A player must first go to the organizer, get assigned, and go to the console station. After finishing a match, the player goes back to the organizer to report.
*   A player walk path is determined by the destination that the player needs to go to. The next step of the player is based on minimizing the distance between the player and the destination. For example if their destination is SE of them they will randomly walk either South or East.  If the next step is blocked by any obstacle, the player will random-walk to get around.
*   If a player does get called to play in a match, the player will either stay or have a 5% chance of walking in a random unoccupied direction. 
*   A player cannot cross over other players.
*   A player walking speed varies from one area to one area depending on how crowded that area is.
*   A player goes from the waiting area to the playing area or vice versa through doors.
*   A player cannot go to the same area that has a player in place.
*   A player cannot cross over the console area.



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/CSS-4581.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/CSS-4581.png "image_tooltip")


Figure 2: An example of the simulation


### What we will change between simulations  {#what-we-will-change-between-simulations}

Each simulation should define the Number of entrants, Number of consoles, configuration of consoles, Number of reporting stations, locations of reporting stations, the bracket phase at which first to 3 starts, and how much each entrant is charged to compete. If a number of entrants is not given the simulation will randomly generate a number between 25 and 60 to determine the number of players. This reflects the nature that most tournament organizers do not know how many people will be at their event until it happens. 


### Simulation Driver   {#simulation-driver}



1. Initialize console configuration, number of players, 
    *   Time is initialized to be 0
    *   The rental fees are calculated as the number of consoles being used * 3 dollars per hour. 
    *   The Profit of the tournaments is calculated as the number of players * the amount they are being charged - the rental fees. 
    *   Create the environment which will represent the venue 
    *   Place consoles and reporting stations and unreachable areas throughout the environment 
    *   Create a number of players and randomly place them throughout the waiting room. 

 	



2. Start the tournament 
    *   Run the tournament until there are no matches left to be played in the bracket 
    *   Time in the tournament will increment in intervals of 1 second at a time
    *   If there are available consoles to be played at the reporting desk / staff member will call pairs of people to fill those setups until there are either no available matches to be called or there are no empty consoles. 
    *   At each time step if a player has a location that they have been assigned to go towards the will move towards that location. If the player has not been assigned a location then they will have a 5% chance of walking in a random unblocked direction. 
    *   When a player is eliminated from the tournament a random amount of time with minimum 10 minutes and maximum 60 minutes will be assigned to them. This will be the amount of time they will stay in the simulation before choosing to leave. 
3. Return the amount of time that the tournament took and the net profit of the tournament.


# Analysis {#analysis}


### Things we will change {#things-we-will-change}



*   Location of consoles 
    *   This determines the time of players need to walk around to finish their matches, and the walking speed of the area.
*   Number of consoles
    *   The more consoles available, the sooner the tournament ends, but the more expensive the organizer spends for the expenses, which results in less profit or under budget.
*   Number of entrants 
    *   The more entrants (players) there are, the more crowded the room will be. Since players cannot walk into a cell occupied by another player, they will need to walk around others (more time).
*   Number of reporting stations 
    *   Players need to get to the reporting stations to get their match pairings and also to report their scores. We would like to test to see if increasing the number of reporting stations will have a significant impact on tournament time.
*   When best of 5 starts 
    *   Typically the competition starts with best of 3 at the beginning to speed up the process. As the competition progresses, to make it fair to every player, best of 5 is used to increase the chance of winning, but it also consumes more time between matches. Thus, we need to determine when to start best of 5 so the competition becomes more attractive.
*   How much we charge each entrant for the tournament 
    *   Currently, WGAC charges $6 dollars a player for the competition. $3 goes toward prizing, and the other $3 is running the competition. We only count the latter $3 as our competition income. If WGAC still has profit after the end of the tournament, the profit will go toward the next competition. The number of entrants is important because we don’t want WGAC to go under budget, and it has to pay out of its pocket.


### Measures of our model  {#measures-of-our-model}



*   Profit (money gained from entry costs - cost of rentals)
*   Time 
*   Number of staff members 

Based on the project description, we will conduct several analysis such as sensitivity analysis on the tournament run time, the walking distance of players, the cost to run the tournament with a configuration. The run time of the tournament can be based on many different factors but the most important factors are the number of players and guests in the areas, total consoles available for playing, and the console layout. Those factors will directly affect the walking distance of each player, and the cost for each player to stay in the tournament. From the observation, we are interested in the following questions:


### Questions we will ask  {#questions-we-will-ask}



*   Does console layout change affect the overall time to run the tournament?
*   What is the optimal number of consoles that the tournament should rent within the tournament allowance time?
*   Where should we place the organizer so that the players walk minimum distance during the tournament? The lower a distance a player must walk, the better the player* (Unproven but it could make sense)
*   All players need to pay a certain amount of money to join the tournament. How much profit will the organizer receiver after the tournament is over?

During our model’s time evolution, we will investigate how people walk in the areas and where the traffic areas are.



*   How people walk helps re-design the next console layout.
    *   The traffic areas will help determine where the space and walkway should be expanded for easy access and emergency evacuation.


### Validation & Verification  {#validation-&-verification}

To validate and verify our model, we have an existing data from known tournament events, so we can compare our model result against to make sure our model simulates the real world environment.


# Testing  {#testing}


### When running simulations we will plot:  {#when-running-simulations-we-will-plot}



*   The locations of different agents in the environment 
    *   This will help us verify that the agents are moving through the simulation correctly according to the behavior that we have defined for them. 
    *   Players will be represented as red squares which occupy a 1x1 square
    *   Reporting Stations will be represented as green squares which occupy a 2x2 square
    *   Consoles will be represented as blue rectangles which occupy a 3 x 1 space 
*   The simulation displays the tournament completion percentage and clock time as time progresses. 
    *   This will be compared against the typical runtime of tournaments to determine if we are accurately simulating the length of tournaments. 


### In testing, we will use doctest to test the following: {#in-testing-we-will-use-doctest-to-test-the-following}



*   The model correctly initializes the environment.
*   The model correctly records the walking distance of each player.
*   The model calculates the runtime of the tournament.
*   The agents behave correctly by testing their methods and states.


# Personnel  {#personnel}



*   **Matthew Taing:** Matt is a senior at UWB that transferred over from UW Seattle. He came up with this idea to write a simulation for Smash tournaments. He participates in these tournaments himself and has the most background knowledge regarding how these tournaments are held and laid out. Matt will be responsible for answering any questions asked about the topic of Smash/Tournaments and creating the general blueprint for how we will be modeling this. He will also be designing the bracket class. 
*   **Jesse Yu:** Jesse is a junior at UWB with some prior experience with Python. He is arguably weak at programming. For this project, he will be given programming tasks with other team members to improve on this. He will also be tasked with doing the analysis and writing the report since he is better at analysing data than analysing code.
*   **Tien Huynh:** Tien is a senior at UWB and majoring in Computer Engineering. He is the Driver of our group, so he will be responsible for keeping the team on task. Based on Tien’s outstanding performance with the Visualize class in ca_diffusion, he will be tasked with doing the Visualize in this project.


# Technologies  {#technologies}

**Discord:** Discord is a messaging app that is primarily used for gaming. Although we are not using Discord for gaming, it will be our means of communication throughout the quarter. For this project, backup communications will be done via SMS to ensure communication can still go through if something such as lack of internet connection disables communication via Discord.

**Git/GitHub: **Git is a free and open source tool for version control on your local machine that uses a branching model that allows you to create separate, independent branches for your code. Branching allows you to create side branches, jump back to previous branches, and execute merge, delete, and recall operations. 

GitHub is a cloud-based repository hosting service that allows you to share your Git projects outside of your local machine. It expands Git’s basic functionality and allows for collaboration of your Git project with others. GitHub is primarily used for software development and for our purposes, we will be using it to collaborate on our final project.

**PyCharm: **PyCharm is a Python-specific IDE developed by JetBrains. It is cross-platform compatible and has WIndows, MacOS, and Linux version. It has some unique functionalities that set it apart from other IDEs and text editors, including (but not limited to): Code analysis/assistance, graphical debugger, in-built testing tools, integration with Version Control Systems such as Git, databasing tools, and support for data science with Anaconda.

In our group, Matt uses PyCharm IDE to code in Python.

**Visual Studio Code: **At its core,** **Visual Studio code can be described as a glorified text editor. Plugins can be downloaded that allow recognition and support for different languages. It features colored text to differentiate different parts of the code. One of the draws of VS Code is its simplicity; it does not come with a bunch of third party softwares installed. It allows you to customize and personalize its use.

In our group, Jesse uses VS Code to code in Python.

**Spyder: **Spyder is a scientific environment that was written in Python, made for Python. Its users are primarily scientists, data analysts, and engineers. Spyder includes many powerful scientific tools and includes all the packages in the scientific Python stack, including [NumPy](https://en.wikipedia.org/wiki/NumPy), [SciPy](https://en.wikipedia.org/wiki/SciPy), [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib), [pandas](https://en.wikipedia.org/wiki/Pandas_(software)), [IPython](https://en.wikipedia.org/wiki/IPython), [SymPy](https://en.wikipedia.org/wiki/SymPy) and [Cython](https://en.wikipedia.org/wiki/Cython). It is also great for displaying graphical output, and has an inline display for graphics produced using [Matplotlib](https://www.edureka.co/blog/python-matplotlib-tutorial/).

Since Tien is doing the Visualize.py class in this project, he will be using Spyder IDE.


# Benchmarks  {#benchmarks}


<table>
  <tr>
   <td>Date To be completed by 
   </td>
   <td>People assigned to this task 
   </td>
   <td>Task 
   </td>
   <td>Description 
   </td>
  </tr>
  <tr>
   <td>2/ 28/ 20
   </td>
   <td>Matt
   </td>
   <td>Research average time matches should occur in
   </td>
   <td>Do research of real life Smash tournaments to find actual data
   </td>
  </tr>
  <tr>
   <td>2/29/20
   </td>
   <td>Everyone
   </td>
   <td>Develop skeleton for all code and post on Github
   </td>
   <td>Create all pseudocode for all the code, and try to flesh it out as much as possible. GitHub repo at: <a href="https://github.com/tienhuynh5312/Smash-Tournament-Simulation">https://github.com/tienhuynh5312/Smash-Tournament-Simulation</a>
   </td>
  </tr>
  <tr>
   <td>3/1/20
   </td>
   <td>Everyone
<p>
/ Mostly Jesse
   </td>
   <td>Write Environment Class
   </td>
   <td>Write the class for the Waiting Room and Game Room environments.
   </td>
  </tr>
  <tr>
   <td>3/1/20
   </td>
   <td>Everyone
<p>
/ Mostly Tien 
   </td>
   <td>Start Simulation Driver (for testing purposes)
   </td>
   <td>Create a temporary makeshift Simulation Driver class to test class functionality later.
   </td>
  </tr>
  <tr>
   <td>3/3/20
   </td>
   <td>Matt
   </td>
   <td>Write Bracket Class
   </td>
   <td>Create the bracket class, which matches next available players and update match scores.
   </td>
  </tr>
  <tr>
   <td>3/3/20
   </td>
   <td>Everyone
   </td>
   <td>Start functions to animate simulation (for testing purposes) 
   </td>
   <td>Create a temporary makeshift version of Visualize.py class to test class functionality
   </td>
  </tr>
  <tr>
   <td>3/3/20
   </td>
   <td>Tien + Jesse
   </td>
   <td>Develop Player class
   </td>
   <td>Player class includes all functionalities regarding the player agent. More functionality will be added as needed.
   </td>
  </tr>
  <tr>
   <td>3/4/20
   </td>
   <td>Tien + Jesse
   </td>
   <td>Test movement of Player Class (using Sim Driver & Visualize) 
   </td>
   <td>Use our makeshift Visualize and Simulation Driver classes to test the player class movement.
   </td>
  </tr>
  <tr>
   <td>3/5/20
   </td>
   <td>Everyone
   </td>
   <td><strong>Milestone</strong>
   </td>
   <td>This is our Milestone for this project
   </td>
  </tr>
  <tr>
   <td>3/7/20
   </td>
   <td>Everyone
   </td>
   <td>Revise code based on results of tests for any missing functionality
   </td>
   <td>Find any missing functionalities that we need for the model and add them.
   </td>
  </tr>
  <tr>
   <td>3/8/20
   </td>
   <td>Matt + Jesse
   </td>
   <td>Complete Simulation Driver
   </td>
   <td>Use our makeshift sim driver as a template to finish sim driver, adding/removing things as needed.
   </td>
  </tr>
  <tr>
   <td>3/8/20
   </td>
   <td>Tien
   </td>
   <td>Complete Visualize.Py class
   </td>
   <td>Use our makeshift Visualize.py as a template to finish Visualoize.py, adding/removing things as needed.
   </td>
  </tr>
  <tr>
   <td>3/9/20
   </td>
   <td>Jesse
   </td>
   <td>Perform Analysis
   </td>
   <td>Analyze our results and answer the questions as noted in the Analysis section.
   </td>
  </tr>
  <tr>
   <td>3/10/20
   </td>
   <td>Matt
   </td>
   <td>Verify Results
   </td>
   <td>Compare our simulation results to real life Smash tournament data that we got in the “Research average time matches should occur in” task.
   </td>
  </tr>
  <tr>
   <td>3/11/20
   </td>
   <td>Jesse
   </td>
   <td>Write Report for analysis
   </td>
   <td>Write a report of the Analysis outcomes from “Perform Analysis”. Data from “Verify Results” will also be included in this report.
   </td>
  </tr>
  <tr>
   <td>3/12/20
   </td>
   <td>Everyone
   </td>
   <td>Present Results of our simulation in class 
   </td>
   <td>Present our result to the class.
   </td>
  </tr>
</table>



# Contribution Breakdown  {#contribution-breakdown}

All team members contributed to the contribution breakdown and agreed with the results. 



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/CSS-4582.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/CSS-4582.png "image_tooltip")


Task Breakdown: 



*   Introduction - Matt 
*   Model Description - Matt + Tien 
*   Analysis: - Matt + Tien + Jesse 
*   Testing: - Matt + Jesse
*   Personnel - Jesse
*   Technologies - Jesse
*   Benchmarks - Matt + Tien + Jesse 

Matt’s Contribution: 

Wrote the entire introduction section and a majority of the model description. Also helped out with revising the analysis and testing sections. 

Tien’s Contribution: 

Discussed the development plan with Matt extensively. After that, I worked on multiple sections: model description, analysis, and benchmarks.

Jesse’s Contribution: 

Completed the Personnel and Technologies sections. Fill out the entire Benchmarks section. Made contributions to the Analysis and Testing sections.


<!-- Docs to Markdown version 1.0β18 -->
