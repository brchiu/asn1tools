SIMPLE_CLASS = {'SimpleClass': {'extensibility-implied': False,
                 'imports': {},
                 'object-classes': {'ITEM': {'members': [{'name': '&id',
                                                          'optional': False,
                                                          'type': 'INTEGER'},
                                                         {'name': '&comment',
                                                          'optional': False,
                                                          'type': 'IA5String'}]}},
                 'object-sets': {'Items': {'class': 'ITEM',
                                           'members': [{'&comment': 'item 0',
                                                        '&id': 0},
                                                       {'&comment': 'item 1',
                                                        '&id': 1}]}},
                 'tags': 'AUTOMATIC',
                 'types': {'ItemWithConstraints': {'members': [{'name': 'id',
                                                                'optional': False,
                                                                'type': 'ITEM.&id'},
                                                               {'name': 'comment',
                                                                'optional': False,
                                                                'type': 'ITEM.&comment'},
                                                               {'name': 'value',
                                                                'optional': False,
                                                                'type': 'REAL'}],
                                                   'type': 'SEQUENCE'},
                           'ItemWithoutConstraints': {'members': [{'name': 'id',
                                                                   'optional': False,
                                                                   'type': 'ITEM.&id'},
                                                                  {'name': 'comment',
                                                                   'optional': False,
                                                                   'type': 'ITEM.&comment'},
                                                                  {'name': 'value',
                                                                   'optional': False,
                                                                   'type': 'REAL'}],
                                                      'type': 'SEQUENCE'}},
                 'values': {}}}