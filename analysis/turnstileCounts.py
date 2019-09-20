import pandas as pd
import glob

path = "Turnstile\*.txt"
all_files = glob.glob(path)
df = pd.concat((pd.read_csv(f) for f in all_files))
export_csv = df.to_txt('TurnstileFull.csv')
