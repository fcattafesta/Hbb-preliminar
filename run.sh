#!/bin/bash

set -x

echo "args: $@"

CMD="python analysis.py"

lep=$1
suffix=$2

if [[ "$lep" == "mu" ]]; then
    model="modelsMuon"
elif [[ "$lep" == "el" ]]; then
    model="modelsElectron"
fi

if [[ $flavsplit == true ]]; then
    model="${model}FlavSplit"
fi

btag=""
if [[ $suffix == *deepcsv* ]]; then
    btag="--btag deepcsv"
elif [[ $suffix == *deepflav* ]]; then
    btag="--btag deepflav"
fi


histodir="/gpfs/ddn/cms/user/malucchi/hbb_out"

$CMD \
    --model ${model} \
    --histfolder ${histodir}/${lep}/${suffix}/ \
    --lep ${lep} \
    --snapshot \
    --sf \
    ${btag} \
    "${@:3}"
