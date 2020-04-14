#!/bin/sh
python3 si_pbf_helper.py test init
python3 si_pbf_helper.py test player test1 Lightning violet
#python3 si_pbf_helper.py test player test2 Ocean rouge
python3 si_pbf_helper.py test energy test1 2
python3 si_pbf_helper.py test gain test1 3
python3 si_pbf_helper.py test growth
python3 si_pbf_helper.py test element test1 water
python3 si_pbf_helper.py test element test1 water

python3 si_pbf_helper.py test play test1 shatter D3
python3 si_pbf_helper.py test play test1 boon D3
python3 si_pbf_helper.py test accelerate test1 shatter
python3 si_pbf_helper.py test test

python3 si_pbf_helper.py test turn
python3 si_pbf_helper.py test test

python3 si_pbf_helper.py test reclaim_one test1 shatter 
python3 si_pbf_helper.py test test

python3 si_pbf_helper.py test reclaim_all test1 
python3 si_pbf_helper.py test forget test1 shatter
python3 si_pbf_helper.py test test

#python3 si_pbf_helper.py test draw_powers 30
#python3 si_pbf_helper.py test test

#python3 si_pbf_helper.py test draw_powers 40
#python3 si_pbf_helper.py test test

