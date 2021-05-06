

# Introduction
I have worked on some websites using selenium to automate logins and data collections.<br>
Websites: <br>
 (1) NSS IITH [Website](https://nss.iith.ac.in/hours_portal/)<br>
 (2) Aims IITH [Website](https://aims.iith.ac.in/aims/)<br>
 (3) Cricbuzz notification through whatsapp [Website](https://www.cricbuzz.com/)<br>
 (4) NTA Results bruteforcing date of birth(Use at own risk,Iam not liable for any legal action) [Website](https://ntaresults.nic.in/resultservices/JEEMain-Feb-2021-auth)<br>
 
## Table of contents
* [General info](#general-info)
* [Modules](#Modules)
* [Setup](#setup)
* [Example-Gif](#Example-Gif)


## General info
You are going to need some modules mentioned below.
Tested on Ubuntu 20.04 LTS<br>
	
## Modules
Code is created with:
* Ubuntu 20.04 LTS
* Selenium version : 3.141.0
* Chromedriver version :  90.0.4430.24 (Always use same version of chromredriver as of chrome)(Better to use latest version)
* Python library version : Python 3.8.5
* opencv-python version : 4.5.1 (To detect captcha)(optional)
* Easy ocr version : 1.3.1
* numpy version : 1.19.5
 
	
## Setup
To run this project, install above modules locally using pip or pip3:

```
$ pip3 install selenium
$ pip3 install opencv-python
$ pip3 install easyocr
$ pip3 install numpy
$ apt install chromium-chromedriver
```
or you can just download the latest version of chromedriver from [Website](https://chromedriver.chromium.org/downloads)<br>
and run in terminal <br>
```
$ pip3 install -r requirements.txt
```
Automate file is for IITH students only<br>
## Example-Gif
(1) NSS Automated Login Gif.<br> <br> <br>
![pag](https://user-images.githubusercontent.com/54314892/113487173-2fbfab00-94d4-11eb-95f4-b646a55e8e89.gif)<br><br>
(2) Aims Automated Login Gif.<br> <br> <br>
![Alt Text](https://github.com/SRIJITH01/Automated-IITH-nss-and-aims/blob/main/ezgif-6-848cf9b92d1f%20(1).gif)<br><br>
Aims second captcha accuracy is 68% only so if there is an error run the code again.<br><br>
(4) NTA  Bruteforcing Login Gif.<br> <br> <br>
![pag](https://user-images.githubusercontent.com/54314892/117259383-9b968a00-ae6b-11eb-9895-5fe1e12b4542.gif)<br><br>
If you need any help in automating logins of any website or come across any error create an issue [here](https://github.com/SRIJITH01/Automated-IITH-nss-and-aims/issues/new).
