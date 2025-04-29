import pandas as pd
from langchain_core.documents import Document


class data_converter:
    def __init__(self):
        print("Initi")
        self.product_data = pd.read_csv(r"/Users/harishk/Documents/Projects/ML/GenAI/customer_chatbot/data/flipkart_product_review.csv")
    def data_trasformation(self):
        required_columns = self.product_data.columns
        required_columns = list(required_columns[1:])
        product_list = []
        for index, row in self.product_data.iterrows():
            object = {
                "product_name":row['product_title'],
                "product_rating":row['rating'],
                "product_summary":row['summary'],
                "product_review":row['review']
            }
            product_list.append(object)
        print(product_list)



if __name__ == '__main__':
    data_conv = data_converter()
    data_conv.data_trasformation()
        
        