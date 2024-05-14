class Product_request:
    id=None
    code = None
    name = None
    amount=None


    def __init__(self, req_data):
        if 'id' in req_data:
            self.id = req_data['id']
        if 'code' in req_data:
            if req_data['code'] != "":
                self.code = req_data['code']
        if 'name' in req_data:
            self.amount = req_data['name']
        if 'amount' in req_data:
            self.amount = req_data['amount']

    def get_code(self):
        return self.code
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    def get_amount(self):
        return self.amount

class DRS_pagination:
    index = None
    offset = None
    limit = 10
    query_limit = 10

    def __init__(self, index):
        self.index = index
        self.offset = (index - 1) * 10
        self.limit = (index) * 10

    def __init__(self, index, limit):
        self.index = index
        self.limit = limit * index
        self.offset = (index - 1) * 5
        # print('page start')
        # print(self.index)
        # print(self.limit)
        # print(self.offset)
        # print('page ends')

    def get_index(self):
        return self.index

    def get_offset(self):
        return self.offset

    def get_limit(self):
        return self.limit

    def get_query_limit(self):
        return self.limit + 1

    def get_data_limit(self):
        return self.limit - 1