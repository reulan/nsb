#!/bin/bash
# mpmsimo - 7/23/17
# ow_playerdata.sh

DATADIR=$HOME/owdata
ACCOUNTS=('Reulan-1746' 'Rangoris-1209')

mkdir $HOME/owdata

for PLAYER in ${ACCOUNTS[@]};
    do echo $PLAYER
        #curl -s https://owapi.net/api/v3/u/$PLAYER/blob | python -m json.tool | tee $DATADIR/$PLAYER-owdata.json
        curl -s https://owapi.net/api/v3/u/$PLAYER/blob?format=json_pretty | tee $DATADIR/$PLAYER-owdata.json
    done
