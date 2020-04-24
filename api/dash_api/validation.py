from datetime import datetime


class JsonValidation:

    def group_validation(self, json_file):
        return all(x in json_file for x in ('group', 'color'))

    def client_validation(self, json_file):
        return all(x in json_file for x in ('name', 'chipset', 'mac'))

    def service_validation(self, json_file):
        return all(x in json_file for x in ('number', 'chipset', 'mac', 'name',
                                            'parameter'))

    def data_validation(self, json_file):
        return all(x in json_file for x in ('chipset', 'mac', 'serviceNumber',
                                            'value'))

    def command_validation(self, json_file):
        return all(x in json_file for x in ('name', 'param'))

class ArgsValidation:

    def client_args(self, args):
        valid_args = {}
        if args.get('name'):
            valid_args['name'] = args.get('name')
        if args.get('channel'):
            valid_args['channel'] = args.get('channel')
        if args.get('chipset'):
            valid_args['chipset'] = args.get('chipset')
        if args.get('mac'):
            valid_args['mac'] = args.get('mac')
        if args.get('dns'):
            valid_args['dns'] = args.get('dns')
        if args.get('from'):
            valid_args['time'] = {'$gte': args.get('from')}
        if args.get('until'):
            valid_args['time'] = {'$lt': args.get('until')}
        if args.get('from') and args.get('until'):
            valid_args['time'] = {'$gte': args.get('from'),
                                  '$lt': args.get('until')}

        return valid_args

    def service_args(self, args):
        valid_args = {}
        if args.get('name'):
            valid_args['name'] = args.get('name')
        if args.get('parameter'):
            valid_args['parameter'] = args.get('parameter')
        if args.get('chipset'):
            valid_args['chipset'] = args.get('chipset')
        if args.get('mac'):
            valid_args['mac'] = args.get('mac')
        if args.get('dns'):
            valid_args['dns'] = args.get('dns')
        if args.get('number'):
            valid_args['number'] = args.get('number', type=int)
        if args.get('from'):
            valid_args['time'] = {'$gte': args.get('from')}
        if args.get('until'):
            valid_args['time'] = {'$lt': args.get('until')}
        if args.get('from') and args.get('until'):
            valid_args['time'] = {'$gte': args.get('from'),
                                  '$lt': args.get('until')}

        return valid_args

    def data_args(self, args):
        valid_args = {}
        if args.get('sensitive'):
            valid_args['sensitive'] = args.get('sensitive', type=int)
        if args.get('serviceNumber'):
            valid_args['serviceNumber'] = args.get('serviceNumber', type=int)
        if args.get('chipset'):
            valid_args['chipset'] = args.get('chipset')
        if args.get('mac'):
            valid_args['mac'] = args.get('mac')
        if args.get('dns'):
            valid_args['dns'] = args.get('dns')
        if args.get('from'):
            valid_args['time'] = {'$gte': args.get('from')}
        if args.get('until'):
            valid_args['time'] = {'$lt': args.get('until')}
        if args.get('from') and args.get('until'):
            valid_args['time'] = {'$gte': args.get('from'),
                                  '$lt': args.get('until')}

        return valid_args
