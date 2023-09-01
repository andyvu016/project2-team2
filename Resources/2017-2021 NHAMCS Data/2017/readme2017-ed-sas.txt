
                                USING SAS WITH NHAMCS DATA
   
  There are two ways to read the 2017 NHAMCS Emergency Department (ED) public use data file using SAS:

  Option 1 - Use the zipped file ed2017_sas.zip in the SAS folder on 
  the FTP server to open a complete SAS dataset of the 2017 NHAMCS ED public use file.

  The steps for this option are as follows:

  1) Create a new folder on your local workstation, for example, C:\MYFILES\ED2017

  2) Download to the new folder the file ed2017_sas.zip and the file ed17for.txt 
     from the FTP server: ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/dataset_documentation/nhamcs/sas

  3) ed2017_sas.zip is a compressed file which you must unzip prior to use. 
     In order to do this, double click on the file name in your directory screen; 
     an option to unzip the file should appear. A new folder, ed2017, containing the  
     unzipped ASCII file ed2017 may be created, or the file itself without the folder 
     may appear. This is the ED ASCII dataset. You can then move the file to your preferred location. 

     Alternately, you can right-click on the name of the compressed file from your directory screen. 
     On the pop-up menu, there should be an option to extract the file to a location of your choosing.

     ed17for.txt is the file containing the formats which you will need to include in your
     program in order for the SAS file to run.  

  4) To use the SAS dataset, the following code provides an example for a file saved to C:\MyFiles\ED2017:

     %inc "C:\MyFiles\ED2017\ed17for.txt";  /*read in the SAS formats*/ 
     libname out1 'C:\MyFiles\ED2017';  /*point to file location on your workstation*/
     data test17; set out1.ed2017_sas;  /*create a temporary working file copied from the unzipped file*/
     proc surveyfreq data=test17;
     tables sex*ager /clwt cl;
     cluster cpsum;
     strata cstratm;
     weight patwt;
     run;
 
  Option 2 - Use the SAS input, label and format files provided to create your own SAS data set. 

  The steps for this option are as follows:

  1) Create a new folder on your local workstation, for example, C:\MYFILES\ED2017

  2) Download to the new folder the 2017 ED dataset (ed2017.zip) from the FTP server: 
     ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/datasets/nhamcs

  3) ed2017.zip is a compressed file which must be unzipped prior to use.
     In order to do this, double click on the file name in your directory screen; 
     an option to unzip the file should appear. A new folder, ed2017, containing the  
     unzipped ASCII file ed2017 may be created, or the file itself without the folder 
     may appear. This is the ED ASCII dataset. You can then move the file to your preferred location. 

  4) Download to the new folder the ed17inp.txt, ed17lab.txt and ed17for.txt files from the FTP server:
     ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/dataset_documentation/nhamcs/sas

  5) Sample SAS code is shown below; other examples can be found here: 
     https://www.cdc.gov/nchs/ahcd/ahcd_presentations.htm

     filename ed17pub "C:\MyFiles\ED2017\ed2017";          /*unzipped ASCII data set*/
     filename ed17for "C:\MyFiles\ED2017\ed17for.txt";     /*SAS format statement*/
     filename ed17inp "C:\MyFiles\ED2017\ed17inp.txt";     /*SAS input statement*/
     filename ed17lab "C:\MyFiles\ED2017\ed17lab.txt";     /*SAS label statement*/

     %inc ed17for;  /*reads in the formats*/

     data test17; 
     infile ed17pub missover lrecl=9999;
     %inc ed17inp;  /*reads in the input statement*/
     %inc ed17lab;  /*reads in the labels*/
     run;

     proc surveyfreq data=test17;
     tables sex*ager /clwt cl;
     cluster cpsum;
     strata cstratm;
     weight patwt;
     run;

   CAUTION - Because the NHAMCS is a sample survey, the application of 
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
