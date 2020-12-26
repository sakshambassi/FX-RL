from gym.envs.registration import register
import pandas as pd
df = pd.read_csv("./data/FX_INR_USD.csv")
register(
	id='FX-RLenv-0',
	entry_point='FX-RL.env:FXenv',
	kwargs={
		'df': df,
		'window_size': 20,
		'frame_bound': (20, len(df.index)
	}
)
