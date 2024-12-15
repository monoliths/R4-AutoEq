#### Simple Translate AutoEQ to Hiby R4
I own a hiby r4 and wanted to add the Parametric EQ files from AutoEq to my device. I did not want to manually punch in the painfully slow menus on the r4 so I just made a short python script create the peq files which you can easily import.  

The code is sloppy and ugly. I just needed something fast.

Requirements
- AutoEq Parametric EQ files from here: https://github.com/jaakkopasanen/AutoEq
- python 3.4

Works best with `jq`

Example 
```
# this will print out the r4 peq (basically json) 
./main.py --eq "tmp/input/7Hz Timeless ParametricEQ.txt" --name "7Hz Timeless ParamestricEQ Test"

# pipe it to jq and feed it to a file to save it and transfer it to your r4
# Remember to save it as a .peq file if not the r4 peq app will not show the file when you browse for it
./main.py --eq "tmp/input/7Hz Timeless ParametricEQ.txt" --name "7Hz Timeless ParamestricEQ Test" | jq . > 7hz_timeless.peq
```