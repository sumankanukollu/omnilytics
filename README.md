# OMNILYTICS Programming challenge:

## 1. Problem Statement:
Write a Web app using React.js to generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.
Sample extracted output:

hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....

 The output should be 2MB in size. Once file generation is done the output should be available as a link which can be then downloaded by clicking on it. Also, there should be a button on the page so by clicking on this button the total number of each random objects will be displayed.

Note: The backend API must be written using Flask (Python) or Express frameworks. All the communication between frontend and backend MUST be done via these APIs only.

Note: Upload the project in Github and share the link with us.

clike here to know about the [challenge](https://docs.google.com/document/d/1RvJaYLFOp7uOydSk8Cy7dMBJh2jz0GZ4_4DqbzhH7JE/edit#)

## 2. Solution Demo:
![demo](https://github.com/sumankanukollu/omnilytics/raw/main/omnilytics_coding_challenge_demo.gif)

## 3. Resources used:
* Django
* Python

## 4. REST API's:
* Home page : http://127.0.0.1:8000/
* To generate four (4) types of printable random objects and store them in a single file : http://127.0.0.1:8000/generate/?
* Generated sample outputfile is at : https://github.com/sumankanukollu/omnilytics/raw/main/omnilyticsApp/omni_log_2.txt
* API to download the generated file :  http://127.0.0.1:8000/download/
* API to display the total number of each random objects : http://127.0.0.1:8000/report/?
