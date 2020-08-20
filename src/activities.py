from src.activities_defined import sleep, feed, play, teach_tricks, walk, wash
from src.manage_time import stop_action, step
from src.save_data import save

activities = {'sleep': sleep, 'feed': feed, 'play': play, 'teach tricks': teach_tricks, 'walk': walk, 'wash': wash,
              'stop': stop_action, 'stand-by': step, 'END': save}
