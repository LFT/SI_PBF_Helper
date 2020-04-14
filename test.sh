#!/bin/sh
python3 si_pbf_helper.py test init
python3 si_pbf_helper.py test player test1 Lightning violet
#python3 si_pbf_helper.py test player test2 Ocean rouge
python3 si_pbf_helper.py test energy test1 2
python3 si_pbf_helper.py test gain test1 3
python3 si_pbf_helper.py test growth
python3 si_pbf_helper.py test element test1 water
python3 si_pbf_helper.py test element test1 water

python3 si_pbf_helper.py test test