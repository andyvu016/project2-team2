
                                USING SAS WITH NHAMCS DATA
   
  There are two ways to read the 2021 NHAMCS Emergency Department (ED) public use data file using SAS:

  Option 1 - Use the zipped file ed2021_sas.zip in the SAS folder on 
  the FTP server to open a complete SAS dataset of the 2021 NHAMCS ED public use file.

  The steps for this option are as follows:

  1) Create a new folder on your local workstation, for example, C:\MYFILES\ED2021

  2) Download to the new folder the file ed2021_sas.zip and the file ed21for.txt 
     from the FTP server: https://ftp.cdc.gov/pub/Health_Statistics/NCHS/dataset_documentation/nhamcs/sas

  3) ed2021_sas.zip is a compressed file which you must unzip prior to use. 
     In order to do this, double click on the file name in your directory screen; 
     an option to unzip the file should appear. This is the ED SAS dataset.

     Alternately, you can right-click on the name of the compressed file from your directory screen. 
     On the pop-up menu, there should be an option to extract the file to a location of your choosing.

     ed21for.txt is the file containing the formats which you will need to include in your
     program in order for the SAS file to run. It can be downloaded from:
     https://ftp.cdc.gov/pub/Health_Statistics/NCHS/dataset_documentation/nhamcs/sas

  4) To use the SAS dataset, the following code provides an example for a file saved to C:\MyFiles\ED2021:

     %inc "C:\MyFiles\ED2021\ed21for.txt";  /*read in the SAS formats*/ 
     libname out1 'C:\MyFiles\ED2021';  /*point to file location on your workstation*/
     data test21; set out1.ed2021_sas;  /*create a temporary working file copied from the unzipped file*/
     proc surveyfreq data=test21;
     tables sex*ager /clwt cl;
     cluster cpsum;
     strata cstratm;
     weight patwt;
     run;
 
  Option 2 - Use the SAS input, label and format files provided to create your own SAS data set. 

  The steps for this option are as follows:

  1) Create a new folder on your local workstation, for example, C:\MYFILES\ED2021

  2) Download to the new folder the 2021 ED dataset (ed2021.zip) from the FTP server: 
     https://ftp.cdc.gov/pub/Health_Statistics/NCHS/datasets/nhamcs

  3) ed2021.zip is a compressed file which must be unzipped prior to use.
     In order to do this, double click on the file name in your directory screen; 
     an option to unzip the file should appear. This is the ED ASCII dataset.  

  4) Download to the new folder the ed21inp.txt, ed21lab.txt and ed21for.txt files from the FTP server:
     https://ftp.cdc.gov/pub/Health_Statistics/NCHS/dataset_documentation/nhamcs/sas

  5) Sample SAS code is shown below; other examples can be found here: 
     https://www.cdc.gov/nchs/ahcd/ahcd_presentations.htm

     filename ed21pub "C:\MyFiles\ED2021\ed2021";          /*unzipped ASCII data set*/
     filename ed21for "C:\MyFiles\ED2021\ed21for.txt";     /*SAS format statement*/
     filename ed21inp "C:\MyFiles\ED2021\ed21inp.txt";     /*SAS input statement*/
     filename ed21lab "C:\MyFiles\ED2021\ed21lab.txt";     /*SAS label statement*/

     %inc ed21for;  /*reads in the formats*/

     data test21; 
     infile ed21pub missover lrecl=9999;
     %inc ed21inp;  /*reads in the input statement*/
     %inc ed21lab;  /*reads in the labels*/
     run;

     proc surveyfreq data=test21;
     tables sex*ager /clwt cl;
     cluster cpsum;
     strata cstratm;
     weight patwt;
     run;

   CAUTION - Because NHAMCS is a sample survey, the application of 
   weights to the sample data is REQUIRED to produce national estimates
   of office visits, as well as to accurately assess the sampling error of
   statistics based on the survey data.  Please refer to the appropriate
   sections of the documentation file for information on how to apply the 
   weights and to obtain relative standard errors of national estimates.
                                                                                                
   For questions, suggestions, or comments concerning NHAMCS data, please
   contact the Ambulatory and Hospital Care Statistics Branch at 
   (301) 458-4600 or by email at ambcare@cdc.gov. 

   For additional information on NCHS data products, please call CDC-INFO at 
   800-CDC-INFO (800-232-4636), TTY (888-232-6348), Monday-Friday 8am-8pm EST, 
   or use the CDC-INFO online request form at https://www.cdc.gov/info.
