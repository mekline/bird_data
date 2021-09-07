# bird_data
Data about bird names!
MKS & BKS

This is the repository for a series of empirical explorations about birds and what they are called. 

### (1) Party activity - Birds

Survey conducted during MKS + BKS joint birthday party; some responses collected over subsequent weeks.

##### Stimuli 

45 birds selected by conducting an informal grouping/clustering process on the core set of [Wingspan](https://stonemaiergames.com/games/wingspan/) cards. For each of the resulting ~30 groups, one or two species were selected as most representative (two distinctive species were chosen for some larger groups).  To this, we added the following super common species, which since non-native to the United States are not in the WS deck:

* Rock Pigeon
* European Starling
* Domestic Chicken

For each bird, we then selected the first photo on that species' [Cornell Lab of Ornithology](https://www.birds.cornell.edu/) page.

##### Method

Survey administered on paper (B&W with color reference photos displayed nearby), with open-response line for each bird.  The instructions given were to "without consulting other peopel, give your best guess for the name of every bird ont he sheet. Even if you know it's not really the bird's name, put down what you would call it.

Survey available [here](https://docs.google.com/document/d/1K_GfLpS-JbVSd9DlX0YtBkTXxo-8M8PKtRsBUlxttTg/edit).

##### Data

`bird_data.tsv`: Data entered by MKS, spelling corrections & simplification of correct answers only (e.g. "Mallard,  maybe" --> "Mallard")
A line for correct answers is also added, make sure not to include in the data analysis!

##### Analysis

`bird_data.R`: R script used to analyze the raw data! See that file for descriptions of specific analyses


