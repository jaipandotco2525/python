import os
import pandas as pd
import time

start = time.time()

os.chdir("C:\\SuperBox\\work\\data\\")

#データ読み込み
df_1 = pd.read_csv("顧客デモ.csv", encoding="cp932", dtype={"郵便番号": "object"})
df_2 = pd.read_csv("受注1デモ.csv", encoding="cp932", dtype={"郵便番号": "object"})
df_3 = pd.read_csv("受注2デモ.csv", encoding="cp932", dtype={"郵便番号": "object"})

#データ結合
join = pd.concat([df_2, df_3], ignore_index=True)
join_new = join.rename(columns={"顧客番号": "顧客番号_#1"})

#データマッチング
data_matching = pd.merge(df_1, join_new, left_on="顧客番号", right_on="顧客番号_#1")
data_matching_new = data_matching.rename(columns={"郵便番号_x": "郵便番号"})

#抽出（あいまい検索）
search = data_matching_new[data_matching_new['商品名'].str.contains('うなぎ', na=False)]

#集計（名寄せ）
syukei = search.groupby(["姓", "名", "生年月日", "電話番号", "郵便番号", "住所"], as_index=False)
syukei_new = syukei.agg({"受注日": 'max', "受注番号": 'count', "受注金額": 'sum'})
syukei_new2 = syukei_new.rename(columns={"受注日": 'MAX＜受注日＞', "受注番号": 'N＜受注番号＞', "受注金額": 'SUM＜受注金額＞'})

#並び替え
sort = syukei_new.sort_values("受注金額",ascending=False)

#順位づけ
rank = pd.RangeIndex(start=1, stop=len(sort.index) + 1, step=1)
sort['ランク'] = rank

#Excelファイル抽出
sort.to_excel("test6.xlsx", encoding="cp932")

elapsed_time = time.time() - start
print ("処理時間:{0}".format(elapsed_time) + "[sec]")