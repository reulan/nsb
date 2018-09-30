#!/bin/bash
# mpmsimo - 7/23/17
# ow_playerdata.sh

# GCP PVC
DATADIR=$HOME/owdata

# Move to file while read ... < accounts
#for item in $? do:
ACCOUNTS=('Reulan-1746' 'Rangoris-1209')

# hour, month, day, year (ex. 6-08-04-17)
DATE=$(date +%l-%m-%d-%y)

mkdir $HOME/owdata

for PLAYER in ${ACCOUNTS[@]};
    do echo $PLAYER
        #curl -s https://owapi.net/api/v3/u/$PLAYER/blob | python -m json.tool | tee $DATADIR/$PLAYER-owdata.json
        curl -s https://owapi.net/api/v3/u/$PLAYER/blob?format=json_pretty | tee $DATADIR/$PLAYER-owdata-$DATE.json
    done
