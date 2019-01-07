from fgo.common import *
from datetime import datetime
random.seed(datetime.now())

class 扶她狗:
    最顶 = (1260, 100)
    最底 = (1260, 630)

    def __getitem__(self, item):
        return getattr(self, '_' + item.__name__)


class 管理室(扶她狗):
    @property
    def _活动(self):
        return (930, 190), 活动()

    @property
    def _迦勒底之门(self):
        return (930, 380), 迦勒底之门()


class 活动(扶她狗):
    pass


class 迦勒底之门(扶她狗):
    @property
    def _每日任务(self):
        return (930, 380), 每日任务()


class 每日任务(扶她狗):
    最底 = (1260, 510)
    x = 930

    @property
    def y(self):
        return (510 - 100) * (1 - random.random()) + 100


def 随便选任务():
    def _():
        # if 随机选择:
        # e = 每日任务()
        # yield MoveTo(1260, e.y)
        # yield click()
        # yield Wait(Exact(0.5))
        # yield MoveTo(e.x, e.y)
        # else:
        yield MoveTo(923, 150)


        yield click()
        yield Wait(Exact(0.5))

        yield MoveTo(644, 340)  # 选择第一个助战
        yield click()
        yield Wait(Exact(0.5))

        yield MoveTo(1200, 675)  # 开战
        yield click()
        yield Wait(Exact(0.5))
    return reduce(Compose, _())


def _打活动():
    e = 管理室()
    yield MoveTo(*e.最顶)
    yield click()
    (a, e) = e._迦勒底之门
    yield MoveTo(*a)
    yield click()

    yield MoveTo(*e.最顶)
    yield click()
    a, e = e._每日任务
    yield MoveTo(*a)
    yield click()

    yield MoveTo(e.x, e.y)
    yield click()

    yield MoveTo(644, 273)  # 选择第一个助战
    yield click()

    yield MoveTo(1200, 675)  # 开战  # yield click()


def 打活动():
    s = reduce(Compose, _打活动())
    return fix_dpi(Compose(Wait(Exact(2)), s))


# s = 打活动()
# # print('->\n'.join(repr(s).split('->')))
# eval_event(s)
