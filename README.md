### Monitorization and control system of the production of Salicornia in the Ria de Aveiro

> Technological evolution has always been present in the life of humanity from its beginnings to the present, in a relationship that has grown and continues to grow at an amazing rate. The paradigm, transversal to any economic activity, consists in resource optimization with the objective to maximize production through the technological evolution. In agricultural production this is not exception, and for this reason, the monitoring mechanisms of the parameters that influence the quantity and quality of production are becoming indispensable and preponderant in the success of the business. Thus, in the cultivation of Salicornia, a plant that grows in the Ria de Aveiro, is also essential create a system that allows monitor and help to control the optimal conditions of cultivation of the specie.

> The main goal of this thesis was the project and the implementation of an information system for the control and monitoring of the Salicornia production in collaboration with a company of the region of Aveiro and the Department of Biology of the University of Aveiro. The developed system is a low-cost and effective solution for data acquisition, processing and storage. In addition, this system is structured to be applied in other contexts beyond the Salicornia cultivation.

#### Dashboard project

> Web platform for client interaction. The architecture has been created to define relation Controller Module VS Sensor Module ([more information](https://github.com/ruipoliveira/sali-dashboard/blob/master/resources/general-electronic-modules.jpg)/ or [thesis](https://github.com/ruipoliveira/sali-report/blob/master/thesis-roliveira.pdf)). 

> The dashboard has possibility:  
> * User management in associated to company; 
> * Actuate remote (valve, motor...);
> * Consult the data values obtained by sensores - graphic and table;
> * Export data to CSV file;
> * Generate alarmes to sensores; 
> * Localizate sensores (Sensor Module + Controller Module) in map; 
> * Consult API documentation; 

![alt text](https://github.com/ruipoliveira/sali-dashboard/blob/master/resources/arquitetura-final-dashboard.jpg)

#### Technologies/ Frameworks used

* Django (python 2.7)
* Django Rest Framework (API REST)
* Rest framework swagger (interactive documentation)
* Django gravatar
* Rest framework authtoken
* smtplib3 (email service)


* PostgreSQL
* Incorporation to Django project
* Trigger created in SQL 


* Gravatar: identification of users on the platform
* API Google Maps: location of modules
* ZingChart: graphical representation of the data


#### Installations and dependencies

`
apt-get install python-pip
`

`
pip install -r requirements.txt
`

`
sudo apt-get install postgresql postgresql-contrib
`


#### Environment (used)

* PyCharm Community (https://www.jetbrains.com/pycharm/)
* pgAdmin - PostgreSQL Tools (https://www.pgadmin.org/)


#### Demo

[![demo youtube](https://img.youtube.com/vi/AH98j7ISiLc/3.jpg)](https://www.youtube.com/watch?v=AH98j7ISiLc&index=1&list=UUMdlsvA5W6tYu35oN_AEZ5A)


#### All repositories

* [sali-report](https://github.com/ruipoliveira/sali-report)
* [sali-dashboard](https://github.com/ruipoliveira/sali-dashboard)
* [sali-deploy](https://github.com/ruipoliveira/sali-deploy)
* [sali-hardware](https://github.com/ruipoliveira/sali-hardware)
* [sali-surveillance](https://github.com/ruipoliveira/sali-surveillance)

#### Author
* Rui Oliveira (ruipedrooliveira@ua.pt)

University of Aveiro, 2017
