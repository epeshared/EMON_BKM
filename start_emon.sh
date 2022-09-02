emon -collect-edp > emon.dat &
sleep 10
emon -stop
sleep 1
emon -process-edp /opt/intel/sep_private_5.33_linux_0316081130eb678/config/edp/edp_config.txt
