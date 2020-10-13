from tasks import *


result = task_1.apply_async(queue='queueA', args=(1,2))
