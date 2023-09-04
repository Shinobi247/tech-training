class MakeQuery:
    def __init__(self, query: str = ""):
        self.query = "Select \n\t" + query + "\n"
        # return self

    def _from(self, table: str):
        self.query += "FROM \n\t" + table + "\n"
        return self

    def _join(self, condition: str):
        self.query += "JOIN \n\t" + condition + "\n"
        return self

    def _on(self, condition: str):
        self.query += "ON \n\t" + condition + "\n"
        return self

    def _where(self, condition: str):
        self.query = "WHERE \n\t" + condition + "\n"
        return self

    def get_query(self):
        return self.query


a = MakeQuery("asdasd,as,d,as,d,asd,a,sd,")
a._from("asdasd")._join("asd")._on("asdasd")._join("hoihoasdasd ")
print(a.get_query())
