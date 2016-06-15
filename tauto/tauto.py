def nums():
    num = 0
    while True:
        yield num
        num += 1

num_generator = nums()

referents = set()

bottom = {}


class Statement:

    def __init__(self, d, s, r):
        self.domain = d
        self.sign = s
        self.referent = r

    def __repr__(self):
        return "IN {}: {} = {}".format(self.domain, self.sign, self.referent)


def new_r():
    n = next(num_generator)
    referents.add(n)
    return n


class Host:

    def __init__(self, name):
        self.name = name

        self.d_idx = {}
        self.s_idx = {}
        self.r_idx = {}

    def statements(self, *args):
        found_referents = {}
        for phrase in args:
            statement = self.entry(phrase[0], phrase[1])
            if statement:
                found_referents[phrase[0]] = statement.referent

        if len(found_referents) > 1:
            raise ValueError("Inconsistent assertions: {}".format(found_referents))
        elif found_referents:
            referent = list(found_referents.values())[0]
        else:
            referent = new_r()

        results = set()
        for phrase in args:
            results.add(self.propose(phrase[0], phrase[1], referent))

    def propose(self, d, s, referent=None):
        statement = self.entry(d, s)
        if not statement:
            if referent is None:
                referent = new_r()
            statement = Statement(d, s, referent)
            self.d_idx.setdefault(d, {})[s] = statement
            self.s_idx.setdefault(s, {})[d] = statement
            self.r_idx.setdefault(referent, set()).add(statement)

        return statement

    def bootstrap(self, name, referent=None):
        if referent is None:
            referent = new_r()

        bottom[self.name] = referent
        return self.propose(name, name, referent=referent)

    def __getitem__(self, value):
        return self.s_idx[value]

    def entry(self, domain, sign):
        return self.d_idx.get(domain, {}).get(sign)

    def synonyms(self, domain, sign):
        entry = self.entry(domain, sign)
        return self.r_idx[entry.referent]


english = Host("ENG")
english.bootstrap("english")
