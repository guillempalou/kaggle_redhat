import pandas as pd

people_df = pd.read_csv('data/people.csv')
train_df = pd.read_csv('data/act_train.csv')
test_df = pd.read_csv('data/act_test.csv')

train_df = train_df.merge(
    people_df,
    on='people_id',
    suffixes=['_act', '_ppl']
)

test_df = test_df.merge(
    people_df,
    on='people_id',
    suffixes=['_act', '_ppl']
)

train_df.to_csv('data/train.csv')
test_df.to_csv('data/test.csv')
