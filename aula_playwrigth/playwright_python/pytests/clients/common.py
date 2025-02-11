import random
import string

class common:
    
    @staticmethod
    def incorrect_payload(incorrect):
        match incorrect:
            case 'playload_vazio':
                return ''
            case 'None':
                return None
            case 'null':
                return 'null'
            case 'hash_vazio':
                return {}
            case 'array_vazio':
                return []
            case 'hash_vazio_string':
                return '{}'
            case 'array_vazio_string':
                return '[]'
            case 'payload_number':
                return 1
            case 'payload_boolean_true':
                return True
            case 'payload_boolean_false':
                return False
            
    @staticmethod
    def velues_change(velue):
        if '.to_i' in velue:
            return int(velue.split('.')[0])
        elif '.to.f' in velue:
            return float(velue.split('.')[0])
        elif velue == 'None':
            return None
        elif velue == 'number_negative':
            return -1
        elif velue == 'boolean_true':
            return True
        elif velue == 'boolean_false':
            return False
        elif '.characters_type_string':
            letters = string.ascii_lowercase
            number = int(velue.split('.')[0])
            return (''.join(random.choice(letters)for i in range(number)))
        elif '.characters_type_number' in velue:
            number = int(velue.split('.')[0])
            return (''.join(random.choice('123456789')for i in range(number)))
        elif velue == 'Array':
            return []
        elif velue == 'Hash':
            return {}
        else: 
            return velue