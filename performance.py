import cProfile
import pstats
from fm import main  # Ensure this is the correct import from your fm.py script

if __name__ == "__main__":
    cProfile.run('main()', 'profile_output')

    # Load the profiling data
    p = pstats.Stats('profile_output')

    # Sort the statistics by cumulative time and print the top entries
    p.sort_stats('cumulative').print_stats(20)

    # Optionally, you can sort by other criteria
    # p.sort_stats('time').print_stats(10)
    # p.sort_stats('calls').print_stats(10)
