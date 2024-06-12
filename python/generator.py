def mygen():

    var = yield 20
    db = yield 40
    abc = yield 10
    print(var, db, abc)
    yield db + abc


g = mygen()
next(g)
next(g)
g.send("asdf")
g.send("asdfasdf")
