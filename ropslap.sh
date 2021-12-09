if (( $# == 3 ))
then
  python3 ROPgadget/ROPgadget.py --binary $1 --ropchain --execute $2 --env $3 > .out-rop.txt
else
  python3 ROPgadget/ROPgadget.py --binary $1 --ropchain --execute $2 > .out-rop.txt
fi