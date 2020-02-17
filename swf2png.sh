#!/bin/sh

for img in *.swf; 
do 
 swfrender "$img" -o "$img.png"
done
