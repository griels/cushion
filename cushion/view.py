

from collections import defaultdict

from .persist import Persist


class View(object):

    def __init__(self, design_name, view_name, mapf, redf=None, wrapper=None):
        super(View, self).__init__()
        self.design = design_name
        self.name = view_name
        self.mapf = mapf
        self.redf = redf
        self._wrapper = wrapper

    def __get__(self, instance, cls=None):
        # this will be the class that's embedding us, so grab it here
        self._wrapper = cls or instance.__class__
        return self

    def __call__(self, wrapper=None, **kw):
        print "CALLING VIEW", self.design, self.name, kw
        result = Persist().query(self.design, self.name, **kw)
        if not result: return
        wr_ = wrapper or self._wrapper
        ret = []
        for r in result:
            if wr_ and result.include_docs:
                ret.append( wr_(_id=r.doc.key, **r.doc.value) )
            else:
                ret.append( r.doc or r )
        return ret



def sync_all(list_of_views):
    """
    accepts list of views from all models and coalates them into design docs
    then syncs them all
    """
    designs = defaultdict(lambda:defaultdict(dict))
    for v in list_of_views:
        d = {'map':v.mapf}
        if v.redf: d['reduce'] = v.redf
        designs[v.design][v.name] = d

    persist = Persist()
    for dname,views in designs.iteritems():
        persist.design_view_create(design=dname, views=views)

