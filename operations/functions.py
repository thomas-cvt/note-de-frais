from .models import Operation

def total(operations=None):
    sum = 0
    if not operations:
        operations=Operation.objects.filter(refunded=None).values()
    for op in operations:
        sum += op["amount"]
    return sum
