 ### To collect EDP data:
  "emon -collect-edp > emon.dat" or <br>
  "emon -collect-edp [edp_file=<edp-events-file>] > emon.dat <br> 
  (Use edp_file optional option to provide custom events file)" <br>
 ### To process data using EDP Ruby script: 
  "emon -process-edp /path/to/edp_config.txt <br> 
  (requires python xlsxwriter library to generate Excel summary sheet on Linux)" <br>
