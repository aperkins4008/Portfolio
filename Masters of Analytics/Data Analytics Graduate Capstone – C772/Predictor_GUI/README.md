## Context and How to Run:

This parallel program is a tool which implements a KNN learning algorithm as fitted within a connected body of work. The study that was ran in parallel with this tool is named “Random Forest on IT Salary Data Set,” and was produced as a Capstone project for my Masters in Data Analytics in conjunction with Wester Governors University. KNN was selected as opposed to the MLP neural network alternative, as it is much faster and is also less likely to be subject to over-fitting.

This program uses the streamlit API as a GUI in order to provide WGU students a way to predict their Salary Tier in future years. The tool uses the final clean dataset from the original study, in order to quickly train the KNN algorithm and produce fast results. Think of the program as a condensed version to the original study, with meaningful value to others. The GUI this program produces allows the KNN algorithm to accept user inputs. After selection of inputs the user can then execute the machine learning algorithm and can predict what pay band they may fall into, in the years to come. 

**TO RUN**

To run this program, do the following:

* Download folder called “Predictor_GUI” and place in directory location of your choice
* Open “Salary_Predictor_GUI.py” and change the directory location in the code to the location where you placed the folder above
* Save the file
* Upload this newly saved file into your Jupyter Notebook tree
* Open your anaconda prompt and type “streamlit run Salary_Predictor_GUI.py” -- then press enter.
* That’s it!!! Now predict your future pay band.

### Below are the Modules and their corresponding version numbers utilized during this study.

*Note:* Any versions not included below are module classes utilized by Python’s base package. 

| Package/Module | Version |
| :----------- | -----------: |
| conda | 4.9.2 |
| Python | 3.7.9 |
| pandas | 1.1.3 |
| numpy | 1.19.2 |
| sklearn | 0.23.2 |
| streamlit | 0.72.0 |