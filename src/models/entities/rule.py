class Rule:
    
    def __init__(self, rule: str, status: bool, creation_date: str, level: int):
        self.rule = rule
        self.status = status
        self.creation_date = creation_date
        self.level = level
