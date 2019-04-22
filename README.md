# Assignment in Telecommunication Software (Riga Technical University)
# Project 411-MTP

## Instructions
* Create a new personal project on GITHUB: 411-MTP

* Combine Tools: Google Colab Notebook and Linux BASH Terminal

	* Ping 5 hosts in five different countries (e.g. USA, DE, LV, IN, BR, ME, KO etc.) with a time interval 3 sec.
	* Collect responses from 100 pings 
	* Organise Data storage in five columns Pandas Data Frame
	* On the next step, use Pandas DF to retrieve:
		* data of ping RTT for each country, specifically:
			* average
			* standard deviation
			* variance
			* depict  Data using HISTOGRAMS (for each separate country)
		* in a one Figure Integrated BOXPLOTs 

## Requirements

### Python requirements
* The following specifications are needed in order to execute the script:
	* Python3
	* OS
	* Subprocess
	* PandasDataFrame
	* Matplotlib

### Bash requirements
* The following specifications are needed in order to execute the script:
	* Authorization to create and modify files
	* Authorization to launch subprocesses from python
	* AWK
	
## Script execution

### Launch the script
* Only the python file needs to be executed, the bash files will follow automatically.
* The users needs to already be in the folder where the python file is situated and type:
```
$ python3 ping.py
```
* Or write the relative path, for example such as:
```
$ python3 /home/ec2-user/environment/Project/411-MTP/ping.py
```

### Results
* The script will generate 
	* a text file for each country in the data folder
	* an histogramm of the data in the images folder
	* a boxplot of the data in the images folder
	* a file data.txt in the 411-MTP folder containing the average, standard deviation and variance of each country 
