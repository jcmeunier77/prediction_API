# Prediction_API
 
## 1. Purpose and project objective 

### Purpose 
- [x] To develop API that capitalizes on real-estate data to render the following functionalities :
  1. modeling a house in 3D from lidar satellite images (geoTIFFs file) by only entering a home address. This part is an extension of a [previous project](https://github.com/jcmeunier77/House_3D_API)
  2. locating the house on a map by entering its address 
  3. making price forecast on the buildings (i.e. houses or apartment) according to multiple features (postal code, number of rooms, living space, surface area, etc.)
- [x] Te deploy the API on azure (using a.o. Docker and Travis) 

### Objectives 

- [x] Consolidate the knowledge in Python, specifically in : NumPy, Pandas, Sklearn, Matplotlib,...
- [x] To be able to search and implement new librairies
- [x] Consolidate knowledge of data science and machine learning algorithm for developping an accurate regression prediction model
- [x] To be able to construct the project with object-oriented programming (OOP)
- [x] To be able to implement the whole project - and make it functioning -  through an API (using Flask)
- [x] To be able to deploy the API on a web based environment (in this case Azure)

### Features 
#### Must-have 
- [x] The API must be functional
- [x] Your model must be functional

#### Nice-to-Have
- [x] The API to be deployed on a web based environment (e.g. Heroku, Azure, etc.)
- [x] Optimize your solution to have the result as fast as possible.
- [x] The API searches for as much information as possible on its own. (For example, area => cadastre)
Better visualization
- [x] You provide a 3d representation of the house

### Context of the project 
- [x] All the work achieved was done during the BeCode's AI/data science bootcamp 2020-2021

## 2. The project 
### Working plan and steps 
#### 1. Research 
- [x] Research and understand the term, concept and requirement of the project.
- [x] Discover new libraries that can serve the project purposes 
- [x] Developing, using and testing machine learning algorithm (i.a. sklearn with linear, SVG, decision trees regression, XGBoost,...)

#### 2. Data collection 
- [x] for 3D house reconstruction 
  - [DTM file for Flandre including Brussels](http://bit.ly/DTM_Flandre)
  - [DSM file for Flandre including Brussels](http://bit.ly/DSM_Flandre)
  - [Shapefiles with cadastral maps and parcels](https://eservices.minfin.fgov.be/myminfin-web/pages/cadastral-plans?_ga=2.167466685.225309318.1604313780-388788923.1602907232)
- [x] for real-estate data
  - Data collection was done in the context of a previous project whose aim was to develop a [Scrapping Bot](https://github.com/jcmeunier77/bot-scrape-zimmo) written in Python, to scrape data (50.000+) from real estate website "Zimmo.be", for a challenge given by Becode.
      
#### 3. Data manipulation 
- [x] Data cleaning : including, a.o., removing outliers and features with to many missing values (>15%) and conducting multivariate feature imputation for the feature with less missing values (using sklearn.impute.IterativeImputer)

- [x] Features engineering : as location (postal code) are not readily amenable to be integrate in quantitative model - but has nonetheless a huge impact on real-estate price - a ranking index was compute based on the average house price for each entities in Belgium. As shown, this index demonstrates a good association with house prices and it seemed that its 3rd polynomials best explained the target (more than 25% of the 'house price' variance explained for this sole feature - based on r_square coefficient).    

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/pc%20ranked%20by%20prices.png">
</p>

#### 4. Modelization
- [x] Features : 
  - type of building: house/apartment
  - living area: square meters
  - field's surface: square meters
  - number of facades
  - number of bedrooms
  - garden: yes/no
  - terrace: yes/no
  - terrace area: square meters
  - equipped kitchen: yes/no
  - fireplace: yes/no
  - swimming pool: yes/no
  - state of the building: as new, just renovated, good, to refresh, to renovate, to restore (one hot encoding)
- [x] Target: 
  - House price: euros 
- [x] Machine learning model: 
  - Multiple models using increasing number of features and based on various algorithm (i.a. linear, SVM, decision tree, XGBoost) were trained and evaluated.
  - The best model was based on the XGBoost algorithm (n_estimators=700, max_depth= 4, learning_rate= 0.3) and provided an r_square coefficient of .82 on the train set and of .76 on the test set
  - The best fitted model was save as a pickel file which was integrated in the API for price estimation 
  - Examples of python code for data manipulation and algorithms development are stored in the [notebook folder](https://github.com/jcmeunier77/prediction_API/tree/master/notebooks%20data%20preparation%20and%20ML%20algorithms) of the current repository

### Project output
#### 1. API Structure 

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/API%20structure.png">
</p>

### 2. API Routes
- [x] Estimate: in

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/API%20estimate%20in.png">
</p>

- [x] Estimate: out

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/API%20estimate%20out.png">
</p>

- [x] Map: in

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/API%20map%20in.png">
</p>

- [x] Map: out

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/API%20map%20out.png">
</p>

- [x] 3D reconstruction: in

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/API%203D%20in.png">
</p>

- [x] 3D reconstruction: out

<p align="center">
    <img src="https://github.com/jcmeunier77/prediction_API/blob/master/img_out/3d%20output.png">
</p>
