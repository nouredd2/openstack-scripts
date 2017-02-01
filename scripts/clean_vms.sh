#!/bin/sh

LIST=$(virsh list --all | awk 'NR>=3 {print $2}')

echo $LIST

for l in $LIST
	do
		echo "virsh destroy $l"
		virsh destroy $l
		echo "virsh undefine --remove-all-storage $l"
		virsh undefine --remove-all-storage $l
done
