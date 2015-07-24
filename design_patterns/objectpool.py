__author__ = 'cgiridhar'
class Resource:
    __value = 0

    def __new__(cls, *args, **kwargs):
        print "Creating New Resource"
        return super(Resource,cls).__new__(cls, *args, **kwargs)

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value


class ObjectPool:
    _resources = []

    def resources(self):
        print("Existing Pool")
        for r in ObjectPool._resources:
            print(r)

    def add(self):
        r = Resource()
        ObjectPool._resources.append(r)
        return r

    def acquire(self):
        if len(ObjectPool._resources) > 0:
            print("Utilizing existing resource")
            return ObjectPool._resources.pop()
        else:
            self.create()

    def release(self, resource):
        print("Releasing resource: " + str(resource))
        ObjectPool._resources.append(resource)


pool = ObjectPool()

pool.resources()
one = pool.add()
two = pool.add()
pool.resources()

r = pool.acquire()
print "Obtained Resource" + str(r)

pool.resources()

pool.release(r)
