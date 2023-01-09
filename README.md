### csci220esnuweb
Small Django web app for students to calculate "What-If" grades on the ESNU scale for CSCI220 (CS@Mines).

*(Originally authored by Joey Lovato Fall 2022)*

## Overview
Canvas has a "What-If" feature which allows students to input assignment/exam scores to speculate their final grade in the course. However, Canvas lacks the ability to calculate grades beyond the traditional percent-based A-F scale. This web app is a substitute for this "What-If" feature, allowing students to input their ESNU scores and calculate their expected final grades. 

## Deployment
This web app is currently deployed using Heroku: https://csci220esnuweb.herokuapp.com/gradecalculator. The app can be easiply deployed elsewhere as a Django web app. The root directly is currently configured to run as a Heroku Django web app. 

## Depency Note
The code to calculate the grades on the back-end is the same as in [esnu-calc](https://github.com/JosephLovato/esnu-calc). The file `esnu_grade_caculations.py` was simply copied from esnu-calc into `grade_calculator/esnucalc` here. Therefore, any updaets to esnu-calc must be copied here to maintain consistency. 
