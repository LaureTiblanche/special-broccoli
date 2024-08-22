# Input for Pathfinder2 Cards

This script take a .csv file and transform it into a "mochouille" .json to create Pathfinder cards with the [Crobi's Rpg-Cards Project](https://github.com/crobi/rpg-cards).

### How to ? 

1- Insert your spells data into the `init_data.csv` : lists are separated with `,` and columns by `;`. 

2- Run the main script in any python3 env

3- upload the `result.json` file in the Rpg-Cards application ! 


Notes :

Some adjustments will need to be made afterwards (such as text size or line breaks) depending on the cards.
For very long descriptions, it may be necessary to make several cards. In this case, use the map copy feature on the site and modify it directly.

### Input : 

* **title** : mandatory
* **action** : can be a list - values must be : 1 / 2 / 3 / free / reaction
* **level** 
* **trait_common** : can be a list
* **trait_uncommon** : can be a list
* **domains** : can be a list
* **cast**
* **area**
* **range**
* **target**
* **saving_throw**
* **trigger**
* **duration**
* **requirement**
* **defense**
* **text** : mandatory - line breaks with <br> 
* **activity_name**
* **activity_action**
* **activity_text**
* **critical_success**
* **success**
* **failure**
* **critical_failure**
* **heightened2**
* **heightened3**
* **heightened4**
* **heightened5**
* **heightened6**
* **heightened7**
* **custom_color** : mandatory
* **back_icon** : mandatory
