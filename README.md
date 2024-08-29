# Input for Pathfinder2 Cards

This script take a .csv file and transform it into a "mochouille" .json to create Pathfinder cards with
the [Crobi's Rpg-Cards Project](https://github.com/crobi/rpg-cards).

### How to ?

1. Insert your spells data into a csv file :

-> lists are separated with `,` and columns by `;`
-> Create a csv file from the template file : `./expl/init_data.csv`
-> Or add directly your data in `./expl/init_data.csv`

2. Run the main script in any python3 env : `python3 main [path_to_your_input_file]` ; If the path is empty the input
   file will be `./expl/init_data.csv`

3. upload the `result.json` file in the Rpg-Cards application (and finalize your lovely cards) !

Notes :

Some adjustments will need to be made afterwards (such as text size or line breaks) depending on the cards.
For very long descriptions, it may be necessary to make several cards. In this case, use the map copy feature on the
site and modify it directly.

### Input :

* **title** : mandatory
* **action** : can have multiple values - each value will create an icon - values must be : 1 / 2 / 3 / free / reaction
* **level**
* **trait_common** : can have multiple values - each value will create a separate tag
* **trait_uncommon** : can have multiple values - each value will create a separate tag
* **domains** : can have multiple values - all values will be displayed in the same property without alteration from the
  input
* **cast**
* **area**
* **range**
* **target**
* **saving_throw**
* **trigger**
* **duration**
* **requirement**
* **defense**
* **text** : mandatory
* **activity_name**
* **activity_action**
* **activity_text**
* **critical_success**
* **success**
* **failure**
* **critical_failure**
* **heightened1**
* **heightened2**
* **heightened3**
* **heightened4**
* **heightened5**
* **heightened6**
* **heightened7**
* **heightened8**
* **heightened9**
* **custom_color** : mandatory - you can check values proposed by Crobi's app
* **back_icon** : mandatory - from the [game-icons project](http://game-icons.net/) and
  the [gameicons-font project](https://seiyria.com/gameicons-font). - check Crobi github for more information.

### Descriptions formatting Pro Tips :

For a better formatting of your spells descriptions you can :

Use bold with `<b>` and `</b>`, add lines breaks `<br>` and other html tags.

**Add bullet lists** : bullet list are a separate property in Crobi's app and are not handled here. You must add them
in "
post-prod" formatting within the app.

Transformation from the generated json :

```
text | my text followed by my list : item A, item B, item C And some more text description.
```

To in the app :

```
text | my text followed by my list :
bullet | item A,
bullet | item B,
bullet | item C
text | And some more text description.
```

For better readability, you can reduce (or augment) the text size (by default 10px). You can also separate your spell
into several cards with the "Duplicate Card" button. For your spell title, you can add a number in superscript like
`My spell ¹` and `My spell ²`.

Add spacing between cards on the printable page ? See the [tip from Rezenbekk](https://github.com/crobi/rpg-cards/issues/95#issuecomment-392575825) : 
```
Solution: go to generator/css/cards.css, add "margin:Xmm;" property to ".card" element, where X is your desired spacing size. 4 mm leaves quite a lot of space for easy cutting.
```
Note : For this solution, you must use a local Crobi's app and not his demo site. Ne need to rebuild the app, just regenerate your final page.
