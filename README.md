# Parking-2D

![GitHub repo size](https://img.shields.io/github/repo-size/Salman-F/Parking-2D)
![Github license](https://img.shields.io/github/license/Salman-F/Parking-2D) 
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?&logo=linkedin&logoColor=white)](https://linkedin.com/in/salman-fichtner)

Parking 2D is a `university project` that allows
` the work with pygame` to ` create a game in python`.

<p align="center">
  <img src="https://github.com/Salman-F/Parking-2D/blob/main/images/readme/teaser.gif" width="500" height="400">
</p>

This project demonstrates how to work with pygame and create a game including
  - a menu created with pygame-menu
  - collision detection
  - map creation
  - saving achieved scores and much more..

If you have any suggestions for improvement, please feel free to contact me.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed (still) installed all default libaries coming with python (json, csv, pickle)
* You have installed the requiered libaries listed in [src\requirements.txt](https://github.com/Salman-F/Parking-2D/blob/main/requirements.txt)
* To do so you can try `pip install -r requirements.txt`
* You have installed python
* This project was tested on python==3.8.0 and it is recommended to use this version

## Installing Parking 2D

To install Parking 2D, follow these steps:

* Download this repository
* Unzip the downloaded file

## Using Parking 2D

To use Parking 2D, follow these steps:

* open main.py
* run main.py and the game should start
 
OR

* Start a terminal within the src folder of this project.
* Type the following command in your teminal.

```
C:\src>python main.py
```

## Possible Output

* Your starting screen should look something like that

<p align="center">
  <img src="https://github.com/Salman-F/Parking-2D/blob/main/images/readme/startScreen.png" width="500" height="400">
</p>

## How to create a new map
* Maps are created with tiles
* For creating a map a level editor is highly recommended
* A free level editor is [Tiled](https://www.mapeditor.org/)
* Create a new map

| :zap:        Change the "tile size" to 16x16 and the "map size" to Width=50tiles and Height=38tiles   |
|-----------------------------------------|

* Open a new tileset from [images\maps\customSpriteSheet.png](https://github.com/Salman-F/Parking-2D/blob/main/images/maps/customSpriteSheet.png) in your level editor
* Create a map with the given 16x16 tiles
* Please note that all black, green and grey blocks are going to be obstacles in the game

| :exclamation:         Your map must include one (just one) brown tile that represents the top left corner of your goal   |
|-----------------------------------------|

* How Big the goal is going to be should be saved in a variable with the numbers of tiles in x and y direction (default is x:6, y:12)
* Your created map with JUST the blocks from [images\maps\customSpriteSheet.png](https://github.com/Salman-F/Parking-2D/blob/main/images/maps/customSpriteSheet.png) should then look something like this.

<p align="center">
  <img src="https://github.com/Salman-F/Parking-2D/blob/main/images/readme/createMapLayoutpng.png" width="500" height="400">
</p>

* Export this file as csv and the obstacles are done. Now you can start designing your layout
* Copy your level and add assets, pictures or text on your level
* Export your copy as an image and the surface the user is going to see is done.
* Your map is now ready to be included into the game and could look something like this.

<p align="center">
  <img src="https://github.com/Salman-F/Parking-2D/blob/main/images/readme/createMapDesign.png" width="500" height="400">
</p>

* Files that you need at the end
1. A csv that includes the layout of your map (created with just the tiles provided in [images\maps\customSpriteSheet.png](https://github.com/Salman-F/Parking-2D/blob/main/images/maps/customSpriteSheet.png))
2. An image that shows the design of your map

You can also start with making a design and afterwards filling it with the tiles provided in [images\maps\customSpriteSheet.png](https://github.com/Salman-F/Parking-2D/blob/main/images/maps/customSpriteSheet.png))

## Thanks to all artist

This project is just for personal and educational use. It is not intendet to earn any money with this project.

* Background: Designed by [vectorpouch](https://www.freepik.com/free-vector/city-car-parking-empty-lots-cartoon_5901242.htm#page=1&query=city%20car%20parking&position=6) / Freepik
* Cars: View@clipartmax.com
* Futuristic sprite pack: by [Skorpi](https://opengameart.org/users/skorpio)
* Race sprite pack: by Kenney Vleugels for [Kenney](www.kenney.nl)
* Font: by [Vic Fieger](https://www.1001fonts.com/users/vicfieger/)
* Honk noise: by [YouTube](https://youtu.be/FQc5zRy6wBU)
* Game music: by Luis Zuno (@ansimuz) | [Patreon](https://www.patreon.com/ansimuz)

## Contributing to Parking 2D

To contribute to Parking 2D, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me you can reach me at [Linkedin](https://www.linkedin.com/).

## License

This project uses the following license: [MIT](https://choosealicense.com/licenses/mit/).
