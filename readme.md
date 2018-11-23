# Green IT challenge

## Project Info

Team: 
  We are ThreeGuys

Directories: 
  data - for saving questions
  static - for Javascript, CSS, images...
  templates - for static HTML files

Packages:
  Flask

APIs
```
  /(<uid>) - use uid to get related question sheet with answers
  /get/<uid> - API to get related answers (should be called in /<uid>)
  /submit/(<uid>) - API to submit results, return json of id: {'id': <uid>}
  /save/(<uid>) - API to save results, return json of id: {'id': <uid>}
```
### Demo 
```
python main.py 
```   
## How to deploy

```
    - Copy generated js file to /static/js/
    - Copy generated css file to /static/css/
    - modify templates/index.html (do not copy files!), link related js and css files
    - if you have data.json changed, put it in assets/data
    - push your work
    - log in as otto(not root!) on remote server (I sent u the password)
    - cd ~/threeguys
    - git pull
    - sudo service main restart
    - sudo service nginx restart
    - goto http://vps613446.ovh.net to check if everything is working alright
```      


## Results


* screenshot

![](https://)

## Developers
|Developer|Contact|
|:-:|:-:|
|Ruoqiu Zhang|zhang_r@epita.fr|
|Qiaoyu Liu|liuqiaoyu233@gmail.com|
|Hao Xu|1044504787@qq.com|
|Udhayashankar|udhayashankar.palanivel@gmail.com|
|Alvaro Bilbao La Vieja|a.bilbaolavieja@gmail.com|

## Licence
Green IT challenge : Threeguys © Sourcecode remain the property of the developers.
