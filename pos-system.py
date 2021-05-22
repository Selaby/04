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
                
    def view_item_list(self):
        for item in self.item_order_list:
            print(f"商品コード:{item}")
    
    # 課題1 item_codeを入力することで、その商品の名前と価格を表示する
    def view_name_and_price(self,item_code):
        for m in self.item_master:
            if item_code == m.item_code:
                # return m.item_name,m.price
                print(f"商品コード:{m.item_code}")
                print(f"商品名:{m.item_name}")
                print(f"価格:{m.price}")
    
    
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    
    # オーダー表示
    # order.view_item_list()

    # 商品情報表示
    order.view_name_and_price("001")
        
if __name__ == "__main__":
    main()