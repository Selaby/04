import pandas as pd

ITEM_MASTER_CSV_PATH="./master.csv" # カレントディレクトリの状態に要注意 ずれているとFileNotFoundErrorが出る

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
                
    # def view_item_list(self):
    #     for item in self.item_order_list:
    #         print(f"商品コード:{item}")
    
    # 課題1 item_codeを入力することで、その商品の名前と価格を表示する
    def view_name_and_price(self,item_code):
        for m in self.item_master:
            if item_code == m.item_code:
                print(f"商品コード:{m.item_code}")
                print(f"商品名:{m.item_name}")
                print(f"価格:{m.price}")
                return m.item_name,m.price

# 課題3 csvから商品マスタを登録する
def register_by_csv(csv_path):
    item_master=[]
    item_master_df = pd.read_csv(csv_path, encoding="utf-8", dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
    for item_code,item_name,price in zip(item_master_df["item_code"],item_master_df["item_name"],item_master_df["price"]):
        item_master.append(Item(item_code,item_name,price))
    # print(item_master)
    return item_master

### メイン処理
def main():
    # マスタ登録
    # item_master=[]
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))

    # 課題3 csvから商品マスタを登録する
    item_master = register_by_csv(ITEM_MASTER_CSV_PATH)
    # item_master = pd.read_csv("./master.csv", encoding="utf-8")
        
    # オーダー登録
    order=Order(item_master)

    # 課題2 ターミナルから商品コードを登録する
    order_code = input("商品コードを入力してください >> ")
    order.add_item_order(order_code)
    # order.add_item_order("001")
    # order.add_item_order("002")
    # order.add_item_order("003")
    
    # オーダー表示
    # order.view_item_list()

    # 商品情報表示
    order.view_name_and_price(order_code)
        
if __name__ == "__main__":
    main()