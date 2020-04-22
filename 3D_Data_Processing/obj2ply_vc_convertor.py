#!/usr/bin/env python
import os
import sys
import argparse
import glob
import re
import ntpath

prog        = re.compile(r"(?P<FID>\D*)(?P<TID>\d*)(.)(\D*$)")
prog_step2  = re.compile(r"(.*)(.)(rename-temp$)")

argv = sys.argv
argv = argv[argv.index("--") + 1:]
argument_parser = argparse.ArgumentParser(description="Convert obj to gltf.",usage="python /path/to/obj2ply_vc_convertor.py -- --input /path/to/input --output /path/to/output --mlx /path/to/mlx")
argument_parser.add_argument("-i", "--input",help="set your input directory")
argument_parser.add_argument("-mlx", "--mlx_prefix",help="set your mlx file")
argument_parser.add_argument("-o", "--output_prefix",help="set your output directory")
args = argument_parser.parse_args(argv)

path_input  = args.input
mlx_file 	= args.mlx_prefix
path_out    = args.output_prefix

if not path_out:
    path_out = path_input

print (path_input, path_out)

objs = sorted(glob.iglob(path_input + '/*.' + 'obj'))


for f in objs:
    basename = ntpath.basename(f)
    nameWithoutExt = os.path.splitext(basename)[0]
    outputFileName = nameWithoutExt + ".ply"
    print(f, basename)
    os.system("/Applications/meshlab.app/Contents/MacOS/meshlabserver -i " + f + " -o " + path_out + "/" + outputFileName + " -m vc -s " + mlx_file)  


