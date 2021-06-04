# Parking-2D

![GitHub repo size](https://img.shields.io/github/repo-size/Salman-F/Parking-2D)
![Github license](https://img.shields.io/github/license/Salman-F/Parking-2D) 
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

Analyze and predict corona data with redis and machine learning name is a `university project ` that allows
` the work with a redis db` to ` analyze and forecast corona data`.

This project demonstrates how to work with a database and analyse the data using different algorithms (including the `SARIMA machine learning algorithm`).

It should be noted that this project mainly deals with the work of the `redis database` and that working with machine learning algorithms has been tested for the first time.

If you have any suggestions for improvement, please feel free to contact me.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed redis on your machine. 
* Another option is to run a docker container on your [machine](https://phoenixnap.com/kb/docker-redis) or [raspberryPi](https://thisdavej.com/how-to-install-redis-on-a-raspberry-pi-using-docker/)
* You have installed the requiered libaries listed in [src\requirements.txt](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/src/requirements.txt)
* To do so you can try `pip install -r requirements.txt`
* It is recommended to install `fbprophet` via [anaconda](https://anaconda.org/conda-forge/fbprophet) or via [pip](https://pypi.org/project/fbprophet/)
```Python
  pip install fbprophet
  conda install -c conda-forge fbprophet
```
* This project was tested on python==3.8.0 and it is recommended to use this version


## Installing Analyze and predict corona data with redis and machine learning

To install Analyze and predict corona data with redis and machine learning, follow these steps:

* Download this repository
* Unzip the downloaded file


## Using Analyze and predict corona data with redis and machine learning

To use Analyze and predict corona data with redis and machine learning, follow these steps:


* Start your redis docker container or server.
* Change the parameters creating a RedisClient object to the specific information of your redis server.
 
![userChoice](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/images/connectRedis.png)
```Python
    try:
        redisDB = RedisClient(_state=state, _redisHost=(localhost or IP), _redisPort="6379"(most likely), _redisPw=(yourRedisPW))
    except Exception as generalError:
        print(f"Somethin went wrong connecting to redis: {generalError}")
        return
```
* Start a terminal within the src folder of this project.
* Type the following command in your teminal with the parameters you want to use.
* Further explanation is given underneath.

```
C:\src>python main.py arg1 arg2 arg3 arg4

arg1: FutureCast          (Default = 10)
arg2: showAnalyzedData    (Default = True)
arg3: showForecastPlots   (Default = True)
arg4: prophetIncluded     (Default = True)
```

You can also change the values in your IDE. Therfore open the main.py file.
Change the parameters shown in the picture below to your liking.
* FutureCast --> Describes the amount of days forecast methods should predict.
* showAnalyzedData --> Is True or False and decides, if plots regarding analyzing 
                          corona data should be shown.
* showForecastPlots --> Is True or False and decides, if plots regarding forecast of 
                          corona data should be shown.
* prophetIncluded --> Decides if the fbProphet algorithm is executed or not.

![userChoice](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/images/userOptions.png)

## Possible Output

| Analyzed Corona Data | FBProphet forecast | Other forecast methods  |
| :-------------: |:-------------:| :-----:|
| ![userChoice](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/images/analyzeCoronaData.png) | ![userChoice](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/images/fbProphetForecast.png)      |    ![userChoice](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/images/forecastingCoronaData.png) |

## Run Unittests
* All unittest will be executed automatically at the end of the program
* If you want to run them seperately you find some test files in src directory
* To use them seperately add at the end of the file

```Python
if __name__ == '__main__':
    unittest.main()
```
* Now you can run the specific File and information should be printed in the terminal (see example underneath)

![userChoice](https://github.com/Salman-F/Analyze-and-predict-corona-data-with-redis/blob/main/images/unittestExample.png)

## Contributing to Analyze and predict corona data with redis and machine learning

To contribute to Analyze and predict corona data with redis and machine learning, follow these steps:

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
