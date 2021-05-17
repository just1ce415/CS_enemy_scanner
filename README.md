# CS Rival Scanner
Provides useful information on your live enemy by analysing statisctics. It's hard to oppose your enemies when you don't know anything about them. This program will solve this problem. It's function is to provide you with intel on your enemies. This will make it easier to choose tactics for next round and, as result, winning.

***

## Table of contents
#### [CS Rival Scanner](#cs-rival-scanner)

#### [Table of contents](#table-of-contents)

#### [Reference](#reference)

#### [Input and output](#input-and-output)

#### [Program structure](#program-structure)

#### [Usage](#usage)

#### [Examples](#examples)

#### [Credits](#credits)

#### [Licence](#licence)

***

## Reference

***

## Input and output
### Input
* Links of enemies' Steam profiles.
* Results of every round.
### Output
* Enemies statistics
* Approximate amount of money, which enemy team possesses.
* Recomendations for next round.

***

## Program structure
### `adt.py`
Our own ADT's
#### `RecomendationADT`
Based on users input, chooses the best tip.

* `process`
Works with user's input so it becomes easier to make a summary and give a tip.

* `advice`
Based on user's input chooses among tips for the best one in this situation.

#### `PlayerStats`
Contains data about enemies.
* `__site_parsing`
Represents it's data on webpage.

* `__steam_get_jsondata`
Returns json object with data from Steam Api.

* `soup_get_nickname`
Returns player's nickname.

* `soup_get_rank`
Returns player's rank.

* `soup_get_other_stats`
Returns other player's stats.

* `soup_get_weapon_list`
Returns list of guns and accuracy with them.

* `steam_get_kd`
Returns your kd in game.

* `steam_get_adr`
Returns your ADR.

* `steam_get_weapon_list`
Returns 3 best weapons and their accuracy.

* `steam_add_accuracy`
Returns weapons' accuracy.

### `application.py`
Main module.

* `index`
Starting state of the webpage.

* `handle_player_info`
State when you can search for enemies stats.

* `handle_recommendation`
State when you can give your input about previous round.

### `arrays.py`
Contains ADT classes: `Array`, `Array2D`, `DynamicArray`

### `get_status_module.py`
This module gets player's stats.

* `start`
Receives player's stats.

***

## Usage
1. Enter enemies' links to their Steam profiles.
![](https://github.com/just1ce415/CS_rival_scanner/blob/main/images/site_1.jpg)
2. After every round fill up the form about it's results.
![](https://github.com/just1ce415/CS_rival_scanner/blob/main/images/site_4.jpg)
3. ???
4. PROFIT

* Because of `step 1` (if that player didn't hide his account info) you will have access to this player's statistics which includes win-rate, accuracy and much more.
* Thanks to `step 2` you'll be always aware about amount of money, which enemy team possesses, their tactics and most-likely their dislocation.

***

## Examples

***

## Credits
* Stepan Sushko - back-end dev.
* Vladyslav Protsenko - front-end dev.
* Vadym Vilhurin - general designer
* Dmytro Kalitin - repository issues
* Vadym Treskot - data analysis

***

## Licence
MIT License

Copyright (c) 2021 Angelo

***
