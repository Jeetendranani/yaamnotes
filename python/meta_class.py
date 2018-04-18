from python.hello import Hello

h = Hello()
h.hello()

h.hello('Randy')


def fn(self, name='world'):
    print("Hello {}.".format(name))


Hello = type('Hello', (object,), dict(hello=fn))


class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "{}:{}".format(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: {}'.format(name))

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: {} => {}".format(k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'model' object has no attribute '{}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'Intert into {} ({}) values ({})'.format(self.__table__, ','.join(fields), ','.join(params))
        print("SQL: {}".format(sql))
        print('ARGS: {}'.format(str(args)))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id='1234', name='Randy', email='test@fb.com', password='my-password')
u.save()